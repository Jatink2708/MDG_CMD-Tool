import random
import string
import fire
import sqlite3
from datetime import date 


# Connect to SQLite database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create passwords table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        purpose TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        date DATE
     
    )
''')



conn.commit()


def generate_password(length=12,
                      uppercase=True,
                      lowercase=True,
                      digits=True,
                      symbols=True):
    """
    Generates a random password of specified length, including uppercase letters,
    lowercase letters, digits, and symbols, based on user preferences.
    """
    # Define the character set to use in the password
    character_set = ''
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        character_set += string.ascii_lowercase
    if digits:
        character_set += string.digits
    if symbols:
        character_set += string.punctuation

    # Generate the password using the defined character set
    password = ''.join(random.choice(character_set) for _ in range(length))

    # Insert the password into the database
    purp = input('Enter the purpose of the password: ')
    dates =  date.today()
    c.execute('INSERT INTO passwords (password, purpose,date) VALUES (?, ?, ?)', (password, purp,dates))
    conn.commit()

    return password


def get_passwords():
    substr = input("Enter the substring of the password you want to retrieve (minimum length=3): ")
    dateee = input("Enter the date on which you created the password in YYYY-MM-DD format: ")
    purp=input("what was its purpose , why you created it? ")
    c.execute("SELECT * FROM passwords WHERE password LIKE ? AND date = ? AND purpose= ? ", ('%' + substr + '%', dateee, purp))
    passwords = c.fetchall()

    return passwords


if __name__ == '__main__':
    fire.Fire({
        'generate': generate_password,
        'get': get_passwords,
    })
