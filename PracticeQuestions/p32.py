# calculate LCM
def lcm(a,b):
    max_term = max(a,b)
    while True:
        if max_term % a == 0 and max_term % b == 0:
            lcm_result = max_term
            break
        max_term += 1
    return lcm_result

a = int(input("enter first number: "))
b = int(input("enter second number: "))
print(f"lcm: {lcm(a,b)}")