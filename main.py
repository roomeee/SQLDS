import sys
from dbhelper import DB
class EMart:
    def __init__(self):
        self.db=DB()
        self.menu()

    def menu(self):
        user_input=input("""
        1.Enter 1 to register.
        2.Enter 2 to Login.
        3.Anything else to leave.""")

        if user_input=="1":
            self.register()
        elif user_input=="2":
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name=input("Enter the name: ")
        email=input("Email:")
        password=input("password:")
        respo=self.db.register(name,email,password)
        if respo:
            print("reg sucesful")
        else:
            print("failed")
        self.menu()



    def login(self):
        email= input("Enter email pls.")
        password= input("Enter password")
        self.db.search(email,password)


obj=EMart()
