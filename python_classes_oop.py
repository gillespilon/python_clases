#! /usr/bin/env python3
"""
Tutorial notes from https://www.youtube.com/c/Coreyms. Look for Python OOP
Tutorial.
"""


def main():
    # part 01
    emp_1 = Employee("Jacinda", "Locke", 100000)
    emp_2 = Employee("Gilles", "Pilon", 200000)
    print(emp_1.email)
    print(emp_2.email)
    # part 02
    print(emp_1.fullname())
    print(emp_2.fullname())


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"


if __name__ == "__main__":
    main()
