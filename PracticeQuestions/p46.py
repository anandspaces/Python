# check a number is positive,negative or zero
def check(a):
    if a > 0:
        return "positive!"
    elif a < 0:
        return "negative!"
    else:
        return "zero!"

num = float(input("enter: "))
print(f"result: {check(num)}")