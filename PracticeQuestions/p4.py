# Build a basic calculator that performs addition, subtraction, multiplication, division
def calc(a,b,c): 
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        if b!=0:
            return a/b
        else:
            return 0
    if c=='+':
        print(add(a,b))
    elif c=='-':
        print(sub(a,b))
    elif c=='*':
        print(mul(a,b))
    elif c=='/':
        print(div(a,b))
    else:
        print("invalid operation!")

try:
    while True:
        a = float(input("input 1: "))
        b = float(input("input 2: "))
        c = input("operation(+,-,*,/): ")
        calc(a,b,c)
except Exception as e:
    print(f"error: {e}")
