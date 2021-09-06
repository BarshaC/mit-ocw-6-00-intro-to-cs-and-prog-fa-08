# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *
SHAPES_FILENAME = 'shapes.txt'

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self,base,height):
        """
        base : base of the triangle
        height : height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        Returns area of the triangle
        """
        return (1/2)*(self.base) * (self.height)
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self,other):
        """
        Two triangles with same are might look different because of the difference of the base and the height of the triangle
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height
        

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self.set = []
        self.index = 0
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        if sh not in self.set:
            self.set.append(sh)
        
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        for each_shape in self.set:
            yield each_shape
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        string_set = ''
        for each in self.set:
            string_set = string_set + str(each) + '\n'
        return string_set
    
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest_shapeSet = (0,)
    largest  = 0
    for shape in shapes:
        try:
            if shape.area() > largest:
                largest = shape.area()
                largest_shapeSet += (shape,)
            elif shape.area() == largest:
                largest = shape.area()
                largest_shapeSet += (shape,)
        except AttributeError:
            largest_shapeSet = (shape,)
    return largest_shapeSet

    

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    file = open(filename, 'r')
    shape_set = ShapeSet()
    for line in file:
        line = line.split(',')
        if line[0] == "circle":
            shape = Circle(line[1])
        elif line[0] == "triangle":
            shape = Triangle(line[1],line[2])
        elif line[0] == "square":
            shape = Square(line[1])
        shape_set.addShape(shape)
    return shape_set
my_shapeSet = readShapesFromFile(SHAPES_FILENAME)
print(my_shapeSet)

        

