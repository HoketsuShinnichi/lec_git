import matplotlib.pyplot as plt
import numpy as np

def tanh(x):
  return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

x=np.arange(-5.0,5.0,0.1)

plt.plot(x,tanh(x))
plt.ylim(-1.2,1.2)
plt.title('tanh')
plt.xlabel('input')
plt.ylabel('output')

plt.show()
