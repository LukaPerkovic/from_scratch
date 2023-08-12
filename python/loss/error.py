def mae(y_pred, y):
    return (y_pred - y).abs().mean()


def mse(y_pred, y):
    return ((y_pred - y) ** 2).mean()


def mape(y_pred, y):
    return ((abs(y_pred - y) / y) * 100).mean()


def rmse(y_pred, y):
    return ((y_pred - y) ** 2).mean().sqrt()


if __name__ == "__main__":

    def my_decorator(func):
        def wrapper(*args):
            print("I just want to say:")
            func(*args)
            print("Thanks for coming.")
            return func(*args)

        return wrapper

    @my_decorator
    def no_more(item):
        print("*takes a deep breath*")
        return f"I want no more {item}!"

    no_more("Taco Tuesdays")
