# determine if a number is odd or even
def is_even(a):
    return a%2==0

a = int(input("enter: "))
if is_even(a):
    print("even")
else:
    print("odd")