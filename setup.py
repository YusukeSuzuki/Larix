from setuptools import setup, find_packages

setup(
    name = 'Larix',
    version = '0.1',
    package_dir = {'' : 'src'},
    packages = find_packages('src'),
    scripts = ['bin/larix'],
    install_requires = ['appdirs', 'PyYAML', 'Jinja2', 'GitPython'],
    include_package_data=True,
    package_data = {
        'larix': ['data/templates/**/*', 'data/larix/*']
    }
)

