#function
# Create function
def sayHello(name):
    print(f'I am {name}')

sayHello('Su Su')

# Return value function
def getSumNum(num1, num2):
    total = num1 + num2
    return total

nums = getSumNum(5, 5)
print(nums)

# A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expressin. Very Similar to JS arrow function.

getSum = lambda num3, num4 : num3 - num4
total = getSum(3, 4)
print(total)