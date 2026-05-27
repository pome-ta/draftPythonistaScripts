from enum import IntEnum, IntFlag


class UIBarButtonItemStyle(IntEnum):
  #[doc(alias = "UIBarButtonItemStylePlain")]
  plain = 0
  # A button item style for a prominent button.
  #
  # For example, use this for a button that completes or finalizes some task.
  # Buttons with this style will not be visually grouped with other items
  # in a navigation bar or toolbar, and will also have other styling changes
  # appropriate to their context to indicate their prominence.
  #[doc(alias = "UIBarButtonItemStyleProminent")]
  prominent = 2
  # A button item style for a prominent button.
  #
  # For example, use this for a button that completes or finalizes some task.
  # Buttons with this style will not be visually grouped with other items
  # in a navigation bar or toolbar, and will also have other styling changes
  # appropriate to their context to indicate their prominence.
  #[doc(alias = "UIBarButtonItemStyleBordered")]
  #[deprecated]
  bordered = 1
  # A button item style for a prominent button.
  #
  # For example, use this for a button that completes or finalizes some task.
  # Buttons with this style will not be visually grouped with other items
  # in a navigation bar or toolbar, and will also have other styling changes
  # appropriate to their context to indicate their prominence.
  #[doc(alias = "UIBarButtonItemStyleDone")]
  #[deprecated]
  done = prominent


# ref: [UIBarButtonSystemItem | Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uibarbuttonsystemitem?language=objc)
class UIBarButtonSystemItem(IntEnum):

  #[doc(alias = "UIBarButtonSystemItemDone")]
  done = 0
  #[doc(alias = "UIBarButtonSystemItemCancel")]
  cancel = 1
  #[doc(alias = "UIBarButtonSystemItemEdit")]
  edit = 2
  #[doc(alias = "UIBarButtonSystemItemSave")]
  save = 3
  #[doc(alias = "UIBarButtonSystemItemAdd")]
  add = 4
  #[doc(alias = "UIBarButtonSystemItemFlexibleSpace")]
  flexibleSpace = 5
  #[doc(alias = "UIBarButtonSystemItemFixedSpace")]
  fixedSpace = 6
  #[doc(alias = "UIBarButtonSystemItemCompose")]
  compose = 7
  #[doc(alias = "UIBarButtonSystemItemReply")]
  reply = 8
  #[doc(alias = "UIBarButtonSystemItemAction")]
  action = 9
  #[doc(alias = "UIBarButtonSystemItemOrganize")]
  organize = 10
  #[doc(alias = "UIBarButtonSystemItemBookmarks")]
  bookmarks = 11
  #[doc(alias = "UIBarButtonSystemItemSearch")]
  search = 12
  #[doc(alias = "UIBarButtonSystemItemRefresh")]
  refresh = 13
  #[doc(alias = "UIBarButtonSystemItemStop")]
  stop = 14
  #[doc(alias = "UIBarButtonSystemItemCamera")]
  camera = 15
  #[doc(alias = "UIBarButtonSystemItemTrash")]
  trash = 16
  #[doc(alias = "UIBarButtonSystemItemPlay")]
  play = 17
  #[doc(alias = "UIBarButtonSystemItemPause")]
  pause = 18
  #[doc(alias = "UIBarButtonSystemItemRewind")]
  rewind = 19
  #[doc(alias = "UIBarButtonSystemItemFastForward")]
  fastForward = 20
  #[doc(alias = "UIBarButtonSystemItemUndo")]
  undo = 21
  #[doc(alias = "UIBarButtonSystemItemRedo")]
  redo = 22
  #[doc(alias = "UIBarButtonSystemItemPageCurl")]
  #[deprecated]
  pageCurl = 23
  #[doc(alias = "UIBarButtonSystemItemClose")]
  close = 24
  #[doc(alias = "UIBarButtonSystemItemWritingTools")]
  writingTools = 25

