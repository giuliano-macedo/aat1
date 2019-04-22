import matplotlib.pyplot as plt
import numpy as np

xs=np.array(range(0,100))
ys=np.array([i**2 for i in xs])
plt.plot(xs,ys,label="test1")
ys=np.array([i**3 for i in xs])
plt.plot(xs,ys,label="test2")
plt.legend(fontsize=8)
plt.title("Test tiltle")
plt.show()