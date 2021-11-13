# for dogs import *
# execution of Dog class, using objects
from classes.dogs import Dog, Cat
dog1 = Dog('Louie', 'Black-Brown', 'French bulldog', 1) # instantiation
# __init__ functions is automatically called (executed)
# dog1 - object; instance of Dog class
# 'Louie', 'Black-Brown', 'French bulldog', 1 - instance variable

print("##### accesing the variables of the object based on the model")
print('name of the dog:', dog1.name)
print('color of the dog:', dog1.color)
print('breed of the dog:', dog1.breed)
print('age of the dog:', dog1.age)

print("##### accesing the methods(functions)")
dog1.run()
dog1.bark()
dog1.sit()
dog1.description()

print("######## accesing the methods(functions)")
dog2 = Dog('Bobo', 'brown', 'kokerspaniel', 5)
dog3 = Dog('Jack', 'black', 'German Shephard', 3)

print("################ accesing the methods(functions)")
dog2.run()
dog2.bark()
dog2.sit()
dog2.description()

print("################ accesing the methods(functions)")
dog3.run()
dog3.bark()
dog3.sit()
dog3.description()


cat1 = Cat()

print("########## (9-1) ########")

class Restaurant():
    #restaurant_name, cuisine_type
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    #describe_restaurant() - use 2 variable above
    def describe_restaurant(self):
        print(f"We are '{self.restaurant_name}' and we are {self.cuisine_type} restaurant.")

    #open_restaurant() - print ("we are open")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

restaurant = Restaurant('Royal Garden', 'Georgian')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()

print('########## 9-2 ############')
restaurant1 = Restaurant('Austrian Brewery', 'Europian')
restaurant2 = Restaurant('Chashnagiri', 'Georgian')
restaurant3 = Restaurant('Dining room', 'European')

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.open_restaurant()
restaurant1.describe_restaurant()

print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)
restaurant2.open_restaurant()
restaurant2.describe_restaurant()

print(restaurant3.restaurant_name)
print(restaurant3.cuisine_type)
restaurant3.open_restaurant()
restaurant3.describe_restaurant()

print('########## 9-3 #########')
class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print(f"user's firs name: {self.first_name}; \nuser's last name: {self.last_name}; \nuser's age: {self.age}; \nuser's sex: {self.sex}.")

    def greet_user(self):
        print(f"Wellcome back {self.first_name} {self.last_name}!")


user1 = User('Andro', 'Jvania', 14, 'M')
user2 = User('Maggie', 'Jvania', 24, 'F')
user3 = User('Matthew', 'Bellamy', 45, 'M')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
