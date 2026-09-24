#!/usr/bin/env python3

class CustomError(Exception):
    pass

def water_plants(plants_list):
    try:
        print("Opening watering system")
        for plant in plants_list:
            if not plant:
                raise CustomError(f"Error: Cannot water {plant} - invalid plant!")
            else:
                print(f"Watering {plant}")
    except CustomError as e:
        print(e)
    finally:    
        print("Closing watering system (cleanup)")

def test_watering_system():
    print("Testing normal watering...")
    plants_list = ["tomato", "lettuce", "carrot"]
    water_plants(plants_list)
    print("Watering completed successfully!")

    print("Testing with error...")
    bad_plants_list = ["tomato", None]
    water_plants(bad_plants_list)
    print("Cleanup always happens even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()