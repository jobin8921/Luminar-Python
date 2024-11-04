#  print sum of key and value if key is even in list comprehension

# dict = {2:8,4:6,6:8,1:4,3:5}

# sum= 0

# list = []

# for i in dict.keys():

#     if i % 2 == 0:

#         sum = i + dict[i]

#         list.append(sum)

# print(sum)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# in list comprehension

# dict = {2:8,4:6,6:8,1:4,3:5}
# result = [i+dict[i] for i in dict.keys() if i % 2 == 0]
# print(result)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

d1 = {"name":"hari","age":24,"job":"trainer","place":"kochi"}

d2 = {"job":"Team lead","job":"Team lead","place":"kakkanad","salary":10000}

for i in d1.keys():  #job

    if i in d2.keys():   # job in [job,place,salary]

        d1[i] = d2 [i]  # trainer = Teamlead

print(d1)

# Output : {'name': 'hari', 'age': 24, 'job': 'Team lead', 'place': 'kakkanad'}





