class User:

    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")


class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):

    def __init__(self, first_name, last_name, username, email, privileges):
        
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges(privileges)

admin_user = Admin("Admin", "User", "admin_user", "admin@example.com", 
                   ["can add post", "can delete post", "can ban user"])
admin_user.privileges.show_privileges()
