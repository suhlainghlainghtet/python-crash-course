#Strings
name = "Su Su"
age = 20

#Concatenate
print("I'm " + name + " and I'm " + str(age) +" years old.")

#Arguments by Position
print("My name is {name} and I'm {age} years old.".format(name=name, age=age))
print(f"Hello, my name is {name} and I'm {age} years old.")

#String Methods
s = 'hello world'

#Capitalize string
print(s.capitalize())

#Upper Case
print(s.upper())

#Lower Case
print(s.lower())

#Swap Case
print(s.swapcase())

#Length
print(len(s))

#Replace
print(s.replace('hello', 'Everyone'))

#Count
print(s.count(s))

#Startswith => return boolean
print(s.startswith('hello'))

#Endswith => return boolean
print(s.endswith('world'))

#Split into a list
print(s.split())

#Find position
print(s.find('e'))

#Is all alphanumeric => return boolean
print(s.isalnum())

#Is all alphabetic => return boolean
print(s.isalpha())

#Is all numeric
print(s.isnumeric())