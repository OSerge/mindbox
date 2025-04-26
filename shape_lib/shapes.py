from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value <= 0:
            raise ValueError("A side must be positive")
        self._a = value
        self._validate_triangle()

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value <= 0:
            raise ValueError("A side must be positive")
        self._b = value
        self._validate_triangle()

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if value <= 0:
            raise ValueError("A side must be positive")
        self._c = value
        self._validate_triangle()

    def _validate_triangle(self):
        if hasattr(self, '_a') and hasattr(self, '_b') and hasattr(self, '_c'):
            a, b, c = self._a, self._b, self._c
            if (a + b <= c) or (a + c <= b) or (b + c <= a):
                raise ValueError("Invalid triangle sides")

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_triangle(self, tolerance=1e-6):
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < tolerance