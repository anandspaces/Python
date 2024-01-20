# claculate gcd
def gcd(a,b):
    if a > b:
        while b:
            a,b = b,a % b
        return a
    else:
        while a:
            b,a = a,b % a
        return b
        
a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
if a > 0 and b > 0:
    print(f"result = {gcd(a,b)}")
else:
    print("invalid!")