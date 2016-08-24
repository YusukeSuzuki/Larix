import appdirs
import logging

# --------------------------------------------------------------------------------
# config object
# --------------------------------------------------------------------------------

class ConfigObject(object):
    pass


app = ConfigObject()
user = ConfigObject()


# --------------------------------------------------------------------------------
# initialize
# --------------------------------------------------------------------------------

def init():
    # default constants
    app.log_format='%(levelname)s:%(module)s: %(message)s'
    app.log_level='WARNING'
    app.default_config_file_path = appdirs.user_config_dir('larix')+'/config.ini'
    app.default_target_template = 'makefile'
    app.default_target = 'default'
    app.project_file_name = 'project.yaml'
    app.contents_file_name = 'contents.yaml'
    app.external_package_repository = ''
    app.additional_package_repositories = ''

    logging.basicConfig(format=app.log_format, level=logging.getLevelName(app.log_level))


def init_with_config(config, section):
    for key, value in config[section].items():
        if key.startswith('user_'):
            setattr(user, key, value)
        elif hasattr(app, key):
            setattr(app, key, value)
        else:
            raise ValueError('no such config value: {}'.format(key))

    logging.basicConfig(format=app.log_format, level=logging.getLevelName(app.log_level))
    logger = logging.getLogger()
    logger.format = app.log_format
    logger.level = logging.getLevelName(app.log_level)

init()

