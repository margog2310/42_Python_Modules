#!/usr/bin/env python3

class GardenManager:
    gardens = {}
    growth = {}
    @classmethod
    def create_garden_network(cls):
        print("=== Garden Management System Demo ===")
        return cls
    @classmethod
    def create_garden(cls, owner):
        if owner in cls.gardens:
            print(f"{owner} already has a garden in the network")
        else:
            cls.gardens[owner] = []
            cls.growth[owner] = 0
    class GardenStats():
        @staticmethod
        def calculate_score(owner):
            garden = GardenManager.gardens[owner]
            regular = 0
            flowering = 0
            prize = 0
            total_score = 0
            print(f"Plants added: {len(garden)}, Total growth: {GardenManager.growth[owner]}")
            for plant in garden:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")
        @staticmethod
        def get_garden_score(owner):
            garden = GardenManager.gardens[owner]
            total_score = 0
            for plant in garden:
                total_score += plant.get_height()
            return total_score

    @classmethod
    def add_plant_to_garden(cls, owner, plant):
        if owner in cls.gardens:
            cls.gardens[owner].append(plant)
            print(f"Added {plant.name} to {owner}'s garden")
        else:
            print(f"{owner} doesn't have a garden in the network yet. Please add and try again.")
    @classmethod
    def garden_report(cls, owner):
        garden = cls.gardens[owner]
        print(f"=== {owner}'s garden report ===")
        print("Plants in garden: ")
        for plant in garden:
            print("- ", end = "")
            print(plant)
    @classmethod
    def garden_manager_report(cls):
        scores = []
        print("Garden scores - ", end = "")
        for key, plants in cls.gardens.items():
            scores.append(f"{key}: {cls.GardenStats.get_garden_score(key)}")
        print(", ".join(scores))
        print(f"Total gardens managed: {len(cls.gardens)}")
    @classmethod
    def grow_garden(cls, owner, n):
        garden = cls.gardens[owner]
        print(f"{owner} is helping all flowers grow")
        for plant in garden:
            plant.set_height(plant.get_height() + n)
            if n >= 0:
                print(f"{plant.name} grew {n}cm")
            if owner not in cls.growth:
                cls.growth[owner] = n
            else:
                cls.growth[owner] += n

class Plant:
    def __init__(self, name, height):
        self.name = name.title()
        self.__height = height
    def __str__(self):
        return f"{self.name}: {self.__height}cm"
    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            self.__height = 0
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    def get_height(self):
        return self.__height

class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.__color = color
    def __str__(self):
        return f"{self.name}: {self.get_height()}cm, {self.__color} flowers (blooming)"
    def set_color(self, color):
        __color = color
    def get_color(self):
        return self.__color

class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.__points = points
    def __str__(self):
        return f"{self.name}: {self.get_height()}cm, {self.get_color()} flowers (blooming), Prize points: {self.__points}"
    def set_point(self, points):
        if point > 0:
            self.__points = points
        else:
            self.__points = 0
            print(f"Invalid operation attempted: prize points {points} [REJECTED]")
            print("Security: Negative prize points rejected")

if __name__ == "__main__":
    manager = GardenManager.create_garden_network()
    print()
    manager.create_garden("Alice")
    manager.add_plant_to_garden("Alice", Plant("Oak Tree", 100))
    manager.add_plant_to_garden("Alice", FloweringPlant("Rose", 25, "red"))
    manager.add_plant_to_garden("Alice", PrizeFlower("Sunflower", 50, "yellow", 10))
    print()
    manager.grow_garden("Alice", 3)
    print()
    manager.garden_report("Alice")
    manager.GardenStats.calculate_score("Alice")
    print()
    manager.create_garden("Bob")
    manager.add_plant_to_garden("Bob", FloweringPlant("Poppy", 10, "red"))
    manager.add_plant_to_garden("Bob", PrizeFlower("Orchid", 25, "white", 50))
    print()
    manager.garden_report("Bob")
    manager.GardenStats.calculate_score("Bob")
    print()
    manager.garden_manager_report()