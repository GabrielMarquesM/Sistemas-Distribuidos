import string
from math import nan


class Expression:
    def __init__(self, id, op, n_1, n_2):
        self.__id: int = id
        self.__op: string = op
        self.__n_1: float = n_1
        self.__n_2: float = n_2

    def solve_expression(self):
        if self.__op == "+":
            return self.__n_1 + self.__n_2
        if self.__op == "-":
            return self.__n_1 - self.__n_2
        if self.__op == "*":
            return self.__n_1 * self.__n_2
        if self.__op == "/":
            return (self.__n_1 / self.__n_2) if (self.__n_2 != 0) else nan

    def get_id(self):
        return self.__id

    def to_string(self):
        result = f"Expression Result: {self.__n_1} {self.__op} {self.__n_2} = {self.solve_expression()}"
        return result
