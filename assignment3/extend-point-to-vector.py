# TASK 5: Extending a Class
import math


class Point:
    """Represents a point in 2D space."""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        """Check equality based on x and y coordinates."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        """String representation of a Point."""
        return f"Point({self.x}, {self.y})"
    
    def distance(self, other):
        """Calculate Euclidean distance to another Point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vector(Point):
    """Vector class inheriting from Point with vector operations."""
    
    def __str__(self):
        """Override string representation for Vector."""
        return f"Vector<{self.x}, {self.y}>"
    
    def __add__(self, other):
        """Override + operator for vector addition."""
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)


if __name__ == "__main__":
    # Demonstrate Point class
    p1 = Point(3, 4)
    p2 = Point(6, 8)
    print(f"Point p1: {p1}")
    print(f"Point p2: {p2}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"Distance p1 to p2: {p1.distance(p2):.2f}")
    
    # Demonstrate Vector class
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(f"\nVector v1: {v1}")
    print(f"Vector v2: {v2}")
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")
    
    # Show different string representations
    same_coords_point = Point(5, 5)
    same_coords_vector = Vector(5, 5)
    print(f"\nPoint(5,5): {same_coords_point}")
    print(f"Vector(5,5): {same_coords_vector}")
