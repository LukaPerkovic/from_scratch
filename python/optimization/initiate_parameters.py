from torch import rand, tensor
from typing import Tuple


def initiate(weight_size: int, bias_size: int) -> Tuple[tensor, tensor]:
    # TODO check if initiating separately the weights and biases causes something
    return (rand(weight_size, requires_grad=True), rand(bias_size, requires_grad=True))


if __name__ == "__main__":
    params = initiate(24, 1)
    w, b = params
    print(w.grad, b.grad)
