from Bird import Bird

class BirdRegistry:
    __instance = None
    __initialized = False

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not self.__initialized:
            self.__initialized = True
            self.birds_map = {}

    def add_obj(self, name: str, obj: Bird):
        self.birds_map[name] = obj

    def get_new_obj(self, name):
        return self.birds_map[name].Clone()
