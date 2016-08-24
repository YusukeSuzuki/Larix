import larix.config as config
import larix.libs.utils as utils
import larix.libs.externals as externals

def init_cmd(namespace):
    pass


def update_cmd(namespace):
    for repository in externals.repository_list():
        repository.setup()
        repository.update()


def list_cmd(namespace):
    packages = {}

    for repository in externals.repository_list():
        repository.setup()
        repo_packages = repository.packages()

        packages = {**packages, **repo_packages}

    for name, package in packages.items():
        out_str = "{}({})".format(name, package.get('version', "x.x.x"))
        print("{:>32}: {}".format(out_str, package.get('description', "")))


def list_local_cmd(namespace):
    pass


def search_cmd(namespace):
    pass


def command(namespace):
    if namespace.externals_command:
        namespace.externals_func(namespace)
    else:
        raise ValueError(
            'no such externals command: {}'.format(namespace.externals_command))


def add_commands(subparsers):
    # list
    sub_parser = subparsers.add_parser('list')
    sub_parser.set_defaults(externals_command='list')
    sub_parser.set_defaults(externals_func=list_cmd)
    # search
    sub_parser = subparsers.add_parser('search')
    sub_parser.set_defaults(externals_command='search')
    sub_parser.set_defaults(externals_func=search_cmd)
    # update
    sub_parser = subparsers.add_parser('update')
    sub_parser.set_defaults(externals_command='update')
    sub_parser.set_defaults(externals_func=update_cmd)
    # list-local
    sub_parser = subparsers.add_parser('list-local')
    sub_parser.set_defaults(externals_command='list-local')
    sub_parser.set_defaults(externals_func=list_local_cmd)

    return subparsers


def add_sub_parser(subparsers):
    sub_parser = subparsers.add_parser('externals')
    sub_parser.set_defaults(sub_command='externals')
    sub_parser.set_defaults(externals_command='')
    sub_parser.set_defaults(func=command)

    externals_parsers = sub_parser.add_subparsers()
    externals_parsers = add_commands(externals_parsers)

    return subparsers


