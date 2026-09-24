#!/usr/bin/env python3

def garden_operations():
    try:
        print("Testing ValueError...")
        temp = int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    try:
        print("Testing ZeroDivisionError...")
        temp = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    try:
        print("Testing FileNotFoundError...")
        f = open("doesntexist.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    try:
        print("Testing KeyError...")
        dictionary = {}
        dictionary["key"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")

def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All errors tested successfully!")

if __name__ == "__main__":
    test_error_types()