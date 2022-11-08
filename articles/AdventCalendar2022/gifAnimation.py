from pathlib import Path
import re
import shutil

import arrow

from objc_util import ObjCClass, ObjCInstance
import photos
import editor
import clipboard


def get_feedback_generator():
  """
  call feedback ex:
  `UIImpactFeedbackGenerator.impactOccurred()`
  """
  style = 4  # 0-4 
  UIImpactFeedbackGenerator = ObjCClass('UIImpactFeedbackGenerator').new()
  UIImpactFeedbackGenerator.prepare()
  UIImpactFeedbackGenerator.initWithStyle_(style)
  return UIImpactFeedbackGenerator


def get_assetURLstr(asset):
  phAsset = ObjCInstance(asset._objc_ptr)
  mainFileURL = phAsset.mainFileURL()
  assetURL_str = str(mainFileURL).strip('file:')
  return assetURL_str


def get_folder_path(path='imgs'):
  data_path = Path(editor.get_path()).parent
  target_path = Path(f'{data_path}', path)
  if not target_path.exists():
    target_path.mkdir()
  return [target_path, path]


def create_filename(name=None, extension='gif'):
  if name:
    return f'{name}.{extension}'
  else:
    _utc = arrow.utcnow().to('JST')
    _now = _utc.format('YYMMDD_HHmmss')
    return f'img{_now}.{extension}'


def set_seveto_clipboard(gif_url):
  origin_path = Path(gif_url)
  root_path, parent_name = get_folder_path()
  save_name = create_filename()
  save_path = Path(root_path, save_name).absolute()

  clipboard.set(f'![screenshot](./{parent_name}/{save_name})')

  shutil.copy(str(origin_path), str(save_path))


def main():
  image_assets = photos.get_assets()
  pick_asset = photos.pick_asset(image_assets)
  if not pick_asset:
    return

  pickURL_str = get_assetURLstr(pick_asset)
  if re.search(r'\.gif$', pickURL_str, flags=re.IGNORECASE):
    feedback = get_feedback_generator()
    set_seveto_clipboard(pickURL_str)
    feedback.impactOccurred()


if __name__ == '__main__':
  main()
