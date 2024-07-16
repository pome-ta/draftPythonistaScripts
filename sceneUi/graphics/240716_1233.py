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
    div_count: int = 16
    w, h = self.size
    self.bg_node = scene.Node()
    #self.bg_node.position = [w / 2, h / 2]
    self.add_child(self.bg_node)
    

    sq_size = int(min([w, h]) / 1.1)
    
    bg_rect = ui.Path.rect(0, 0, sq_size, sq_size)
    self.bg_shapeNode = scene.ShapeNode(path=bg_rect,fill_color=0.5,parent=self.bg_node)
    #self.bg_shapeNode.anchor_point=(0.0, 0.0)
    

    cell_size = sq_size / div_count
    for x_i,x_w in enumerate(range(div_count)):
      color = hsv_to_rgb(x_i/div_count, 1.0, 1.0)
      
      
      cell_rect = ui.Path.rect(0, 0, cell_size, cell_size)
      self.cell = scene.ShapeNode(path=cell_rect, fill_color=color,parent=self.bg_shapeNode)
      self.cell.position = (cell_size*x_i, 0.0)
    #self.cell.

  @ui.in_background
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
  
