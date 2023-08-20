from torch import sigmoid, where


def binary_loss(predictions, targets):
    predictions = sigmoid(predictions)
    return where(targets == 1, 1 - predictions, predictions).mean()
