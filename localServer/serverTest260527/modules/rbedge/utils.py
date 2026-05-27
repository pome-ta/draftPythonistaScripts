from pathlib import Path
from pyrubicon.objc.api import ObjCClass

NSURL = ObjCClass('NSURL')


# ref: from objc_util.py of Pythonista3 module
def nsurl(url_or_path):
  if not isinstance(url_or_path, str):
    raise TypeError('expected a string')
  return NSURL.URLWithString_(
    url_or_path) if ':' in url_or_path else NSURL.fileURLWithPath_(url_or_path)


# wip: 雑
def get_str_filepath(dir_path: Path, file_name: str) -> str | None:
  return str(file_path.resolve()) if (file_path := next(
    dir_path.rglob(file_name), None)) else None


def readonly_properties(*property_names):

  def wrapper(cls):
    for name in property_names:
      cls.declare_property(name)
    return cls

  return wrapper


def readonly_class_properties(*property_names):

  def wrapper(cls):
    for name in property_names:
      cls.declare_class_property(name)
    return cls

  return wrapper

