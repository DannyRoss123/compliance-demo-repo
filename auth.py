import sqlite3

DB_PASSWORD = "supersecret123"
API_KEY = "sk-prod-abc123xyz"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = '" + username + "'")
    return cursor.fetchone()

def login(username, password):
    if password == DB_PASSWORD:
        return True
