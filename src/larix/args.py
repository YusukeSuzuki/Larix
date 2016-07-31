import argparse
import larix.subcmd.init as subcmd_init

def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(target='')

    sub_parser = parser.add_subparsers()
    sub_parser = subcmd_init.add_sub_parser(sub_parser)

    return parser

