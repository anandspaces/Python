# generate random number
import random

def generate_random(a,b):
    return random.randint(a,b)

a = int(input("enter: "))
b = int(input("enter: "))
print(f"random number between {a},{b}: {generate_random(a,b)}")