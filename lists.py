#Lists (it is an array)

# Create a list
fruits = ['Apples', 'Oranges', 'Pears']

#Create an array using Constructor
numbers = list((1, 2, 3, 4, 5))
print(fruits, numbers)

# Append list
fruits.append('Mango')

#Remove list
fruits.remove('Mango')

#Insert to list => 1 is index value
fruits.insert(1, 'Mango')

#Get length
print(len(fruits))

#Pop list
fruits.pop(len(fruits) - 1)

# Change Value
fruits[0] = 'Apples'

#Reverse List
fruits.reverse()

#Sort list
fruits.sort()

#Reverse sort list
fruits.sort(reverse=True)

print(fruits)