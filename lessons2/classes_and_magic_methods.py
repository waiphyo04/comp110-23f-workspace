"""Challenge Question CLass"""

from __future__ import annotations

class Point:
    x: float
    y: float

    def __init__ (self, init_x: float, init_y: float):
        self.x = init_x
        self.y = init_y

    def __str__ (self) -> str:
        return f"{self.x},{self.y}"
    
    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)
    
my_point: Point = Point(1.0, 2.0)
new_point: Point = my_point.scale(2.0)
print(my_point)
print(f"My new point is: {new_point}")
