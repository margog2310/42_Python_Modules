#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name.title()
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, {self.color} color")
    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")
    def produce_shade(self):
        print(f"{self.name} provides {self.trunk_diameter * 1.5} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")

if __name__ == "__main__":
    rose = Flower("Rose", 25, 30, "red")
    rose.bloom()
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    sunflower.bloom()
    print("\n")
    oak = Tree("Oak", 500, 1825, 50)
    oak.produce_shade()
    ash = Tree("Ash", 400, 785, 20)
    ash.produce_shade()
    print("\n")
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 65, 100, "spring", "vitamin A")