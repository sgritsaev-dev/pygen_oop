class AttrsNumberObject:
    def __init__(self, **kwargs) -> None:
        self.attrs_num = self.__dict__
        for key, value in kwargs.items():
            self.__setattr__(key, value)

    def __getattribute__(self, name: str):
        if name == "attrs_num":
            return len(object.__getattribute__(self, name))
        return object.__getattribute__(self, name)
