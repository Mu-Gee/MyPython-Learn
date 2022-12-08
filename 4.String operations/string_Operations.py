# Operations on strings
# Using quotes within quotes
course = "Python's for beginners" 
# Indexing, -ve indices can be used to get the characters from the end
print(course[-6])
# Returns all characters from beginning index (zero) inclusive onwards but excludes the last specified index(three)
print(course[0:3])
# This syntax clones the string though indices are  not specified they are by default assumed by python
print(course[:])
name = 'Mugambi'
print(name[1:-1])
