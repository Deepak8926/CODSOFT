import random

def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

length = int(input("Enter the desired length of password:"))
password = generate_password(length)
print("Generated password:", password)
