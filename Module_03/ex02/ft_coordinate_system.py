#!/usr/bin/env python3

import sys
import math

def calculate_distance(origin, dest):
    x1, y1, z1 = origin
    x2, y2, z2 = dest

    diff_x = (x2 - x1) ** 2
    diff_y = (y2 - y1) ** 2
    diff_z = (z2 - z1) ** 2

    return math.sqrt(diff_x + diff_y + diff_z)

def parse_coordinates():
    try:
        if len(sys.argv) != 4:
            raise ValueError("Invalid arguments. Usage: python3 ft_coordinate_system.py <x> <y> <z>.")
    except ValueError as e:
        print(e)
        return 
    try:
        print(f"Parsing coordinates: {str(sys.argv[1:])}")
        pos = [int(arg) for arg in sys.argv[1:]]
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return 
    return pos

def coordinate_system():
    print("=== Game Coordinate System ===")
    start = (0, 0, 0)
    spawn = (10, 20, 5)
    print(f"Position created: {spawn}")
    print(f"Distance between {start} and {spawn}: {calculate_distance(start, spawn):.2f}")
    pos = parse_coordinates()
    if pos is not None:
        print(f"Parsed position: {pos}")
        print(f"Distance between {start} and {pos}: {calculate_distance(start, pos):.2f}")
        print("Unpacking demonstration:")
        x, y, z = pos
        print(f"Player at x = {x}, y = {y}, z = {z}")
        print(f"Coordinates: X = {x}, Y = {y}, Z = {z}")

if __name__ == "__main__":
    coordinate_system()