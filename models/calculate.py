# Calculate
from random import randint


class Calculate:

    def __init__(self: object, dificulty: int) -> None:
        """

        :rtype: object
        """
        self.__dificulty: int = dificulty
        self.__value1: int = self._generate_value
        self.__value2: int = self._generate_value
        self.__operation: int = randint(1, 3)  # somar = 1; subtrair = 2; multiplicar = 3
        self.__result: int = self._generate_result

    @property
    def dificulty(self) -> int:
        return self.__dificulty

    @property
    def value1(self) -> int:
        return self.__value1

    @property
    def value2(self) -> int:
        return self.__value2

    @property
    def operation(self) -> int:
        return self.__operation

    @property
    def result(self) -> int:
        return self.__result

    def __str__(self) -> str:
        op = ''
        if self.operation == 1:
            op = 'Somar'
        elif self.operation == 2:
            op = 'Subtrair'
        elif self.operation == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação Desconhecida!'

        return f'Value 1: {self.value1} \n' \
               f'Value 2: {self.value2} \n' \
               f'Dificulty: {self.dificulty} \n' \
               f'Operação: {op}'

    @property
    def _generate_value(self: object) -> int:
        pass

    @property
    def _generate_result(self: object) -> int:
        pass

    def check_result(self: object, answer: int) -> bool:
        pass

