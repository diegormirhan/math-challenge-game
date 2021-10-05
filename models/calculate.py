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
    def _generate_value(self) -> int:
        if self.dificulty == 1:
            return randint(0, 10)
        elif self.dificulty == 2:
            return randint(0, 100)
        elif self.dificulty == 3:
            return randint(0, 1000)
        else:
            return randint(0, 10000)

    @property
    def _generate_result(self) -> int:
        if self.operation == 1:  # somar
            return self.value1 + self.value2
        elif self.operation == 2:  # subtrair
            return self.value1 - self.value2
        else:  # multiplicar
            return self.value1 * self.value2

    @property
    def _op_simbolo(self) -> str:
        if self.operation == 1:
            return '+'
        elif self.operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self, answer: int) -> bool:
        correct: bool = False
        if self.result == answer:
            print('Resposta Correta')
            correct = True
        else:
            print('Resposta Errada')
        print(f'{self.value1} {self._op_simbolo} {self.value2} = {self.result}')
        return correct

    def show_operation(self) -> None:
        print(f'{self.value1} {self._op_simbolo} {self.value2} =')
