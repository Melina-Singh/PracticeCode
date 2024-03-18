class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        # self.odometer_reading = 0 #now lets modify this value
        self.odometer_reading = 23



    def descriptive_name(self):
        long_name = str(self.year)+ " "+self.make+ " "+self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " "+ "miles on it.")

    def update_odometer(self, mileage):
        # self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print("Incremental mileage:", miles)


myused_car = Car("Subaru", "outback",2013)
print(myused_car.descriptive_name())



myused_car = Car("Subaru", "outback",2012)


# print(myused_car.odometer_reading())
initial_mileage = myused_car.odometer_reading
print("Initial mileage:", initial_mileage)

print(myused_car.update_odometer(23400))
updated_mileage = myused_car.odometer_reading
print("Updated mileage:", updated_mileage)

myused_car.increment_odometer(100)
myused_car.read_odometer()