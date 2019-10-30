import load_dictionary
import sys


def main():
    file = "2of4brif.txt"
    words = load_dictionary.load(file)
    palindromes = []
    for w in words:
        if len(w) > 1 and w == w[::-1]:
            palindromes.append(w)
    print("\nNumber of palindromes found = {}\n".format(len(palindromes)))

    """ 
        You can use the splat operator (designated by
        the *), which takes a list as input and expands it into positional arguments in the
        function call. The last argument is the separator used between multiple list values for
        printing. The default separator is a space (sep=' '), but instead, print each item on a new
        line (sep='\n').
    """

    print(*palindromes, sep="\n")


if __name__ == "__main__":
    main()
