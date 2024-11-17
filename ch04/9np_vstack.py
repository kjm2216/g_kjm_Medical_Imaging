import numpy as np
import matplotlib.pyplot as plt

a = np.ones((4,3))
b = np.zeros((4,3))
c = np.ones((4,3))*10

ret = np.vstack( (a,b,c) )

print(ret)
plt.imshow(ret, cmap = "gray")
plt.show()


