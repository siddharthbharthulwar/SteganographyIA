import numpy as np 
import matplotlib.pyplot as plt 

a = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
a = np.array(a)

b = ([0, 0, 1], [0, 0, 1], [0, 0, 1])

b = np.array(b)

plt.imshow(np.subtract(a, b))
plt.show()