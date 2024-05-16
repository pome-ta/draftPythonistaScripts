# decorator の理解

# xxx: 変数が存在しない場合、生成できないのでは？

fnc_list = []
'''
def add_fnc(fnc):
  def a(h):
    print(h)
    print('a')
  #print(a,fnc)
  return a
    
  #fnc_list.append(fnc)
'''


def _create_reuse_dict(cellClass: 'UITableViewCell', identifier: str) -> dict:
  return {
    'cellClass': cellClass,
    'identifier': identifier,
  }


prototypes = []


def add_prototype(identifier: str):

  def wrapper(cellClass: 'UITableViewCell'):
    prototypes.append(_create_reuse_dict(cellClass, identifier))

  return wrapper


def add_fnc(fnc):

  def a(h):
    #print(h)
    #print('a')
    fnc_list.append({'hoge': h, 'fuga': fnc})

  #print(a,fnc)
  return a


@add_prototype('higeeeeee')
def fnc01():
  pass


@add_prototype('aaaaa')
def fnc02():
  pass


#fnc_list = [fnc01, fnc02]

