
# numbers = [1,2,3,4]    # [1,4,9,16]


# def square(a):

#     a=a**2

#     return a


# map >> Make an iterator that computes the function using arguments fromeach of the iterables. Stops when the shortest iterable is exhausted.

# map (fn,)



# print(list(map(lambda a : a**2,numbers)))  

#<map object at 0x00000225E4261B10>

# output >>> [1, 4, 9, 16]

# numbers = [1,2,3,4,5,6,7,8]

# def even(a):

#     if a%2==0:

#         return a

# print(list(filter(even,numbers)))


numbers = [1,5,3,4,15,6,7,20,28,35,10]

# def odd(a):

#     if a%2!=0:

#         return a
    
result = list(filter(lambda a: a%2!=0,numbers))
print(result)
# output >>> [1, 5, 3, 15, 7, 35]

# print(list(filter(odd,numbers)))
