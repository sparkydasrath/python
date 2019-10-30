""" Aiming to load a file from the 12Dicts folder """
import sys


def load(file):
    """ Open text file and return list of lowercase strings """
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            """ 
            the words in the list are converted to lowercase via list comprehension
            List comprehension is a shorthand way to convert a list, or other iterable, into another list.
            """
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(
            "{}\n Error Opening {}. Killing this bitch!".format(e, file),
            file=sys.stderr,
        )
        sys.exit(1)

