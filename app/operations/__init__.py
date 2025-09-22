# This is the __init__.py file for the operations module called "Operations.py", containing the 'Operations' class with the four static methods.
# It initializes the operations package and makes the functions 
# (addition, subtraction, multiplication, and division) available for import.
# These static methods perform basic arithmetic operations on two numbers.
# The static methods can be called directly on the class without creating an instance of the class.

class Operations:
    """
    A class containing static methods for basic arithmetic operations: addition, subtraction, multiplication, and division.
    
    Each method takes two numbers (either integers or floats) as input and returns the result of the operation.
    The division method includes a check to prevent division by zero, raising a ValueError if attempted.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Return the sum of a and b.
        The 'float' type indicates that the function expects decimal numbers.
        The '-> float' part indicates that the function will return a decimal number.
        Example: If we call Operations.addition(2.0, 3.0), it will return 5.0.
        """
        return a + b # Adding the two numbers together and returning the result.
    
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Return the difference of a and b (a - b).
        The 'float' type indicates that the function expects decimal numbers.
        The '-> float' part indicates that the function will return a decimal number.
        Example: If we call Operations.subtraction(5.0, 2.0), it will return 3.0.
        """
        return a - b # Subtracting the second number from the first and returning the result.
    
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Return the product of a and b.
        The 'float' type indicates that the function expects decimal numbers.
        The '-> float' part indicates that the function will return a decimal number.
        Example: If we call Operations.multiplication(2.0, 3.0), it will return 6.0.
        """
        return a * b # Multiplying the two numbers together and returning the result.
    
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Return the quotient of a and b (a / b).
        Dividing means breaking the first number into equal parts based on the second number.
        BUT WAIT! There's an important check here: before we divide, we need to make sure that 'b' is not zero.
        
        Why? Because dividing by zero doesn't work. If we try to divide by zero, we get a big error!
        
        So, if 'b' is zero, we raise a 'ValueError', which is a way of telling the program, "Stop! You can't do this."
        Example: if we call Operations.division(10.0, 2.0), it will return 5.0.
        But if we call Operations.division(10.0, 0.0), it will raise a ValueError and say "Division by zero is not allowed."
        """
        if b == 0:
            # This part checks if 'b' is zero. If it is, we raise an error and stop the function.
            raise ValueError("Division by zero is not allowed.") # This sends an error message when someone tries to divide by zero.
        return a / b # If 'b' is not zero, we divide the first number (a) by the second number (b) and return the result.

