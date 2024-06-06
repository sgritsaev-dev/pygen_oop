class EasyDict(dict):
    def __getattr__(self, key):
        return self.__getitem__(key)


easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

print(easydict['name'])
print(easydict.city)
