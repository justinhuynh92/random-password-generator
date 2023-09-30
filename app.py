#ask user if they want to generate a password or not
#if yes, ask for password length
#generate password
#print password
#if no, exit program
import string
import random

#take a list of characters we want to generate our password from
characters == list(string.ascii_letters + string.digits + "!@#$%^&*()")

#create function that takes an input of how long the users want the password
def generate_password():
    password_length = int(input("How long would you like your passworwd to be? "))

    random.shuffle(characters)
    #empty list that's going to hold the new password input
    password = []
    #use for loop to pick random charcters
    for i in range(password_length):
        password.append(random.choice(characters))

    #shuffle the password
    random.shuffle(password)
