# check perfect square
def is_perfect_square(a):
    root = int(a ** 0.5)
    return (root ** 2) == a

num = int(input("enter: "))
if is_perfect_square(num):
    print("it is perfect square")
else:
    print("it is not perfect square")