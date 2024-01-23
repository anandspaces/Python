# remove duplicates from a list
def remove_duplicates(a):
    return list(set(a))

a = [1,2,2,3,3,3,4,4,5]
result_list = remove_duplicates(a)
print(f"list: {result_list}")