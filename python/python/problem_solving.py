'''
name = input("what is ur name? \n")
print(f"Hello {name}, How are you.")

num1 = int ( input("Enter numbers: "))
num2 = int ( input("Enter numbers: "))
sum = num1 + num2
subtract = num1 - num2
multi = num1*num2
div = num1 / num2
print(f'{num1} / {num2} = {div}' )
-------------------------------------------------------
#problem: Receive miles and convert to kilometers
#KM = miles *1.60934
miles = float(input('Enter miles: '))
km = miles * 1.60934
print(f'{miles} miles is {km} kilometers.')
----------------------------------------------------------

#caculation
#store 2 numbes and based on operator print appropriate calculation.


num1,num2,operator = input('Enter 2 numbers and an operator: ').split()
num1 = int(num1)
num2 = int(num2)

try:

    if operator == '+':
      result = num1 + num2
      print(result)
    elif operator == '-':
       result = num1 - num2
       print(result)
    elif operator == '*':
      result = num1*num2
      print(result)
    elif operator == '/':
       result = num1/num2
       print(result)
    elif operator == '%':
       result = num1 % num2
       print(result)
except ValueError:
        print("Value Error")
except ZeroDivisionError:
        print("zero divison")
----------------------------------------------------------

#working with logical operators
age = int(input('Enter age: '))

try:
 if age >= 1 and age <= 18 :
    print('important')
 elif age >= 21 and age <= 50:
    print ('important')
 elif age > 64:
    print('important')
 else:
    print('Not important')
except ValueError as err:
    print(err)
---------------------------------
    
   # use for loop to run throuh numbers and list the odds
for i in range(22):
   if i % 2 != 0:
      print(i)
----------------------------------------------------------
# Have the user enter investment and expected interest
# Each year investment will increase by their investment + their investment * interest rate is
# print out earings after a 10 year period

investment, rate = input("Enter Investment and expected rate: ").split()
investment = float(investment)
rate = float(rate)*0.01

for i in range(10):
   investment = investment + investment*rate

print('Value after 10 years is {:.2f} dollars'.format(investment))
--------------------------------------------------------------------
Print a tree

Height = int(input('Enter Height of tree: '))
Height = int(Height)

spaces = Height - 1
stump = Height - 1
hash = 1

while Height != 0 :
   for i in range(spaces):
      print(' ',end='')
   for i in range(hash):
      print('#',end='')
   print()

   hash+=2
   spaces-=1
   Height-=1

for i in range(stump):
    print(' ',end='')

print('#')
-----------------------------------

#create an acrynom
string = input("Enter the word: ")
string = string.upper()
list_of_words = string.split()
for i in list_of_words:
   print(i[0],end='')

print()
-----------------------------------

# Encryption and Decryption
normal_string = input("Enter your message: ")
#normal_string = normal_string.upper()
secrete_message = ''
for char in normal_string:
   secrete_message+=str(ord(char)-23)

print(secrete_message)
orginal_message = ''
for i in range(0,len(secrete_message)-1,2):
   char_code = secrete_message[i]+secrete_message[i+1]
   orginal_message+=chr(int(char_code)+23)
print(orginal_message)
-----------------------------------------------
# another encrption and decrption
message = input("Enter your message : ")
key = int(input("How many characters should we shift (1 - 26)"))
 
# Prepare your secret message
secret_message = ""
 
# Cycle through each character in the message
for char in message:
 
    # If it isn't a letter then keep it as it is in the else below
    if char.isalpha():
 
        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
 
        # If uppercase then compare to uppercase unicodes
        if char.isupper():
 
            # If bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
 
            # If smaller than A add 26
            elif char_code < ord('A'):
                char_code += 26
 
        # Do the same for lowercase characters
        else:
            if char_code > ord('z'):
                char_code -= 26
            elif char_code < ord('a'):
                char_code += 26
 
        # Convert from code to letter and add to message
        secret_message += chr(char_code)
 
    # If not a letter leave the character as is
    else:
        secret_message += char
print("Encrypted :", secret_message,end='')
'''

employess = []
while True:
 prompt= input("Do you want to enter a name: Y/N ")
 prompt=prompt.lower()
 if prompt == 'y':
  fname,lname = input('Enter employee name: ').split()
  employess.append({'fname':fname,'lname':lname})
 elif prompt=='n':
   break
for xus in employess:
 print(xus['fname'],xus['lname'])































