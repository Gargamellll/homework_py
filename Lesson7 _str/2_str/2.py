#2.Count all letters, digits, and special symbols from a given string
word="In#s>5tal4@lati&on"
symbols=0
digit=0
chars=0
for x in word:
    if x.islower() or x.isupper():
        symbols+=1
    elif x.isdigit():
        digit+=1
    else:
        chars+=1

print(symbols,digit,chars)                