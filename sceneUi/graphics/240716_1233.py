from colorsys import hsv_to_rgb

import scene
import ui


def create_button(icon_name):
  button_icon = ui.Image.named(icon_name)
  button = ui.ButtonItem(image=button_icon)
  return button


class MainView(ui.View):

  def __init__(self, canvas):
    self.bg_color = TINT_COLOR
    self.tint_color = TITLE_COLOR
    self.name = TITLE
    self.height_ratio = 0.96  # todo: safe area

    self.canvas = canvas
    self.scene_view = None

    self.setup_navigationbuttons()
    self.setup_scene()
    self.show_scene()

  def draw(self):
    # todo: init background color
    w = self.width
    h = self.height * self.height_ratio
    wrap = ui.Path.rect(0, 0, w, h)
    ui.set_color(BG_COLOR)
    wrap.fill()

  def layout(self):
    self.scene_view.width = self.width
    self.scene_view.height = self.height * self.height_ratio
    self.scene_view.x = self.width / 2 - self.scene_view.width / 2

  def setup_scene(self):
    scene_view = scene.SceneView()
    scene_view.frame_interval = 2
    scene_view.shows_fps = True
    scene_view.alpha = 0
    scene_view.scene = self.canvas

    self.add_subview(scene_view)
    self.scene_view = scene_view
    self.layout()

  @ui.in_background
  def show_scene(self):

    def dissolve():
      self.scene_view.alpha = 1

    ui.animate(dissolve, duration=.3)

  def setup_navigationbuttons(self):
    show_console_icon = 'iob:ios7_download_outline_32'
    show_console_button = create_button(show_console_icon)
    show_console_button.action = self.show_console

    self.right_button_items = [show_console_button]

  @ui.in_background
  def show_console(self, sender):
    raw_image = self.canvas.view._debug_quicklook_()
    image = ui.Image.from_data(raw_image, 2.0)
    image.show()


class Canvas(scene.Scene):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.background_color = BG_COLOR

  @ui.in_background
  def setup(self):
    #print(self)
    div_count: int = 16
    w, h = self.size
    self.cells_node = scene.Node()
    self.add_child(self.cells_node)
    
    #self.cells_node.point_from_scene = (1.0, 1.0)
    #self.cells_node.position = [w / 2, h / 2]
    print(self.cells_node.point_to_scene((w / 2, h / 2)))
    print(w / 2, h / 2)
    #self.cells_node.position = [w / 2, h / 2]
    #self.cells_node.point_from_scene((w / 2, h / 2))
    
    #self.cells_node.position = [0.0, 0.0]
    

    sq_size = int(min([w, h]) / 1.1)
    path_rect = ui.Path.rect(0.0,0.0,sq_size,sq_size)
    self.bg = scene.ShapeNode(path=path_rect,parent=self)
    self.bg.position = [w / 2, h / 2]
    #self.bg.anchor_point=(1.0,1.0)
    

    cell_size = sq_size / div_count

    self.cells_list = [[
      self.set_cells(cell_size, self.bg, div_count, x, y)
      for x in range(div_count)
    ] for y in range(div_count)]

  def set_cells(self, cell_size, parent, div_count, x, y):
    h = (x + (y * div_count)) / (div_count * div_count)
    fill_color = hsv_to_rgb(h, 1.0, 1.0)
    cell_rect = ui.Path.rect(0, 0, cell_size, cell_size)
    cell = scene.ShapeNode(path=cell_rect,
                           fill_color=fill_color,
                           parent=parent)
    #cell.anchor_point = (0.0, 0.0)
    cell.position = (cell_size * x, cell_size * y)
    return cell

  #@ui.in_background
  def update(self):
    #print(f'{self.t}')  # 画面左下にlog として表示される
    pass


if __name__ == '__main__':
  TITLE = 'プログラミングでお絵描き'

  BG_COLOR = 0.872
  TINT_COLOR = 0.128
  TITLE_COLOR = 0.872
  AF_COLOR = TINT_COLOR

  canvas = Canvas()

  view = MainView(canvas)
  view.present(style='fullscreen',
               orientations='portrait',
               title_bar_color=TINT_COLOR,
               title_color=TITLE_COLOR)

  #scene.run(canvas)

