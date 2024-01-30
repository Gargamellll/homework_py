#Write a Python program to find the second smollest in a list
numbers=[11,9,14]
num=numbers[0]
for x in numbers:
    if x < num < x:
        num=x
print(num)