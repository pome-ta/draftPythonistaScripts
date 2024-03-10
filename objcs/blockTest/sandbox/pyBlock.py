import os
import ctypes
from ctypes.util import find_library

import typing
import inspect

from objc_util import c, type_encodings


_ctype_for_type_map = {
  type(None): None,
  int: ctypes.c_int,
  float: ctypes.c_double,
  bool: ctypes.c_bool,
  bytes: ctypes.c_char_p,
  object: ctypes.py_object,
}

_cfunc_type_block_copy = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p,
                                          ctypes.c_void_p)
_cfunc_type_block_dispose = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)
#_encoding_for_ctype_map = {}

_ctype_for_encoding_map = {}

#[Pythonで辞書のキーと値を入れ替える | note.nkmk.me](https://note.nkmk.me/python-dict-swap-key-value/)
#d_swap = {v: k for k, v in d.items()}
_encoding_for_ctype_map = {v: k for k, v in type_encodings.items()}


def register_encoding(encoding, ctype):
  """Register an additional conversion between an Objective-C type encoding
    and a C type.

    "Additional" means that any existing conversions in either direction are
    *not* overwritten with the new conversion. To register an encoding and
    overwrite existing conversions, use :func:`register_preferred_encoding`.
    """

  _ctype_for_encoding_map.setdefault(encoding, ctype)
  _encoding_for_ctype_map.setdefault(ctype, encoding)


def with_encoding(encoding):
  """Register an additional conversion between an Objective-C type encoding
    and the decorated C type.

    This is equivalent to calling :func:`register_encoding` on the
    decorated C type.
    """

  def _with_encoding_decorator(ctype):
    register_encoding(encoding, ctype)
    return ctype

  return _with_encoding_decorator


@with_encoding(b"@")
class objc_id(ctypes.c_void_p):
  """The `id <https://developer.apple.com/documentation/objectivec/id?language=objc>`__
    type from ``<objc/objc.h>``.
    """


@with_encoding(b"@?")
class objc_block(objc_id):
  """The low-level type of block pointers.

    This type tells Rubicon's internals that the object in question is a block
    and not just a regular Objective-C object, which affects method argument and
    return value conversions. For more details, see :ref:`objc_blocks`.

    .. note::

        This type does not correspond to an actual C type or Objective-C class.
        Although the internal structure of block objects is documented, as well
        as the fact that they are Objective-C objects, they do not have a
        documented type or class name and are not fully defined in any header
        file.

        Aside from the special conversion behavior, this type is equivalent to
        :class:`objc_id`.
    """


def encoding_for_ctype(ctype):
  """Return the Objective-C type encoding for the given ctypes type.

    If a type encoding has been registered for the C type, that encoding is
    returned. Otherwise, if the C type is a pointer type, its pointed-to type
    is encoded and used to construct the pointer type encoding.

    Automatic encoding of other compound types (arrays, structures, and unions)
    is currently not supported. To encode such types, a type encoding must be
    manually provided for them using :func:`register_preferred_encoding` or
    :func:`register_encoding`.

    :raises ValueError: if the conversion fails at any point
    """

  
  #print('----')
  #from pprint import pprint
  #pprint(_encoding_for_ctype_map)
  try:
    return _encoding_for_ctype_map[ctype]
  except KeyError:
    try:
      return b"^" + encoding_for_ctype(ctype._type_)
    except KeyError:
      raise ValueError(f"No type encoding known for ctype {ctype}")


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

  print('___')
  print(tp)
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


class BlockDescriptor(ctypes.Structure):
  _fields_ = [
    ("reserved", ctypes.c_ulong),
    ("size", ctypes.c_ulong),
    ("copy_helper", _cfunc_type_block_copy),
    ("dispose_helper", _cfunc_type_block_dispose),
    ("signature", ctypes.c_char_p),
  ]


_lib_path = ["/usr/lib"]
_framework_path = ["/System/Library/Frameworks"]


def load_library(name):
  """Load and return the C library with the given name.

    If the library could not be found, a :class:`ValueError` is raised.

    Internally, this function uses :func:`ctypes.util.find_library` to search
    for the library in the system-standard locations. If the library cannot be
    found this way, it is attempted to load the library from certain hard-coded
    locations, as a fallback for systems where ``find_library`` does not work
    (such as iOS).
    """

  path = find_library(name)
  if path is not None:
    return ctypes.CDLL(path)

  # On iOS (and probably also watchOS and tvOS), ctypes.util.find_library
  # doesn't work and always returns None. This is because the sandbox hides
  # all system libraries from the filesystem and pretends they don't exist.
  # However, they can still be loaded if the path is known, so we try to load
  # the library from a few known locations.

  for loc in _lib_path:
    try:
      return ctypes.CDLL(os.path.join(loc, "lib" + name + ".dylib"))
    except OSError:
      pass

  for loc in _framework_path:
    try:
      return ctypes.CDLL(os.path.join(loc, name + ".framework", name))
    except OSError:
      pass

  raise ValueError(f"Library {name!r} not found")


libc = load_library('c')
_NSConcreteStackBlock = (ctypes.c_void_p * 32).in_dll(libc,
                                                      '_NSConcreteStackBlock')

#_NSConcreteStackBlock_ = (ctypes.c_void_p * 32).in_dll(c, '_NSConcreteStackBlock')


class BlockConsts:
  HAS_COPY_DISPOSE = 1 << 25
  HAS_CTOR = 1 << 26
  IS_GLOBAL = 1 << 28
  HAS_STRET = 1 << 29
  HAS_SIGNATURE = 1 << 30


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

    print(restype)
    
    self.literal = BlockLiteral()
    self.literal.isa = ctypes.addressof(_NSConcreteStackBlock)
    self.literal.flags = (BlockConsts.HAS_STRET
                          | BlockConsts.HAS_SIGNATURE
                          | BlockConsts.HAS_COPY_DISPOSE)
    self.literal.reserved = 0
    cfunc_wrapper = cfunc_type(self.wrapper)
    self.literal.invoke = ctypes.cast(cfunc_wrapper, ctypes.c_void_p)

    self.descriptor = BlockDescriptor()
    self.descriptor.reserved = 0
    self.descriptor.size = ctypes.sizeof(BlockLiteral)

    self.cfunc_copy_helper = _cfunc_type_block_copy(self.copy_helper)
    self.cfunc_dispose_helper = _cfunc_type_block_dispose(self.dispose_helper)
    self.descriptor.copy_helper = self.cfunc_copy_helper
    self.descriptor.dispose_helper = self.cfunc_dispose_helper

    
    print(signature)
    self.descriptor.signature = (
      encoding_for_ctype(restype) + b"@?" +
      b"".join(encoding_for_ctype(arg) for arg in signature))
    self.literal.descriptor = ctypes.cast(ctypes.byref(self.descriptor),
                                          ctypes.c_void_p)
    self.block = ctypes.cast(ctypes.byref(self.literal), objc_block)
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

