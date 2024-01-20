# implementation of selection sort
def selection_sort(a):
    for x in range(len(a)):
        min_index = x
        for y in range(x + 1,len(a)):
            if a[y] < a[min_index]:
                min_index = y
        a[x],a[min_index] = a[min_index],a[x]
    return a

a = [10,20,30,40,90,80,70,60,50]
print(selection_sort(a))