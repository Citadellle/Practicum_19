from typing import Tuple

class Point:
    '''
    A class representing a point on a plain.

    Attributes:
        x (int): The x coordinate of the point.
        y (int): The y coordinate of the point.

    Methods:
        get_x(): Returns the x coordinate.
        get_y(): Returns the y coordinate.
        distance(): Calculates the Euclidean distance to another point.
        sum(): Returns a new Point representing the vector sum with another point.
    '''
    def __init__(self, coords: Tuple[int, int] = (0, 0)):
        '''
        Initialize a new Point instance.

        Args:
            coords (Tuple[int, int]): A tuple containing (x, y) coordinates.
        '''
        self.x = coords[0]
        self.y = coords[1]

    def __str__(self):
        '''
        Returns a string representation of the point.

        Returns:
            str: The coordinates as a tuple string.
        '''
        return f'{self.x, self.y}'

    def get_x(self) -> int:
        '''
        Returns the x coordinate of the point.

        Returns:
            int: The x coordinate.
        '''
        return self.x
    
    def get_y(self) -> int:
        '''
        Returns the y coordinate of the point.

        Returns:
            int: The y coordinate.
        '''
        return self.y
    
    def distance(self, other: 'Point') -> float:
        '''
        Calculates distance between two points.

        Args:
            other (Point): Another Point object.

        Returns:
            float: Distance between two points.
        '''
        dist = ((self.x - other.x)**2 +
                (self.y - other.y)**2)**0.5
        return dist
    
    def sum(self, other) -> 'Point':
        '''
        Returns a new Point.

        Args:
            other (Point): Another Point object.

        Returns:
            Point: A new Point at (self.x + other.x, self.y + other.y).
        '''
        return Point((self.x + other.x, self.y + other.y))