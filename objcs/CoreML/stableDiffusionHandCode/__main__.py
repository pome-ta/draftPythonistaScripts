from pathlib import Path
#import pyStableDiffusion
from pyStableDiffusion.pipeline.StableDiffusionPipeline_Resources import StableDiffusionPipeline

#if __name__ == '__main__':
# todo: Pythonista3 かPython で切り分け
models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'
resourceURL = Path(models_root_path)
pipeline = StableDiffusionPipeline(resourceURL)

