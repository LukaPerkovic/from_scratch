from numpy import array, mean
from math import sqrt


def mae(y_pred, y):
    return mean(abs(array(y_pred) - array(y)))


def mse(y_pred, y):
    return mean((array(y_pred) - array(y)) ** 2)


def mape(y_pred, y):
    return mean(abs(array(y_pred) - array(y)) / y) * 100


def rmse(y_pred, y):
    return sqrt(mse(y_pred, y))


if __name__ == "__main__":

    def count(func):
        def wrapper():
            print(len(func()))

        return wrapper

    def split(string):
        return list(string)

    print(split("Hello"))

    split = count(split())
