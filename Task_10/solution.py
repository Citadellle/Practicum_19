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
        return f'({self.x};{self.y})'
    
    def __repr__(self):
        '''
        Returns a represented value of the point.

        Returns:
            str: Same as __str__.
        '''
        return str(self)

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
    
    def distance(self, other) -> float:
        '''
        Calculates distance between two points.

        Args:
            other (Point): Another Point object.

        Returns:
            float: Distance between two points.
        '''
        dist = ((self.x - other.x) ** 2 +
                (self.y - other.y) ** 2) ** 0.5
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


class Segment:
    '''
    A class representing a line segment between two points.

    Attributes:
        point1 (Point): The first endpoint of the segment.
        point2 (Point): The second endpoint of the segment.
        one_intersection (bool): Indicates whether the segment intersects exactly one axis.

    Methods:
        None (aside from constructor and string methods).
    '''
    def __init__(self, point1: Point, point2: Point):
        '''
        Initialize a new Segment instance.

        Args:
            point1 (Point): The first endpoint.
            point2 (Point): The second endpoint.
        '''
        self.point1 = point1
        self.point2 = point2

        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y

        cros_x = (y1 == 0 or y2 == 0 or (y1 * y2 < 0))
        cros_y = (x1 == 0 or x2 == 0 or (x1 * x2 < 0))
        self.one_intersection  = cros_x ^ cros_y
    
    def __str__(self):
        '''
        Returns a string representation of the segment.

        Returns:
            str: The segment as a pair of points.
        '''
        return f'({self.point1}, {self.point2})'
    
    def __repr__(self):
        '''
        Returns a represented value of the segment.

        Returns:
            str: Same as __str__.
        '''
        return str(self)
    

class CoordinateSystem:
    '''
    A class representing a coordinate system containing multiple segments.

    Attributes:
        segments (list): List of Segment objects.

    Methods:
        add_segment(): Adds a segment to the coordinate system.
        axis_intersection(): Counts segments that intersect exactly one axis.
    '''
    def __init__(self):
        '''
        Initialize a new CoordinateSystem instance.
        '''
        self.segments = []
    
    def __str__(self):
        '''
        Returns a string representation of all segments.

        Returns:
            str: String representation of the segments list.
        '''
        return str(self.segments)
    
    def add_segment(self, segment: Segment) -> None:
        '''
        Adds a segment to the coordinate system.

        Args:
            segment (Segment): The segment to add.

        Returns:
            None
        '''
        self.segments.append(segment)
    
    def axis_intersection(self) -> int:
        '''
        Counts how many segments intersect exactly one coordinate axis.

        Returns:
            int: The number of segments with exactly one axis intersection.
        '''
        return  sum(1 for segment in self.segments if segment.one_intersection)