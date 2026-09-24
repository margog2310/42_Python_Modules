#!/usr/bin/env python3

def check_temperature(temp_str):
    print(f"Testing temperatue: {temp_str}")
    try:
        inp = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: {temp_str} is not a valid number")
    if inp >= 0 and inp <= 40:
        return int(temp_str)
    elif inp < 0:
        raise ValueError(f"Error: {temp_str} is too cold for plants (min 0°C)")
    else:
        raise ValueError(f"Error: {temp_str} is too hot for plants (max 40°C)")

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    try:
        inp = check_temperature("25")
        print(f"Temperature {inp} is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        inp = check_temperature("abc")
        print(f"Temperature {inp} is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        inp = check_temperature("100")
        print(f"Temperature {inp} is perfect for plants!")
    except ValueError as e:
        print(e)
    try:
        inp = check_temperature("-50")
        print(f"Temperature {inp} is perfect for plants!")
    except ValueError as e:
        print(e)
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()