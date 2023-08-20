class SGDOptimizer:
    def __init__(self, model, loss_func):
        self.model = model
        self.loss = loss_func
        self.learning_rate = None

        self.params = model.initiate()

    def _step(self):
        predictions = self.model.activate(self.params)
        loss = self.loss(predictions, self.model.y)
        loss.backward()
        print("PARAMS:", self.params)
        for p in self.params:
            p.data -= self.learning_rate * p.grad
            p.grad = None
        print(loss.detach().mean())

    def apply(self, epochs: int, lr: float):
        self.learning_rate = lr
        print(self.params[0], self.params[1])
        for i in range(epochs):
            self._step()

        print(self.params[0], self.params[1])
        return self.params


if __name__ == "__main__":
    from python.models.linear_model import LinearModel
    from python.loss.error import mse
    import torch

    X = torch.rand(20, 3)
    y = torch.rand(20, 1)

    lm = LinearModel(X, y)

    opt = SGDOptimizer(lm, mse)

    opt.apply(10, 0.0001)

    # lm = linear(X.ndim[0], 1)
    # opt = SGDOptimizer(linear, mse, )
