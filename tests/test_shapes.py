import pytest
import math
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shape_lib.shapes import Circle, Triangle

def test_circle_area():
    circle = Circle(1)
    assert abs(circle.area() - math.pi) < 1e-6
    circle.radius = 2
    assert abs(circle.area() - math.pi * 4) < 1e-6

def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-1)
    circle = Circle(1)
    with pytest.raises(ValueError):
        circle.radius = -1

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert abs(triangle.area() - 6.0) < 1e-6
    triangle.a = 6
    triangle.b = 8
    triangle.c = 10
    assert abs(triangle.area() - 24.0) < 1e-6

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)
    triangle = Triangle(2, 2, 3)
    with pytest.raises(ValueError):
        triangle.c = 10

def test_right_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_triangle()
    triangle.a = 5
    triangle.b = 5
    triangle.c = 5
    assert not triangle.is_right_triangle()

if __name__ == '__main__':
    pytest.main()