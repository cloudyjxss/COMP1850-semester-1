# A bad class implementation

# What does the runtime error mean?
# How do we fix the code?

class Point:
    """
    A point in 2D space.
    """

    def __init__(self,x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate

    def x_getter(self):
        return self.x

    def y_getter(self):
        return self.y

    


p = Point(1.5, 2.0)
print(p.x_getter())
print(p.y_getter())
