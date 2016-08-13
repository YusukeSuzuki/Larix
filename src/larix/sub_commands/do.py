import larix
import larix.libs.actions as actions

def command(namespace):
    actions.do(namespace)

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('do')
    sub_parser.set_defaults(sub_command='do')
    sub_parser.set_defaults(func=command)

    sub_parser.add_argument('action', type=str)
    sub_parser.add_argument('target', type=str, default=larix.default_target)

    return subparsers

