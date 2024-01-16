import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the line chart
plt.plot(x, y, label='Line Chart')

# Adding labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Chart')
plt.legend()

# Display the plot
plt.show()
