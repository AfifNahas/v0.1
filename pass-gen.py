import random
import string

number = string.digits
upper = string.ascii_uppercase 
lower = string.ascii_lowercase
characters = string.punctuation

def password(size):

    a = input("Include numbers? (y/n): ")
    b = input("Include uppercase? (y/n): ")
    c = input("Include lowercase? (y/n): ")
    d = input("Include punctuation? (y/n): ")
    result = ''

    if a == 'y':
        result += number
    if b == 'y':
        result += upper
    if c == 'y':
        result += lower
    if d == 'y':
        result += characters

    for i in range(0,size):     
        print(random.choice(result), end='')

x = input("Enter the size of the password (Number): ")
password(int(x))