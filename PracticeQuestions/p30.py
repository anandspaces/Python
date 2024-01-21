# convert binary to decimal
def binary_decimal(a):
    a = a[::-1]
    result = 0
    for i in range(len(a)):
        result += int(a[i]) * (2 ** i)
    return result

num = input("enter binary number: ")
print(f"decimal number: {binary_decimal(num)}")