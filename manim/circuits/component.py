from manim import *


class Component():
    """ A circuit component
    """
    def __init__(self, bounding_rect=Rectangle()):
        # The bounding rectangle
        self.rect = Rectangle(width=bounding_rect.width,height=bounding_rect.height)
        # Every Visual Mobject is stored in elements()
        self.elements = Group()
        # The image is what should be drawn to the screen
        self.image = VGroup()
        # The start position, where you would "plug something in"
        self.start = Point(self.rect.get_left())
        # The end position, where it would get output
        self.end = Point(self.rect.get_right())

    def get_start_pos(self):
        return self.start.get_center()
    
    def get_end_pos(self):
        return self.end.get_center()
    
    def get_start_point(self) -> Point:
        return Point(self.start.get_center())
    
    def get_end_point(self) -> Point:
        return Point(self.end.get_center())