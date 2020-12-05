import sys


def _extract_all_list(*, _d=0):
    # thanks Dadrik for `setdefault`
    return sys._getframe(_d + 1) \
            .f_locals.setdefault('__all__', [])


def _export_by_name(name, _d=0):
    _extract_all_list(_d = _d + 1).append(name)


def export_from_module(thing):
    _export_by_name(thing.__name__, _d=1)
    return thing


export_from_module.by_name = _export_by_name


export_from_module(export_from_module)  # :)

