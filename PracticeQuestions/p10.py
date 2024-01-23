# calculate factorial of a given number
def factorial(a):
    if a==1 or a==0:
        return 1
    else: 
        return a*factorial(a-1)

a = int(input("number:"))
print(factorial(a))