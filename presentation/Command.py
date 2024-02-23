from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    """<<interface>>"""
    def __init__(self) -> None:
        pass
    
    # @abstractmethod
    # def execute(self):
    #     pass
    
"""
HOW TO USE INTERFACES:

class Shape(ABC):
    def __init__(self, color):
        self.color = color  # Instance variable

    @abstractmethod
    def area(self):
        pass

# Concrete class implementing the Shape interface
class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Concrete class implementing the Shape interface
class Square(Shape):
    def __init__(self, side_length, color):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

# Create instances of the child classes
circle = Circle(radius=5, color="Red")
square = Square(side_length=4, color="Blue")

# Access and modify instance variable through instances
print(circle.color)      # Output: Red
print(square.color)      # Output: Blue

# Modify instance variable through instances
circle.color = "Green"
square.color = "Yellow"

# Access modified instance variable
print(circle.color)      # Output: Green
print(square.color)      # Output: Yellow
"""