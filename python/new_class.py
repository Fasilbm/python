from class_of_student import Student

stu1 = Student("Fasil", "Engineering", 3.1)
stu2 = Student("Jesus", "Business", 3.99)


print(stu1.on_honor_roll())



result_out_of_100 = float(input("Enter your result: "))

if  result_out_of_100 >= 90 and result_out_of_100 < 100:
      print("A+")
elif result_out_of_100 >=83 and result_out_of_100 < 90:
      print("A")
elif result_out_of_100 >= 80 and result_out_of_100 < 83:
      print("A-")
elif result_out_of_100 >= 75 and result_out_of_100 < 80:
      print("B+")
elif result_out_of_100 >= 68 and result_out_of_100 < 75:
      print("B")
elif result_out_of_100 >= 65 and result_out_of_100 < 68:
      print("B-")
elif result_out_of_100 >= 60 and result_out_of_100 < 65:
      print("C+")
elif result_out_of_100 >= 55 and result_out_of_100 < 60:
       print("C")
elif result_out_of_100 >= 45 and result_out_of_100 < 50:
       print("C-")
elif result_out_of_100 >= 40 and result_out_of_100 < 45:
       print("D")
elif result_out_of_100 >= 0 and result_out_of_100 < 45:
     print("You failed")
else:
    print("Invalid input")

print(len(4))
