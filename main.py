import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.age = 0
        self.hunger = 50  
        self.energy = 50  
        self.happiness = 50  

    def eat(self):
        if self.hunger > 0:
            print(f"{self.name} is eating...")
            self.hunger -= 20
            self.energy += 10
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy = 100
        self.hunger += 20

    def play(self):
        if self.energy > 20:
            print(f"{self.name} is playing!")
            self.happiness += 20
            self.energy -= 20
        else:
            print(f"{self.name} is too tired to play.")

    def grow_older(self):
        self.age += 1
        self.hunger += 10
        self.energy -= 10
        self.happiness -= 10

    def status(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def live_a_day(self):
        print(f"Starting a new day for {self.name}...")
        self.status()
        actions = [self.eat, self.sleep, self.play]
        for _ in range(random.randint(2, 5)):  
            action = random.choice(actions)
            action()
            time.sleep(1) 
        self.grow_older()
        print(f"Day ended for {self.name}.")
        self.status()
        print("-" * 20)


cat = Pet(name="Whiskers", species="Cat")
for _ in range(7):  
    cat.live_a_day()

    
