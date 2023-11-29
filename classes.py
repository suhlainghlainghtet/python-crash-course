# A class is like a blueprint for creating objects. An object has properties and methods
# (functions) associated with it. Almost everything in Python is an object

# Create Class
class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def greeting(self): 
        return f'I am {self.name} and I am {self.age} years old.' 
    def birthday(self):
        self.age += 1

class Customer (User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance    

    def greeting(self): 
        return f'I am {self.name} and I am {self.age} years old. My balance is {self.balance}'     
    
obj = User('Su Su', 'susu@gmail.com', 20)   
cus = Customer('Alex', 'alex@gmail.com', 30)
cus.set_balance(500)
print('cus..', cus.greeting())

print(obj.name)  
obj.birthday() 
print(obj.greeting())  