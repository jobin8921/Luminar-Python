#sum of square of even numbers in list
nums = [1,2,9,65,4,3,7,6]
print(nums)
sum = 0

for i in nums:

    if i%2==0:

        sum=sum+i **2

        
print(sum)


# nums = [1,2,9,65,4,3,7,6]    #>>>>>>  [3,7,6,1,2,9,65,4]

# for i in range (3):

#     last = nums.pop()
#     print(last)

#     nums.insert(0,last)

# print(nums)

# Given pattern
# Text="ABABDC"
# Write a program to print first non-recursive character output=c

text = "ABABDC"

items = list(text)

print(items)

for i in items:

    if items.count(i)==i:

        print(i)

        break
