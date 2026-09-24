#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class Plant():
    def __init__(self, name, water, sun):
        self.name = name
        self.water = water
        self.sun = sun

class GardenManager():
    def __init__(self):
        self.plants = []
    def add_plant(self, plant):
        if not plant.name:
            raise GardenError(f"Error adding plant: Plant name can't be empty!")
        self.plants.append(plant)
        print(f"Added {plant.name} successfully")
    def water_plants(self):
        try:
            print("Opening watering system")
            for plant in self.plants:
                if not plant:
                    raise GardenError(f"Error: Cannot water {plant.name} - invalid plant!")
                else:
                    print(f"Watering {plant.name} - success")
        except GardenError as e:
            print(e)
        finally:    
            print("Closing watering system (cleanup)")
    @staticmethod
    def check_plant_health(plant):
        if not plant.name:
            raise ValueError("Error: Plant name can't be empty!")
        elif plant.water < 1:
            raise ValueError(f"Error: Water level {plant.water} is too low (min 1)")
        elif plant.water > 10:
            raise ValueError(f"Error: Water level {plant.water} is too high (max 10)")
        elif plant.sun < 2:
            raise ValueError(f"Error: Sunlight hours {plant.sun} is too low (min 2)")
        elif plant.sun > 12:
            raise ValueError(f"Error: Sunlight hours {plant.sun} is too high (max 12)")
        else:
            print(f"{plant.name}: healthy (water: {plant.water}, sun: {plant.sun})")

def test_garden_management():
    manager = GardenManager()
    try:
        print("Adding plants to garden...")
        manager.add_plant(Plant("tomato", 5, 8))
        manager.add_plant(Plant("lettuce", 7, 15))
        manager.add_plant(Plant(None, 0, 0))
    except Exception as e:
        print(e)
    try:
        print("Watering plants...")
        manager.water_plants()
    except Exception as e:
        print(e)
    try:
        print("Checking plant health...")
        for plant in manager.plants:
            GardenManager.check_plant_health(plant)
    except Exception as e:
        print(e)
    try:
        print("Testing error recovery...")
        raise GardenError("Not enough water in tank")
    except Exception as e:
        print(f"Caught {type(e).__name__}: {e}")
        print("System recovered and continuing...")

if __name__ == "__main__":
    print("=== Garden Management System ===")
    test_garden_management()
    print("Garden management system test complete!")
