#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name):
        self.name = name.title()
        print(f"Plant created: {self.name}")
    def __str__(self):
        return f"Current plant: {self.name} ({self.__height}cm, {self.__age} days)"
    def set_height(self, height):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
    def get_height(self):
        return self.__height   
    def get_age(self):
        return self.__age

if __name__ == "__main__":
    print("== Garden Security System ==")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    rose.set_age(-10)
    print(rose)
