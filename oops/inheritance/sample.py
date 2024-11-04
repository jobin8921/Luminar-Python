# # Single level inheritqnce
# #=============================================================================
# class P1:
#     def m1(self):
#         print("parent 1")

# class P2:
#     def m2(self):
#         print("parent 2")

# class Child(P1):
#     def m3(self):
#         print("i am the child")

# obj1=Child()

# obj1.m1()    

# Multi level inheritqnce
#=============================================================================
# class P1:
#     def m1(self):
#         print("parent 1")

# class Child1(P1):
#     def m2(self):
#         print("child 1")

# class Child2(Child1):
#     def m3(self):
#         print("child 2")


# obj1=Child2()
# obj1.m1()   #parent 1

# Multiple  inheritqnce
#=============================================================================
# class P1:
#     def m1(self):
#         print("parent 1")

# class P2():
#     def m2(self):
#         print("child 1")

# class Child(P1,P2):
#     def m3(self):
#         print("child 2")


# obj1=Child()
# obj1

#method overloading
#====================================================================

# class Sum:

#     def add(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#         if (a+b):
#             print("helloa")
#         elif(a+b+c):
#             print("ans")    

# obj1=Sum()
#method overriding
#====================================================================
class P1:
    def car(self):
        print("Tata Safarai")


    def bike(self):
        print("Splendor")    

class Child(P1):
    
    pass

obj1=Child()
obj1.car()
























































