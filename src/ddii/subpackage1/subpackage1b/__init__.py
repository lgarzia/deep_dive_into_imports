print("in nested subpackage of 1 in b")
import ddii
print("in nested subpackage of 1 in b - after top level import ddii call")

ddii.function_top_level_one()
ddii.function_top_level_two()

def hello_nested_1b():
    print('hello world from nested 1b')