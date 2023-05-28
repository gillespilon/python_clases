# Python OOP tutorial&mdash;classes and instances

- Create a simple class
- What is the difference between a class and an instance of a class
- How to initialize class attributes
- How to create class methods

# Why use classes

They logically group our data (attributes) and functions (methods) in a way that is easy to use, reuse, and build upon.

# Example

We have an application for our company. We want to represent our employees in our Python code. Each individual employee is going to have specific attributes and methods. Each employee is going to have: name, email, pay, and actions they can perform. A class is a blueprint for creating instance. Each unique employee that we create using our employee class will be an instance of that class. Instance variables contain data that are unique to each instance.

When we create methods within a class they receive the instance as the first argument automatically. By convention we call the instance self. After self we can specify other arguments we want to accept.

In the code, `employee_1` will be passed in as self and then the `__init__` will set all of the attributes.

When we create an instance of our employee class, we pass in the values that we specified in our `__init__` method. The `__init__` method takes the instance which we called `self` and the first name, last name, and pay as arguments. We do not have to specify `self` because it is passed automatically.

when we pass this code:

    employee_1 = Employee(first_name="John", last_name="Smith", annual_pay=100000)

the `__init__` method will be run automatically. `employee_1` will be passed in as `self` and then it will set the attributes `first_name`, `last_name`, and `annual_pay`.

Let's say we want to perform some kind of action. We add methods to our class. For example, we want to display the full name of an employee. We create a function `def fullname(self)` and write code within that.

# Code for this video

This code is based on the video. I've made edits to make it more readable and explicit, which is easier to do in the code than in the notes above.

    #! /usr/bin/env python3
    """
    Tutorial notes from https://www.youtube.com/c/Coreyms. Look for Python OOP
    Tutorial.
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
