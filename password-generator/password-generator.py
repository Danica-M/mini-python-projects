import string
import random

def generatePass() :
    #ensuring that the password contains different types of characters
    characters = string.ascii_letters + string.digits + string.punctuation

    #Ask user the length of password they prefer
    password_length = int(input("Enter desired password length: "))

    password = []
 
    for i in range(password_length):
    
        # Picking a random characters
        randomchar = random.choice(characters)
        
        # appending a random character to password
        password.append(randomchar)

    #joining all the characters in password[] into a string
    gen_password = "".join(password)

    #returning the generated password to user
    print("Genarated Password: ",gen_password)

#allows user to regenerate a password
while True:
    generatePass()
    again = str(input("Generate another password? Y/N: "))
    if again.upper() == "N":
        break
