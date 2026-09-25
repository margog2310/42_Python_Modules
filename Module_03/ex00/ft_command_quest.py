#!/usr/bin/env python3

def command_interpreter():
    import sys
    l = len(sys.argv)

    print("=== Command Quest ===")
    try:
        if l < 2:
            raise ValueError("No arguments provided.")
    except ValueError as e:
        print(e)
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {l - 1}")
    for idx in range(1, l):
        print(f"Argument {idx}: {sys.argv[idx]}")
    print(f"Total arguments: {l}")

if __name__ == "__main__":
    command_interpreter()