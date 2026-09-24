#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Error: Plant name can't be empty!")
    elif water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} is too high (max 12)")
    else:
        print(f"Plant '{plant_name}' is healthy!")

def test_plant_checks():
    try:
        print("Testing good values...")
        check_plant_health("tomato", 5, 8)
    except ValueError as e:
        print(e)
    try:
        print("Testing empty plant name...")
        check_plant_health(None, 5, 8)
    except ValueError as e:
        print(e)
    try:
        print("Testing bad water level...")
        check_plant_health("tomato", -1, 8)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("tomato", 12, 8)
    except ValueError as e:
        print(e)
    try:
        print("Testing bad sunlight hours...")
        check_plant_health("tomato", 5, -5)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("tomato", 5, 15)
    except ValueError as e:
        print(e)    

if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()
    print("All error raising tests completed!")