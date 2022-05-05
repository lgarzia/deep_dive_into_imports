__version__ = '.1'

print(f"In top level import statement for ddii")

def function_top_level_one():
    print('I am function from top level before call to subpackage')
    
from ddii.subpackage1.subpackage1b import hello_nested_1b #hello_world
#hello_nested_1b()
def function_top_level_two():
    print('I am function from top level after call to subpackage')

print(f"Top Level Import Statement Completed")