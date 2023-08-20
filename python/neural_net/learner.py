class Learner:
    def __init__(self):
        data: None
        architecture: None
        optimizer: None
        loss_function: None
        metrics: None

    def fit(self, epochs, learning_rate):
        pass


if __name__ == "__main__":
    from torch.utils.data import DataLoader
    from python.models.linear_model import LinearModel
    from python.loss.binary_loss import binary_loss
    from python.optimization.basic_optimizer import SGDOptimizer

    sgd = SGDOptimizer(LinearModel, binary_loss)
