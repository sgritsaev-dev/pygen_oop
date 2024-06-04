from contextlib import contextmanager
import io


@contextmanager
def safe_write(filename):
    buffer = io.StringIO()
    try:
        yield buffer
        dt = buffer.getvalue()
        file = open(filename, "w")
        file.write(dt)
        file.close()
    except Exception as err:
        print(f"Во время записи в файл было возбуждено исключение {type(err).__name__}")


with safe_write("under_tale.txt") as file:
    file.write("Тень от руин нависает над вами, наполняя вас решительностью\n")

with safe_write("under_tale.txt") as file:
    print("Под весёлый шорох листвы вы наполняетесь решительностью", file=file)
    raise ValueError

with open("under_tale.txt") as file:
    print(file.read())
