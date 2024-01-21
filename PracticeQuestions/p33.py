# check armstrong number
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

num = int(input("enter: "))
if is_armstrong(num):
    print("it is an armstrong number")
else:
    print("it is not a armstrong number")