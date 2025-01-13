# crerate a  database , create a table
# create var for name, score, winning state
# create a quiz game
import sqlite3
database = sqlite3.connect()
cursor = database.cursor()
cursor.execute('''create table if not exists quiz(name varchar(255), score int, winning_status varchar(255))''')
#-------------------------------------
print("WELCOME TO THE QUIZ!!!!")
name = input("Enter your name: ")