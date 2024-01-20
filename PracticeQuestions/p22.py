# implementation of insertion sort
def insertion_sort(a):
    for i in range(1,len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

a = [10,20,30,40,90,80,70,60,50]
print(insertion_sort(a))