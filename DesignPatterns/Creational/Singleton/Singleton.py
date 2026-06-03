class Singleton:
    _initialized = False
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, a):
        if self._initialized == False:
            self._initialized = True
            self.a = a

    def print(self):
        print(f"self.a = {self.a}")


a = Singleton(5)
b = Singleton(6)

a.print()
b.print()

print(id(a), "\t", id(b))
print(a is b)