#!/usr/bin/env python3

class Plant:
    def __init__(self, plant, height, age_):
        self.plant = plant
        self.height = height
        self.age_ = age_
        print("== Created: ", end = "")
        print(self)
    def __str__(self):
        return f"{self.plant.title()} ({self.height}cm, {self.age_} days)"
    def grow(self, n):
        self.height += n
    def age(self, n):
        self.age_ += n
    def get_info(self):
        return self.plant, self.height, self.age_

if __name__ == "__main__":
    plants = [Plant("Rose", 25, 60) , Plant("Oak", 200, 365), 
              Plant("Sunflower", 80, 45), Plant("Cactus", 15, 120),
              Plant("Fern", 15, 120)]
    print("Total plants created: " + str(len(plants)))
