import math


class Calc:
    def __init__(self):
        pass

    def add(self, first_value: str, second_value: str) -> str:
        if not first_value or first_value.isspace():
            return self.__getStrValueError("Первое значение")

        if not second_value or second_value.isspace():
            return self.__getStrValueError("Второе значение")

        first_value_int: int = self.__parse(first_value)
        second_value_int: int = self.__parse(second_value)

        return str(first_value_int + second_value_int)

    def _parse(self, value: str) -> int:
        result: int = 0
        index: int = len(value) - 1

        for char in value:
            symbol_value: int = self._getIntFromChar(char)
            result = result + symbol_value * math.pow(10, index)

            index -= 1

        return int(result)

    def __getIntFromChar(self, symbol: str) -> int:
        if symbol == "1":
            return 1

        if symbol == "2":
            return 2

        if symbol == "3":
            return 3

        if symbol == "4":
            return 4

        if symbol == "5":
            return 5

        if symbol == "6":
            return 6

        if symbol == "7":
            return 7

        if symbol == "8":
            return 8

        if symbol == "9":
            return 9

        return 0

    def __getStrValueError(self, value_name):
        return "{name} имеет не корректное значение.".format(name = value_name)
