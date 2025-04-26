
# 📘 Class 7 - Object Oriented Programming (OOP)

# What is OOP?
# OOP (Object-Oriented Programming) is a style where code is structured around objects — things that contain both data (attributes) and functions (methods).

# Benefits:
# - Structured
# - Reusable
# - Disciplined
# - Easy to manage

# 1. Creating a Simple Class
class Student:
    name: str = "Okasha"
    age: int = 18

Student1 = Student()
print("Instance: ", Student1)
print(Student1.name)
print(Student1.age)


# 2. Using Constructor (__init__)
class Student:
    def __init__(self, user_name, user_age):
        self.name = user_name
        self.age = user_age

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

def print_student_info(name, age):
    student = Student(name, age)
    student.display_info()

# Example Usage
print_student_info("Okasha", 18)
print_student_info("Ali", 20)


# 3. Access Modifiers
class Person:
    def __init__(self, user_name, user_age, roll_num):
        self.name = user_name        # Public
        self.age = user_age          # Public
        self.__roll_no = roll_num    # Private

    def get_roll_num(self):
        return self.__roll_no

person_data = Person("Okasha", 20, 1234)

print(person_data.name)
print(person_data.age)
# print(person_data.__roll_no)  # ❌ Will give an error
print(person_data.get_roll_num())  # ✅ Correct way


# 4. Four Pillars of OOP

# 4.1 Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound.")

class Dog(Animal):  # Inheriting Animal class
    def bark(self):
        print(self.name, "barks.")

dog1 = Dog("Buddy")
dog1.speak()   # From Animal class
dog1.bark()    # From Dog class


# 4.2 Polymorphism
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

# Polymorphism in action
for animal in (Cat(), Dog()):
    animal.speak()


# 4.3 Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract Base Class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car is starting...")

my_car = Car()
my_car.start()


# 4.4 Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)   # ❌ Will give an error


# 🎯 Summary:
# Inheritance   - One class inherits from another
# Polymorphism  - One function behaves differently for objects
# Abstraction   - Hiding internal details, showing only essentials
# Encapsulation - Hiding data and providing public methods

# ✅ Congratulations! You have completed the basics of OOP in Python!
