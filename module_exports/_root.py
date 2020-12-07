import sys


def _export_from_module(names, _depth=0):
    'Appends `names` to `__all__`-list `_depth`-frames up.'
    # [*]: thanks Dadrik for `setdefault`
    sys._getframe(_depth + 1) \
        .f_locals.setdefault('__all__', []) \
        .extend(names)


class _ExportSyntax:
    __slots__ = ()

    def __call__(self, *things):
        _export_from_module(
            (thing.__name__ for thing in things),
            _depth=1
        )
        if len(things) == 1:
            # return exported object
            # if used as decorator
            # (for one thing)
            return things[0]

    @staticmethod
    def by_name(*names):
        _export_from_module(names, _depth=1)


export_from_module = _ExportSyntax()


export_from_module.by_name('export_from_module')  # :)

