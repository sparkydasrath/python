hello = 'hello world'
print(type(hello))  # <class 'str'>
print(hello.upper())  # HELLO WORLD
print(hello.lower())  # hello world
print(hello.capitalize())  # Hello world
print(hello.title())  # Hello World
print(hello.strip())  # hello world
print(hello.replace('l', 'p'))  # heppo world
print(hello.split('l'))  # ['he', 'o wor', 'd']

# ['hello', 'world', 'welcome', 'to', 'the', 'jungle']
# default split by whitespace
print('hello world welcome to the jungle'.split())

# print(hello.count()) # ERROR must specify a substring to count
print(hello.count('ll'))  # 1
