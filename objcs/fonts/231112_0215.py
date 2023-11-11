from objc_util import ObjCClass

[print(f'- {name}') for name in ObjCClass('UIFont').familyNames()]

