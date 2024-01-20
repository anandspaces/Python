# calculate factorial using recursion
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else: 
        return a*factorial(a - 1)

a = int(input("Enter number: "))
if a >= 0:
    print("result = {}".format(factorial(a)))
else:
    print("invalid!")