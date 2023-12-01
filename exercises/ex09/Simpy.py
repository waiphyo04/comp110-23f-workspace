"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Simpy."""
    values: list[float]

    def __init__(self, values: list[float]):
        """init."""
        self.values = values
    
    def __str__(self) -> str:
        """Str."""
        return f"Simpy({self.values})"
    
    def fill(self, x: float, y: int) -> None:
        """Fill."""
        i: int = 0
        new_list: list[float] = []
        while i < y:
            new_list.append(x)
            i += 1
        self.values = new_list
        return self.values
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Arrange."""
        assert step != 0.0
        if start < stop:
            while start < stop:
                self.values.append(start)
                start += step
        else:
            while start > stop:
                self.values.append(start)
                start += step
    
    def sum(self) -> float:
        """Sum."""
        result = sum(self.values)
        return result
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Add."""
        new_list: list = []
        if isinstance(rhs, float):
            for x in self.values:
                new_list.append(x + rhs)
        else:
            i: int = 0
            while i < len(self.values):
                new_list.append(self.values[i] + rhs[i])
                i += 1
        return Simpy(new_list)

    def __pow__(self, abc: Union[Simpy, float]) -> Simpy:
        """Pow."""
        new_list: list = []
        i: int = 0
        if isinstance(abc, float):
            for x in self.values:
                new_list.append(x ** abc)
        else:
            while i < len(self.values):
                new_list.append(self.values[i] ** abc[i])
                i += 1
        return Simpy(new_list)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Eq."""
        new_list: list[bool] = []

        if isinstance(rhs, float):
            for x in self.values:
                if x == rhs:
                    new_list.append(True)
                else:
                    new_list.append(False) 
        else:
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
                i += 1
        return new_list
    
    def __gt__(self, abc: Union[Simpy, float]) -> list[bool]:
        """Gt."""
        new_list: list[bool] = []
        if isinstance(abc, Simpy):
            for x in range(min(len(self.values), len(abc.values))):
                if self.values[x] > abc[x]:
                    new_list.append(True)
                else:
                    new_list.append(False)
        else:
            for x in self.values:
                if x > abc:
                    new_list.append(True)
                else:
                    new_list.append(False) 
        return new_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Getitem."""
        if type(rhs) is int:
            return self.values[rhs]
        elif type(rhs) is list:
            filtered_value = []
            for x in range(len(self.values)):
                if rhs[x]:
                    filtered_value.append(self.values[x])
        return Simpy(filtered_value)
    

max_temps = Simpy([21.0, 30.0, 41.0, 31.0, 45.0, 31.5])
precip = Simpy([0.0, 1.5, 0.1, 0.3, 0.2, 0.8])

p = precip[max_temps > 32.0]
result = sum(p)

print(result)