# conditional operators in python are used to evaluate conditions 
# and execute code based on the result of those conditions.

# Example of using conditional operators in Python

less_than_10 = 5 < 10
print("5 is less than 10:", less_than_10)

# equality operator
equal = (5 == 5)
print("5 is equal to 5:", equal)

not_equal = (5 != 10)
print("5 is not equal to 10:", not_equal)

# greater than operator
greater_than_10 = (15 > 10)
print("15 is greater than 10:", greater_than_10)

# less than or equal to operator
less_than_or_equal = (5 <= 5)
print("5 is less than or equal to 5:", less_than_or_equal)

print('is a > Z? ', 'a' > 'Z')  # comparing characters
# ASCII values for comparison
print('ord of a =', ord('a'), 'ord of Z =', ord('Z'))  

# using chr
print('chr(97) =', chr(97))  # prints 'a'

print("Ordinal values of lowercase alphabet:")
for c in range(ord('a'), ord('z') + 1):
    print(f"{chr(c)}: {c}", end='  ')
print("\nOrdinal values of uppercase alphabet:")
for c in range(ord('A'), ord('Z') + 1):
    print(f"{chr(c)}: {c}", end='  ')

print('a' > 'ab')  # comparing strings

# CHAINED CONDITIONAL OPERATORS
x = 7
y = 8
z = 10

result1 = x == y
result2 = y > x
result3 = z < x + 2

print("Result of first condition (x == y):", result1)
print("Result of not first condition (y > x):", not result1)

result4 = result1 or result2 and result3
print("Result of chained conditional operators:", result4)
