# determine if a string is palindrome
def is_palindrome(a):
    return a[::-1]==a

a = input("string: ")
if(is_palindrome(a)):
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")