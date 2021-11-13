# chapter 9 (cont.)
# working with classes and instances
# defining the classes here


# create a car class with following state and behavior
# make, model, year, max_speed <-- arguments
# get_description(), get_mileage(), add_mileage(miles)

# get_description(), get_mileage(), set_mileage(new_mileage)
# create a function : increment_odometer(miles)

class Car:
    """this is general model of all cars."""
    def __init__(self, make:str, model:str, year:int):
        """constructor of Car class."""
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0  # encapsulation: hiding data


    def get_description(self):
        """prints detailed description of the car"""
        print(f"this is {self.make.title()} {self.model.title()} {self.year}.")

    def get_mileage(self):
        """returns the odometer reader mileage."""
        print(f"Car has {self.__mileage} miles on it.")

    def set_mileage(self, new_mileage):
        """Updates the value of odometer reader."""
        if new_mileage > self.__mileage:
            self.__mileage = new_mileage
            print("odometer reader updated.")
        else:
            print("odometer reader was not updated.")

    def increment_odometer(self, miles):
        if miles > 0:
            self.__mileage = self.__mileage + miles   # \ this two lines are same
            self.__mileage += miles                   # / this two lines are same
            print("miles added")
        else:
            print("odometer can not be updated with given value.")

    def fill_gas_tank(self):
        print(f"filling the tank for {self.model} ... Done!")

class ElectricCar(Car):#inheritance happens here
    """Model for electric cars based on regular car features. Car is parent class."""

    def __init__(self, make, model, year):
        # everything from parent.
        super().__init__(make, model, year)# calling the constructor from parent class
        self.battery_size = 70 #70KWh

    def fill_gas_tank(self):
        """ polymorphism: Method overriding, same method from parent class"""
        print(f"this is {self.model}, gas is not used.")
