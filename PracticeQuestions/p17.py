#determine if two strings are anagrams of each other
def isAnagrams(a,b):
    a = a.replace(" ","").lower()
    b = b.replace(" ","").lower()
    return sorted(a)==sorted(b)
    
a = input("string1: ")
b = input("string2: ")
if isAnagrams(a,b):
    print("given strings are anagrams")
else:
    print("given string are not anagrams")