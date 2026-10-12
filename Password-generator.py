import random
import string 

pass_length = int(input("Enter password length: "))

password = ""

for i in range(pass_length):
    password += random.choice(string.digits + string.ascii_letters + string.punctuation)

print(password)


