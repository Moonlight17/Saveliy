import matplotlib.pyplot as plt
import numpy as np
import math

xi = np.arange(-25, 25, .001)
yi1 = [math.sqrt(x - x**2 + 1) if (x - x**2 + 1)>=0 else float('nan') for x in xi]
yi2 = np.tan(xi)

plt.figure(figsize=(10,4))
plt.ylim([-10, 10])
plt.grid()
plt.plot(xi, yi2)
plt.plot(xi, yi1)


plt.show