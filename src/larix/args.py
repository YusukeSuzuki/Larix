import argparse
import larix.sub_commands as sc
import importlib as il

def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(sub_command='')

    sub_parsers = parser.add_subparsers()

    for module_name in sc.modules():
        module = il.import_module('larix.sub_commands.'+module_name)
        sub_parsers = module.add_sub_parser(sub_parsers)

    return parser

