from encryption import encrypt_data, decrypt_data
from authentication import register_user, authenticate_user
from utils.password_generator import generate_password
from utils.data_masking import mask_data
import json
import os

DATA_FILE = "data/encrypted_data.json"

def save_encrypted_data(username, password, data):
    encrypted = encrypt_data(data, password)
    with open(DATA_FILE, "w") as f:
        json.dump({"user": username, "data": encrypted}, f)
    print("✅ Data saved securely!")

def load_encrypted_data(password):
    if not os.path.exists(DATA_FILE):
        print("❌ No data file found.")
        return
    with open(DATA_FILE, "r") as f:
        content = json.load(f)
    decrypted = decrypt_data(content["data"], password)
    print(f"🔓 Retrieved data: {mask_data(decrypted)}")

def main():
    print("=== Secure Data Manager ===")
    choice = input("1. Register  2. Login: ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if authenticate_user(username, password):
            print("✅ Login successful!")
            while True:
                action = input("\n1. Save Data  2. Retrieve Data  3. Generate Password  4. Exit: ")
                if action == "1":
                    data = input("Enter sensitive data to encrypt: ")
                    save_encrypted_data(username, password, data)
                elif action == "2":
                    load_encrypted_data(password)
                elif action == "3":
                    print("Generated Password:", generate_password())
                elif action == "4":
                    break
                else:
                    print("Invalid option.")
        else:
            print("❌ Invalid credentials.")

if __name__ == "__main__":
    main()
