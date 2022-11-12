from math import *


character_name = "john new"
character_age = 34
# strings

#print(character_age)
#print("There once was a man named " + character_name + ",")
#print("He was "  + str(character_age) + " years old.")
#print("He really liked the name " + character_name + ", ")
#print("But didnt like being " + str(character_age) + ".")
#print(str(character_age) + " is old.")
#print(character_name.upper().islower())
#print(len(character_name))
#print(character_name[2])
#print(character_name.index("n"))
#print(character_name.replace("new", "Wick"))

# maths functions

#print(abs(character_age))
#print(max(7,2))
#print(round(3.54))
#print(pow(7,2))
#print(floor(63.2))
print(ceil(7.246))
#print(sqrt(144))


#input from user

#name = input("Enter ur name: ")
#age = input("Enter ur age: ")
#print("hi " + name + "! you are " +age+ " Nice" )

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = int(num1)+int(num2)
#print(result)

#color = input("Enter a color: ")
#noun = input("Enter a noun: ")
#celebrity = input("Enter a celebrity: ")
#num = 2

#lists

#print("roses are " +color+ ",")
#print(noun+ " are blue")
#print("I love " +celebrity+ ".")
#print("And he loves u " +str(num)+ ".")
friends = ["Kevin", "fasil", "fasil", "hamdu"]
friends[1] = "mike" 
#print(friends[1:]) print starting from index 1 and to last index
#print(friends[-1]) prints last element

# list function

lucky_numbers = [5, 8, 4, 165, 35, 6]
friends.append("creed")
#friends.extend(lucky_numbers)
friends.remove("hamdu")
friends.insert(1, "kelly")
friends2 = friends.copy()
#lucky_numbers.sort() assending order
friends.sort()       
#lucky_numbers.reverse() reverse order
#print(friends)
#print(lucky_numbers)
#friends.clear() remove all
#friends.pop() remove last index
#print(friends.index("fasil"))
#print(friends.count("fasil")) count how many times name is written

# Tuples.........similar to list but they are not editable "immutable"
coor = (4, 5 )

#print(coor[0])

#functions
'''
def say_hi(name, age):
    print("hello " + name + " you are " + str(age))
say_hi("fasil",54)
'''
#def cube(num):
   # return num*num*num
    # result = cube(5)
#print(result)

#if statments

is_male = False
is_tall = False


if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("you are male and short")
elif not(is_male) and is_tall:
    print("You are tall but femlae")
else:
        print("You are a female and short")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    elif num3>=num1 and num3>=num2:
        return num3
    else:
        print(num1)
print(max_num(5,12,1))

#num1=float(input("1st no: "))
#op = input("operator: ")

#num2= float(input("2nd no: "))

#if op == "+":
#    print(num1+num2)
#elif op == "-":
 #   print(num1-num2)
#elif op == "*":
  #  print(num1*num2)
#elif op == "/":
   # print(num1/num2)
#else:
    #print("Invalid operator")

    # dictionary

month_conversions = {
    "Jan":"January",
     "Feb":"February",
     "Mar":"March",
     "May":"May",
     "Jun":"June",
     "Jul":"July",
     "Aug":"August",
      "Sep":"September",
     "Oct":"October",
     "Nov":"November",
     "Dec":"December",
 }

#print(month_conversions.get("Nov", "Invalid key"))
print(month_conversions["Dec"])



# while loops

word = "red"
color_pick = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

#while color_pick != word and not(out_of_guess):
    #if guess_count < guess_limit:
       #color_pick = input("Guess the color: ")
       #guess_count += 1
    #else:
        #out_of_guess = True
#if out_of_guess:
    #print("out off guess")
#else:
    #print("well Done")

    #for loop

for index in range(len(friends)):
    print(friends[index])

def raise_to_pow(base_num, pow_num):
    result = 1
    for index in range(pow_num):
         result = result * base_num
    return result

print(raise_to_pow(2,7))

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]

]

#print(number_grid[1][2])


for row in number_grid:
    for col in row:
        #print(row)



      def translate(phrase):
           translation = ""
           for letter in phrase:
              if letter in "AEIOUaeiou":
                 translation = translation + "g"
              else:
               translation = translation + letter
           return translation
#print(translate(input("Enter a phrase")))


#try/except

#try:
    #ghy = 108/0
    #nu_ber=int(input("Enter a number: "))
    #print(nu_ber)
   
#except DivisionByZero as err:
    #print(err)
    # except ValueError as err:
    #print(err)

   # reading files



employee_file = open("pyspy.txt", "r")

#employee_file.write("Pam - receptionist")
#print(employee_file.readlines())

employee_file.close()


# modules

import useful_modules

#print(useful_modules.roll_dice(2))

# classes and objects

from class_of_student import Student

stu1 = Student("Fasil", "Engineering", 3.1)
stu2 = Student("Jesus", "Business", 3.99)


print(stu1.on_honor_roll())


 #inhertance


 

     
    






 
