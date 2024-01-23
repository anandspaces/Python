# calculate simple moving average
def simple_moving_average(data,size):
    sma_values = []
    for i in range(len(data) - size):
        window = data[i:i + size]
        sma = sum(window) / size
        sma_values.append(sma)
    return sma_values

numbers = [23,12,34,56,78,45,67,89,23,12]
size = 3
print(f"simple moving average = {simple_moving_average(numbers,size)}")