# Assignment 1: Design Your Own Class! 

class Superhero:
    """Base Superhero class with encapsulation and constructors"""
    
    def __init__(self, name, real_name, power_level=50):
        self.name = name                  
        self.real_name = real_name         
        self._power_level = power_level    
        self.__secret_weakness = "Unknown"
        self.missions_completed = 0
    
    def get_power_level(self):

        return self._power_level
    
    def train(self, hours):
        if hours > 0:
            self._power_level += hours * 2
            print(f"{self.name} trained for {hours} hours! Power level increased to {self._power_level}")
        else:
            print("Training hours must be positive!")
    
    def complete_mission(self):
    
        self.missions_completed += 1
        print(f"{self.name} completed a mission! Total missions: {self.missions_completed}")
    
    def use_power(self):
        
        print(f"{self.name} uses their generic superhero power!")
    
    def introduce(self):
    
        print(f"I am {self.name}! My power level is {self._power_level}")

class FlyingHero(Superhero):
    
    def __init__(self, name, real_name, power_level=50, flight_speed=100):
        super().__init__(name, real_name, power_level)  
        self.flight_speed = flight_speed
    
    def use_power(self):  
        print(f"{self.name} soars through the sky at {self.flight_speed} mph!")
    
    def fly_rescue(self):
    
        print(f"{self.name} flies to rescue civilians from danger!")

class StrengthHero(Superhero):
    
    def __init__(self, name, real_name, power_level=50, strength_multiplier=10):
        super().__init__(name, real_name, power_level)
        self.strength_multiplier = strength_multiplier
    
    def use_power(self):  
        print(f"{self.name} lifts enormous objects with {self.strength_multiplier}x human strength!")
    
    def break_barriers(self):
        
        print(f"{self.name} smashes through obstacles!")

class TechHero(Superhero):
    
    def __init__(self, name, real_name, power_level=50, tech_level=5):
        super().__init__(name, real_name, power_level)
        self.tech_level = tech_level
        self.gadgets = []
    
    def use_power(self): 
        print(f"{self.name} deploys advanced technology and gadgets!")
    
    def add_gadget(self, gadget):
      
        self.gadgets.append(gadget)
        print(f"{self.name} acquired new gadget: {gadget}")

# Assignment 2: Polymorphism Challenge!

class Vehicle:
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def move(self):
     
        print(f"{self.name} is moving at {self.speed} mph")

class Car(Vehicle):
    def __init__(self, name, speed, fuel_type="gasoline"):
        super().__init__(name, speed)
        self.fuel_type = fuel_type
    
    def move(self): 
        print(f"{self.name} is driving on the road at {self.speed} mph!")

class Plane(Vehicle):
    def __init__(self, name, speed, altitude=30000):
        super().__init__(name, speed)
        self.altitude = altitude
    
    def move(self):  
        print(f"{self.name} is flying through the sky at {self.speed} mph at {self.altitude} feet!")

class Boat(Vehicle):
    def __init__(self, name, speed, water_type="ocean"):
        super().__init__(name, speed)
        self.water_type = water_type
    
    def move(self): 
        print(f"{self.name} is sailing across the {self.water_type} at {self.speed} mph!")

class Bicycle(Vehicle):
    def __init__(self, name, speed, gear_count=21):
        super().__init__(name, speed)
        self.gear_count = gear_count
    
    def move(self):
        print(f"{self.name} is pedaling along at {self.speed} mph with {self.gear_count} gears!")