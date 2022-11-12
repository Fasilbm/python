age = 2

print(f"The price is {age:.2f} dollars")

class person:
    def __init__ (self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name


    def my_function (self):
        print(self.first_name,self.last_name)
    
x = person("Jon", "Doe")  
    
x.my_function()




    #List is a collection which is ordered and changeable. Allows duplicate members.
    #Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    #Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    #Dictionary is a collection which is ordered** and changeable. No duplicate members.