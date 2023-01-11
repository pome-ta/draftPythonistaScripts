from pathlib import Path


if __name__ == '__main__':
  # todo: Pythonista3 かPython で切り分け

  models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'
  root_path = Path(models_root_path)
  path = Path('./')
  print('hoge')
  print(path)
  print(path.resolve())
  print(path)
