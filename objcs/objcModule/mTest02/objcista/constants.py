from dataclasses import dataclass


@dataclass
class UIRectEdge:
  # ref: [UIRectEdge | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uirectedge?language=objc)
  none: int = 0
  top: int = 1 << 0
  left: int = 1 << 1
  bottom: int = 1 << 2
  right: int = 1 << 3
  all: int = top | left | bottom | right


@dataclass
class UIView_ContentMode:
  # ref: [UIView.ContentMode | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiview/contentmode)
  scaleToFill: int = 0
  scaleAspectFit: int = 1
  scaleAspectFill: int = 2
  redraw: int = 3
  center: int = 4
  top: int = 5
  bottom: int = 6
  left: int = 7
  right: int = 8
  topLeft: int = 9
  topRight: int = 10
  bottomLeft: int = 11
  bottomRight: int = 12


@dataclass
class UIModalPresentationStyle:
  # ref: [UIModalPresentationStyle | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
  automatic: int = -2
  none: int = -1
  fullScreen: int = 0
  pageSheet: int = 1
  formSheet: int = 2
  currentContext: int = 3
  custom: int = 4
  overFullScreen: int = 5
  overCurrentContext: int = 6
  popover: int = 7
  blurOverFullScreen: int = 8


@dataclass
class UITableViewCell_AccessoryType:
  # ref: [UITableViewCell.AccessoryType | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype)
  none: int = 0
  disclosureIndicator: int = 1
  detailDisclosureButton: int = 2
  checkmark: int = 3
  detailButton: int = 4


@dataclass
class UIBarButtonItem_SystemItem:
  # ref: [UIBarButtonSystemItem | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem?language=objc)
  done = 0
  cancel = 1
  edit = 2
  add = 4
  flexibleSpace = 5
  fixedSpace = 6
  compose = 7
  reply = 8
  action = 9
  organize = 10
  bookmarks = 11
  search = 12
  refresh = 13
  stop = 14
  trash = 16
  play = 17
  pause = 18
  rewind = 19
  fastForward = 20
  undo = 21
  redo = 22
  pageCurl = 23  # Deprecated
  close = 24


@dataclass
class NSTextAlignment:
  # ref: [NSTextAlignment | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/nstextalignment?language=objc)
  left = 0
  right = 2
  center = 1
  justified = 3
  natural = 4
