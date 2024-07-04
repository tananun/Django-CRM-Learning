import os
import mysql.connector
from dotenv import load_dotenv
load_dotenv('.env') 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = os.getenv('DATABASE_USER'),
    passwd = os.getenv('DATABASE_PASSWORD')

)

## cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE elderco")

print("ALl DONE")