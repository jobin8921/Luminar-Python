# > greather than
# < lesser than
# >= greater than or equal to
# <= lesser than or equal to
# != not equal to
# == both are equals


#Either True or False

# n1 = 4
# n2 = 2
# print(n2>n1)
# print(n2<=n1)

# print(True<False) 

# print(True == 1)

# print("ad" < "ab")


# Logical Operators
# ================================

n1=3
n2=4
n3=5
n4=6

# print((n1>n2) and (n2<n3))

#   0       and     1         0
#   0       or      1         1

print(((n1<n2)and(n3>n4)) or (n1<n2))
#   T       and     T         True
#   F       or        T        True



print(((n4>n3) or (n1<n4)) and ((n3<n1) or (n2>n4)))
#       1      or    1            0      or  0
#             true         and          false

#                         false
