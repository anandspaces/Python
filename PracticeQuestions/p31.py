# calculate the length of the list
def length(a):
    count = 0
    for i in a:
        count +=1
    return count

a = [10,20,30,40,50]
print(f"length: {length(a)}")