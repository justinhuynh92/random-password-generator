import string
import random

#take a list of characters we want to generate our password from
char == list(string.ascii_letters + string.digits + "!@#$%^&*()")

#create function that takes an input of how long the users want the password
def generate_password():
    password_length = int(input("How long would you like your passworwd to be? "))

    random.shuffle(char)
    #empty list that's going to hold the new password input
    password = []
    #use for loop to pick random charcters
    for i in range(password_length):
        password.append(random.choice(char))

    #shuffle the password
    random.shuffle(password)
    #join password to blank quotes to assign to password variable
    password = "".join(password)

    print(password)

#ask user
option = input("Do you want to generate a password? (Yes/No)")
#if yes, ask for password length
if option == "Yes":
    generate_password()
#if no, exit program
elif option == "No":
    print("Program ended")
    quit()
#error handling if not yes or no
else:
    print("Invalid input, please input Yes or No")
    quit()
