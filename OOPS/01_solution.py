# 1. Basic Class and Object
#    Problem: Create a Car class with attributes like brand and model.
#             Then create an instance of this class.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand) # Toyota
# print(my_car.model) # Fortuner

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model) # Safari


# 2. Class Method and Self
#    Problem: Add a method to the Car class that displays the full name of the car (brand and model)

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    

# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand) #Toyota
# print(my_car.model) # Fortuner
# print(my_car.full_name()) # Toyota Fortuner

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model) # Safari


# 3. Inheritance
#    Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.full_name()) # Tesla Model S


# 4. Encapsulation
#    Problem: Modify the Car class to encapsulation the brand attribute, making it private, and provide a getter method for it

# Encapsulation means wrapping data (variables) and methods together inside a class.
# It helps protect the data from being accessed or changed directly from outside the class.
# In Python, we commonly use _ (protected) and __ (private) to indicate restricted access.
# It improves data security and control over how data is accessed or modified.

# Example:
# class Student:
#     def __init__(self, marks):
#         self.__marks = marks   # private variable
# Here, __marks is treated as a private variable, so it should not be accessed directly from outside the class.


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.brand + " ! "

#     def full_name(self):
#         return f"{self.brand} {self.model}"
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.brand)
# print(my_tesla.get_brand()) # Tesla !


# 5. Polymorphorism
#    Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviours.

# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def get_brand(self):
#         return self.brand + " ! "

#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#             return "Electric charge"


# my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.fuel_type()) # Electric charge

# safari = Car("Tata", "Safari")
# print(safari.fuel_type()) # Petrol or Diesel


# 6. Class Variables
#    Problem: Add a class variable to Car that keeps track of the number of cars created.

# class Car:
#     total_car = 0

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.total_car += 1

#     def get_brand(self):
#         return self.brand + " ! "

#     def full_name(self):
#         return f"{self.brand} {self.model}"

#     def fuel_type(self):
#         return "Petrol or Diesel"
    

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size

#     def fuel_type(self):
#             return "Electric charge"


# Car("Tesla", "Model S")
# Car("Tata", "Safari")

# print(Car.total_car) # 2


# 7. Static Method
#    Problem: Add a static method to the Car class that return a general description of a car

class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def get_brand(self):
        return self.brand + " ! "

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod # jab hum static method laga dete ha to self ki jarurat nhi padti 

    def general_description():
        return "Cars are the means of transport"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge" 


my_car = Car("Tesla", "Model S")
Car("Tata", "Safari")

# print(my_car.general_description())
print(Car.general_description())