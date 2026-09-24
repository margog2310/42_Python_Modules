#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

def test_custom_errors():
    try:
        print("Testing PlantError...")
        raise PlantError("PlantError: The tomato plant is wilting")
    except PlantError as e:
        print(f"Caught {e}")
    try:
        print("Testing WaterError...")
        inp = -10
        if inp < 0:
            raise WaterError("WaterError: Not enought water in the tank!")
    except WaterError as e:
        print(f"Caught {e}")

    try:
        print("Testing catching all garden errors...")
        raise PlantError("PlantError: The tomato plant is wilting")
    except GardenError as e:
        print(f"Caught {e}")
    try:
        raise WaterError("WaterError: Not enought water in the tank!")
    except GardenError as e:
        print(f"Caught {e}")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
    print("All custom error types work correctly!")