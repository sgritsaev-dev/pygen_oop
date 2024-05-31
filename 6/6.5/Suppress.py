class Suppress:
    def __init__(self, *args) -> None:
        self.exceptions = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.exceptions:
            self.exception = exc_value
        return True


with Suppress(TypeError, ValueError) as context:
    number = int("я число")

print(context.exception)
print(type(context.exception))
