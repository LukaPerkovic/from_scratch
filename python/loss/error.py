import numpy as np


def mae(y_pred, y):
    return np.mean(abs(np.array(y_pred) - np.array(y)))


if __name__ == "__main__":
    print(mae([1, 2], [1, 2]))
