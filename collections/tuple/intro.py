
# Tuple

# tuple is a collection, a tuple is similaer to a python list in terms of indexing,nested objects,and repetions

t = ("abc",)    #always give a comma while adding elements in a tuple type or it will be class as string     

# <class 'tuple'>

print(type(t))  #<class 'str'>  





# items = (1,"abc",True,1)

# print(type(items))   # <class 'tuple'>

# print(items)    # (1, 'abc', True, 1)

# print(items[1])    # abc



numbers  = [1,2,3,4,(2,5),True,"hello"]  #>>  [1,2,3,4,(2,5,False),True,"hello"]

m = numbers.pop(4)

n=list(m)

#print(n)  # [2, 5]

n.append(False)

print(n)
# [2, 5, False]

numbers.insert(4,tuple(n))

print(numbers)    # [1, 2, 3, 4, (2, 5, False), True, 'hello']










