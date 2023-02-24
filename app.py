import psycopg2
from config import config


def connect():
    connection = None
    try:
        params = config()
        print("Connection to PostgreSQL database...")
        connection = psycopg2.connect(**params)

        # Create cursor
        crsr = connection.cursor()
        print("fetching data from database")
        crsr.execute('DELETE FROM test WHERE number = 12;')
        connection.commit()
        test1 = crsr.fetchone()
        print(test1)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close
        print("Database connection Terminated.")

connect()
