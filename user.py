class User:

    def __init__(self, first_name, last_name):
        print("Пользователь создан")
        self.fName = first_name
        self.lName = last_name

    def sayFName(self):
        print(self.fName)
    
    def sayLName(self):
        print(self.lName)
    
    def sayFLName(self):
        print(self.fName + " " + self.lName)
