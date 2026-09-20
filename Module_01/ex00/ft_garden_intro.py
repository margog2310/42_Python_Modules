#!/usr/bin/env python3

class Plant:
    def __init__(self, plant, heigth, age):
        self.plant = plant
        self.heigth = heigth
        self.age = age
    def __str__(self):
        return f"Plant: {self.plant}" + "\n" + f"Height: {self.heigth}cm" + "\n" + f"Age: {self.age} days"

def ft_garden_intro():
    print(Plant("Rose", 25, 60))
    
if __name__ == "__main__":
    print("== Welcome to My Garden ==")
    ft_garden_intro()
    print("== End of Program ==")