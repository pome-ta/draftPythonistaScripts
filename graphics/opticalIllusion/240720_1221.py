import math
from itertools import product
import operator

import ui


def list_add(*args):
  return list(map(operator.add, *args))


class CrossLineView(ui.View):

  def __init__(self, div_num, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.fps = 60
    self.update_interval = 1 / self.fps
    self.counter = 0

    self.div_num = div_num
    self.div_cross = self.div_num - 1

    _pattern = [
      *[0, 1, 0, 0],
      *[1, 0, 1, 1],
    ]
    pattern = _pattern * -int(-(self.div_cross) // len(_pattern)
                              ) if self.div_cross > len(_pattern) else 1

    self.patterns = [
      pattern[-i:] + pattern[:-i] for i in range(self.div_cross)
    ]

  def draw(self):

    pattern = self.patterns

    line_width = 1.5
    #print(self.counter)

    div_range = range(self.div_cross)
    for x, y in product(div_range, div_range):
      move_x = x * self.cell_size + self.cell_size
      move_y = y * self.cell_size + self.cell_size
      stroke_length = self.cell_size / 6

      strokes = [
        [
          move_x - stroke_length,
          move_y,
        ],
        [
          move_x + stroke_length,
          move_y,
        ],
        [
          move_x,
          move_y - stroke_length,
        ],
        [
          move_x,
          move_y + stroke_length,
        ],
      ]

      r, g, b, a = ui.parse_color(pattern[y][x])
      a = math.sin(
        (self.update_interval * 8) * (math.pi * 2.0) * self.counter)

      ui.set_color((r, b, g, a))
      self.ppp = ui.Path()
      line = ui.Path()
      for stroke in strokes:
        line.move_to(move_x, move_y)
        line.line_to(*stroke)

      line.line_cap_style = ui.LINE_CAP_ROUND
      line.line_width = line_width * a
      line.stroke()

  def update(self):
    self.counter += self.update_interval
    self.set_needs_display()

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

