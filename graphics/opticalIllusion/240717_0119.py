from colorsys import hsv_to_rgb

import ui

class BoardView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'blue'
    self.update_interval = 1 / 60


  def update(self):
      print('update')
      self.set_needs_display()
  
  def layout(self):
    print('layout')


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    #self.update_interval = 1 / 60
    self.board_view = BoardView()
    self.add_subview(self.board_view)

    self.div_num = 16

  def will_close(self):
    pass

  def draw(self):
    pass

  def update(self):
    print('update')
    self.set_needs_display()

  def layout(self):
    pass


if __name__ == '__main__':
  view = MainView()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

