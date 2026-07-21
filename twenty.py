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

def addStudent():
    connectDB = sqlite3.connect("first.db") #establising a connection to the db
    connector = connectDB.cursor()
    student_name = input("enter student name :-")
    student_age = int(input("enter student age:- "))
    student_address = input("enter student address:- ")
    connector.execute(
    '''
    INSERT INTO Student(name, age, address)
        VALUES(?,?,?)
    ''', (student_name, student_age, student_address))


    connectDB.commit()
    print("student added")

connector.close()


def main():
    while True:
        print("welcome t o student management system")
        ch = int(input("1.ADD STUDENT\n2. VIEW STUDENT"))
        if ch == 1:
            addStudent()
        else:
            print("invalid choice")


main()



