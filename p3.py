import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)
x = np.random.rand(50)
y = 2 * x + 1 + 0.1 * np.random.randn(50)

# Set Seaborn style
sns.set(style="whitegrid")

# Create a scatter plot using Seaborn only
sns.scatterplot(x=x, y=y, color='blue', marker='o', s=50)

# Set plot title and axis labels using Matplotlib
plt.title('Seaborn Scatter Plot Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show the plot
plt.show()
