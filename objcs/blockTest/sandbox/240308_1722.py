import ctypes
import typing
import inspect

from objc_util import c

_ctype_for_type_map = {
  type(None): None,
  int: ctypes.c_int,
  float: ctypes.c_double,
  bool: ctypes.c_bool,
  bytes: ctypes.c_char_p,
  object: ctypes.py_object,
}


def ctype_for_type(tp):
  """Look up the C type corresponding to the given Python type.
  指定された Python 型に対応する C 型を検索します。


    This conversion is applied to types used in
    :class:`~rubicon.objc.api.objc_method` signatures,
    :class:`~rubicon.objc.api.objc_ivar` types, etc. This function translates
    Python built-in types and :mod:`rubicon.objc` classes to their
    :mod:`ctypes` equivalents. Unregistered types (including types that are
    already ctypes) are returned unchanged.
    """

  return _ctype_for_type_map.get(tp, tp)


class BlockLiteral(ctypes.Structure):
  _fields_ = [
    ("isa", ctypes.c_void_p),
    ("flags", ctypes.c_int),
    ("reserved", ctypes.c_int),
    ("invoke",
     ctypes.c_void_p),  # NB: this must be c_void_p due to variadic nature
    ("descriptor", ctypes.c_void_p),
  ]

_NSConcreteStackBlock = (ctypes.c_void_p * 32).in_dll(c.libc, '_NSConcreteStackBlock')




NOTHING = object()


class Block:
  """A wrapper that exposes a Python callable object to Objective-C as a block.
  Python 呼び出し可能オブジェクトをブロックとして Objective-C に公開するラッパー。


    .. note::

        :class:`Block` instances are currently *not* callable from Python,
        unlike :class:`ObjCBlock`.
    """

  _keep_alive_blocks_ = {}

  def __init__(self, func, restype=NOTHING, *argtypes):
    """The constructor accepts any Python callable object.

        If the callable has parameter and return type annotations, they are used
        as the block's parameter and return types. This allows using
        :class:`Block` as a decorator:

        .. code-block:: python

            @Block
            def the_block(arg: NSInteger) -> NSUInteger:
                return abs(arg)

        For callables without type annotations, the parameter and return types
        need to be passed to the :class:`Block` constructor in the ``restype``
        and ``argtypes`` arguments:

        .. code-block:: python

            the_block = Block(abs, NSUInteger, NSInteger)
        """

    if not callable(func):
      raise TypeError('Blocks must be callable')

    self.func = func

    if restype is NOTHING:
      if argtypes:
        # This can't happen unless the caller does something hacky, but
        # guard against it just in case.
        # 呼び出し元が不正なことをしない限り、このようなことは起こりませんが、念のため注意してください。
        raise ValueError('Cannot pass argtypes without a restype')

      # No explicit restype/argtypes were passed into the constructor,
      # so try to extract them from the function's type annotations.
      # 明示的な restype/argtype がコンストラクターに渡されていないため、関数の型注釈から抽出してみてください。

      try:
        hints = typing.get_type_hints(func)
        signature = inspect.signature(func)
      except (TypeError, ValueError):
        raise ValueError(
          'Could not retrieve function signature information - '
          'please pass return and argument types directly into Block')

      try:
        restype = hints['return']
      except KeyError:
        raise ValueError(
          'Function has no return type annotation - '
          'please add one, or pass return and argument types directly into Block'
        )

      argtypes = []
      for name in signature.parameters:
        try:
          argtypes.append(hints[name])
        except KeyError:
          raise ValueError(
            f'Function has no argument type annotation for parameter {name!r} - '
            f'please add one, or pass return and argument types directly into Block'
          )

    signature = tuple(ctype_for_type(tp) for tp in argtypes)

    restype = ctype_for_type(restype)
    cfunc_type = ctypes.CFUNCTYPE(restype, ctypes.c_void_p, *signature)

    self.literal = BlockLiteral()
    self.literal.isa = addressof(_NSConcreteStackBlock)
    self.literal.flags = (BlockConsts.HAS_STRET
                          | BlockConsts.HAS_SIGNATURE
                          | BlockConsts.HAS_COPY_DISPOSE)
    self.literal.reserved = 0
    cfunc_wrapper = cfunc_type(self.wrapper)
    self.literal.invoke = cast(cfunc_wrapper, c_void_p)

    self.descriptor = BlockDescriptor()
    self.descriptor.reserved = 0
    self.descriptor.size = sizeof(BlockLiteral)

    self.cfunc_copy_helper = _cfunc_type_block_copy(self.copy_helper)
    self.cfunc_dispose_helper = _cfunc_type_block_dispose(self.dispose_helper)
    self.descriptor.copy_helper = self.cfunc_copy_helper
    self.descriptor.dispose_helper = self.cfunc_dispose_helper

    self.descriptor.signature = (
      encoding_for_ctype(restype) + b"@?" +
      b"".join(encoding_for_ctype(arg) for arg in signature))
    self.literal.descriptor = cast(byref(self.descriptor), c_void_p)
    self.block = cast(byref(self.literal), objc_block)
    self._as_parameter_ = self.block

  def wrapper(self, block, *args):
    # ObjC blocks take the block as the first argument when they're invoked;
    # but since this is a wrapper around a Python object, we know the function
    # that has to be invoked.
    return self.func(*args)

  def dispose_helper(self, dst):
    Block._keep_alive_blocks_.pop(dst, None)

  def copy_helper(self, dst, src):
    # Update our keepalive table because objc just informed us that it
    # took ownership of a block/copied a block we are concerned with.
    # Note that sometime later we can expect calls to dispose_helper
    # for each of the 'dst' blocks objc told us about, but until then we
    # need to make sure the python code they reference stays in memory,
    # so basically put self in a class variable dictionary so it is
    # guaranteed to stay around until dispose_helper tells us they are all
    # gone.
    Block._keep_alive_blocks_[dst] = self

