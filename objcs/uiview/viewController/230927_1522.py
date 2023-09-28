from objc_util import ObjCClass,ObjCInstance, on_main_thread
import ui

import pdbg


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #self.bg_color = 'maroon'
    #0.141176 0.2 0.243137
    self.bg_color = 'red'
    #self.bg_color = (0.141176, 0.2, 0.243137,1)
    btn_item_kwargs = {
      'image': ui.Image.named('iob:arrow_down_a_24'),
      'action': present_objc,
    }
    btn_item = ui.ButtonItem(**btn_item_kwargs)
    self.right_button_items = [btn_item]
    
    self.label= ui.Label()
    self.label.text = 'ほげ☺️'
    self.add_subview(self.label)

  def will_close(self):
    #print('close')
    present_objc(None)
    
    pass

  def layout(self):
    pass


@on_main_thread
def present_objc(sender):
  #print(dir(sender))
  #pdbg.state(ObjCInstance(sender))
  # xxx: 全体的に改善
  app = ObjCClass('UIApplication').sharedApplication()
  #pdbg.all(app)
  window = app.keyWindow()
  
  root_vc = window.rootViewController()
  presented_vc = root_vc.presentedViewController()
  view = presented_vc.view()
  #pdbg.all(presented_vc.view())
  #pdbg.mthd(presented_vc.window())
  #pdbg.state(presented_vc)
  #pdbg.mthd(view.window())
  pdbg.mthd(window)
  
  
  #pdbg.all(root_vc)
  #view = root_vc.view()
  #pdbg.all(view)
  #pdbg.state(root_vc.view())
  #pdbg.state(root_vc.detailViewController())
  #pdbg.state(root_vc.detailViewController().view())
  #pdbg.all(root_vc.detailViewController().view())


  '''
  while root_vc.presentedViewController():
    print('w')
    root_vc = root_vc.presentedViewController()
  '''
  #pdbg.all(root_vc.view())
  #pdbg.state(root_vc)
  #pdbg.all(root_vc)
  #pdbg.state(root_vc.view().superview())
  #pdbg.state(root_vc.view())

if __name__ == '__main__':
  view = View()
  #view.present()

  #present_objc()

  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

