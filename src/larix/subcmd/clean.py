
def command(namespace):
    print('clean command is not implemented yet')

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('clean')
    sub_parser.set_defaults(sub_command='clean')
    sub_parser.set_defaults(func=command)
    
    return subparsers

