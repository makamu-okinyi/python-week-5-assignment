# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"{self.brand} {self.model}"

# Child class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # inherit brand & model
        self.__storage = storage        # private attribute (Encapsulation)
        self.battery = battery

    def charge(self, amount):
        self.battery += amount
        print(f"🔋 Battery charged to {self.battery}%")

    def get_storage(self):
        return f"📱 Storage: {self.__storage}GB"

# Create unique objects
phone1 = Smartphone("Samsung", "Galaxy S25", 256, 80)
phone2 = Smartphone("Apple", "iPhone 16", 512, 50)

print(phone1.info())       # Samsung Galaxy S25
print(phone1.get_storage()) # 📱 Storage: 256GB
phone1.charge(10)          # 🔋 Battery charged to 90%
# Week 5: OOP Concepts - Inheritance and Encapsulation
