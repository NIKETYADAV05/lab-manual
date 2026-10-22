
# Practical 4: Count the frequency of each word

import string


def count_words(text):
    normalized = text.lower()
    normalized = normalized.translate(str.maketrans("", "", string.punctuation))
    words = normalized.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def main():
    text = input("Enter a string: ")
    word_count = count_words(text)

    print("\nWord Frequencies:")
    for word, count in word_count.items():
        print(word, ":", count)


if __name__ == "__main__":
    main()
