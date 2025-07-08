# module use # 1
# from my_module import greet

# greet("test1")

# module use #2
import my_module

my_module.greet("test2")
print(dir(my_module))
