import string
import secrets

def generate_password(length=16, symbols=False, numbers=False, uppercase=False, lowercase=False):
    charset = []

    if lowercase:
        charset += list(string.ascii_lowercase)
    if uppercase:
        charset += list(string.ascii_uppercase)
    if numbers:
        charset += list(string.digits)
    if symbols:
        charset += list("!@#$%^&*()-_=+[]{};:,.<>?/")

    if not charset:
        return "Error: you must select at least one option"


    return ''.join(secrets.choice(charset) for _ in range(length))
