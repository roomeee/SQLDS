import mysql.connector
import sys
class DB:
    def __init__(self):

        try:
           self.conn= mysql.connector.connect(host="localhost", user="root", password="", database="first")

           self.my_cursor=self.conn.cursor()
        except:
            print("error")
            sys.exit(0)

        else:
            print("connected")

