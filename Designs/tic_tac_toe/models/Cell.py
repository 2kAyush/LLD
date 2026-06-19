from .Symbol import Symbol

class Cell:
    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__symbol = None

    def set_symbol(self, symbol: Symbol):
        self.__symbol = symbol

    def empty_cell(self):
        # used for undoing move
        self.__symbol = None

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col

    def get_symbol(self):
        if not self.__symbol:
            return None
        return self.__symbol.get_symbol()

    def is_empty(self):
        return self.__symbol == None
