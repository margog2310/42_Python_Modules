#!/bin/usr/env python3

def ft_seed_inventory(plant, n, unit):
    if unit == "packets":
        print(f"{plant.title()} seeds: {n} {unit} available")
    elif unit == "grams":
        print(f"{plant.title()} seeds: {n} {unit} total")
    elif unit == "area":
        print(f"{plant.title()} seeds: covers {n} square meters")
    else:
        print("Unknown unit type")

ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")