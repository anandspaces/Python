# binary search using recursion
def binary_search(a,low,high):
    if low <= high:
        mid = (high + low) // 2
        if (a[mid] == element):
            return True
        elif a[mid] > element:
            return binary_search(a,low,mid)
        else:
            return binary_search(a,mid+1,high)
    else:
        return False

a = [10,20,30,40,90,80,70,60,50]
element = 40
a.sort()
if binary_search(a,0,len(a)-1):
    print("element found.")
else:
    print("element not found.")