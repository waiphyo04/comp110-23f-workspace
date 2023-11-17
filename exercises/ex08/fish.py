"""File to define Fish class."""
__author__ = "730651254"

class Fish:
    """Fish."""
    age: int

    def __init__(self, inp_age: int = 0):
        """init."""
        self.age = inp_age
        return None
    
    def one_day(self):
        """one_day."""
        self.age += 1
        return None