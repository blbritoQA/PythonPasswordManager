from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        generate_key()

    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = fer.decrypt(passw.encode()).decode()
            print("User:", user, "| Password:", decrypted_password)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        encrypted_password = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_password + "\n")

key = load_key()
fer = Fernet(key)

while True:
    mode = input("Gostaria de adicionar uma nova senha ou visualizar as existentes? (view, add), pressione q para sair? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
