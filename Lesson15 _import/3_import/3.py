#Password Checker:
import random 
import string
user_password=input('Enter your password: ')
symbols_uppercase=string.ascii_uppercase
symbols_lowercase=string.ascii_lowercase
symbols_digit=string.digits
symbols_punctuation=string.punctuation
def check_password(user_password):
    strong_password=symbols_punctuation + symbols_uppercase + symbols_digit
    for x in user_password:
        if x in strong_password:

            if len(user_password) >= 8:
                return True
        else:
            return False

print(check_password(user_password))            
