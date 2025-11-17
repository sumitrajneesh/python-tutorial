# class Bike:
#     name = ""
#     gear = 0

# bike1 = Bike()

# bike1.gear = 11
# bike1.name = "Mountain Bike"

# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")


""" Create Multiple Objects of Python Class"""

# class Employee:

#     # define property

#     employee_id = 0
# emp1 = Employee()
# emp2 = Employee()

# emp1.employee_id = 10001
# print(f"Employee ID: {emp1.employee_id}")

# emp2.employee_id = 10002
# print(f"Employee ID: {emp2.employee_id}")

""" Python method : function declare inside the python class"""

# class Room:
#     len = 0
#     wid = 0

#     def calculate_area(self):
#         print("Area of Room =", self.len * self.wid)

# study_room = Room()

# study_room.len = 42
# study_room.wid = 3

# study_room.calculate_area()

""" Python Constructors """

class Bike:

    def __init__(self, name=""):
        self.name = name

bike1 = Bike("Mountain Bike")