names = ['John', 'Bob', 'James', 'Sarah', 'Zainab']
#You can specify specific indices for items
print(names[4])
print(names[:4])
print(names[2:])
print(names[:-1])

#Like strings the square brackets & collon don't modify the list
print(names)

#You can update specific item using their indices
names[0] = 'Jon'
print(names[0])