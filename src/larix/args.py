import argparse
import larix.subcmd.init as subcmd_init
import larix.subcmd
import importlib as il

def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(target='')

    sub_parsers = parser.add_subparsers()

    for module_name in larix.subcmd.modules():
        module = il.import_module('larix.subcmd.'+module_name)
        sub_parsers = module.add_sub_parser(sub_parsers)

    return parser

