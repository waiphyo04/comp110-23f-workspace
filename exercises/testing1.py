"""GIven the string my_words, outputs the same string"""

"""def mimic (my_words: str) -> str:
    return(my_words)

print(mimic("character"))

print doesnot return"""

def mimic (my_words: str, letter_idx: int) -> str:
    if letter_idx >= len(my_words):
        #print("Too high of an idex")
        return("Index too high") #codes end after return
        """output: str = my_words[letter_idx]
        print(output)
    return(output)"""
    return(my_words[letter_idx])

print(mimic("apple",1))


    

