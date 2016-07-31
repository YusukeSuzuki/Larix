import larix.args as args

def run():
    parser = args.get_parser()
    namespace = parser.parse_args()

    if namespace.target:
        namespace.func(namespace)
    else:
        parser.print_help()

