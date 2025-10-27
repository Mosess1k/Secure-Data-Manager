import hashlib
import json
import os

AUTH_FILE = "data/auth.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    users = {}
    if os.path.exists(AUTH_FILE):
        with open(AUTH_FILE, "r") as f:
            users = json.load(f)
    if username in users:
        print("⚠️ Username already exists.")
        return
    users[username] = hash_password(password)
    os.makedirs("data", exist_ok=True)
    with open(AUTH_FILE, "w") as f:
        json.dump(users, f)
    print("✅ User registered successfully!")

def authenticate_user(username, password):
    if not os.path.exists(AUTH_FILE):
        print("❌ No users found.")
        return False
    with open(AUTH_FILE, "r") as f:
        users = json.load(f)
    return users.get(username) == hash_password(password)
