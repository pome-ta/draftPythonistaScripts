import scene
import ui

TITLE = 'プログラムでお絵描き'

BG_COLOR = 0.872
TINT_COLOR = 0.128
TITLE_COLOR = 0.872
AF_COLOR = TINT_COLOR


class Canvas(scene.Scene):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.background_color = BG_COLOR

  @ui.in_background
  def setup(self):
    self.set_line(1)

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


class View(ui.View):
  def __init__(self):
    self.bg_color = TINT_COLOR
    self.tint_color = TITLE_COLOR
    self.name = TITLE

    btns = self.setup_nav()
    self.right_button_items = btns
    self.canvas = Canvas()
    self.set_up()

  def set_up(self):
    scene_view = scene.SceneView()
    scene_view.alpha = 1
    scene_view.frame_interval = 2
    scene_view.shows_fps = True
    scene_view.alpha = 0
    scene_view.scene = self.canvas
    self.scene_view = scene_view
    self.add_subview(self.scene_view)
    self.view_in()

  @ui.in_background
  def view_in(self):
    def animation():
      self.scene_view.alpha = 1

    ui.animate(animation, duration=.3)

  def draw(self):
    w = self.width
    h = self.height * .96
    x = self.width / 2 - w / 2
    wrap = ui.Path.rect(x, 0, w, h)
    ui.set_color(BG_COLOR)
    wrap.fill()

  def layout(self):
    self.scene_view.width = self.width
    self.scene_view.height = self.height * .96
    self.scene_view.x = self.width / 2 - self.scene_view.width / 2

  def create_navbtn(self, icon):
    btn_icon = ui.Image.named(icon)
    btn = ui.ButtonItem(image=btn_icon)
    return btn

  def setup_nav(self):
    save_icon = 'iob:ios7_download_outline_32'
    save_btn = self.create_navbtn(save_icon)
    save_btn.action = self.save_view
    return [save_btn]

  @ui.in_background
  def save_view(self, sender):
    raw_img = self.canvas.view._debug_quicklook_()
    png = ui.Image.from_data(raw_img, 2.0)
    # fixme: 保存時に1.0 になっちゃう
    png.show()


view = View()
view.present(
  style='fullscreen',
  orientations='portrait',
  title_bar_color=TINT_COLOR,
  title_color=TITLE_COLOR)

