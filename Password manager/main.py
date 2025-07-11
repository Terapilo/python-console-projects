import json
from datetime import datetime
FILENAME = "passwords.json" 
def add_password():
    website = input("Website").strip().lower()
    username = input("Username:").strip()
    password = input("Password:").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_data = {
        website: {
            "username": username,
            "password": password,
            "saved_at": timestamp
        }
    }
    try:
        with open (FILENAME, "r")as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    
    data.update(new_data)

    with open (FILENAME, "w")as f:
        json.dump(data, f, indent=4 )
    print("Password saved!")

def view_passwords():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)

            if not data:
                print("No passwords saved yet")
                return
            print("\nSaved Passwords")
            for site, creds in data.items():
                print(f"-{site}")
                print(f"Username: {creds["username"]}")
                print(f"Password: {creds["password"]}")
                print(f"Saved_at: {creds["saved_at"]}\n")
    except FileNotFoundError:
        print ("Password file does not exist")

#Main Loop
while True:
    print("===PASSWORD MANAGER===")
    print("1: Add password")
    print("2: View password")
    print("3: Exit")

    option = input("Choose an option").strip()
     
    if option == "1":
        add_password()
    elif option == "2":
        view_passwords()
    elif option == "3":
        print("Exiting PASSWORD MANAGER")
        break
    else:
        print("Invalid option. Try again!")
