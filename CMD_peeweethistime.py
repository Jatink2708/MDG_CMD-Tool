import random
import string
import fire
from datetime import datetime
from datetime import date
from peewee import *

# Connect to SQLite database using Peewee ORM
db = SqliteDatabase('passdb.db')

# Define the model for the passwords table
class passwordclass(Model):
    id = AutoField()
    passwordclm = TextField()
    purpose = TextField()
    created_at = TimestampField(default=datetime.now)
    date = DateField(default=date.today)

    class Meta:
        database = db
        table_name = 'passtable'

# Create the passwords table if it doesn't exist
db.create_tables([passwordclass])

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
    passvar = ''.join(random.choice(character_set) for _ in range(length))

    # Insert the password into the database
    purp = input('Enter the purpose of the password: ')
    password = passwordclass(passwordclm=passvar, purpose=purp)
    password.save()

    return passvar


def get_passwords():
    
    purp=input("what was its purpose , why you created it? ")
    passvar = passwordclass.get(passwordclass.purpose == purp)

    return passvar.passwordclm, passvar.created_at


if __name__ == '__main__':
    fire.Fire({
        'generate': generate_password,
        'get': get_passwords,
    })
