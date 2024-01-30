# calculate area of a triangle
def area_of_triangle(a,b):
    return (0.5 * b * a)

def area_of_et(a):
    return ((3 ** 0.5) / 4) * (a ** 2)

def area_of_it(a,b):
    return (0.5 * b * (((a ** 2) - ((b ** 2) / 4)) ** 0.5)) 

def area_of_st(a,b,c):
    s = (a + b + c) / 2
    return ((s * (s - a) * (s - b) * (s - c)) ** 0.5)

dim_of_triangle = int(input("choose input dimensions:\n\
1) base and height\t\
2) equilateral side\t\
3) isosceles sides and base\t\
4) scalene sides\n\
enter: "))
if dim_of_triangle  == 1:
    base = float(input("enter base: "))
    height = float(input("enter area: "))
    print(f"area: {area_of_triangle(base,height)}")
elif dim_of_triangle == 2:
    a = float(input("enter side: "))
    print(f"area: {area_of_et(a)}")
elif dim_of_triangle == 3:
    a = float(input("enter common side: "))
    b = float(input("enter base: "))
    print(f"area: {area_of_it(a,b)}")
elif dim_of_triangle == 4:
    a = float(input("enter side a: "))
    b = float(input("enter side b: "))
    c = float(input("enter side c: "))
    print(f"area: {area_of_st(a,b,c)}")
else:
    print("invalid entry!")