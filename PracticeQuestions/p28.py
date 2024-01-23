# count the number of words in the given string
def count_words(a):
    return len(a.split())

a = input("enter: ")
print(f"no. of words = {count_words(a)}")
