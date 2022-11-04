from objc_util import ObjCClass, ObjCInstance, CGRect, CGPoint, CGSize
import ui

import pdbg

CAShapeLayer = ObjCClass('CAShapeLayer')
UIBezierPath = ObjCClass('UIBezierPath')
UIColor = ObjCClass('UIColor')


class ShapeLayerView(ui.View):
  def __init__(self, frame=CGRect((0, 0), (100, 100)), *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'green'
    self.flex = 'WH'
    self.overlayLayer = CAShapeLayer.new()
    self.objc_instance.layer().addSublayer_(self.overlayLayer)

  def layout(self):
    self.overlayLayer.frame = self.objc_instance.bounds()


class View(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    self.bg_color = 'maroon'
    self.shapelayer_view = ShapeLayerView()
    self.add_subview(self.shapelayer_view)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

