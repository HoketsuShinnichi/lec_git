import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5.0, 5.0, 0.1)

def sigmoid(x):
  return 1/(1+np.exp(-x))

def softmax(x):
  exp_x=np.exp(x)
  sum_exp_x=np.sum(exp_x)
  return exp_x/sum_exp_x

def relu(x):
  return np.maximum(0, x)

sigmoid_graph = sigmoid(x)
softmax_graph = softmax(x)
relu_graph = relu(x)

plt.plot(x, sigmoid_graph, label='sigmoid')
plt.plot(x, softmax_graph, label='softmax')
plt.plot(x, relu_graph, label='relu')
plt.ylim(-1.2,1.2)
plt.xlabel('input')
plt.ylabel('output')

plt.legend()
plt.show()
