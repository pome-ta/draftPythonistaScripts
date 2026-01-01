from pyrubicon.objc.runtime import load_library
from pyrubicon.objc.types import CGRect

CoreGraphics = load_library('CoreGraphics')
CGRectZero = CGRect.in_dll(CoreGraphics, 'CGRectZero')
