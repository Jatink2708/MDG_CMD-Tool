import random
import string
import fire
import sqlite3



# Connect to SQLite database
conn = sqlite3.connect('passwords.db')
c = conn.cursor()

# Create passwords table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        password TEXT NOT NULL,
        purpose TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    c.execute('INSERT INTO passwords (password,purpose) VALUES (?, ?)', (password,purp))
    conn.commit()

    return password


def get_passwords():
    purp=input("what was its purpose , why you created it? ")
    c.execute("SELECT password, created_at FROM passwords WHERE  purpose= ? ", (purp))
    passwords = c.fetchall()

    return passwords


if __name__ == '__main__':
    fire.Fire({
        'generate': generate_password,
        'get': get_passwords,
    })
