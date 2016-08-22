import argparse
import importlib as il
import larix.config
import larix.sub_commands as sc

def get_parser():
    parser = argparse.ArgumentParser()
    parser.set_defaults(sub_command='')
    parser.add_argument('--log', type=str, default='WARNING')
    parser.add_argument('--config-file', type=str, default=larix.config.app.default_config_file_path)
    parser.add_argument('--config-section', type=str, default='DEFAULT')

    sub_parsers = parser.add_subparsers()

    for module_name in sc.modules():
        module = il.import_module('larix.sub_commands.'+module_name)
        sub_parsers = module.add_sub_parser(sub_parsers)

    return parser

