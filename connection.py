import mysql.connector
from mysql.connector import Error

def connect_fetch():
    conn = None

    try:
        conn = mysql.connector.connect(host = "localhost", database = "sarah-first-table", username = "root", password = "Ist@r1500")
        print("Connecting to database server")
        if conn.is_connected:
            print("Connected to database server")
        
            sql_query = "select * from human"
            cursor = conn.cursor()
            cursor.execute(sql_query)
            records = cursor.fetchall()
            print("Total number of rows in human is: ", cursor.rowcount)

            print("\nprinting each human record")
            for row in records:
                print("Human Id is:", row[0])
                print("Name is:", row[1])
                print("Color is:", row[2])
                print("Gender is:", row[3])
                print("Bloodgroup is:", row[4], "\n")

    except Error:
        print("Cannot connect due to", Error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database shutdown")

connect_fetch()