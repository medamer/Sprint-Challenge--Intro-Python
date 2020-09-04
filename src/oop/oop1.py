# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    def __init__(self):
        pass

class GroundVehicle(Vehicle):
    """This class inherits from the Vehicle class"""
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    """This class inherits from Vehicle class"""
    def __init__(self):
        pass
class Car(GroundVehicle):
    """This class inherits from GroudVehicle class"""
    def __init__(slef):
        pass
class Motorcycle(GroundVehicle):
    """This class inherits from GroudVehicle class"""
    def __init__(self):
        pass
class Starship(FlightVehicle):
    """This class inherits from FlightVehicle class"""
    def __init__(self):
        pass

class Airplane(FlightVehicle):
    """This class inherits from FlightVehicle class"""
    def __init__(self):
        pass