# generate random password
import secrets
import string

def generate_random_password(length = 8):
    character = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(character) for _ in range(length))

password_length = int(input("enter password length: "))
print(f"password: {generate_random_password(password_length)}")