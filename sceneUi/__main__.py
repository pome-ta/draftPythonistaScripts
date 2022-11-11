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
    x = self.width / 2 - w / 2
    wrap = ui.Path.rect(x, 0, w, h)
    ui.set_color(BG_COLOR)
    wrap.fill()

  def layout(self):
    self.scene_view.width = self.width
    self.scene_view.height = self.height * self.height_ratio
    self.scene_view.x = self.width / 2 - self.scene_view.width / 2

  def setup_scene(self):
    scene_view = scene.SceneView()
    scene_view.alpha = 1
    scene_view.frame_interval = 2
    scene_view.shows_fps = True
    scene_view.alpha = 0
    scene_view.scene = self.canvas
    self.add_subview(scene_view)
    self.scene_view = scene_view

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
    self.set_line(50)

  def set_line(self, dire):
    w2, h2 = self.size / 2
    path = ui.Path()
    path.move_to(w2 - 128, h2 - 128)
    path.line_to(w2 + 128, h2 + 128)
    line = scene.ShapeNode(parent=self)
    line.path = path
    line.stroke_color = 'red'
    line.position = self.size / 2

  @ui.in_background
  def update(self):
    pass

  def rgba(self, r, g, b, a=255):
    raba = []
    for j in r, g, b, a:
      t = j / 255
      rgba += t,
    return tuple(rgba)


if __name__ == '__main__':
  TITLE = 'プログラムでお絵描き'

  BG_COLOR = 0.872
  TINT_COLOR = 0.128
  TITLE_COLOR = 0.872
  AF_COLOR = TINT_COLOR

  canvas = Canvas()

  view = MainView(canvas)
  view.present(
    style='fullscreen',
    orientations='portrait',
    title_bar_color=TINT_COLOR,
    title_color=TITLE_COLOR)

