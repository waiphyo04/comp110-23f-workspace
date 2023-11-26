"""River simulation."""
___author__ = "730651254"

from exercises.ex08.river import River

my_river: River = River(10, 2)
print(my_river.view_river())
print(my_river.one_river_week())