#count the number of vowels and consonants in a string
def count(a):
    vow = 0
    cons = 0
    a = a.lower()
    for i in a:
        if i.isalpha():
            if i=='a' or i=='i' or i=='e' or i=='o' or i=='u':
                vow+=1
            else:
                cons+=1
        else:
            continue
    print(f"number of vowels = {vow}\nnumber of consonants = {cons}")

a = input("string: ")
count(a)          