# Working with strings
course = 'python for Beginners'

# len is a general purpose method for counting characters
print(len(course))

# upper method converts characters to uppercase
print(course.upper())

# lower method converts characters to lowercase
print(course.lower())

# Returns the index of the character given
print(course.find('B'))

# This is used to replace characters/string with other characters/string
print(course.replace('Beginners','Absolute Beginners'))

# Returns a boolean value after checking if the given value is in the string
print('Python' in course)
