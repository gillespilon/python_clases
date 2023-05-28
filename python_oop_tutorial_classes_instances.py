#! /usr/bin/env python3
"""
Tutorial notes for:
- https://www.youtube.com/c/Coreyms
- Python OOP Tutorials - Working with Classes

Script:
- python_oop_tutorial_classes_instances.py
"""


def main():
    # Create an instance of employee 1.
    employee_1 = Employee(
        first_name="John",
        last_name="Smith",
        annual_pay=100000
    )
    # Create an instance of employee 2.
    employee_2 = Employee(
        annual_pay=200000,
        last_name="Jones",
        first_name="Robert"
    )
    # You do not need () because email is an attribute.
    print(employee_1.email)
    print(employee_2.email)
    # YOu need () because fullname is a method.
    print(employee_1.fullname())
    print(employee_2.fullname())
    # The next two lines are equivalent.
    print(employee_1.fullname())          # Passes the instance automatically.
    print(Employee.fullname(employee_1))  # Must pass the instance manually.
    # employee_1.fullname() gets transformed into Employee.fullname(employee_1)
    # employee_1 is passed in as self.


class Employee:

    def __init__(self, first_name, last_name, annual_pay):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_pay = annual_pay
        self.email = first_name + "." + last_name + "@company.com"

    def fullname(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    main()
