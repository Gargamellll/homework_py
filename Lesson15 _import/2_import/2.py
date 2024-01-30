#  Write a function that generates a random password for the user. Allow the user
# to specify the length and complexity of the password (include letters, numbers,
# and symbols).
import random 
import string
password_len=int(input("User password len"))
password_complexity=input("Choice complexity of password: easy, middle, high")
symbols_uppercase=string.ascii_uppercase
symbols_lowercase=string.ascii_lowercase
symbols_digit=string.digits
symbols_punctuation=string.punctuation
def generate_password(password_len,password_complexity):
    symbols=symbols_digit +symbols_lowercase +symbols_uppercase +symbols_punctuation
    for i in range(password_len):
        if password_len>=10:
            easy=''.join(random.choice(symbols) for i in range(password_len))
            return easy
        elif password_len >=12:        
            middle=''.join(random.choice(symbols) for i in range(password_len))
            return middle
        elif password_len >=15: 
            high=''.join(random.choice(symbols) for i in range(password_len))
            return high
        else:
            return "Your password must be at least 10 symbols long"    

print(generate_password(password_len, password_complexity))    
    