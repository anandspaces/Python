#calculate a simple interest given the principal,rate and time
def si(p,r,t):
    return (p*r*t)/100

p = int(input("principal: "))
r = int(input("rate: "))
t = int(input("time: "))
print(f"simple interest = {si(p,r,t)}")