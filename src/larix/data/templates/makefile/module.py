"""
makefile target type module
"""

# --------------------------------------------------------------------------------
# module actions
# --------------------------------------------------------------------------------

def configure(project, target, namespace):
    """ do configure action """
    print('configure')


def build(project, target, namespace):
    """ do build action """
    print('build')


def clean(project, target, namespace):
    """ do clean action """
    print('clean')


def rebuild(project, target, namespace):
    """ do rebuild ation """
    print('rebuild')


# --------------------------------------------------------------------------------
# module infomations
# --------------------------------------------------------------------------------

module_action_dict = {x.__name__:x for x in
    [build, configure, clean, rebuild]}

def actions():
    """ return available action names """
    return list(module_action_dict.keys())


def do_action(project, target, namespace, action_name):
    """ do ation """
    if action_name in module_action_dict:
        return module_action_dict[action_name](project, target, namespace)

    """
    Todo:
        * write error message
    """
    raise ValueError()


def is_action_enable(action_name):
    """ do rebuild ation """
    return action_name in module_action_dict


