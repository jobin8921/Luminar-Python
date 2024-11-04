a,b = map(int,input('enter 2 numbers : ').split())
o = input('enter operator : ')
if o== '+':
    print(f'add = {a+b}')
elif o== '-':
    print(f'sub = {a-b}')
elif o== '*':
    print(f'mul = {a*b}')
elif o== '/':
    print(f'div = {a/b}')
elif o== '%':
    print(f'mod = {a%b}')
    