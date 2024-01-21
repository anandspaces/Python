# count characters in a string
def count_char(a):
    char_count = {}
    for char in a:
        char_count[char] = char_count.get(char,0) + 1
    return char_count

a = input("enter: ")
result = count_char(a)
for char,count_char in result.items():
    print(f"character {char} occurs {count_char} times")