# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using pip package manager
# (including Django) as well as custom modules

# Core modules
import datetime 
from datetime import date
import time
from time import time

# Camelcase module
from camelcase import CamelCase

# Custom module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
print(today)

timeStamp = time()
print(timeStamp)

c = CamelCase()
print(c.hump('hello world ...'))

email = 'test@gmail.com'
if validate_email(email):
    print('Email is good...')
else:
    print('Email is bad...')