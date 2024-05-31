class Trace:
    def __enter__(self):
        print("Начало выполнения блока with")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print(
                f"Во время выполнения блока with было возбуждено исключение {exc_value}"
            )
        print("Конец выполнения блока with")
        return True


with Trace():
    print("Python generation!")
    print(*123)
    print(1 / 0)
    print(*123)
