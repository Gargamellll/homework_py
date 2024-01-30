# Write a Python program to find intersection of two given arrays using
# Lambda.
num_1=[1,64,35,4,0,12,8]
num_2=[0,67,4,2,23,9,14]
def for_func(num_1):
    for x in num_1:
        return x

def for_func(num_2):
    for x in num_2:
        return x      

intersection=list(filter(lambda x: x in num_1,num_2))
print(intersection)