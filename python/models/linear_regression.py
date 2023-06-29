import numpy as np


def linear_regession(params, variables, const=1):
    return sum(np.array(params) * np.array(variables)) + const


if __name__ == "__main__":
    a = [0.1, 0.5, 0.2, -0.4, -0.2]
    x = [4, 1, 3, 5, 2]

    print(linear_regession(a, x))
