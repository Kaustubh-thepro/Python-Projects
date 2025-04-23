# Python-Projects
Python projects

class Vehicles (object):
    color = 'white'
    def __init__(self, Max_speed, mileage):
        self.max_speed = Max_speed
        self.mileage = mileage

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def property_display(self):
        print("Properties of car:")
        print("Color:",self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

car1 = Vehicles(200,20)
car1.assign_seating_capacity(5)
car1.property_display()
