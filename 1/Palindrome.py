def is_palindrome(text):
    normalized = text.lower().replace(" ", "")
    return normalized == normalized[::-1]


def main():
    text = input("Enter a string: ")

    if is_palindrome(text):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    main()
