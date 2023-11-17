"""Dice Game"""
from random import randint
roll1: int = randint(1,6)
roll2: int = randint(1,6)
roll3: int = randint(1,6)

idx: int = 0
dice_sum: int = 0
dice_rolls: list[int] = [roll1,roll2,roll3]

while idx < len(dice_rolls):
    dice_sum += dice_rolls[idx]
    idx += 1

print(dice_rolls)
print(dice_sum)