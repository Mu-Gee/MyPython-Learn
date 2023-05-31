numbers = [5, 3, 1, 2, 7, 4, 6, 3]

#append-adding to the end of the list
numbers.append(20)
print(numbers)

#insert(x,y) x-index y-item to insert
numbers.insert(0, 10)
print(numbers)

#remove a specified item here it is 5
numbers.remove(5)
print(numbers)

#pop-remove last item
numbers.pop()
print(numbers)

#index-check existence of item here being 7
#returns the index of item if present
print(numbers.index(7))

#in operator checking for item
#returns boolean value(True/False)
print(7 in numbers)

#counting occurrences of an item
print(numbers.count(3))

#reverses the list
numbers.reverse()
print(numbers)

#sorting a list in ascending order
numbers.sort()
print(numbers)

#now you can use reverse to sort in descending order
numbers.reverse()
print(numbers)

#making a copy of the list
numbers2 = numbers.copy()
#changing initial list doesn't affect the copied list
numbers.append(5)
print(numbers)
print(numbers2)

#clear entire list
numbers.clear()
print(numbers)