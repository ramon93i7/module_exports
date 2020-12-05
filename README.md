# module-exports


Single decorator that injects `__name__` of object to export into `__all__`.


```python
from module_exports import export_from_module

@export_from_module
def some_public_function():
  return 4

SOME_CONSTANT = 100500

export_from_module.by_name('SOME_CONSTANT')


#  __all__ == ['some_public_function', 'SOME_CONSTANT']

```
