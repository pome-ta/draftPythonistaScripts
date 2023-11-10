from pathlib import Path
import site
import shutil

print(site.getsitepackages())

print(site.getusersitepackages())

getsitepackages = site.getusersitepackages()

pack_path = Path(getsitepackages)

pack_list= [pack for pack in pack_path.iterdir()]

#print(list(pack_path.glob()))

#/private/var/containers/Bundle/Application/99EB2042-EF33-4FDA-9808-9886DC80C7CC/Pythonista3.app/Frameworks/Py3Kit.framework/pylib/site-packages/pythonista/cb.py
