import mysql.connector
from mysql.connector import Error

def connect_insert():
    conn = None

    try:
        conn = mysql.connector.connect(host = "localhost", database = "sarah-first-table", username = "root", password = "Ist@r1500")
        print("Connecting to database server")

        if conn.is_connected:
            print("Connected to database server")
            sarah_cursor = conn.cursor()

            #create a variable to contain the sql query to be executed
            sql = "insert into human (humanId, name, color, gender, bloodgroup) values (%s, %s, %s, %s, %s)" 
            val = []
            numberOfLoops = int(input("Enter number of times you want to input: "))

            for counter in range(numberOfLoops):
                humanId = input("Enter humanId: ")
                name = input("Enter name: ")
                color = input("Enter color: ")
                gender = input("Enter gender: ")
                bloodgroup = input("Enter bloodgroup: ")
                val.append((humanId, name, color, gender, bloodgroup))
             

            #create a list variable to contain all the values we want to insert into the table
            

            #execute the query using executemany function
            sarah_cursor.executemany(sql, val)

            #commit to the database
            conn.commit()

            #print a success message
            print(sarah_cursor.rowcount, "rows was inserted")

            #close the cursor
            sarah_cursor.close()

    except Error:
        print("Failed to connect due to", Error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
        print("Disconnected from the database")

connect_insert()