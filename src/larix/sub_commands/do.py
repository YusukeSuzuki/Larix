import larix
import larix.libs.utils as utils
import larix.libs.project as project
from pathlib import Path
import yaml

def command(namespace):
    pass

def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('do')
    sub_parser.set_defaults(sub_command='do')
    sub_parser.set_defaults(func=command)

    sub_parser.add_argument('--target','-t', type=str, default='default')

    return subparsers

