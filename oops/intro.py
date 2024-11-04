# # oops

# # object oriented

# # class   #class is blueprint(design)
# #===========================================================
# # a class is a blueprint for creating objects (a particular data structure)
# #
# #instance of objects
# #
# #
# # list,str,int
# # numbers =[1,2,3]
# # item=[]

# # name = " "

# # item=()

# # object

# class list:

#     def append()

#     def pop()    
        
 

# class Students:

#     # method 1


#     # method 2


# class Student:

#     name : str
#     age : int

#     def greet(self):

#         print("welcome to luminar")
# person=Student()      # person is a object 

# print(type(person))  # <class '__main__.Student'>

# person.greet()


# class Students:

#     def register(self,name,place):
        
#         self.name=name

#         self.place=place

#     def greet(self):

#         print(f"welcome {self.name}")   

#     def details(self):

#         print(f"welcome {self.name} ur from {self.place}")    


# student1= Students()
# student2=Students()

# student1.register(name='hari',place='kochi')

# student2.register(name='josel',place='trivandram')


# student1.greet()
# student1.details()
# student2.greet()
# student2.details()

# class Classname:

        # def method(self)

# objectname = Class_name()

# create a class named Employee with methods 

# method1 {name,role,salary,place}

# method2 {name,place}

# method3 {name,role,salary}

# method4 {role,salary}

class Employee:

    name  : str
    role : str
    salary : int
    place : str

    def details(self,name,role,salary,place):

        self.name = name
        self.role=role
        self.salary=salary
        self.place=place

    def show_details(self):

        print(f"welcome {self.name } ur role {self.role} and salary is {self.salary} and ur from {self.place}")  

    def meth3(self):

        print(f"welcome {self.name } ur from {self.place} ur salary is {self.salary}") 

    def meth4(self):

        print(f"ur role {self.role } ur salary is {self.salary}") 

emp1=Employee()

emp1.details(name='josel',role='plumber',salary=100,place='kollam')

emp1.show_details()
# emp1.meth3()
# emp1.meth3()
# emp1.meth4()







