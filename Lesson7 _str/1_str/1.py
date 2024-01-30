#1.Arrange string characters such that lowercase letters should come first
simple_str="PyNaTive"
lowercase=[]
uppercase=[]
for x in simple_str:
    if x.islower():
        lowercase.append(x)
    else:
        uppercase.append(x)

word_lower="".join(lowercase + uppercase)
print(word_lower)            
        
    

