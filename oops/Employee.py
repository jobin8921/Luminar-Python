
class Employee:

    name:str

    place:str

    role:str

# __init__ .A contructor in python is a special method called when a object is created.
# Its purpose is to asign values t

    def __init__(self,name,place,role):

        self.name=name
        self.role=role
        self.place=place

    def show_name(self):

        return self.name
    
    def show_place(self):
        
        return self.place
    
    def show_role(self):

       pass

    def __str__(self):
        
        return self.name



    
#The pass statement is used as a placeholder for future code. 
person=Employee(name="hari",role="trainer",place="kollam")
print(person )                    #<__main__.Employee object at 0x000001DF48F72120>
# print(person.show_name())
# print(person.show_place())
# print(person.show_role())