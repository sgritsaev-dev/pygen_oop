class ProtectedObject:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, name: str):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, name)
