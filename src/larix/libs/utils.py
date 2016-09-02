from pathlib import Path
from larix.config import app as app_config

def current_project_yaml_path():
    # to do find project file by argument or environment variable
    project_dir = Path().cwd() / app_config.project_file_name
    project_file_path = None

    for pdir in project_dir.parents:
        if (pdir / app_config.project_file_name).exists():
            project_file_path = pdir / app_config.project_file_name
            break

    return project_file_path

def flatten_nested_list(l):
    if isinstance(l, (list, tuple)) and not isinstance(l, str):
        return reduce( lambda x, y: x + flatten(y), l, [])

    return [l]

