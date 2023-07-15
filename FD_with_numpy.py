# FINITE DIFFERENCE WITH NUMPY

import numpy as np
import matplotlib.pyplot as plt

t = np.zeros(1001)  # Preallocate t as a NumPy array of zeros
Temp = np.zeros(1001)  # Preallocate Temp as a NumPy array of zeros
Heat = np.zeros(1001)  # Preallocate Heat as a NumPy array of zeros

deltaT = 0.1  # Example value for deltaT
Cap = 10  # Example value for Cap

for i in range(2, 1001):
    t[i] = i * 300
    Heat[i] = 100 * np.random.uniform(-1.0, 1.0) + 10 * np.sin(t[i])
    Temp[i] = (deltaT / Cap) * Heat[i] + Temp[i - 1]

plt.plot(t, Temp)
plt.xlabel('t')
plt.ylabel('Temp')
plt.show()