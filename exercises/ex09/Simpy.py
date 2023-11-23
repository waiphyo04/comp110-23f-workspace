"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    values: list[float]

    def __init__(self, values) -> list[float]:
        self.values = values

    def __str__(self) -> str:
        return f"Simpy({self.values})"
    
    def fill(self, x: float, y: int) -> list[float]:
        i: int = 0
        while i < y:
            self.values.append(x)
        return self.values
    
    def arrange(self, start: float, stop: float, step: float) -> list[float]:
        assert step != 0.0
        while start < stop:
            self.values.append(start)
            start += step
        return self.values
    
    def sum(self):
        return sum(self.values)
    
    def __add__(self, rhs: float | Simpy) -> Simpy:
        new_list: list = []
        if type(rhs) is float:
            for x in self.values:
                new_list.append(x + rhs)
            self.values = new_list
        else:
            i: int = 0
            while i < len(self.values) and len(rhs):
                self.values[i] += rhs[i]
                new_list.append(self.values[i])
                i += 1
            self.values = new_list
        return self.values

    def __pow__(self, abc: float | Simpy) -> Simpy:
        new_list: list = []
        if type(abc) is float:
            for x in self.values:
                new_list.append(x ** abc)
            self.values = new_list
        else:
            i: int = 0
            while i < len(self.values) and len(abc):
                self.values[i] ** abc[i]
                new_list.append(self.values[i])
                i += 1
            self.values = new_list
        return self.values

    def __eq__(self, abc: Simpy | float):
        new_list: list[bool] = []
        if type(abc) is Simpy:
            for x in range(min(len(self.values), len(abc))):
                if self.values[x] == abc[x]:
                    new_list.append(True)
                else:
                    new_list.append(False)
        else:
            for x in self.values:
                if x is abc:
                    new_list.append(True)
                else:
                    new_list.append(False) 
        return new_list
           
    def __gt__(self, abc: Simpy | float):
        new_list: list[bool] = []
        if type(abc) is Simpy:
            for x in range(min(len(self.values), len(abc))):
                if self.values[x] > abc[x]:
                    new_list.append[True]
                else:
                    new_list.append[False]
        else:
            for x in self.values:
                if x is abc:
                    new_list.append(True)
                else:
                    new_list.append(False) 
            return new_list

    def __getitem__(self, rhs: int | list[bool]) -> float | Simpy:
        
        return self.values[rhs]

#ones: Simpy = Simpy([1.0, 1.0, 1.0, 1.0, 1.0])
#twos = Simpy.fill(2.0, 4)
#print(twos)

twos = Simpy([])
print(twos.fill(2.0, 3))



 # TODO: Your constructor and methods will go here.