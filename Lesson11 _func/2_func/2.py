#2.Wite a Python function to calculate count o each letter in string 
def count_letter(word):
    result={}
    for letter in word:
        if letter in result:
            result[letter] +=1
        else:
            result[letter] =1       
    return result       
print(count_letter('abrakadabra'))