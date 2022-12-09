# A simple weight converter using if statements
weight = int(input("weight: "))
unit = input('(L)bs or K(g)')
# Convert user input unit to uppercase to make program not case sensitive
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")
