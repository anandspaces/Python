# linear search using recursion
def linear_search(a,index):
    if index < (len(a) - 1):
        if a[index] == element:
            return True
        else:
            return linear_search(a,index + 1)
    return False

a = [10,20,30,40,90,80,70,60,50]
element = 40
if linear_search(a,0):
    print("element found!")
else:
    print("element not found!")