import random
import string 
while True:
    try:
        pass_length = int(input("\nEnter password length: "))

        password = ""

        if pass_length <=0 :
            print("Password length must be greater than 0.")
        elif pass_length >=101 :
            print("Password length cannot be greater than 100.")
        else:
            for i in range(pass_length):
                password += random.choice(string.digits + string.ascii_letters + string.punctuation)
            print()
            print(password)
            print()
            break

    except ValueError :
        print("Enter valid input!")