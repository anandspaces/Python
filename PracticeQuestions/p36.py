# check perfect number
def is_perfect(num):
    if num <= 0:
        return False
    else:
        divisor_sum = sum(i for i in range(1,num) if num % i == 0)
        return divisor_sum == num

num = int(input("enter number: "))
if is_perfect(num):
    print("it is a perfect number")
else:
    print("it is not a perfect number")