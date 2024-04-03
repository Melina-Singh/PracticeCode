class Users:
    def __init__(self, fname, lname, username, email):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Name: {self.fname} {self.lname}")
        print(f"UserName:  {self.username}")
        print(f"Email : {self.email}")

class Admin(Users):
    def __init__(self,fname, lname, username, email, privileges):
        super().__init__(fname, lname, username, email)
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        for privileges in self.privileges:
            print("-"+ privileges)

AU = Admin("Admin", "User", "Admin_user", "admin@example.com",
           ["can add post","can delete post", "can ban user"])
AU.show_privileges()



    

