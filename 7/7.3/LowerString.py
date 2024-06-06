class LowerString(str):
    def __new__(cls, object=""):
        instance = super().__new__(cls, str(object).lower())
        return instance
