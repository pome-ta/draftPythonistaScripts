#from colorsys import hsv_to_rgb
from itertools import product

import ui


class BoardView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'green'

    self.div_num = 16
    self.check_colors = [1.0, 0.72]

  def draw(self):
    dev_range = range(self.div_num)

    for x, y in product(dev_range, dev_range):
      check_bool = y % 2 != 0 if x % 2 == 0 else y % 2 == 0
      ui.set_color(self.check_colors[check_bool])
      rect = [
        x * self.cell_size,
        y * self.cell_size,
        self.cell_size,
        self.cell_size,
      ]
      ui.fill_rect(*rect)

  def update(self):
    print('update')
    self.set_needs_display()

  def layout(self):
    _, _, w, h = self.frame
    self.cell_size = min(w, h) / self.div_num


class MainView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    #BG_COLOR = 0.872
    #self.bg_color = 'maroon'
    self.bg_color = 0.872
    #self.update_interval = 1 / 60
    self.board_view = BoardView()
    self.add_subview(self.board_view)

  def will_close(self):
    pass

  def update(self):
    print('update')
    self.set_needs_display()

  def layout(self):
    _, _, w, h = self.frame
    sq_size = int(min(w, h) * 0.88)
    frame = (
      (w - sq_size) / 2,
      (h - sq_size) / 2,
      sq_size,
      sq_size,
    )
    self.board_view.frame = frame


if __name__ == '__main__':
  view = MainView()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

