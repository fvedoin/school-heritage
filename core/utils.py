import hashlib
import string
import random

def generate_password(string_length=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))