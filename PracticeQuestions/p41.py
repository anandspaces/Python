# check quadratic roots
def roots_of_equation(a,b,c):
    d = ((b ** 2) - 4 * a * c)
    root1 = (-b + (d ** 0.5)) / (2 * a)
    root2 = (-b - (d ** 0.5)) / (2 * a)
    return root1,root2

a = float(input("enter value of a: "))
b = float(input("enter value of b: "))
c = float(input("enter value of c: "))
roots = []
roots = roots_of_equation(a,b,c)
print(f"result: {roots}")