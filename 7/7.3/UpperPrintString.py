class UpperPrintString(str):
    def __str__(self) -> str:
        return super().__str__().upper()
