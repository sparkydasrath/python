"""Example wordpair palingrams are nurses run and stir grits.

Our program will examine the core word - we can make the following inferences about the core word:
    1. It can have either an odd or even number of letters.
    2. One contiguous part of the word spells a real word when read backward.
    3. This contiguous part can occupy part or all of the core word.
    4. The other contiguous part contains a palindromic sequence of letters.
    5. The palindromic sequence can occupy part or all of the core word.
    6. The palindromic sequence does not have to be a real word (unless it occupies the whole word).
    7. The two parts cannot overlap or share letters.
    8. The sequence is reversible.

"""
import load_dictionary


def find_palingrams():
    file = "2of4brif.txt"
    word_list = load_dictionary.load(file)
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in word_list:
                    pali_list.append((word, rev_word[end - i :]))
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in word_list:
                    pali_list.append((rev_word[: end - i], word))
    return pali_list


def main():
    palingrams = find_palingrams()
    # sort on first word
    palingrams_sorted = sorted(palingrams)
    print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
    for first, second in palingrams_sorted:
        print("{} {}".format(first, second))


if __name__ == "__main__":
    main()
