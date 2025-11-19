#----------------------------------------------------------------
# MySQL connection
#---------------------------------------------------------------
# Provides a reusable function to establish a connection to MySQL
# using credentials stored securely in config.py (loaded from .env).
# Returns a connection object if successful, else None.
# Note: The connection after use


from config import MYSQL_DATABASE,MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD
import mysql.connector


def get_mysql_connection():
    try:
        conn=mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        return conn
    except:
        print("MySQL connection error")
        return None
