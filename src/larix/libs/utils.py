from pathlib import Path
from larix import project_file_name

def current_project_yaml_path():
    project_dir = Path().cwd() / project_file_name
    project_file_path = None

    for pdir in project_dir.parents:
        if (pdir / project_file_name).exists():
            project_file_path = pdir / project_file_name
            break

    return project_file_path

