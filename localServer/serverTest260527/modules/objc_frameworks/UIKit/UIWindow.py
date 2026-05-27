from .constants import _get_const

UIKeyboardFrameBeginUserInfoKey = _get_const('UIKeyboardFrameBeginUserInfoKey')
UIKeyboardFrameEndUserInfoKey = _get_const('UIKeyboardFrameEndUserInfoKey')
UIKeyboardAnimationDurationUserInfoKey = _get_const(
  'UIKeyboardAnimationDurationUserInfoKey')
UIKeyboardAnimationCurveUserInfoKey = _get_const(
  'UIKeyboardAnimationCurveUserInfoKey')
UIKeyboardIsLocalUserInfoKey = _get_const('UIKeyboardIsLocalUserInfoKey')
UIKeyboardCenterBeginUserInfoKey = _get_const(
  'UIKeyboardCenterBeginUserInfoKey')
UIKeyboardCenterEndUserInfoKey = _get_const('UIKeyboardCenterEndUserInfoKey')
UIKeyboardBoundsUserInfoKey = _get_const('UIKeyboardBoundsUserInfoKey')


class NSNotificationName:
  didBecomeVisibleNotification = _get_const(
    'UIWindowDidBecomeVisibleNotification')
  didBecomeHiddenNotification = _get_const(
    'UIWindowDidBecomeHiddenNotification')
  didBecomeKeyNotification = _get_const('UIWindowDidBecomeKeyNotification')
  didResignKeyNotification = _get_const('UIWindowDidResignKeyNotification')
  keyboardWillShowNotification = _get_const('UIKeyboardWillShowNotification')
  keyboardDidShowNotification = _get_const('UIKeyboardDidShowNotification')
  keyboardWillHideNotification = _get_const('UIKeyboardWillHideNotification')
  keyboardDidHideNotification = _get_const('UIKeyboardDidHideNotification')
  keyboardWillChangeFrameNotification = _get_const(
    'UIKeyboardWillChangeFrameNotification')
  keyboardDidChangeFrameNotification = _get_const(
    'UIKeyboardDidChangeFrameNotification')

