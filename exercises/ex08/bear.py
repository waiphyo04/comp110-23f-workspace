"""File to define Bear class."""
__author__ = "730651254"


class Bear:
    """Bear."""

    age: int
    hunger_score: int

    def __init__(self, inp_age: int = 0, inp_hs: int = 0):
        """init."""
        self.age = inp_age
        self.hunger_score = inp_hs
        return None
    
    def one_day(self):
        """one_day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """eat."""
        self.hunger_score += num_fish

    
