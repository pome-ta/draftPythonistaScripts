import ui


class View(ui.View):
  def __init__(self):
    self.bg_color = 1

  def did_load(self):
    pass

  def will_close(self):
    pass

  def draw(self):
    pass

  def layout(self):
    pass

  def touch_began(self, touch):
    pass

  def touch_moved(self, touch):
    pass

  def touch_ended(self, touch):
    pass

  def keyboard_frame_will_change(self, frame):
    pass

  def keyboard_frame_did_change(self, frame):
    pass


if __name__ == '__main__':
  view = View()
  view.present()
  #view.present(hide_title_bar=True)
  #view.present(style='fullscreen', orientations=['portrait'])

