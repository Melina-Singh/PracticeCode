# this is called importing modules

from car import Car
from car import ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
 
myTesla = ElectricCar("Tesla", 'model s', 2016)
print(myTesla.get_descriptive_name())
print(myTesla.battery.describe_battery())
# print(myTesla.battery.get_range())
