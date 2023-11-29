# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    "first_name": "Alex",
    "last_name": "Ohmn",
    "age": 20
}
# print(person)

# Create Constructor
person2 = dict(name = "Su Su", age = 22)
print(person2)

# Get Value
print(person["first_name"])
print(person.get('first_name'))

# Add key and Value
person['address'] = 'Yangon'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy dict
person2 = person.copy()
person2['ph'] = '555-555-55'

# Remove items
del person2['ph']
person2.pop('age')
print(person2)

# Clear
person2.clear()
print(person2)

# Get length
print(len(person))

# List of dict
person3 = [
    {
    "first_name": "Alex",
    "last_name": "Ohmn",
    "age": 20
    },
    {
    "first_name": "Su Su",
    "last_name": "Hlaing",
    "age": 25
    },
]
print(person3[0]['age'])