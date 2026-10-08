#!/usr/bin/env python3

import sys

class Inventory():
    def __init__(self):
        self.inventory = {}
    def add_item(self, item, quantity):
        if item in self.inventory:
            print(f"{item.title()} already in inventory. Updating quantity by {quantity}.")
            self.inventory[item] += int(quantity)
        else:
            self.inventory[item] = int(quantity)
    def system_analysis(self):
        print("=== Inventory System Analysis ===")
        total = 0
        items = len(self.inventory)
        for quantity in self.inventory.values():
            total += int(quantity)
        print(f"Total items in inventory: {total}")
        print(f"Unique item types: {items}")
        return total
    def current_inventory(self):
        print("=== Current Inventory ===")
        total = sum(int(q) for q in self.inventory.values())
        for item, quantity in self.inventory.items():
            percent = (int(quantity) * 100) / total
            print(f"{item}: {quantity} {'unit' if quantity == 1 else 'units'} ({percent:.1f}%)")
    def inventory_statistics(self):
        print("=== Inventory Statistics ===")
        most, maxItem = max(self.inventory.items(), key=lambda x: x[1])
        least, minItem = min(self.inventory.items(), key=lambda x: x[1])
        print(f"Most abundant: {most} ({maxItem} {'unit' if maxItem == 1 else 'units'})")
        print(f"Least abundant: {least} ({minItem} {'unit' if minItem == 1 else 'units'})")
    def item_categories(self):
        print(f"=== Item Categories ===")
        mod = {}
        scarce = {}
        for item, q in self.inventory.items():
            if q >= 5:
                mod[item] = q
            else:
                scarce[item] = q
        print(f"Moderate: {mod}")
        print(f"Scarce: {scarce}")

if __name__ == "__main__":
    _inventory = Inventory()

    for arg in sys.argv[1:]:
        l = len(arg)
        for colon in range(0, l + 1):
            if arg[colon] != ':':
                colon += 1
            else:
                break
        _inventory.add_item(arg[:colon], arg[colon + 1:])
        #print(f"{arg[:colon]}, {arg[colon + 1:]}")
    _inventory.system_analysis()
    print()
    _inventory.current_inventory()
    print()
    _inventory.inventory_statistics()
    print()
    _inventory.item_categories()
    print("\n===Management Suggestions ===")
    print("Restock needed:", ", ".join(item for item, qty in _inventory.inventory.items() if qty <= 1))
    print("\n=== Dictionary Property Demo ===")
    print(f"Dictionary keys:", ", ".join(_inventory.inventory.keys()))
    print(f"Dictionary values:", ", ".join(str(value) for value in _inventory.inventory.values()))
    print(f"Sample lookup: - 'sword' in inventory: {bool(_inventory.inventory.get('sword'))}")