import os
import json
import hashlib


class Pass:
    def __init__(self, email, password):
        self.__password = password
        self.email = email
        self.__randomBytes = None


    def get_password(self):
        return self.__password
    def get_salt(self):
        return self.__randomBytes
    
    def encrypt(self):
        randomBytes = os.urandom(16) # 
        hashed = hashlib.sha256(randomBytes+self.__password.encode()).hexdigest()
        self.__password = hashed
        self.__randomBytes = randomBytes.hex()
        return f"your encrypted password is {hashed}"




path = 'C:/Users/jihed/Documents/vs code/python/OOP and DS/pwd_manager.json' # <<-- Path Here -->>

while True:
    email = input("your email? ")
    if email.find("@") == -1 or email.find(".") == -1:
        print("enter a valid email")
        email = input("your email? ")
    else:
        pwd = input("your password? ")
        if len(pwd) < 8:
            print("more than 8 characters! ")
            pwd = input("your password? ")
        else:
            break
    


# choose to encrypt your password or not
def take_choice():
    choice = input('encrypt your password before pasting it to the database? y/n ')
    if choice == "y":
        encrypted = informations.encrypt()
        print(encrypted)
        print("your password have been encrypted and saved to the data base!")
    elif choice == "n":
        pass



informations = Pass(email, pwd)
take_choice()


# Loading the json file and starting it up
if os.path.exists(path) and os.path.getsize(path) > 0:
    with open(path, 'r') as file:
        data = json.load(file)
else:
    data = {"manager": []}
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)

# save your informations 
def save_data():
    newinfos = {'email': email, 'password': informations.get_password()}
    if informations.get_salt():
        newinfos['salt'] = informations.get_salt()
    data['manager'].append(newinfos)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


save_data()


