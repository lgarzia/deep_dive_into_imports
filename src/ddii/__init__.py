__version__ = '.1'

print(f"In top level import statement for ddii")

from ddii.subpackage1.subpackage1b import hello_nested_1b #hello_world
hello_nested_1b()

print(f"In top level after all import")