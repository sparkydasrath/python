import automation

def main():
    print("Hello, World!")
    
    # Call the fibonacci function with n=10
    result = fibonacci(10)
    print(f"The 10th Fibonacci number is: {result}")


def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    return fibonacci(n - 1, b, a + b)


if __name__ == "__main__":
    main()

