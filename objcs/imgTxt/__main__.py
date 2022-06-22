from objc_util import ObjCClass

import pdbg

VNRecognizeTextRequest = ObjCClass('VNRecognizeTextRequest')
request = VNRecognizeTextRequest.new()

# todo: default_`en_US` <- `request.recognitionLanguages()`

VNImageRequestHandler = ObjCClass('VNImageRequestHandler')


pdbg.state(request.recognitionLanguages())

