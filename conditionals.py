# Conditonals (if, else if, else)

x = 10
y = 50

# Simple if
if y > x:
    print(f'{y} is greater than {x}')

# if/else
if y < x:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elf
if y < x:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} and {y} are equal.')    
else:     
    print(f'{y} is greater than {x}')

#Nested if
if x > 9:
    if x <= 20:
        print(f'{x} is greater than 10 and less than and equal to 20.')

# Logical opeartors (and , or, not)
# and
if x > 2 and y < 100:
    total = x + y
    print('total..', total)
else:
    print('it is something wrong..')

#or
if x > 10 or y < 100:
    print('it is right..')

# not
if not(x == y):
    print('x and y are different..')

#Membership operator is to check whether a sequence is present in the object or not (in , not in)
# in
numbers = [1, 2, 3, 4]
if x in numbers:
    print(x in numbers)
else:
    print(0)

 # not in
if x not in numbers:
    print(x not in numbers) 

# Identity operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location.
# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)