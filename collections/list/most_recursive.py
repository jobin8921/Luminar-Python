"""
Given a pattern text=”ABEABAIACB”
   Write a program to print most recursive consonant from above text 
   Output=B
 """


text = "ABEABAIACB"

new_text = list(text)

print(new_text)  # ['A', 'B', 'E', 'A', 'B', 'A', 'I', 'A', 'C', 'B']

count= 0

for i in new_text:

    if i in "AEIOU":

        print(" ")

    else:

        if new_text.count(i) > count:
