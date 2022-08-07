import random
import string
import asyncio
import os

print("Password Generator is up and ready to go!")

length = int(input('\nEnter password length:'))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)

os.system("pause")
