
def command(namespace):
    print('build command is not implemented yet')

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('build')
    sub_parser.set_defaults(target='build')
    sub_parser.set_defaults(func=command)
    
    return subparsers

