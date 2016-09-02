"""
makefile target type module
"""
import yaml
from jinja2 import Template
import logging
from pathlib import Path
import subprocess as sp
import larix.libs.pathlib

# --------------------------------------------------------------------------------
# module actions
# --------------------------------------------------------------------------------

module_action_list = ['build', 'configure', 'clean', 'rebuild']

def actions():
    """ return available action names """
    return module_action_list


def do_action(project, target, namespace, action_name):
    """ do ation """
    if action_name not in module_action_list:
        raise ValueError('invalid action name')

    print('[{}]'.format(action_name))
    logging.debug(project)
    logging.debug(target)
    logging.debug(namespace)

    settings_template = Template(open('targets/{}/settings.yaml'.format(target['target_template'])).read())
    settings_yaml = yaml.load(settings_template.render(target))

    if not settings_yaml:
        raise Exception('setting.yaml not found')

    Path(target['build_dir']).mkdir(parents=True, exist_ok=True)

    target['project_root'] = Path(target['build_dir']).relpath_to('./')

    for action in settings_yaml[action_name]['actions']:
        if action['type'] == 'parse':
            template = Template(open('targets/{}/{}'.format(target['target_template'], action['file'])).read())
            with open(action['to'], 'w') as f:
                f.write(template.render(target))
        elif action['type'] == 'exec':
            # sp.run() require python 3.5
            # sp.run([action['command']] + action['args'])
            sp.call([action['command']] + action['args'])


def is_action_enable(action_name):
    """ do rebuild ation """
    return action_name in module_action_list


