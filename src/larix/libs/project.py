from jinja2 import Template
import pkg_resources as pr
import yaml
from larix import project_file_name, contents_file_name

def parse_contents(path, name, contents_yaml, template_name, template_dict):
    for entity in contents_yaml['entities']:
        if entity['type'] == 'directory':
            (path/entity['name']).mkdir()
            parse_contents(path/entity['name'], name, entity, template_name, template_dict)

        elif entity['type'] == 'generated':
            resource = pr.resource_string(
                'larix', 'data/templates/{}/{}'.format(template_name, entity['base'])).decode()
            file_template = Template(resource)
            with (path/entity['name']).open('w') as f:
                f.write(file_template.render(template_dict))

        elif entity['type'] == 'file':
            resource = pr.resource_stream(
                'larix', 'data/templates/{}/{}'.format(template_name, entity['base']))
            with (path/entity['name']).open('wb') as f:
                f.write(resource.read())

def init(path, name, template_name):
    template_dict = {
        'name': name
        }

    template_str = pr.resource_string(
        'larix', 'data/templates/{}/{}'.format(template_name, project_file_name))
    template = Template(template_str.decode())

    with (path/project_file_name).open('w') as f:
        f.write(template.render(template_dict))

    contents_yaml_str = pr.resource_string(
        'larix', 'data/templates/{}/{}'.format(template_name, contents_file_name))

    contents_yaml = yaml.load(contents_yaml_str)
    print(name)
    parse_contents(path, name, contents_yaml, template_name, template_dict)


def configure(project_yaml, namespace):
    pass

def build(project_dir_path, project_yaml, namespace):
    build_target = None

    for bt in project_yaml['build_targets']:
        if bt['name'] == namespace.target:
            build_target = bt

    if not build_target:
        raise Exception('build target {} not found'.format(namespace.target))

    build_template_str = \
        (project_dir_path / 'build_templates' / build_target['base']).open().read()
    build_template = Template(build_template_str)

    print(build_template.render())

def run():
    pass

