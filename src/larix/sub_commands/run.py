import larix
import larix.libs.actions as actions

def command(namespace):
    actions.do(namespace)

def add_sub_parser(subparsers):
    action_name = 'run'

    sub_parser = subparsers.add_parser(action_name)
    sub_parser.set_defaults(sub_command=action_name)
    sub_parser.set_defaults(func=command)

    sub_parser.set_defaults(action=action_name)
    sub_parser.set_defaults(target=larix.default_target)

    return subparsers


