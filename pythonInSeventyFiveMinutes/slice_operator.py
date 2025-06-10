# SLICE OPERATOR

""" The slice operator in Python lets you extract parts (subsequences) of lists, strings, or other sequence types using the syntax [start:stop:step].

start: index to begin the slice (inclusive)
stop: index to end the slice (exclusive)
step: (optional) how many indices to skip (default is 1) 

"""

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ['hi', 'there', 'how', 'are', 'you']

print('Slicing examples:')

print(x[1:5])      # [2, 3, 4, 5]   (from index 1 to 4)
print(x[:3])       # [1, 2, 3]      (from start to index 2)
print(x[::2])      # [1, 3, 5, 7, 9] (every second element)
print(x[-3:])      # [7, 8, 9]      (last 3 elements)

z = 'hello world'
print(z[0:5])      # 'hello'
z2 = z[::-1]     # 'dlrow olleh'  (reversed string)
print(z)
print(z2)

# Sets do not support slicing !!