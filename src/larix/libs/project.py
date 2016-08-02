from jinja2 import Template
import pkg_resources as pr
from larix import project_file_name

def init(path, name):
    template_str = pr.resource_string('larix', 'data/'+project_file_name)
    template = Template(template_str.decode())

    with (path/project_file_name).open('w') as f:
        f.write(template.render(name=name))

def configure():
    pass

def build():
    pass

def run():
    pass

