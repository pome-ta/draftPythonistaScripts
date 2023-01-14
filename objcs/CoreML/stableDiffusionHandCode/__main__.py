from pathlib import Path

from pyStableDiffusion.pipeline.StableDiffusionPipeline_Resources import StableDiffusionPipeline

# if __name__ == '__main__':
# todo: Pythonista3 かPython で切り分け
models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'

resourceURL = Path(models_root_path)
# resourceURL = Path('./objcs/CoreML/stableDiffusionHandCode', models_root_path)

#pipeline = StableDiffusionPipeline(resourceURL)
pipeline = StableDiffusionPipeline.init_resourcesAt_configuration_(resourceURL)

prompt: str = "cat"
imageCount: int = 1
stepCount: int = 2
seed: int = 500
step: int = 2

image = pipeline.generateImages(
  prompt=prompt, imageCount=imageCount, stepCount=stepCount, seed=seed)

x = 1

