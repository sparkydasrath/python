import sys
def main():
    while True:
        word = input("Enter word to translate\n")
        vowels = set("a e i o u")
        if not word: return        
        if (word[0] not in vowels): pig_latin = word[1:] + word[0] + "ay"
        else: pig_latin = word + "way"
        
        print()
        print("{}".format(pig_latin, file=sys.stderr))

        try_again = input("\n\nTry again? (Press Enter else n to stop)\n ")
        if try_again.lower() == "n": return

if __name__ == "__main__":
    main()