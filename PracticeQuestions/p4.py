#Build a basic calculator that performs addition, subtraction, multiplication, division
def calc(a,b,c): 
    def sum(a,b):
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
        print(sum(a,b))
    elif c=='-':
        print(sub(a,b))
    elif c=='*':
        print(mul(a,b))
    elif c=='/':
        print(div(a,b))
    else:
        exit()

try:
    while True:
        a = int(input("a: "))
        b = int(input("b: "))
        c = input("operation(+,-,*,/): ")
        calc(a,b,c)
except Exception as e:
    print(f"error: {e}")
