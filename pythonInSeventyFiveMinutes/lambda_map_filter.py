# Lambdas in python are anonymous functions defined using the `lambda` keyword.

# not the best way to define/use a lambda function
lx = lambda a, b: a + b

print(lx(5, 3))  # Output: 8

# map

x = [1, 2, 3, 4, 5]
print("x =", x)
mp = map(lambda a: a * 2, x)
# map applies the lambda function to each element in the iterable
# and returns a map object which is an iterator that can be converted to a list
print(type(mp))  # Output: <class 'map'>
print("mp=", list(mp))  # Output: [2, 4, 6, 8, 10]


y = range(10)
f = filter(lambda a: a % 3 == 0, y)
# filter returns true of false based on the condition and
# will return only those elements that satisfy the condition
print("f=", list(f))  # Output: [0, 3, 6, 9]
