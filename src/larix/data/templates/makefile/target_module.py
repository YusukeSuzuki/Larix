"""
makefile target type module
"""

# --------------------------------------------------------------------------------
# module actions
# --------------------------------------------------------------------------------

def init(project, target, namespace):
    """ do configure action """
    pass


def configure(project, target, namespace):
    """ do configure action """
    pass


def build(project, target, namespace):
    """ do build action """
    pass


def clean(project, target, namespace):
    """ do clean action """
    pass


def rebuild(project, target, namespace):
    """ do rebuild ation """
    pass


# --------------------------------------------------------------------------------
# module infomations
# --------------------------------------------------------------------------------

module_actions = [build, configure, clean, rebuild]
module_action_names = [x.__name__ for x in module_actions]
module_action_dict = {x.__name__:x for x in module_actions}

def actions():
    """ return available action names """
    return module_action_names


def do_action(project, target, namespace, action_name):
    """ do ation """
    if action_name in module_action_dict:
        return module_action_dict[action_name](project, target)

    """
    Todo:
        * write error message
    """
    raise ValueError()


def is_action_enable(action_name):
    """ do rebuild ation """
    return action_name in module_action_names


