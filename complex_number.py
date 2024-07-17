from typing import Union
from math import atan2, degrees, sqrt


class Complex:
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0) -> None:
        self.x: Union[int, float] = x
        self.y: Union[int, float] = y
        # self.mod = self.modulus()

    def __add__(self, other: 'Complex') -> 'Complex':
        if not isinstance(other, Complex):
            return NotImplemented
        else:
            return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Complex') -> 'Complex':
        if not isinstance(other, Complex):
            return NotImplemented
        else:
            return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union['Complex', int, float]) -> 'Complex':
        if isinstance(other, Complex):
            real = (self.x * other.x) - (self.y * other.y)
            imag = (self.x * other.y) + (self.y * other.x)
            return Complex(real, imag)
        elif isinstance(other, (int, float)):
            return Complex(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __truediv__(self, other: Union['Complex', int, float]) -> 'Complex':
        if isinstance(other, Complex):
            if other.x == 0 and other.y == 0:
                raise ZeroDivisionError("division by zero")
            mag = other.magnitude() ** 2
            real = ((self.x * other.x) + (self.y * other.y)) / mag
            imag = ((self.y * other.x) - (self.x * other.y)) / mag
            return Complex(real, imag)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            else:
                return Complex(self.x / other, self.y / other)
        else:
            return NotImplemented

    def __eq__(self, other: Union['Complex', int, float]) -> bool:
        if isinstance(other, Complex):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, (int, float)):
            return self.modulus() == other
        else:
            return NotImplemented

    def magnitude(self) -> Union[int, float]:
        return self.modulus()

    def modulus(self) -> Union[int, float]:
        return sqrt((self.x * self.x + self.y * self.y))

    def __abs__(self) -> Union[int, float]:
        return self.modulus()

    def argument(self) -> float:
        return degrees(atan2(self.y, self.x))

    def conjugate(self) -> 'Complex':
        return Complex(self.x, -self.y)

    def coordinate(self) -> tuple[Union[int, float], Union[int, float]]:
        return self.x, self.y

    def to_polar(self) -> tuple[Union[int, float], Union[int, float]]:
        return self.magnitude(), self.argument()

    def __str__(self) -> str:
        if self.y >= 0:
            return f"{self.x} + {self.y}"
        else:
            return f"{self.x} - {-self.y}"

    def __repr__(self) -> str:
        return f"Complex({self.x}, {self.y})"
