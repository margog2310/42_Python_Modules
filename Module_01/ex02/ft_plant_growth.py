#!/usr/bin/env python3

class Plant:
    def __init__(self, plant, height, age_):
        self.plant = plant
        self.height = height
        self.age_ = age_
    def __str__(self):
        return f"{self.plant.title()}: {self.height}cm, {self.age_} days old"
    def grow(self, n):
        self.height += n
    def age(self, n):
        self.age_ += n
    def get_info(self):
        return self.plant, self.height, self.age_

def ft_plant_growth(plant, n):
    print("=== Day 1 ===")
    print(plant)
    plant.grow(n - 1)
    plant.age(n - 1)
    print(f"=== Day {n} ===")
    print(plant)

if __name__ == "__main__":
    Plants = [Plant("Rose", 25, 60) , Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]
    for i in Plants:
        ft_plant_growth(i, 7)