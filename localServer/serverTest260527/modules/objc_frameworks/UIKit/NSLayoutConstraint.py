from enum import IntEnum


class UILayoutPriority(IntEnum):

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutpriorityrequired?language=objc)
  #UILayoutPriorityRequired = 1000
  required = 1000

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutprioritydefaulthigh?language=objc)
  #UILayoutPriorityDefaultHigh = 750
  defaultHigh = 750

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutprioritydragthatcanresizescene?language=objc)
  #UILayoutPriorityDragThatCanResizeScene = 510
  dragThatCanResizeScene = 510

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutpriorityscenesizestayput?language=objc)
  #UILayoutPrioritySceneSizeStayPut = 500
  sceneSizeStayPut = 500

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutprioritydragthatcannotresizescene?language=objc)
  #UILayoutPriorityDragThatCannotResizeScene = 490
  dragThatCannotResizeScene = 490

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutprioritydefaultlow?language=objc)
  #UILayoutPriorityDefaultLow = 250
  defaultLow = 250

  # [Apple's documentation](https://developer.apple.com/documentation/uikit/uilayoutpriorityfittingsizelevel?language=objc)
  #UILayoutPriorityFittingSizeLevel = 50
  fittingSizeLevel = 50

