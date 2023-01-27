from pathlib import Path

from pyStableDiffusion.pipeline.StableDiffusionPipeline_Resources import StableDiffusionPipeline

# if __name__ == '__main__':
# todo: Pythonista3 かPython で切り分け
models_root_path = './models/coreml-stable-diffusion-v1-4_original_compiled'

resourceURL = Path(models_root_path)
'''
# resourceURL = Path('./objcs/CoreML/stableDiffusionHandCode', models_root_path)

#pipeline = StableDiffusionPipeline(resourceURL)

import os

#root = os.path.join(os.path.expanduser('~/Documents'), MODEL_FILENAME)

#root = os.path.expanduser(models_root_path)
#root = os.path.expanduser('~/Documents')
root = os.path.expanduser('~')

MODEL_FILENAME = 'mobilenet.mlmodel'
MODEL_PATH = os.path.join(os.path.expanduser('~/Documents'), MODEL_FILENAME)

#'TextEncoder.mlmodelc'
ml = '/TextEncoder.mlmodelc'

txtEnc = Path(resourceURL, ml)

rslv = txtEnc.resolve()
rslv_str = str(rslv)

from objc_util import nsurl, ObjCClass, NSBundle, NSURL
import pdbg

#add_path = NSBundle.bundleWithPath_(resourceURL)

main = NSBundle.allBundles()
#NSBundle.allBundles

bundl = NSBundle.new()
#pdbg.state(bundl)

#inipath = bundl.initWithPath_(rslv_str)
#pathForResource_ofType_
#txtpath = bundl.pathForResource_ofType_(nsurl(rslv_str), '.mlmodelc')

mynsurl = NSURL.new()
#pdbg.state(mynsurl.baseURL())
#pdbg.state(NSURL)

#ns_rslv = mynsurl.initFileURLWithPath_isDirectory_(nsurl(rslv_str), 0)

ns_rslv = NSURL.fileURLWithPath_isDirectory_(models_root_path + ml, 0)

pdbg.state(ns_rslv.relativePath())

_model_ns = nsurl(MODEL_PATH)
_rslv_ns = nsurl(rslv_str)
_root = nsurl(root)

#pdbg.state(_model_ns.description())
#pdbg.state(_rslv_ns)
MLModel = ObjCClass('MLModel')

c_model_url = MLModel.compileModelAtURL_error_(_rslv_ns, None)
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


