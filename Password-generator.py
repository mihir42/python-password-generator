import random
import string 

try:
    pass_length = int(input("Enter password length: "))

    password = ""

    if pass_length <=0 :
        print("Password length must be grater than 0")
    elif pass_length >=101 :
        print("Password length cannot be greater than 100")
    else:
        for i in range(pass_length):
            password += random.choice(string.digits + string.ascii_letters + string.punctuation)
        print(password)

except ValueError :
    print("password length cannont be letters")