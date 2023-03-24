The main aim for CMD tool is to generate the password as per user needs and specifications, store it in a database with its purpose and other crieterions, and incase the user forgets it , he/she will be able to retrieve it safely, with a correct answer of few questions. 


I have use Python and the fire module to make my code executable in the CMD:

Here is the detailed explanation of my code:
import random and import string imports the necessary modules for generating random passwords and string operations.
import fire imports the Fire module which allows the functions to be called from the command line.
import sqlite3 imports the sqlite3 module which is used for creating and manipulating SQLite databases.
from datetime import date imports the date class from the datetime module, which is used to get the current date.


sqlite3.connect('passwords.db') |||| connects to a database file called "passwords.db" if it exists, or creates a new one if it doesn't exist.
conn.cursor() ||||creates a cursor object which is used to execute SQL queries on the database.

c.execute()  ||||  executes an SQL query on the database through the cursor object.
This query creates a table called "passwords" if it doesn't already exist, with the following columns:
"id": an integer column which is the primary key of the table and auto-increments for each new row.
"password": a text column which stores the generated password.
"purpose": a text column which stores the purpose of the password.
"created_at": a timestamp column which automatically stores the date and time at which the password was created.
"date": a date column which stores the date on which the password was created.

conn.commit() |||| saves the changes made to the database after executing an SQL query.

def generate_password()  |||| defines a function that generates a random password of specified length based on user preferences, and inserts the password and its purpose into the database.
string.ascii_uppercase, string.ascii_lowercase, string.digits, and string.punctuation are built-in constants in the string module that contain uppercase letters, lowercase letters, digits, and punctuation symbols respectively.
random.choice() selects a random element from a sequence, which in this case is the character set defined by the user preferences.
''.join() joins the randomly selected characters into a string.
Finally, it prompts the user to enter a purpose for the password, inserts the password and its purpose into the passwords table,and date on which it is created and returns the generated password.

The get password section inputs the substr, date , purpose of the initially created password and return the corresponding password. This features enables safe password retrieval
in case of the password bieng forgotten. Thus only the person who created password would be able to retrieve it.

Finally the last code block checks whether the current script is being executed as the main program or not. If the current script is being executed as the main program
(i.e., not being imported as a module by another script), then it calls the fire.Fire() method to create a command line interface (CLI) for the generate_password() 
and get_passwords() functions.
