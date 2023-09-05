from objc_util import ObjCClass, create_objc_class


def searchBar_textDidChange_(_self, _cmd, _searchBar, _searchText) -> None:
  print(f'01 : searchBar_textDidChange_')
  pass


methods = [searchBar_textDidChange_]
SearchBarDelegate = create_objc_class(name='SearchBarDelegate',methods=methods,protocols=['UISearchBarDelegate', ])
