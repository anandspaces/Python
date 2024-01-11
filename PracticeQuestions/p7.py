#determine if a year is a leap year
def isLeap(a):
    if a%4==0:
        return True
    else:
        return False

a = int(input("year: "))
if isLeap(a):
    print("it is a leap year")
else:
    print("it is not a leap year")