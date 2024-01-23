# determine if a year is a leap year
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
       
a = int(input("year: "))
if is_leap(a):
    print("it is a leap year")
else:
    print("it is not a leap year")