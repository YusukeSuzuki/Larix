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


def configure():
    pass

def build():
    pass

def run():
    pass

