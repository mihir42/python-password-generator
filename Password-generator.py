import random
import string 

pass_length = int(input("Enter password length: "))

password = ""

if pass_length <=0 :
    print("Password cannot be 0")
else:
    for i in range(pass_length):
        password += random.choice(string.digits + string.ascii_letters + string.punctuation)
    print(password)


