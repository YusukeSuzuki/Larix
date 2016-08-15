import pathlib
import sys
from os.path import relpath

def mkdir_ex(self, mode=0o777, parents=False, exist_ok=False):
    if sys.version_info >= (3,5):
        self.mkdir_orig(mode, parents, exist_ok)
    else:
        try:
            self.mkdir_orig(mode, parents)
        except FileExistsError as e:
            if not exist_ok:
                raise e

if pathlib.Path.mkdir is not mkdir_ex:
    pathlib.Path.mkdir_orig = pathlib.Path.mkdir
    pathlib.Path.mkdir = mkdir_ex

def relpath_to(self, to):
    return pathlib.Path(relpath(str(to), str(self)))

pathlib.Path.relpath_to = relpath_to



