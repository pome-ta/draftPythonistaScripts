from objc_util import ObjCClass

import pdbg


VNRecognizeTextRequest = ObjCClass('VNRecognizeTextRequest')
request = VNRecognizeTextRequest.new()

pdbg.state(request)
