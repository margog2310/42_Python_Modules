#!/usr/bin/env python3

def achievement_tracker():
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}

    print("=== Achievement Tracker System ===")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {alice.union(bob, charlie)}")
    print(f"Total unique achievements: {len(alice.union(bob, charlie))}")
    print(f"\nCommon to all players: {alice & bob & charlie}")
    print(f"Rare achievements (1 player): {(alice - bob - charlie) | (bob - alice - charlie) | (charlie - bob - alice)}")
    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice vs Charlie common: {alice & charlie}")
    print(f"Bob vs Charlie common: {bob & charlie}")
    print(f"Alice unique: {alice - bob - charlie}")
    print(f"Bob unique: {bob - alice - charlie}")
    print(f"Charlie unique: {charlie - bob - alice}")

if __name__ == "__main__":
    achievement_tracker()