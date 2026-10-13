import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2
y3 = np.sin(x)

# Create a linear plot with different line formatting

# Line 1: Solid blue line with markers
plt.plot(
    x, y1, label='Linear', color='blue',
    linestyle='-', marker='o', markersize=4
)

# Line 2: Dashed red line
plt.plot(
    x, y2, label='Quadratic', color='red',
    linestyle='--'
)

# Line 3: Dotted green line with triangles
plt.plot(
    x, y3, label='Sine', color='green',
    linestyle=':', marker='^', markersize=4
)

# Add labels and a legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Plot with Line Formatting')
plt.legend()

# Display the plot
plt.grid()
plt.show()