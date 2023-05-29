#Finding largest number in the list
numbers = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 0]

#Variable max will hold the largest number
#Assume the first index is the largest number
max = numbers[0]

#Iterate through the list comparing each number to max
for number in numbers:
    if number > max: #check if number is greater than max
        max = number #reset max to new largest number
print(max)        