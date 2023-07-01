# ask user if they want ot generate a passeword or not
# If yes, ask for the password length
# Generate password
# print password
# If initial response is no, exit program

import string 
import random

characters =list( string.ascii_letters+string.digits+"!@#$%&*()")
def generate_password():
    password_length = int(input("ow long would you like your password length: "))
    random.shuffle(characters)

    password = []
    for x in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)

    password = "".join(password)
    print(password)
    
while True:
    option = input("Do you wanna generate a password: (Y/N) ")
    if option =='Y':
        generate_password()
    elif option == 'N':
        print("programm ended")
        quit()
    else:
        print("Invalid input")