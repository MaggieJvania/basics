# chapter 9 (cont.)
# working with classes and instances
# instantiaiting the classes (executing)
from classes.cars import *

car1 = Car('Toyota', 'Camry', '2021')
print(car1.make)
print(car1.model)

car1.set_mileage(25)
car1.get_mileage()
#print('miles:', car1.__mileage)

car1.set_mileage(-5)
car1.get_mileage()
car1.set_mileage(24)
car1.get_mileage()
print("---------------------------")
car1.increment_odometer(50)
car1.increment_odometer(-10) # not possible in real world


car2 = ElectricCar('Tesla', 'Model X', 2022)
car2.get_description()
print(car2.model)
car1.fill_gas_tank()
car2.fill_gas_tank('abc')

