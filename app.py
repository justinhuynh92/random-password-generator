#ask user if they want to generate a password or not
#if yes, ask for password length
#generate password
#print password
#if no, exit program
import string
import random

#take a list of characters we want to generate our password from
characters == list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your passworwd to be? "))
