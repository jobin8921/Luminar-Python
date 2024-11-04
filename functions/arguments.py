# def sum_num(*args):
#     sum=0
#     print(args)

#     for i in args:

#         sum+=i
    
#     return sum

# print(sum_num(1,2,3,4,5))

# *args,**kwargs


def detail(**kwargs):# to pass a keyword, variable length argumengt to a function

    print(kwargs)    # {'name': 'sukumar', 'password': 'qwerty'}  dictonary

detail(name="sukumar",password="qwerty")

