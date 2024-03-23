class Users: 

    def __init__(self, fname, lname, username, email, age):
        self.fname = fname
        self.lname = lname
        self.username = username  
        self.email = email
        self.age = int(age)

    def describe_user(self):
        print(f" First Name : {self.fname}\n Last name : {self.lname}\n Username = {self.username}\n Email Id = {self.email}\n Age : {self.age}")

    def greet_user(self):
        print(f'Hello Mr. {self.lname} Namaste, Welcome to the office')
              
c = Users("RAM","Kishan","RK","rk@gmail.com", 25)

c.describe_user()
c.greet_user()





    
