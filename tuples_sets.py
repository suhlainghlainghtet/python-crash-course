# A Tuple a collection whch is ordered and unchangeable. Allows duplicate members.

# Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# Create Tuple
# fruits2 = tuple((1, 2, 3))

# Single value need tralling comma
fruits2 = ('Pineapples',)
# print(type(fruits2))

# Get value
# print(fruits[1])

# Delete tuple
del fruits2
# print(fruits2)

# Get length
print(len(fruits))

# A set is a collection which is unordered and unindexed. No duplicated members.
# Create Set
fruits_set = {'Apples', 'Oranges'}

# Get length
# print(len(fruits_set))

# Add to set
fruits_set.add('Mangoes')

# Remove from set
fruits_set.remove('Mangoes')
print(fruits_set)

# Check if in set
# print('Apples' in fruits_set)

# Clear
fruits_set.clear()
# print(fruits_set)

#Delete set
del fruits_set
print(fruits_set)