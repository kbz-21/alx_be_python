# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (no access to class/instance data)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Return the product of two numbers.
        Also prints the class attribute 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
