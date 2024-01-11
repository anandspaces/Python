#use list comprehension to create a list of squares of numbers from 1 to 10
def squaredList(list):
    for i in range(len(list)):
        list[i] = list[i]**2
    return list

list = [1,2,3,4,5]
square = squaredList(list)
print(f"List: {square}")