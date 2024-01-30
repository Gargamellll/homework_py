#write a python program to get the smallest number fron a list
numbers=[7,6,42,14]
num=numbers[0]
for x in numbers:
    if x < num:
        num=x
print(num)