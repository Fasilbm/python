import random
import math


randlist=[6,4,5]



i = len(randlist)-1

while i> 1:
   j=0
   while j<i:
        if randlist[j] > randlist[j+1]:
           temp = randlist[j]
           randlist[j] = randlist[j+1]
           randlist[j+1] = temp
        else:
            j+=1
        
 
   i-=1


for k in randlist:
    print(k, end=',')
print()




def get_area (shape):
    if shape ==  'square':
        return square()
    elif shape == 'rhombus':
        return rhombus()
    elif shape == 'parallelogram':
        return parallelogram()
    elif shape == 'triangle':
        return triangle()
    elif shape == 'trapizeum':
        return trapezium()
    else:
        print('Enter the shape correctly:')

def triangle():
    base =float(input('Enter base: '))
    height=float(input('Enter height: '))
    area = 0.5*base*height
    print(area)
def rhombus():
    dia1=float(input('Enter diagonal 1'))
    dia2=float(input('Enter diagonal 2'))
    area = 0.5*dia1*dia2
    print(area)
def parallelogram():
    base=float(input('Enter base1: '))
    height=float(input('Enter height: '))
    area = base*height
    print(area)
def square():
    side=float(input('Enter a side: '))
    area = pow(side,2)
    print(area)
def trapezium():
    base1=float(input('Enter base1: '))
    base2=float(input('enter base2: '))
    height=float(input('Enter height: '))
    area=0.5*(base1+base2)/height
    print(area)


def main():

    shape = input('Enter the shape: ')
    shape = shape.lower()
    get_area(shape)
main()




