import sqlite3
connectDB = sqlite3.connect("first.db") #establising a connection to the db
connector = connectDB.cursor() # to interact with the database

# operations
connector.execute(
    '''
    CREATE TABLE IF NOT EXISTS Student(
    name VARCHAR(20),
    AGE INTEGER,
    address TEXT
    )
'''
)

connector.close()

