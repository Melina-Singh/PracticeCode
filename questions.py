class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def describe_restaurant(self):
        print(f"Restaurent Name : {self.name}, Restaurent type: {self.type}")

    def open_restaurant(self):
        print(f"The {self.name} is now Open for {self.type} of food. thank you :)")

R = Restaurant("Royal Tandoori", "Veg & Non-Veg")
r1 = Restaurant("Atlos", "Italian")
r2 = Restaurant("5 star", "Thai")
r3 = Restaurant("thakali", "Chinese")

print("Restaurant name = ", R.name)
print("Restaurent Food items = ", R.type)

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()