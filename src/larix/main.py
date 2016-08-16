import logging
import larix.args as args

def run():
    parser = args.get_parser()
    namespace = parser.parse_args()
    logging.getLogger().setLevel( logging.getLevelName(namespace.log) )

    if namespace.sub_command:
        namespace.func(namespace)
    else:
        parser.print_help()

