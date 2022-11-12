'''
from random import randrange


x, y, name, is_cool = (1, 2.5, 'John', True)
print(x)
print(type(name),name)
name = 'Brad'
age = 37

# Concatenate
#print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))
# F-strings

#print(f'hello my name is {name} and i am {age}')
s = 'JAVA'
# Capitalize string(only fist letter)


print(s.capitalize())
# Swap case (swap up to lower case vise versa)
print(s.swapcase())
# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())



# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor same as numbers
numbers2 = list((1, 2, 3, 4, 5))

print(numbers2[0])

fruits.pop(2)
print(fruits)

# Reverse sort
fruits.sort(reverse=True)

print(fruits)

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Using a constructor same as fruits
 fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

 # Single value needs trailing comma
fruits2 = ('Apples',)

# Delete tuple
del fruits2


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)


# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)

# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')


# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])


lisy = []
num=int(input('Enter the number: '))
for u in range(1,num+1):

    if u%5==0 and u%3==0:
        lisy.append('fizzbuzz')
    elif u%3==0:
        lisy.append('fizz')
    elif u%5==0:
       lisy.append('buzz')
    else:
        lisy.append(u)

print(lisy)

listr=[]
for i in range(5):
 listr.append(randrange(10))
print(listr)

#table = [[0]*5 for i in range (5)]
#for m in multi_table:
 #print(m)
 '''
 class MyStack:

    def __init__(self):
        self.data=[]
        

    def push(self,x: int) -> None:
        self.data.append(data)
        

    def pop(self) -> int:
            return self.data.pop()
        

    def top(self) -> int:
        return self.data(data[len(list)-1])

    def empty(self) -> bool:
        return self.data(self.len(list)==0)
    
'''
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

'''        