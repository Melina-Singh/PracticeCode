# Inheritance

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        self.odometer_reading = 0  
        
    def get_descriptivename(self):
        long_name = str(self.year) + " "+ self.make+ " "+self.model
        return long_name.title()
    def read_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self,make,model,year):

        super().__init__(make, model, year)
        self.battery = 70

    def describe_battery(self):
        print("This car has a "+str(self.battery)+ "-kwh battery")

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")



class Battery():

    def __init__(self,battery_size= 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+ "-kwh battery.")


my_tesla = ElectricCar('tesla','model s', 2016)
# print(my_tesla.get_descriptivename())

my_tesla.describe_battery()
my_tesla.battery.describe_battery()
