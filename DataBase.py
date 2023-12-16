import sqlite3 as sql
from os.path import join, exists
from os import getcwd, makedirs, remove

def startDB():
    print("Searching for database.")
    if lookUpIfDBExists():
        print("Database exist.")
        print()
        keyIn = input("Do we need to create a new database? [y/n]")
        if keyIn.lower() != 'y' and keyIn.lower() != 'n':
            while True:
                keyIn = input(""" Wrong input. Please press "y" for yes or "n" for no.""")
                if keyIn.lower() == 'y' or keyIn.lower() == 'n':
                    break
        if keyIn.lower() == 'y':
            print()
            print("Old database will be deleted.")
            deleteDB()
            print("Old database deleted.")
            print("New database will be created.")
            createDB()
            print("New database created.")
        if keyIn.lower() == 'n':
            print()
            print("Old database will be used.")
    else:
        print("No database found. A database will be created.")
        createDB()
        print("Database created.")
    addToDB()

def pathDBDir():
    return join(getcwd(), join("Data", "Database"))

def pathDB():
    return join(pathDBDir(), "SRAR.db")

def lookUpIfDBExists():
    if exists(pathDB()):
        return True
    else:
        return False

def deleteDB():
    remove(pathDB())

def createDB():
    if not exists(pathDBDir()):
        makedirs(pathDBDir())
    if not exists(pathDB()):
        DB = sql.connect(pathDB())
        DBCur = DB.cursor()
        DBCur.execute("CREATE TABLE persons(id primary key, givenName, surName, age, job)")
        DBCur.execute("INSERT INTO persons VALUES (?,?,?,?,?)", (0, None, None, None, None))
        DB.commit()

def addToDB():
    DB = sql.connect(pathDB())
    DBCur = DB.cursor()
    while True:
        idx = DBCur.execute("SELECT * FROM 'persons' ORDER BY id desc limit 1").fetchone()[0]
        print()
        print("At the moment the database has " + str(idx) + " entries.")
        print()
        keyIn = input("Do we need to add something to database? [y/n]")
        print()
        if keyIn.lower() != 'y' and keyIn.lower() != 'n':
            while True:
                keyIn = input("""You hit the wrong key. Press "y" if you want to add something to database. Else press "n".""")
                if keyIn.lower() == 'y' or keyIn.lower() == 'n':
                    break
        if keyIn.lower() == 'y':
            print("Let us add your given name, surname, age and job to the database.")
            while True:
                print()
                givenName = input("What is your given name?: ")
                print()
                if not givenName:
                    answer = input("You have no given name. Is this correct? [y/n]")
                else:
                    answer = input("Your given name is " + givenName + ". Is this correct? [y/n]")
                if answer.lower() != 'y' and answer.lower() != 'n':
                    while True:
                        print()
                        if not givenName:
                            answer = input("""You hit the wrong button. Press "y" if you have no given name. Else press "n".""")
                        else:
                            answer = input("""You hit the wrong button. Press "y" if your given name is """ + givenName + """. Else press "n".""")
                        if answer.lower() == 'y' or answer.lower() == 'n':
                            break
                print()
                if answer.lower() == 'y':
                    if not givenName:
                        givenName = None
                        print("No given name is set.")
                        break
                    else:
                        print(givenName + " is set as given name.")
                        break
                if answer.lower() == 'n':
                    print("You can correcting your input.")
            while True:
                print()
                surName = input("What is your surname?: ")
                print()
                if not surName:
                    answer = input("You have no surname. Is this correct? [y/n]")
                else:
                    answer = input("Your surname is " + surName + ". Is this correct? [y/n]")
                if answer.lower() != 'y' and answer.lower() != 'n':
                    while True:
                        print()
                        if not surName:
                            answer = input("""You hit the wrong key. Press "y" if you have no surname. Else press "n".""")
                        else:
                            answer = input("""You hit the wrong key. Press "y" if your surname is """ + surName + """. Else press "n".""")
                        if answer.lower() == 'y' or answer.lower() == 'n':
                            break
                print()
                if answer.lower() == 'y':
                    if not surName:
                        surName = None
                        print("No surname is set.")
                        break
                    else:
                        print(surName + " is set as surname.")
                        break
                if answer.lower() == 'n':
                    print("You can correcting your input.")
            while True:
                print()
                age = input("What is your age?: ")
                print()
                if not age:
                    answer = input("Your are ageless. Is this correct? [y/n]")
                else:
                    answer = input("Your age is " + age + ". Is this correct? [y/n]")
                if answer.lower() != 'y' and answer.lower() != 'n':
                    while True:
                        print()
                        if not age:
                            answer = input("""You hit the wrong key. Press "y" if you are ageless. Else press "n".""")
                        else:
                            answer = input("""You hit the wrong key. Press "y" if your age is """ + age + """. Else press "n".""")
                        if answer.lower() == 'y' or answer.lower() == 'n':
                            break
                print()
                if answer.lower() == 'y':
                    if not age:
                        age = None
                        print("You age is set to ageless.")
                    else:
                        print(age + " is set as your age.")
                        age = int(age)
                    break
                if answer.lower() == 'n':
                    print("You can correcting your input.")
            while True:
                print()
                job = input("What is your job?: ")
                print()
                if not job:
                    answer = input("You are jobless. Is this correct? [y/n]")
                else:
                    answer = input("Your job is " + job + ". Is this correct? [y/n]")
                if answer.lower() != 'y' and answer.lower() != 'n':
                    while True:
                        print()
                        if not job:
                            answer = input("""You hit the wrong key. Press "y" if you are jobless. Else press "n".""")
                        else:
                            answer = input("""You hit the wrong key. Press "y" if your  job is """ + job + """. Else press "n".""")
                        if answer.lower() == 'y' or answer.lower() == 'n':
                            break
                print()
                if answer.lower() == 'y':
                    if not job:
                        job = None
                        print("Your job is set to jobless")
                    else:
                        print(job + " is set as your job.")
                    break
                if answer.lower() == 'n':
                    print("You can correcting your input.")
            data = (int(idx)+1, givenName, surName, age, job)
            DBCur.execute("INSERT INTO persons VALUES (?, ?, ?, ?, ?)", data)
            DB.commit()
        if keyIn.lower() == 'n':
            print("Nothing new will add to database.")
            break
    print()
    print("We are done with the database.")
    print()

def readDBOut(idx):
    DB = sql.connect(pathDB())
    DBCur = DB.cursor()
    return DBCur.execute("SELECT * FROM 'persons' WHERE id=" + str(idx)).fetchone()