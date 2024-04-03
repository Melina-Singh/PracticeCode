
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

class IceCreamStand(Restaurant):    

    def __init__(self, restaurant_name, cuisine_type, flavors):
        
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        
        for flavor in self.flavors:
            print("- " + flavor)


ice_cream_stand = IceCreamStand("Scoops Ahoy", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.display_flavors()
