#! /usr/bin/env python3
"""
docstring
"""

from pathlib import Path
import time

import datasense as ds
import pandas as pd


class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


def main():
    my_first_dog = Dog(name="Bunnie", age=7)
    print(
        f"My dog's name is {my_first_dog.name}. "
        f"{my_first_dog.name} is {my_first_dog.age} months old."
    )
    my_first_dog.sit()
    my_first_dog.roll_over()
    my_second_dog = Dog(name="Rosie", age=7)
    print(
        f"My dog's name is {my_second_dog.name}. "
        f"{my_first_dog.name} is {my_second_dog.age} months old."
    )
    my_second_dog.sit()
    my_second_dog.roll_over()


if __name__ == "__main__":
    main()
