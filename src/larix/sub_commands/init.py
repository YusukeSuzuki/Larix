import larix
import larix.libs.actions as actions

def command(namespace):
    actions.init(namespace)

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('init')
    sub_parser.set_defaults(sub_command='init')
    sub_parser.set_defaults(func=command)

    sub_parser.add_argument(
        '--target-template', type=str, default=larix.default_target_template)
    sub_parser.add_argument('name', type=str, nargs=1)

    return subparsers

