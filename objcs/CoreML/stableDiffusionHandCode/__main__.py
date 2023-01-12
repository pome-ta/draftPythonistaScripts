from pathlib import Path
#import stableDiffusion
from pyStableDiffusion.pipeline import StableDiffusionPipeline



#if __name__ == '__main__':
  # todo: Pythonista3 かPython で切り分け
models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'
root_path = Path(models_root_path)
hoge = StableDiffusionPipeline()
