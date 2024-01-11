#generate and print the fibonacci sequence up to a specified number of terms
def fib(a):
    if a<=0:
        return []
    elif a==1:
        return [0]
    elif a==2:
        return [0,1]
    else:
        fibSeries = fib(a-1)
        fibSeries.append(fibSeries[-1]+fibSeries[-2])
        return fibSeries
    
a = int(input("number terms: "))
print(f"fibonacci series: {fib(a)}")