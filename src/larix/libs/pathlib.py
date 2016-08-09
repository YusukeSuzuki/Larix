import pathlib
import sys

def mkdir_ex(self, mode=0o777, parents=False, exist_ok=False):
    if sys.version_info >= (3,5):
        self.mkdir_orig(mode, parents, exist_ok)
    else:
        try:
            self.mkdir_orig(mode, parents)
        except FileExistsError as e:
            if not exist_ok:
                raise e

pathlib.Path.mkdir_orig = pathlib.Path.mkdir
pathlib.Path.mkdir = mkdir_ex

