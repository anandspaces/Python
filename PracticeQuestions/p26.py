# generate prime numbers in given range
def prime_num(a,b):
    prime_list = []
    for i in range(a,b + 1):
        prime_flag = True
        for j in range(2,int(i ** (1/2)) + 1):
            if i % j == 0:
                prime_flag = False
                break
        if prime_flag:
            prime_list.append(i)
    return prime_list

a = int(input("enter start range: "))
b = int(input("enter end range: "))
print(f"prime numbers in given range are: {prime_num(a,b)}")