# For loops

people = ['Su Su', 'Aye Aye', 'Khin Khin', 'Hla Hla']

# Simple for loop  (person is each item..)
for person in people: 
    print(person)

# Break
for person in people:
    if person == 'Khin Khin':
        break
    print(person)

# Continue
for person in people:
    if person == 'Khin Khin':
        continue
    print(person)

# Range (Range is similar to for loop in Js)
for i in range(len(people)):
    print(people[i])

for i in range(0, 10): # first parameter is start point
    print(i) 

# While
count = 0
while count <= 11:
    print(f'count: {count}')
    count += 1