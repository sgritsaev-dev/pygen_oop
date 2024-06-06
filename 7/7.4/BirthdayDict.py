from collections import UserDict


class BirthdayDict(UserDict):
    def __setitem__(self, key, item) -> None:
        for k, v in self.data.items():
            if item == v:
                print(
                    f'Хей, {key}, не только ты празднуешь день рождения в этот день!')
                return
        return super().__setitem__(key, item)
