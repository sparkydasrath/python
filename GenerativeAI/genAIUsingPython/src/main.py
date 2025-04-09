from csv_parser import parse_csv, append_to_csv


def main():
    print("Hello, World!")

    # Call the fibonacci function with n=10
    # result = fibonacci(10)
    # print(f"The 10th Fibonacci number is: {result}")
    # Example of how to use the function
    try:
        data = parse_csv("users.csv")
        for row in data:
            print(row)
    except Exception as e:
        print(f"Error: {e}")

    # Example of adding a new row to the CSV file
    try:
        new_user = {
            "name": "alice",
            "age": "33",
            "city": "miami"
        }
        append_to_csv("users.csv", new_user)
        print("Successfully added new user to CSV")
    except Exception as e:
        print(f"Error appending to CSV: {e}")


def fibonacci(n, a=0, b=1):
    if n == 0:
        return a
    return fibonacci(n - 1, b, a + b)


if __name__ == "__main__":
    main()
