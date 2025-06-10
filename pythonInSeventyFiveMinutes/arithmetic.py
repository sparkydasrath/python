x = 9
y = 3
result = x + y  # addition
print("Addition:", result)  # Output: Addition: 12


x1 = 9
y1 = 3.14
result1 = x1 * y1  # multiplication
print("Multiplication:", result1)  # Output: Multiplication: 28.26

x2 = 9
y2 = 3
result2 = x2 / y2  # division
print("Division:", result2)  # Output: Division: 3.0
# division always returns a float in Python 3

# you can convert the result to an integer if needed
result2_int = int(result2)
# Output: Division (as integer): 3
print("Division (as integer):", result2_int)

# if you want to perform integer division, use the // operator
x3 = 10
y3 = 3
result3 = x3 // y3  # integer division
# Output: Integer (floor) Division: 3
print("Integer (floor) Division:", result3)

print(bool(0))  # Output: False
print(bool(1))  # Output: True
