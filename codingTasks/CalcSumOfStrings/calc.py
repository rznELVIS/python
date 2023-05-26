class Calc:
    def __init__(self):
        pass

    def add(self, first_value: str, second_value: str) -> str:
        if not first_value:
            return self.__getStrValueError("Первое значение")

        if first_value.isspace():
            return self.__getStrValueError("Первое значение")

        return "0"

    def __parse(self, value) -> int:
        pass

    def __getStrValueError(self, value_name):
        return "{name} имеет не корректное значение.".format(name = value_name)

print(f'Hello world, calc')