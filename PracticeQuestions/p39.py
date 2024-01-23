# check punctuation
import string

def is_punctuation(char):
    return char in string.punctuation

test = input("enter a character: ")
if is_punctuation(test):
    print("it is a punctuation")
else:
    print("it is not a punctuation")