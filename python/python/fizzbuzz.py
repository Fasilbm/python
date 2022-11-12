'''
list=[]
n=int(input('Enter a number: '))
for n in range (1, n+1):
        if n % 3 == 0 and n % 5 == 0:
             list.append("FizzBuzz")
        elif n % 5 == 0:
           list.append("Buzz") 
        elif  n % 3 == 0 :
         list.append("Fizz") 
        else:
            list.append (str(n))

print(list)
'''
list1=[5,54,5,552]
list2=[]
list2=list1[::-1]
print (list2)