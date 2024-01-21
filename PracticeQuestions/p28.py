# count the number of words in the given string
def count_words(a):
    words = a.split()
    return len(words)

a = input("enter: ")
print(f"no. of words = {count_words(a)}")
