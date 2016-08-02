
def command(namespace):
    print('configure command is not implemented yet')

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('configure')
    sub_parser.set_defaults(target='configure')
    sub_parser.set_defaults(func=command)
    
    return subparsers

