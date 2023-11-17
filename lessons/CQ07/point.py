"""Point.py."""

from __future__ import annotations


class Point:
    """class."""
    x: float
    y: float
    
    def __init__(self, x_init: float | int = 0.0, y_init: float | int = 0.0) -> None:
        """init."""
        self.x = x_init
        self.y = y_init
        return 
    
    def scale_by(self, factor: int) -> float | int:
        """scale_by."""
        self.x = self.x * factor
        self.y = self.y * factor 
    
    def scale(self, factor: int) -> Point:
        """scale."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """str."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """multiplication."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, add_input: int | float) -> Point:
        """Addition."""
        new_point: Point = Point(self.x + add_input, self.y + add_input)
        return new_point