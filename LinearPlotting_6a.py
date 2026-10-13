import matplotlib.pyplot as plt
import numpy as np

m = 5
c = 5

# When y = x
x = np.arange(-4, 4)
y = np.arange(-4, 4)

plt.axvline(color='g')
plt.axhline(color='g')

plt.title("Linear Plotting")

# When y = x
plt.plot(x, y, color='g', marker='D', label='Y=X')

# When y = -x
plt.plot(x, -y, color='k', marker='*', label='Y=-x')

# When slope = 5 and intercept = 5
plt.plot(x, m*x+c, color='r', marker='o', label='Y=5X+5')

# When slope = -5 and intercept = 5
plt.plot(x, -m*x+c, color='b', marker='^', label='Y=-5X+5')

plt.grid()
plt.legend(bbox_to_anchor=(1,0.5))
plt.show()