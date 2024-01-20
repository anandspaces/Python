# implement bubble sort 
def bubble_sort(a):
    size = len(a)
    for y in range(size):
        for x in range(0,size-y-1):
            if a[x] > a[x + 1]:
                a[x],a[x + 1] = a[x + 1],a[x]
    return a

a = [10,20,30,40,90,80,70,60,50]
print(bubble_sort(a))