from pathlib import Path

from pyStableDiffusion.pipeline.StableDiffusionPipeline_Resources import StableDiffusionPipeline

# if __name__ == '__main__':
# todo: Pythonista3 かPython で切り分け
models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'

resourceURL = Path(models_root_path)



from objc_util import nsurl
import pdbg


textEncoderURL = Path(resourceURL, 'TextEncoder.mlmodelc')

text_enc_path = str(textEncoderURL.resolve())
text_enc_nsurl = nsurl(text_enc_path)

print(text_enc_nsurl.isFileURL())


'''
pipeline = StableDiffusionPipeline.init_resourcesAt_configuration_(resourceURL)

prompt: str = 'cat'
imageCount: int = 1
stepCount: int = 2
seed: int = 500
step: int = 2

image = pipeline.generateImages(
  prompt=prompt, imageCount=imageCount, stepCount=stepCount, seed=seed)

x = 1
'''


