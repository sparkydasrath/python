"""
The with statement in Python is used with file handling to ensure that
the file is properly closed after its suite finishes, even if an
exception is raised.
"""


def read_file(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    with open(file_path, "r") as file:
        return file.read()


with open("lorem.txt", "r") as file:
    content = file.readline()
    print(content)

# appending to a file
with open("lorem.txt", "a") as file:
    file.write("\nThis is a new line added to the file.")
    print(read_file("lorem.txt"))


# writing to a file
def write_to_file(file_path: str, content: str) -> None:
    """
    Writes content to a file, overwriting any existing content.

    Args:
        file_path (str): The path to the file to be written to.
        content (str): The content to write to the file.
    """
    with open(file_path, "w") as file:
        file.write(content)


# Example usage of write_to_file
write_to_file("example.txt", "This is an example content.")

# This will read the content of the file we just wrote
print(read_file("example.txt"))
