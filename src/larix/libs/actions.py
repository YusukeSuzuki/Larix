from jinja2 import Template
import pkg_resources as pr
import yaml
from pathlib import Path
import re, os, sys, logging
import importlib as il

import larix.config
import larix.libs.utils as utils

def parse_contents_yaml(path, contents_yaml, template_name, template_dict):
    for entity in contents_yaml['entities']:
        if entity['type'] == 'directory':
            (path/entity['name']).mkdir()
            parse_contents_yaml(path/entity['name'], entity, template_name, template_dict)
            continue

        elif (path/entity['name']).exists():
            print('file {} already exists.'.format(str(path/entity['name'])))
        elif entity['type'] == 'generated':
            resource = pr.resource_string(
                'larix', 'data/templates/{}/{}'.format(template_name, entity['base'])).decode()
            with (path/entity['name']).open('w') as f:
                ''' Todo: avoid overwrite '''
                f.write(Template(resource).render(template_dict))
        elif entity['type'] == 'file':
            resource = pr.resource_stream(
                'larix', 'data/templates/{}/{}'.format(template_name, entity['base']))
            with (path/entity['name']).open('wb') as f:
                ''' Todo: avoid overwrite '''
                f.write(resource.read())


def parse_build_target(build_target):
    def parse_variables(line):
        return line

    def glob_files(line):
        files = [str(path) for path in Path().glob( parse_variables(line) )]
        return files

    result = {}

    files_re = re.compile('.+_files$')

    for key, value in build_target.items():
        if files_re.match(key):
            logging.debug(key)
            logging.debug(value)
            result[key] = []
            for line in value:
                result[key].extend(glob_files(line))
        else:
            result[key] = value

    return result


def init(namespace):
    # ----
    path = Path(namespace.name[0])

    if not path.exists():
        path.mkdir()

    if not path.is_dir():
        raise Exception('name: {} is not directory'.format(path))


    # ----
    project_name = path.resolve().name
    target_name =  larix.config.app.default_target
    logging.debug(namespace)
    template_name = namespace.target_template

    template_dict = {
        'project_name': project_name,
        'name': project_name,
        'target_template': template_name,
        'target_name': target_name,
    }

    # ----
    os.chdir(str(path))

    larix_project_yaml_str = pr.resource_string(
        'larix', 'data/larix/{}'.format(larix.config.app.project_file_name)).decode()
    project_yaml_str = pr.resource_string(
        'larix', 'data/templates/{}/{}'.format(
            template_name, larix.config.app.project_file_name)).decode()

    with Path(larix.config.app.project_file_name).open('w') as f:
        f.write(larix_project_yaml_str )
        f.write(Template(project_yaml_str).render(template_dict))

    contents_yaml_str = pr.resource_string(
        'larix', 'data/templates/{}/{}'.format(
            template_name, larix.config.app.contents_file_name)).decode()

    contents_yaml = yaml.load(Template(contents_yaml_str).render(template_dict))
    parse_contents_yaml(Path(), contents_yaml, template_name, template_dict)


def do(namespace):
    # ----
    # read project.yaml
    project_file_path = utils.current_project_yaml_path()

    if not project_file_path:
        raise Exception('{} not found'.format(larix.config.app.project_file_name))

    project_file_path = Path(project_file_path)
    project_dir_path = project_file_path.parent
    project_yamls = yaml.load_all(project_file_path.open().read())

    os.chdir(str(project_dir_path))

    # ----
    # find target
    print('try find target {} for action {}'.format(namespace.target, namespace.action))

    target = None

    for yaml_doc in project_yamls:
        if not 'targets' in yaml_doc:
            continue

        for target in yaml_doc['targets']:
            if target['name'] == namespace.target:
                target = target

    if not target:
        raise Exception('no target {} in {}'.format(namespace.target, larix.config.app.project_file_name))

    target = parse_build_target(target)
    target['template_dir'] = 'targets/{}/'.format(target['target_template'])
    target['build_dir'] = 'build/{}/'.format(target['name'])

    # ----
    # load module
    module_path = Path(target['template_dir']+'module.py')

    if not module_path.exists():
        raise Exception('{} not found'.format(str(module_path)))

    module_loader = il.machinery.SourceFileLoader(
        'targets.{}.module'.format(target['name']), str(module_path))
    sys.dont_write_bytecode = True
    module = module_loader.load_module()

    print('available actions: {}'.format(module.actions()))

    # ----
    # do action
    project = {}
    module.do_action(project, target, namespace, namespace.action)

    # ----
    # finalize
    sys.dont_write_bytecode = False


