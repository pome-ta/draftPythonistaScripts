from colorsys import hsv_to_rgb

import ui


class BoardView(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.bg_color = 'green'

    self.div_num = 16
    #self.check_colors = []

  def draw(self):
    #print(self.frame)
    max_count = self.div_num * self.div_num
    for x in range(self.div_num):
      for y in range(self.div_num):
        h = (x + (y * self.div_num)) / max_count
        fill_color = hsv_to_rgb(h, 1.0, 1.0)
        
        n = (x + (y * self.div_num)) / max_count
        #print(n)

        #ui.set_color(1)
        if x == 0:
          ui.set_color(0)
        else:
          ui.set_color(fill_color)

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

