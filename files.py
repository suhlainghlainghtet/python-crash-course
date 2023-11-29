# Python has functions for (CRUD)
# Open file
myFile = open('myFile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('isClosed: ', myFile.closed)
print('mode: ', myFile.mode)

# Write
myFile.write('Hello world...')
myFile.write('I am here.')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write('Where are you?')
myFile.close()

# Read file
myFile = open('myFile.txt', 'r+')
text = myFile.read(200)
print(text)