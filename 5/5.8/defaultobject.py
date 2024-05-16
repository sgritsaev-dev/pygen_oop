class DefaultObject:
    def __init__(self, default=None, **kwargs) -> None:
        self.default = default
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __getattr__(self, attr):
        return self.__getattribute__("default")
