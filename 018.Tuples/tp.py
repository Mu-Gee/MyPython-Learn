#Tuples are like lists, can be used to store items
#Tuples cannot be modified, are immutable

numbers = (5, 3, 1, 5, 2, 7, 4, 6, 3, 5)
#numbers.many methods are not available only count & index

print(numbers[0])

#As you see from the error tuples can't be modified
numbers[0] = 10
print(numbers[0])