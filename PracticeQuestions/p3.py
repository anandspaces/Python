#determine if a number is odd or even
def isEven(a):
    if a%2==0:
        return True
    else:
        return False

a = int(input("a: "))
if isEven(a):
    print("even")
else:
    print("odd")