# convert decimal to binary
def decimal_binary(a):
    digit = []
    while a!= 1 and a!= 0:
        digit.append(a % 2)
        a //= 2
    digit.reverse()
    return ''.join(map(str,digit))

a = int(input("enter decimal number: "))
print("binary number: " + decimal_binary(a))