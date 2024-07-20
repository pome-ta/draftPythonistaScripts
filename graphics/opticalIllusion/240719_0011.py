from itertools import product
import operator

import ui


def list_add(*args):
  return list(map(operator.add, *args))


class CrossLineView(ui.View):

  def __init__(self, div_num, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.div_num = div_num

  def draw(self):
    line_width = 1
    interval = self.cell_size / 2

    to_top = [10, 0]
    to_end = [self.width, self.height]

    for i in range(self.div_num * 2):
      x = interval * i
      y = self.height - (interval * i)

      line = ui.Path()
      for top_end in range(2):
        line.move_to(x, y)
        line.line_to(*(to_top if top_end else to_end))
        line.stroke()

      oval = ui.Path.oval(x, y, 8, 8)

  def layout(self):
    _, _, w, h = self.frame
    self.cell_size = min(w, h) / self.div_num


class CheckerBoardView(ui.View):

  def __init__(self, div_num, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'maroon'
    self.div_num = div_num
    self.check_colors = [0.92, 0.72]

  def draw(self):
    dev_range = range(self.div_num)

    for y, x in product(dev_range, dev_range):
      m = 2
      check_bool = y % m != 0 if x % m == 0 else y % m == 0
      ui.set_color(self.check_colors[check_bool])
      rect_set = [
        x * self.cell_size,
        y * self.cell_size,
        self.cell_size,
        self.cell_size,
      ]
      ui.fill_rect(*rect_set)

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
    self.bg_color = 0.5  #0.872
    #self.update_interval = 1 / 60
    self.div_num = 13

    self.checker_board = CheckerBoardView(self.div_num)
    self.cross_line = CrossLineView(self.div_num)
    self.add_subview(self.checker_board)
    self.add_subview(self.cross_line)

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
    self.checker_board.frame = frame
    self.cross_line.frame = frame


if __name__ == '__main__':
  view = MainView()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

