import numpy as np


def sigmod(x):
    return 1 / (1+np.exp(-x))

# create "Neuron" class


class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x):
        s = np.dot(self.w, x)
        return sigmod(s)


Xi = np.array([0, 0, 0, 0])  # input data
Wi = np.array([5, 4, 3, 1])  # Weight data
n = Neuron(Wi)  # create object Neuron class

print('Y=', n.y(Xi))
