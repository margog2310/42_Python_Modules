#!/usr/bin/env python3

class Plant:
    def __init__(self, plant, height, age):
        self.plant = plant
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.plant.title()}: {self.height}cm, {self.age} days old"

def ft_garden_data():
    Plants = [Plant("Rose", 25, 60) , Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120)]

    print("== Garden Plant Registry ==")
    for i in range(len(Plants)):
        print(Plants[i])

if __name__ == "__main__":
    ft_garden_data()