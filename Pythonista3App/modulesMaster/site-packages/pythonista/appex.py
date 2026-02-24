#import 'pythonista'
from _appex import is_running_extension, is_widget, is_shortcut, get_input
import _appex
import sys
import ui
PY3 = sys.version_info[0] >= 3

_widget_view = None

if PY3:
    unicode = str
else:
    bytes = str

def _path2url(path):
    if PY3:
        from urllib.parse import urljoin
        from urllib.request import pathname2url
    else:
        from urlparse import urljoin
        from urllib import pathname2url
        return urljoin('file:', pathname2url(path))

def get_attachments(uti='public.data'):
    output_attachments = []
    input_items = get_input()
    for item in input_items:
        attachments = item.get('attachments', None)
        if attachments:
            for attachment_dict in attachments:
                for attachment_type in attachment_dict:
                    if attachment_type == uti or _appex._uti_conforms(attachment_type, uti):
                        output_attachments.append(attachment_dict[attachment_type])
    return output_attachments

def _image_from_attachment(image_attachment, image_type='pil', raw_data=False):
    image_type = image_type.lower()
    if not raw_data and image_type not in ['pil', 'ui']:
        raise TypeError('Unsupported image_type')
    
    use_ui = (image_type != 'pil')
    
    if isinstance(image_attachment, bytes):
        # raw image data
        if raw_data:
            return raw_data
        try:
            if use_ui:
                return ui.Image.from_data(image_attachment)
            else:
                from PIL import Image
                from io import BytesIO
                buffer = BytesIO(image_attachment)
                img = Image.open(buffer)
                return img
        except:
            return None
    elif isinstance(image_attachment, unicode):
        # image path
        if raw_data:
            with open(image_attachment, 'rb') as f:
                return f.read()
        try:
            if use_ui:
                return ui.Image.named(image_attachment)
            else:
                from PIL import Image
                return Image.open(image_attachment)
        except:
            return None

def get_images(image_type='pil'):
    image_attachments = get_attachments('public.image')
    images = []
    if image_attachments:
        for image_attachment in image_attachments:
            img = _image_from_attachment(image_attachment, image_type)
            if img:
                images.append(img)
    return images

def get_image(image_type='pil'):
    image_attachments = get_attachments('public.image')
    if image_attachments:
        return _image_from_attachment(image_attachments[0], image_type)
    return None

def get_image_data():
    image_attachments = get_attachments('public.image')
    if image_attachments:
        return _image_from_attachment(image_attachments[0], raw_data=True)
    return None

def get_images_data():
    image_attachments = get_attachments('public.image')
    images = []
    if image_attachments:
        for image_attachment in image_attachments:
            data = _image_from_attachment(image_attachment, raw_data=True)
            if data:
                images.append(data)
    return images

def get_web_page_info():
    infos = get_attachments('com.omz-software.pythonista.webpage')
    if not infos:
        return {}
    return infos[0]

def get_text():
    text_attachments = get_attachments('public.text')
    if text_attachments:
        return '\n'.join(text_attachments)
    return None

def get_urls():
    url_attachments = get_attachments('public.url')
    urls = []
    if url_attachments:
        for url_attachment in url_attachments:
            if url_attachment.startswith('/'):
                url = _path2url(url_attachment)
                urls.append(url)
            else:
                urls.append(url_attachment)
    if not urls:
        web_info = get_web_page_info()
        try:
            urls.append(web_info['url'])
        except KeyError:
            pass
    return urls

def get_url():
    urls = get_urls()
    if urls:
        return urls[0]
    return None

def get_file_paths():
    url_attachments = get_attachments('public.url')
    paths = []
    if url_attachments:
        for url_attachment in url_attachments:
            if url_attachment.startswith('/'):
                paths.append(url_attachment)
    return paths

def get_file_path():
    url_attachments = get_attachments('public.url')
    if url_attachments:
        first_path = url_attachments[0]
        if first_path.startswith('/'):
            return first_path
    text = get_text()
    if text and text.startswith('/') and os.path.exists(text):
        return text
    return None

def get_vcards():
    vcard_attachments = get_attachments('public.vcard')
    if vcard_attachments:
        return vcard_attachments
    return None

def get_vcard():
    vcard_attachments = get_attachments('public.vcard')
    if vcard_attachments:
        return vcard_attachments[0]
    return None

WIDGET_W = min(556, min(ui.get_screen_size()) - 16)
WIDGET_H = 110 if min(ui.get_screen_size()) >= 760 else 120

class _WidgetSimulatorView (ui.View):
    def __init__(self, v, script_path=None):
        super().__init__(self, frame=(0, 0, WIDGET_W + 16, 560), background_color='#dbdbdb', name='Widget')
        self.expanded = False
        self.script_path = script_path
        self.expanded_height = max(WIDGET_H, v.height)
        self.container = ui.View(frame=(8, 8, WIDGET_W, WIDGET_H + 36), flex='lr', background_color='#ffffff')
        self.container.corner_radius = 10
        v.frame = (0, 36, WIDGET_W, WIDGET_H)
        v.flex = 'wh'
        self.container.add_subview(v)
        title_view = ui.View(frame=(0, 0, WIDGET_W, 36), flex='w', background_color='#f5f5f5')
        self.container.add_subview(title_view)
        if self.expanded_height > 120:
            display_mode_button = ui.Button(title='Show More', font=('<System>', 12), tint_color='#666')
            display_mode_button.frame = (WIDGET_W-80, 0, 80, 36)
            display_mode_button.action = self.toggle_view_mode
            self.container.add_subview(display_mode_button)
        self.add_subview(self.container)
        if self.script_path:
            use_in_today_button = ui.ButtonItem(title='Use in "Today"')
            use_in_today_button.action = self.use_in_today
            self.right_button_items = [use_in_today_button]
	
    def use_in_today(self, sender):
        import console, os, objc_util
        relative_path = os.path.relpath(self.script_path, os.path.expanduser('~/Documents'))
        objc_util.ObjCClass('PA2SharedUserDefaults').sharedDefaults().setObject_forKey_(relative_path, 'WidgetScriptPath')
        console.alert('Widget Script Set', 'The script "%s" is now used in the Pythonista Today widget. You can also change this in Pythonista\'s settings.\n\nThe Pythonista widget is available in the \"Today\" tab of Notification Center, and on the first page of the home/lock screen. You may need to add the widget first (by tapping the "Edit" button at the bottom).\n\nPlease note that widget scripts have a lot less memory available than scripts in the main app, so not all scripts will work as widgets.' % (relative_path,), 'OK', hide_cancel_button=True)
	
    def toggle_view_mode(self, sender):
        self.expanded = not self.expanded
        if self.expanded:
            sender.title = 'Show Less'
            container_height = self.expanded_height + 36
        else:
            sender.title = 'Show More'
            container_height = 110 + 36
        def animation():
            self.container.height = container_height
        ui.animate(animation)

def _simulate_widget(v, script_path=None):
    if v is not None:
        sim_view = _WidgetSimulatorView(v, script_path)
        sim_view.present('sheet')

def set_widget_view(view):
    if view is not None and not isinstance(view, ui.View):
        raise TypeError('view must be ui.View or None')
    if not is_running_extension():
        script_path = None
        try:
            import inspect
            script_path = inspect.currentframe().f_back.f_globals.get('__file__')
        except:
            pass
        _simulate_widget(view, script_path)
    else:
        import console
        console.clear()
        global _widget_view
        _widget_view = view
        _appex.set_widget_view(view)

def get_widget_view():
    return _widget_view

def finish(js=None):
    if js:
        # NOTE: JavaScript isn't executed if shared items were never requested...
        get_web_page_info()
        _appex.finish(js)
    else:
        _appex.finish()
