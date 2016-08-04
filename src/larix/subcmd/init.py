from pathlib import Path
import larix.libs.project

def command(namespace):
    path = Path(namespace.name[0])

    if not path.exists():
        path.mkdir()

    if not path.is_dir():
        raise Exception('name: {} is not directory'.format(path))

    project_name = path.resolve().name

    larix.libs.project.init(path, project_name, namespace.template_name)

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('init')
    sub_parser.set_defaults(target='init')
    sub_parser.set_defaults(func=command)
    sub_parser.set_defaults(template_name='default')
    sub_parser.add_argument('name', type=str, nargs=1)

    return subparsers
