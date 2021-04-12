# https://www.codewars.com/kata/5ebcfe1b8904f400208e3f0d

class FuncAdd:
    store = {}

    def __init__(self, func):
        self.name = func.__name__
        if self.name not in self.store.keys():
            self.store[self.name] = []
        self.store[self.name].append(func)

    def __call__(self, *args, **kwargs):
        if self.name not in self.store.keys():
            raise NameError
        return tuple(fn(*args, **kwargs) for fn in self.store[self.name])

    @classmethod
    def delete(cls, func):
        del cls.store[func.name]

    @classmethod
    def clear(cls):
        cls.store.clear()
