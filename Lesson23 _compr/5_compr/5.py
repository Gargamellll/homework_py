#Given a list of words, create a dictionary where keys are words, and values are their lengths, but only for words with lengths greater than 3.
list_word=' A day of funeral flowers, gold leafing and a bunch of so many of my favourites'
s_list=list_word.split( )
dic_len={x:len(x) for x in s_list if len(x)>3}
print(dic_len)
