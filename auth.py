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


def reset_password(user_id, new_password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = '" + new_password + "' WHERE id = " + str(user_id))
    conn.commit()

def fetch_profile(url):
    response = requests.get(url, verify=False)
    return response.json()
