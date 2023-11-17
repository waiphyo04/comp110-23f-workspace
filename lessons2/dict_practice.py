"""Practicing dictionary."""
#constructing a dictionary
ice_cream: dict[str, float] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Made my dictionary")
print(ice_cream)

#Adding elements
ice_cream["mint"] = 24
print("After adding mint...")
print(ice_cream)

#Removing elements
ice_cream.pop("mint")
print("After removing mint")
print(ice_cream)

#Printing the updating the values
print(f"The order of chocolate is {ice_cream["chocolate"]}")

"""Updating the value"""
ice_cream["chocolate"] += 5 # or ice_cream["chocolate"] = 12
print(ice_cream)

#checking the key
print("Is chocolate in ice cream?")
print("chocolate" in ice_cream)

print("Is mint in the ice cream")
print("mint" in ice_cream)

if "chocolate" in ice_cream:
    print(f"There are {ice_cream["chocolate"]} chocolate icecream")
else:
    print("No order of chocolate")

if"mint" in ice_cream:
    print(f"There are {ice_cream["mint"]} orders.")
else:
    print("There is no mint ice cream order")

#for loop and printing out eery flavor and its numbers of orders
for i in ice_cream:
    print(f"{i} has {ice_cream[i]} orders.")


#finding the length
print(f"The number of key value pairs is {len(ice_cream)}.")
temps: dict[str, float] = {"Floride": 72.5, "Raleigh": 56.2}
temps["DC"] = 52.6
print(temps)

