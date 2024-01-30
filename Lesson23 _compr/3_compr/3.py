#3.Create a list of vowels present in a given word.
word='chocolate'
vowels_alphabet=['a','e','u','o','i']
vowels=[x for x in word if x in vowels_alphabet ]
print(vowels)