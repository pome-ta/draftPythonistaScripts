from objc_util import ObjCClass

UIImpactFeedbackGenerator = ObjCClass('UIImpactFeedbackGenerator')

aUIImpactFeedbackGenerator = UIImpactFeedbackGenerator.alloc().init()

aUIImpactFeedbackGenerator.prepare()
style = 4  # 0-4 
aUIImpactFeedbackGenerator.initWithStyle_(style)
aUIImpactFeedbackGenerator.impactOccurred()

