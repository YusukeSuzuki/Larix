import larix
import larix.libs.utils as utils
import larix.libs.project as project
from pathlib import Path
import yaml

def command(namespace):
    project_file_path = utils.current_project_yaml_path()

    if not project_file_path:
        raise Exception('{} not found'.format(larix.project_file_name))

    project_file_path = Path(project_file_path)
    project_dir_path = project_file_path.parent

    print(project_file_path)
    (project_dir_path/'build'/namespace.target).mkdir(parents=True, exist_ok=True)
    project_yaml = yaml.load(project_file_path.open().read())
    project.build(project_dir_path, project_yaml, namespace)

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('build')
    sub_parser.set_defaults(sub_command='build')
    sub_parser.set_defaults(func=command)

    sub_parser.add_argument('--target','-t', type=str, default='default')

    return subparsers
