from jinja2 import Template
import pkg_resources as pr

def init(path, name):
    template_str = pr.resource_string('larix', 'data/project.yaml')
    template = Template(template_str.decode())
    print(template.render(name=name))

