from itertools import product

import ui


class CrossLineView(ui.View):

  def __init__(self, div_num, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.div_num = div_num

    pattern_base = [*[0, 1, 0, 0, 1, 0], *[1, 0, 1, 1, 0, 1]]
    self.pattern = pattern_base * -int(-self.div_num**2 // len(pattern_base))
    n = 1
    p = pattern_base[n:] + pattern_base[:n]

    print(pattern_base)
    print(p)

  def draw(self):
    dev_range = range(1, self.div_num)
    line_width = 1
    pre_indx = 0
    for y, x in product(dev_range, dev_range):

      print(x)
      move_x = x * self.cell_size
      move_y = y * self.cell_size
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

      m = 3
      check_bool = y % m == 0 if x % m == 0 else y % m != 0
      # 0,1,0,0,1,0,    1,1,0,1,0,
      # 1,0,1,1,0,1,
      #print(n)
      ui.set_color(self.pattern[n])
      n += 1

      line = ui.Path()
      for stroke in strokes:
        line.move_to(move_x, move_y)
        line.line_to(*stroke)

      line.line_cap_style = ui.LINE_CAP_ROUND
      line.line_width = line_width
      line.stroke()
    #print(n)

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
    self.div_num = 16

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

