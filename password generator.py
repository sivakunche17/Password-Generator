
# 6th mini project 
# password generator

import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"

length = int(input("Enter password length: "))

password = ''

count = 0

while count < length:
    choice = random.choice(chars)
    count +=1
    password = password + choice
print(password)