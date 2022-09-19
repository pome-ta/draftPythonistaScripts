import ui
import scene
import editor
from objc_util import ObjCClass, on_main_thread, ObjCInstance

import pdbg

src = '''precision highp float;
uniform float u_time;
varying vec2 v_tex_coord;
void main(){
  //float pi = acos(-1.0);
  float t = u_time;
  vec2 uv = v_tex_coord;
  
  vec3 out_color = vec3(uv.x, uv.y, abs(sin(t)));
  gl_FragColor = vec4(out_color, 1.0);
  
}
'''


class ShaderScene(scene.Scene):
  def setup(self):
    self.shdr = scene.SpriteNode(parent=self)
    _x, _y = self.get_canvas_size()
    self.shdr.size = (_x, _y)
    self.shdr.shader = scene.Shader(src)

    self.shdr.shader.set_uniform('u_resolution', (_x, _x))
    # todo: Initial position before touching
    self.shdr.shader.set_uniform('u_offset', (0.5, 0.5))

  def did_change_size(self):
    _x, _y = self.get_canvas_size()
    self.shdr.size = (_x, _y)
    sx, sy = self.shdr.size / 2
    self.shdr.position = (sx, sy)

  def get_canvas_size(self):
    _x = self.size.x
    _y = self.size.y
    return _x, _y


class CodeEditorView:
  @on_main_thread
  def __init__(self, mode='javascript', ext_kb=True, *args, **kwargs):
    valid_modes = {
      'python': 'OMPythonSyntaxHighlighter',
      'html': 'OMHTMLSyntaxHighlighter',
      'javascript': 'OMJavaScriptSyntaxHighlighter',
      'markdown': 'OMMarkdownSyntaxHighlighter',
      'text': 'OMBaseSyntaxHighlighter'
    }
    if mode not in valid_modes:
      raise ValueError('invalid syntax mode')

    OMTextEditorView = ObjCClass('OMTextEditorView')

    OMSyntaxHighlighterTheme = ObjCClass('OMSyntaxHighlighterTheme')
    SyntaxHighlighter = ObjCClass(valid_modes[mode])

    PA2UITheme = ObjCClass('PA2UITheme')

    theme_dict = PA2UITheme.sharedTheme().themeDict().mutableCopy()

    theme_dict['font-family'] = 'Source Code Pro'
    theme_dict['font-size'] = 13
    theme_dict['background'] = '00000000'

    theme = OMSyntaxHighlighterTheme.alloc().initWithDictionary_(theme_dict)

    f = ((0.0, 0.0), (100.0, 100.0))
    self.editor_view = OMTextEditorView.alloc()
    self.editor_view.initWithFrame_syntaxHighlighterClass_theme_(
      f, SyntaxHighlighter, theme)
    self.editor_view.textView().setAutocapitalizationType_(0)
    self.editor_view.textView().setAutocorrectionType_(1)
    flex_width, flex_height = (1 << 1), (1 << 4)
    self.editor_view.setAutoresizingMask_(flex_width | flex_height)
    #margins = UIEdgeInsets(16, 10, 16, 10)
    #margins = UIEdgeInsets(4, 8, 8, 8)
    #self.editor_view.setMarginsForPortrait_landscape_(margins, margins)
    if ext_kb:
      kb_types = {
        'python': 'KeyboardAccessoryTypePythonCompact',
        'markdown': 'KeyboardAccessoryTypeMarkdownWithoutSnippets',
        'html': 'KeyboardAccessoryTypeHTML',
        'javascript': 'KeyboardAccessoryTypeHTML'
      }
      kb_type = kb_types.get(mode)
      if kb_type:
        OMKeyboardAccessoryView = ObjCClass('OMKeyboardAccessoryView')
        accessory_view = OMKeyboardAccessoryView.alloc()
        accessory_view.initWithType_dark_(kb_type, False)  #.autorelease()
        self.editor_view.setKeyboardAccessoryView_(accessory_view)
        self.editor_view.setKeyboardAppearance_(1)
        #pdbg.state(self.editor_view)

  @property
  #@on_main_thread
  def text(self):
    text_view = self.editor_view.textView()
    text = text_view.text()
    return str(text)

  @text.setter
  #@on_main_thread
  def text(self, new_text):
    if not isinstance(new_text, str):
      raise TypeError('expected string/unicode')
    text_view = self.editor_view.textView()
    text_view.setText_(new_text)

  #@on_main_thread
  def insert_text(self, text):
    if not isinstance(text, basestring):
      raise TypeError('expected string/unicode')
    text_view = self.editor_view.textView()
    text_view.insertText_(text)

  #@on_main_thread
  def replace_range(self, range, text):
    text_view = self.editor_view.textView()
    ns_range = NSRange(range[0], range[1] - range[0])
    text_range = ObjCClass('OMTextRange').rangeWithNSRange_(ns_range)
    text_view.replaceRange_withText_(text_range, text)

  @property
  #@on_main_thread
  def selected_range(self):
    text_view = self.editor_view.textView()
    range = text_view.selectedRange()
    return (range.location, range.location + range.length)

  @selected_range.setter
  #@on_main_thread
  def selected_range(self, new_value):
    text_view = self.editor_view.textView()
    range = NSRange(new_value[0], new_value[1] - new_value[0])
    text_view.setSelectedRange_(range)

  #@on_main_thread
  def begin_editing(self):
    text_view = self.editor_view.textView()
    text_view.becomeFirstResponder()
    print('begin_editing')

  #@on_main_thread
  def end_editing(self):
    text_view = self.editor_view.textView()
    text_view.resignFirstResponder()
    print('end_editing')


class MainView(ui.View):
  def __init__(self, *args, **kwargs):
    ui.View.__init__(self, *args, **kwargs)
    #self.bg_color = 'maroon'
    self.bg_color = 'slategray'
    self.shader_scene = ShaderScene()
    self.ui_scene = scene.SceneView()
    self.ui_scene.shows_fps = True
    self.ui_scene.frame_interval = 2  # 30fps
    self.ui_scene.scene = self.shader_scene

    self.add_subview(self.ui_scene)

    self.cev = CodeEditorView()
    self.cev.text = src

    self.objc_instance.addSubview_(self.cev.editor_view)
    self.reload_btn()

  def layout(self):
    self.ui_scene.width = self.width
    self.ui_scene.height = self.height
    self.shader_scene.did_change_size()

  def reload_btn(self):
    self.reload_icon = self.create_btn('iob:ios7_refresh_outline_32')
    self.reload_icon.action = (lambda sender: self.reload_src())
    self.right_button_items = [self.reload_icon]

  def create_btn(self, icon):
    btn_icon = ui.Image.named(icon)
    return ui.ButtonItem(image=btn_icon)

  def reload_src(self):
    self.shader_scene.shdr.shader = scene.Shader(self.cev.text)


if __name__ == '__main__':
  view = MainView()
  editor.present_themed(
    view, theme_name='Oceanic', style='fullscreen', orientations=['portrait'])
  #view.present(style='fullscreen', orientations=['portrait'])
  #view.present()
