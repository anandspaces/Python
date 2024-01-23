# calculate a simple interest given the principal,rate and time
def simple_interest(p,r,t):
    return (p*r*t)/100

p = int(input("principal: "))
r = int(input("rate: "))
t = int(input("time: "))
print(f"simple interest = {simple_interest(p,r,t)}")