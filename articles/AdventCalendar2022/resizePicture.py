from pathlib import Path

from PIL import Image as ImageP
import arrow

from objc_util import ObjCClass
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


def get_folder_path(path='imgs'):
  data_path = Path(editor.get_path()).parent
  target_path = Path(str(data_path), path)
  if not target_path.exists():
    target_path.mkdir()
  return [target_path, path]


def create_filename(name=None, extension='png'):
  if name:
    return f'{name}.{extension}'
  else:
    _utc = arrow.utcnow().to('JST')
    _now = _utc.format('YYMMDD_HHmmss')
    return f'img{_now}.{extension}'


def scale_to_width(img, width=640):
  height = round(img.height * width / img.width)
  return img.resize((width, height), ImageP.LANCZOS)


def set_seveto_clipboard(img):
  root_path, parent_name = get_folder_path()
  save_name = create_filename()
  save_path = Path(root_path, save_name).absolute()

  clipboard.set(f'![screenshot](./{parent_name}/{save_name})')

  img.save(str(save_path))


def main():
  screenshots = photos.get_screenshots_album()
  screenshot_imag = photos.pick_asset(screenshots)
  if screenshot_imag:
    feedback = get_feedback_generator()

    pick_pil = screenshot_imag.get_image()
    out_img = scale_to_width(pick_pil)

    set_seveto_clipboard(out_img)
    feedback.impactOccurred()


if __name__ == '__main__':
  main()

