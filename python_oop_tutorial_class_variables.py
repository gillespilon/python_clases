#! /usr/bin/env python3
"""
Tutorial notes for:
- https://www.youtube.com/c/Coreyms
- Python OOP Tutorials - Working with Classes

Script:
- python_oop_tutorial_class_variables.py
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
    # When we access raise_amount from our instances they do not have that
    # attribute. They are accessing the class's raise_amount attribute.
    # Print the namespace of employee_1.
    print(employee_1.__dict__)
    print(employee_1.annual_pay)
    # Print the namespace of Employee.
    print(Employee.__dict__)
    employee_1.apply_raise()
    print(employee_1.annual_pay)
    # Print the namespace of employee_1.
    print(employee_1.__dict__)
    # Employee.raise_amount = 1.05 changes the raise_amount for the class and
    # all of the instances.
    # employee_1.raise_amount = 1.05 changes the raise amount only for
    # employee_1. This creates the raise_amount attribute within employee_1.
    # This is important because one could use Employee.raise_amount or
    # self.raise_amount in the method apply_raise. It is probably better to
    # use the latter in order to be able to give different raise amounts to
    # different employees, if so desired, by changing the raise_amount for
    # the instances of some employees. If one does this before running
    # apply_raise, it will apply the 1.04 to all employees except those we
    # changed the raise_amount in their instances.
    # Using self.raise_amount will allow any subclass to override that constant
    # if they wanted to.

    # This next statement uses Employee.number_employees in the __init__
    # rather than self.number_employees in a method.
    print(Employee.number_employees)


class Employee:

    # Class variable that can be changed for different employee instances.
    raise_amount = 1.04
    # Class variable that we will not change; it will be the same for all
    # instances of the class.
    number_employees = 0

    def __init__(self, first_name, last_name, annual_pay):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_pay = annual_pay
        self.email = first_name + "." + last_name + "@company.com"
        Employee.number_employees += 1

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        # Two ways do raise an employee's pay. The first one makes more sense.
        self.annual_pay = int(self.annual_pay * self.raise_amount)
        # self.annual_pay = int(self.annual_pay * Employee.raise_amount)


if __name__ == "__main__":
    main()
