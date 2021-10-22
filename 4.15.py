import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Perseptron class


class Perceptron(object):

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    # Figure the model for training data.
    # Options
    # X - Training data: array, dimension -
    #   X [N_SAM PLES, N_FEATURES],
    # where
    # N_SAMPLES - the number of samples,
    # P _features - the number of signs,
    # y - target values: array, dimension - y [n_samples]
    # Retset
    # Self: Object
    def fit(self, X, y):
        self.w = np.zeros(1 + X.shape[1])
        self.errors_ = []  # errors : error list

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    '''Calculate clean input'''

    def net_input(self, X):
        return np.dot(X, self.w_[1:]+self.w_[0])

    '''Return a class label after a single jump'''

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)
