class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

ModelX = Vehicle(300, 20)
print(f"Model X Maximum speed: {ModelX.max_speed}")
print(f"Model X Mileage: {ModelX.mileage}")