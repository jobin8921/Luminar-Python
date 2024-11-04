
def swap_num(fn):
    def wrapper(a, b):
        if a<b:
            b,a=a,b
        return fn(a,b)
    return wrapper




@swap_num
def substraction(a,b):
    return a-b

print(substraction(4,6))