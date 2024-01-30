#2. Write a Python program to find if a given string starts with a given
#character using Lambda.
simple_string='Gone with the wind'
def find_1(character):
    for i in simple_string:
        if i[0]==character:
            return True
    return False        
find=list(filter(lambda i:find_1,simple_string))
print(find_1('k'),find)