from sqlite3 import connect

DB_NAME = "database/donations.db"  # database name

connection = connect(DB_NAME,check_same_thread= False)


cursor = connection.cursor()
def create_table():
    """function to create table inside database"""
    # create table donation inside database if not exists
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

    return total,len(data)

def insert_donation(amount, date):
    """function to insert record inside table"""
    cursor.execute("INSERT INTO Donation(amount, date) VALUES(?, ?)",
                   (amount, date))
    connection.commit()


def fetch_records():
    """function to fetch donation records"""
    data = cursor.execute("SELECT * FROM Donation")
    return data