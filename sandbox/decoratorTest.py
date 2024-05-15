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


def add_fnc(fnc):
  def a(h):
    #print(h)
    #print('a')
    fnc_list.append({'hoge':h, 'fuga':fnc})
  #print(a,fnc)
  return a



@add_fnc('higeeeeee')
def fnc01():
  pass

#@add_fnc('fuga')
def fnc02():
  pass


#fnc_list = [fnc01, fnc02]

