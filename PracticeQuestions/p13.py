#determine if a string is palindrome
def isPalindrome(a):
    if a[::-1]==a:
        return True
    else:
        return False

a = input("string: ")
if(isPalindrome(a)):
    print("given string is a palindrome")
else:
    print("given string is not a palindrome")