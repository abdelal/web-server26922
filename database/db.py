from datetime import date
from functools import reduce
from sqlite3 import connect
from sqlite3.dbapi2 import Cursor
from functools import reduce
DB_NAME = "database/donations.db"  # database name
# create database inside database folder if not exists
connection = connect(DB_NAME,check_same_thread= False)


cursor = connection.cursor()
def create_table():
    """function to create table inside database"""
    # create table user inside database if not exists
    table_script = '''CREATE TABLE IF NOT EXISTS Donation(

                    amount VARCHAR(255),
                    date VARCHAR(150)
                );
                '''
    cursor.executescript(table_script)
    connection.commit()


def get_summery():
    data = cursor.execute("select amount from Donation")
    data = cursor.fetchall()
    
    total = sum([float(x[0]) for x in data])

    print(len(data))
    return total,len(data)

def insert_donation(amount, date):
    """function to insert record inside table"""
    cursor.execute("INSERT INTO Donation(amount, date) VALUES(?, ?)",
                   (amount, date))
    connection.commit()


def fetch_records():
    """function to fetch User records"""
    data = cursor.execute("SELECT * FROM Donation")
    return data