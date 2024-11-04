numbers = [1,2,3,[4,5,6,[2,3,4],4],10,9] # [1,2,3,[4,5,6,"hello"[2,3,4],4],10,9]

print(len(numbers))

n=numbers.pop(3)

n.insert(3,"hello")

print(n)    # [4, 5, 6, 'hello', [2, 3, 4], 4]

numbers.insert(3,n)

print(numbers)   # [1, 2, 3, [4, 5, 6, 'hello', [2, 3, 4], 4], 10, 9]




