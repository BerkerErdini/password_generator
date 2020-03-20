import random
import string

def random_number(password_length):
    source = string.digits + string.ascii_letters + string.punctuation
    return ''.join(random.sample(source, password_length))

password_length = input("How many digits of password you would like to create: ")
print("Your new password generated:",random_number(password_length))