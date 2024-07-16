import matplotlib.pyplot as plt
import numpy as np

# generate a basic sample point array on x-axis
x = np.arange(0, 6,0.1)

y0 = (abs(-(x-2)))+2
plt.plot(x, y0, color = 'r', linewidth = 3)

# Create a dash cos function sample
y1 = np.cos(x)
plt.plot(x, y1, 'b--', linewidth = 1)
plt.ylim(1, 4)
plt.xlim(1,3)
plt.show()