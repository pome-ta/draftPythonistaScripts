from pyrubicon.objc.types import NSUInteger

from .constants import framework as ARKit

ARSCNDebugOptionShowFeaturePoints = NSUInteger.in_dll(
  ARKit, 'ARSCNDebugOptionShowFeaturePoints').value
showFeaturePoints = ARSCNDebugOptionShowFeaturePoints

ARSCNDebugOptionShowWorldOrigin = NSUInteger.in_dll(
  ARKit, 'ARSCNDebugOptionShowWorldOrigin').value
showWorldOrigin = ARSCNDebugOptionShowWorldOrigin

