import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6,0.1)

y0 = -3*(x)+10
plt.plot(x, y0, color = 'b', linewidth = 1)

y1 = (2*x)
plt.plot(x, y1, 'b', linewidth = 1)
plt.ylim(1, 4)
plt.xlim(1,3)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xticks(np.arange(1.,3.5,0.5),['1.0','1.5','2.0','2.5','3.0'])
plt.show()