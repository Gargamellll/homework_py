# Write a program that prompts the user to enter a word and checks if it is
# a palindrome. A palindrome is a word that reads the same backward as
# forward. Use string slicing and an if-else statement to compare the
# original word with its reverse

palindrom_word=list(input("Enter you palindrom word "))
palindrom=palindrom_word[::-1]
for x in palindrom_word:
    if palindrom_word == palindrom:
        print("Your word is palindrom")
    else:
        print("Your word is not palindrom ")
        

           