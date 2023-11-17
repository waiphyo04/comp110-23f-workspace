"""pets: list[str] = ["Louie", "Bo", "Bear"]
for name in pets:
    print(f"Good boy, {name}")"""

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names),2):
    actual_name: str = names[idx]
    print(actual_name)