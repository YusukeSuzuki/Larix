import pkg_resources as pr
from configparser import ConfigParser
import logging
import os
from pathlib import Path
import larix
import larix.args as args
import larix.config
import larix.libs.pathlib

def app_init():
    user_config_file = Path(larix.config.app.default_config_file_path)
    user_config_file.parent.mkdir(parents=True, exist_ok=True)

    if not user_config_file.exists():
        app_config_ini_str = pr.resource_string('larix', 'data/larix/config.ini').decode()
        user_config_file.open('w').write(app_config_ini_str)


def init(namespace):
    logging.getLogger().setLevel( logging.getLevelName(namespace.log) )

    #   read application config
    app_config_ini_str = pr.resource_string('larix', 'data/larix/config.ini').decode()
    config = ConfigParser(strict=False)
    config.read_string(app_config_ini_str)

    #   load defalut config
    try:
        config.read(namespace.config_file)
    except Exception as e:
        if namespace.config_file != larix.config.user_config_file_path:
            raise e

    section = namespace.config_section

    #   overwrite and append config from environment_variables
    
    for key, value in os.environ.items():
        key = key.lower()
        if key.startswith('larix_app_'):
            config[section][key[len('larix_app_'):]] = value
        elif key.startswith('larix_user_'):
            config[section][key[len('larix_'):]] = value

    #   overwrite and append config from commandline options
    # re-init config
    larix.config.init_with_config(config, section)


def run():
    app_init()

    parser = args.get_parser()
    namespace = parser.parse_args()

    init(namespace)

    if namespace.sub_command:
        namespace.func(namespace)
    else:
        parser.print_help()

