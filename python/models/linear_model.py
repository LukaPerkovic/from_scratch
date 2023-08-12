from python.optimization.initiate_parameters import initiate
from python.functions.linear_regression import linear


class LinearModel:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.func = linear

    def initiate(self, bias_size=1):
        return initiate(self.X.shape[1], bias_size)

    def activate(self, params):
        return self.func(self.X, params)
