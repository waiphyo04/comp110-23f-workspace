"""Demonstrate while loop by finding low value in the string"""

cards: str = "51239"
card_idx: int = 0
lowest: int = int(cards[0])
while card_idx < 4: #things before while loop don't word anymore
    #we would like to update current_card. So, put current_card into while loop. 
    current_card: int = int(cards[card_idx])
    if current_card < lowest:
        lowest = current_card #put current_card into lowest
    card_idx = card_idx + 1
    
print("The lowest card is " + str(lowest))   