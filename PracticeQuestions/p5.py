# calculate and print the area of a circle
def area(r):
    return (22 / 7) * (r ** 2)

radius = float(input("enter radius of circle: "))
print(f"area of the circle = {area(radius)} square unit")