import sys


def export_from_module(thing):
    def _extract_all_list():
        fr = sys._getframe(
            1  # _extract_all_list
            +
            1  # export_from_module
        )
        all_list = fr.f_locals.get('__all__')
        if all_list is None:
            all_list = []
            fr.f_locals['__all__'] = all_list
        return all_list

    all_list = _extract_all_list()
    all_list.append(thing.__name__)
    return thing


export_from_module(export_from_module)
