#Find the maximum and minimum values in a list of numbers
def result(list):
    return [max(list),min(list)]

list = [4,5,6,7,8,9]
result_list = result(list)
print(f"max and min are: {result_list}")