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

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.full_name()) # Tesla Model S

# my_car = Car("Toyota", "Fortuner")
# print(my_car.brand) 
# print(my_car.model) 
# print(my_car.full_name()) 

# my_new_car = Car("Tata", "Safari")
# print(my_new_car.model) 