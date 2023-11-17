"""File to define River class."""
__author__ = "730651254"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
        
    def check_ages(self):
        """check_ages."""
        new_bear: list[Bear] = []
        for x in self.bears:
            if x.age <= 5:
                new_bear.append(x)
        self.bears = new_bear
        new_fish: list[Fish] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        self.fish = new_fish
        
    def remove_fish(self, amount: int):
        """remove_fish."""
        for x in range(0, amount):
            self.fish.pop(x)
    
    def view_river(self):
        """View_river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
             
    def one_river_day(self):
        """Simulate one day of life in the river."""
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        
    def bears_eating(self):
        """bears_eating."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        
    def check_hunger(self):
        """check_hunger."""
        new_list: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                new_list.append(bears)
        self.bears = new_list

    def repopulate_fish(self):
        """Repopulate fish."""
        off_spring: int = len(self.fish) // 2 * 4
        for x in range(0, off_spring):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """repopulate_bears."""
        offspring: int = len(self.bears) // 2
        for x in range(0, offspring):
            self.bears.append(Bear())

    def one_river_week(self):
        """one_river_week."""
        for x in range(0, 7):
            self.one_river_day()
        return 