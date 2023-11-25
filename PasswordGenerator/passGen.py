# password generator with symbol and number

import random
import string

def passwordGenerator():
    # generate a random password with 12 characters
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(12))
    return password

print(passwordGenerator())
