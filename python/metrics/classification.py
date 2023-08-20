from torch import where


def accuracy(predictions, targets):
    where([targets == predictions, 1, 0]).mean()
