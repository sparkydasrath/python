# use the input() function to take user input

input("Enter your name: ")  # this will prompt the user to enter their name

name = input("Enter your name again: ")  # prompt the user to enter their name
print("Hello, " + name + "!")  # this will greet the user

# converting numeric input to number
num = input("Enter a number: ")  # prompt the user to enter a number

# print(num - 5)  # this will cause an error because num is a string

# to fix the error, convert num to an integer or float
print(int(num) - 5)  # this will work if num is a valid integer
