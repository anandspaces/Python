# calculate median
def median(a):
    sorted_items = sorted(a)
    mid = len(sorted_items) // 2
    if len(sorted_items) % 2 == 0:
        median_value = (sorted_items[mid] + sorted_items[mid - 1]) / 2
    else:
        median_value = sorted_items[mid]
    return median_value

a = [10,20,40,30,80,90,70,60,50]
print(f"result: {median(a)}")