# import numpy as np
from torch import tensor


def linear(vars, params):
    weights, bias = params
    return vars @ weights + bias


if __name__ == "__main__":
    # a = [0.1, 0.5, 0.2, -0.4, -0.2]
    # x = [4, 1, 3, 5, 2]
    weight_tns = tensor([0.1, 0.5, 0.2, -0.4, -0.2])
    var_tns = tensor([4, 1, 3, 5, 2]).float()
    bias = tensor(1)

    print(linear((weight_tns, bias), var_tns))
