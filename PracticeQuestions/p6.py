# convert a temperature in celsius to farenheit
def convert(a):
    return (a*(9/5))+32

temp = float(input("enter temperature(in celsius): "))
print(f"temperature: {convert(temp)} degree farenheit")