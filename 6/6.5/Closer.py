class Closer:
    def __init__(self, obj) -> None:
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, *args, **kwargs):
        if hasattr(self.obj, "__exit__"):
            self.obj.close()
        else:
            print("Незакрываемый объект")


with Closer(5) as i:
    i += 1

print(i)
