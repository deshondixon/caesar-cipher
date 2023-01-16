import ssl
import nltk
import re

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

word_db = set(words.words())
names_db = set(names.words())


def encrypt(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result


def decrypt(string, shift):
    return encrypt(string, 26 - shift)


def crack(string):
    for shift in range(1, 26):
        attempt = decrypt(string, shift)
        word_list = attempt.split()
        count = 0
        for word in word_list:
            word = re.sub(r"[^A-Za-z]+", "", word)
            if word.lower() in word_db or word in names_db:
                count += 1
        if count / len(word_list) > 0.90:
            return attempt
    return ""


if __name__ == "__main__":
    choice = input("(e)ncrypt, (d)encrypt, (c)rack, or (q)uit: ")
    if choice.lower() == "e":
        msg = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        print(encrypt(msg, shift))
    elif choice.lower() == "d":
        msg = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        print(decrypt(msg, shift))
    elif choice.lower() == "c":
        msg = input("Enter the message to crack: ")
        cracked = crack(msg)
        print("Result: ", cracked)
    elif choice.lower() == "q":
        print("Goodbye!")
    else:
        print("Invalid choice, Goodbye!")
