class NonNegativeObject:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            if isinstance(value, (int, float)):
                self.__setattr__(key, abs(value))
            else:
                self.__setattr__(key, value)
