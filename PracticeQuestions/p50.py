# calculate bmi
def bmi(height,weight):
    return weight / (height ** 2)

height = float(input("enter height(in cm): "))
weight = float(input("enter weight(in kg): "))
print(f"body mass index: {bmi(height,weight)}")