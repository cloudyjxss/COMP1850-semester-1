# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)
        self.width = width
        self.height = height
        if not type(self.width) is int:
            raise TypeError()
        elif not type(self.height) is int:
            raise TypeError()
        if self.width <= 0:
            raise ValueError()
        elif self.height <= 0:
            raise ValueError

    def is_square(self):
        """Calculates if rectangle is a square"""

        if self.height == self.width:
            return True
        else:
            return False

    def area(self):
        """Calculates area"""
        area = self.height * self.width
        return area

    def perimeter(self):
        """Calculates perimeter"""
        perimeter = (self.width *2) + (self.height *2)
        return perimeter
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)

