
def command(namespace):
    print('run command is not implemented yet')

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('run')
    sub_parser.set_defaults(target='run')
    sub_parser.set_defaults(func=command)
    
    return subparsers

