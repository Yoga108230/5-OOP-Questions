#Determine if School bus is also an instance of the Vehicle class.

class Vehicle:
    def __init__(self, make, model):
        self.make= make
        self.model= model
    def drive(self):
        print("Driving...")

class School_Bus(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity= capacity
    def drive(self):
        print("School bus is driving with kids in it!")

school_bus= School_Bus("Ford", "Transit", 40)

print("Is School Bus an instance of Vehicle?", isinstance(school_bus, Vehicle))

school_bus.drive()