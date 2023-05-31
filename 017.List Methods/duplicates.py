#removing duplicate items in a list

numbers = [5, 3, 1, 5, 2, 7, 4, 6, 3, 5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)
uniques.sort()
print(uniques)