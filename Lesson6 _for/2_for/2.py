#2.Vowel Counter
vowels=['a','e','u','i','o']
count_vowels=0
word=input('Write your word')

for i in word:
    if i in vowels:
        count_vowels+=1
        
print(count_vowels)
