# calculate a simple interest given the principal,rate and time
def simple_interest(p,r,t):
    return (p*r*t)/100

p = float(input("principal: "))
r = float(input("rate: "))
t = float(input("time: "))
print(f"simple interest = {simple_interest(p,r,t)}")