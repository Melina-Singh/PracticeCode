class Resturant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_resturants(self):
        print(f"The name of our resturant is {self.name}")

    def open_resturant(self):
        print("the reusturant is open.")

obj = Resturant("Taj","Dalbhat")

print(f"Restaurant Name: {obj.name}")
print(f"Cuisine Type: {obj.cuisine_type}")
# print(obj)
obj.open_resturant()
obj.describe_resturants()