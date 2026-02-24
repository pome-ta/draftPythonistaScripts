#LyX
import sys
import importlib
import os
import warnings
from objc_util import ObjCClass
import appex

import _frameworksimporter
import ctypes
from importlib.machinery import ExtensionFileLoader, ModuleSpec, PathFinder

NSBundle = ObjCClass("NSBundle")

class Extension:

    def __init__(self, module):
        self.__original_module__ = module
    
    def __repr__(self):
        return self.__original_module__.__repr__() # __repr__() isn't called for modules

    def __getattribute__(self, attr):
        if attr == "__original_module__" or attr == "__repr__":
            return super().__getattribute__(attr)
        else:
            return getattr(self.__original_module__, attr)

    def __setattr__(self, attr, value):
        if attr == "__original_module__":
            super().__setattr__(attr, value)
        else:
            setattr(self.__original_module__, attr, value)


class FrameworksLoader(ExtensionFileLoader):
    def __init__(self, fullname, path):
        self.fullname = fullname
        super().__init__(fullname.split(".")[-1], path)

    def create_module(self, spec):
        fullname = self.fullname
        mod = sys.modules.get(fullname)
        if mod is None:
            with warnings.catch_warnings(record=True) as w:
                mod = _frameworksimporter.module_from_framework(fullname, spec)
                mod.__repr__ = self.mod_repr
                mod = Extension(mod)
                sys.modules[fullname] = mod
            return mod

        mod.__repr__ = self.mod_repr
        return mod

    def exec_module(self, module):
        pass

    def mod_repr(self):
        return f"<module '{self.fullname}' from '{self.path}'>"


class FrameworksImporter(PathFinder):
    """
    Meta path for importing frameworks to be added to `sys.meta_path`.
    """

    __is_importing__ = False

    def find_spec(self, fullname, path=None, target=None):
        frameworks_path = str(NSBundle.mainBundle().privateFrameworksPath())
        if appex.is_running_extension():
            frameworks_path = os.path.abspath(os.path.join(frameworks_path, '../../../Frameworks'))
        framework_name = fullname.replace(".", "-") + ".framework"
        framework_path = frameworks_path + "/" + framework_name
        #print('framework path:', framework_path)
        binary_path = None
        found = True
        if not os.path.isdir(framework_path):
            not_found = False
            framework_name = (fullname.split(".")[0] + "-") + ".framework"
            framework_path = frameworks_path + "/" + framework_name
            
        if os.path.isdir(framework_path):

            for path in os.listdir(framework_path):
                if (
                    path.endswith(".so")
                    or path == framework_name.split(".framework")[0]
                ):
                    path = framework_path + "/" + path
                    binary_path = path

            if not found:
                lib = ctypes.cdll.LoadLibrary(binary_path)
                try:
                    getattr(lib, "PyInit_" + fullname.split(".")[-1])
                except AttributeError:
                    return None

            loader = FrameworksLoader(fullname, binary_path)
            spec = ModuleSpec(fullname, loader)
            return spec

__all__ = ["FrameworksImporter"]