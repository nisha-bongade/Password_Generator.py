# Random Password Generator


import random 
import string

pass_len = 8          #we can pass any length in it.
charValues = string.ascii_letters + string.digits + string.punctuation

password = "" 
for i in range(pass_len):
    password += random.choice(charValues)


print("Your suggested password is: ", password)