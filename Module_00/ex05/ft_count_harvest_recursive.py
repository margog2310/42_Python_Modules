#!/usr/bin/env python3

def helper(n, start):
    if start > n:
        return print("Harvest time!")
    print(f"Day {start}")
    helper(n, start + 1)

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    helper(days, 1)
    
ft_count_harvest_recursive()
