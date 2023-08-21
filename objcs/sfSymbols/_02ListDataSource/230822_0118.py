import ui


class View(ui.View):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)


if __name__ == '__main__':
  view = View()
  view.present(style='fullscreen', orientations=['portrait'])

