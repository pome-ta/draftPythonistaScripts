# coding: utf-8
import console
console.show_activity('Preparing...')

import lib2to3.main as _2to3
import libmodernize.main as modernize
import editor, io, os, shutil, tempfile, sys, difflib, ui, time, jinja2

webview = None
new_script = None
script_path = None

html_tpl = '''
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<meta charset="utf-8">
<style>
	body {
		overflow: scroll;
		background-color: {{ background_color }};
		-webkit-text-size-adjust: 100%;
	}
	pre {
		font-family: Menlo;
		font-size: 14px;
		white-space: pre-wrap;
		margin-top: 0;
		margin-bottom: 0;
	}
	.added {
		color: green;
		background-color: rgba(0, 255, 0, 0.1);
	}
	.deleted {
		color: {{ text_color }};
		opacity: 0.6;
		text-decoration: line-through;
	}
	.common {
		color: {{ text_color }};
		opacity: 0.35;
	}
	@media only screen and (max-width: 767px) {
		pre {
			font-size: 12px;
		}
	}
</style>
</head>
<body>
	{% for line in lines %}
		{% if line.startswith('- ') %}
			<pre class="deleted">{{ line[2:] }}</pre>
		{% elif line.startswith('+ ') %}
			<pre class="added">{{ line[2:] }}</pre>
		{% elif line.startswith('  ') %}
			<pre class="common">{{ line[2:] }}</pre>
		{% endif %}
	{% endfor %}

	<script type="text/javascript">
		function findPos(obj) {
			var curtop = 0;
			if (obj.offsetParent) {
				do {
					curtop += obj.offsetTop;
				} while (obj = obj.offsetParent);
				return [curtop];
			}
		}
		window.scroll(0, findPos(document.getElementsByClassName("added")[0]));
	</script>
</body>
</html>
'''

def html_from_diff(diff):
	diff = [line.replace('\t', '&nbsp;&nbsp;&nbsp;&nbsp;') for line in diff]
	theme = editor.get_theme_dict()
	tpl = jinja2.Template(html_tpl)
	html = tpl.render(lines=diff, background_color=theme['background'], text_color=theme['default_text'])
	return html

def apply_changes(sender):
	webview.close()
	path = editor.get_path()
	if path != script_path:
		return
	text = editor.get_text()
	editor.replace_text(0, len(text), new_script)
	
def main():
	global webview, script_path, new_script
	stderr = sys.stderr
	temp_dir = tempfile.mkdtemp()
	try:
		script_path = editor.get_path()
		with open(script_path, 'r', encoding='utf-8') as f:
			old_script = f.read()
		old_lines = old_script.splitlines()
		sys.argv = [__file__, '--no-diffs', '-W', '-n', '-o', temp_dir, script_path]
		sys.stderr = io.StringIO()
		
		new_script_path = None
		console.hide_activity()
		try:
			selected_modernizer = console.alert('Conversion Type', 'Use `modernize` if you\'d like to keep compatibility with Python 2.7. The result may depend on the `six` package (included in Pythonista).\n\nIf you only want to run the script with Python 3, use 2to3 instead.', 'Use modernize', 'Use 2to3')
		except KeyboardInterrupt:
			return
		console.show_activity('Analyzing...')
		if selected_modernizer == 1:
			temp_script_path = os.path.join(temp_dir, os.path.split(script_path)[1])
			shutil.copy(script_path, temp_script_path)
			res = modernize.main(['--no-diffs', '-w', '-n', temp_script_path])
			new_script_path = temp_script_path
		else:
			res = _2to3.main('lib2to3.fixes')
		console.hide_activity()
		if res != 0:
			console.alert('Conversion Failed', 'The selected script could not be converted to Python 3. Please check for syntax errors.', 'OK', hide_cancel_button=True)
			return
		if not new_script_path:
			new_script_path = os.path.join(temp_dir, os.path.split(script_path)[1])
		if os.path.exists(new_script_path):
			with open(new_script_path, 'r', encoding='utf-8') as f:
				new_script = f.read()
			if new_script == old_script:
				console.hud_alert('No changes required', 'success')
				return
			new_lines = new_script.splitlines()
			differ = difflib.Differ()
			diff = differ.compare(old_lines, new_lines)
			html = html_from_diff(diff)
			theme = editor.get_theme_dict()
			webview = ui.WebView()
			webview.background_color = theme['background']
			webview.name = 'Preview'
			webview.load_html(html)
			apply_btn = ui.ButtonItem('Apply', style=2)
			apply_btn.action = apply_changes
			webview.right_button_items = [apply_btn]
			webview.tint_color = theme['tint']
			time.sleep(0.5)
			webview.present(title_bar_color=theme['bar_background'], title_color=theme['default_text'])
		else:
			print('Could not find result:', new_script_path)
			console.alert('Conversion Failed', 'The selected script could not be converted to Python 3. Please check for syntax errors.', 'OK', hide_cancel_button=True)
	finally:
		sys.stderr = stderr
		console.hide_activity()
		shutil.rmtree(temp_dir)

main()
