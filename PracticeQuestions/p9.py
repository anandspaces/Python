# determine if a number is prime or not
def is_prime(a):
    if a<2:
        return False
    else:
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                return False
    return True

a = int(input("number: "))
if(is_prime(a)):
    print("given number is a prime number")
else:
    print("given number is not a prime number")