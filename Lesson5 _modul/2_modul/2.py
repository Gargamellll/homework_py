#2.Write a Python program to get the largest number from a list.
numbers=[3,6,42,14]
num=numbers[0]

for x in numbers:
    if x > num:
        num=x
print(num)