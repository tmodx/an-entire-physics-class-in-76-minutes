from manim import *
import numpy as np

from circuits import component

class Light(component.Component):
    """ A light bulb
    """
    def __init__(self, bounding_rect=None, color=WHITE):
        if bounding_rect is None:
            bounding_rect = Rectangle(width=1,height=1)
        super().__init__(bounding_rect=bounding_rect)

        self.color = color
        
        self.create_lines()


    def create_lines(self):
        self.elements.add(self.rect)
        self.elements.add(self.start)

        height = self.rect.height
        width = self.rect.width

        circle = Circle(radius = height/3,color=self.color)
        circle.move_to(self.rect.get_center()+UP*height/6)
        self.elements.add(circle)
        self.image.add(circle)

        # angle between radius thing pointing to the vertical of the bottom of the light and a vertical line
        angle = PI/6

        bound_left = circle.get_center()+DOWN*(height/3)*np.cos(angle)+RIGHT*(height/3)*np.sin(angle)
        bound_right = circle.get_center()+DOWN*(height/3)*np.cos(angle)+LEFT*(height/3)*np.sin(angle)
        line1 = Line(start=bound_left,
                     end=bound_left[0]*RIGHT+self.rect.get_bottom()[1]*UP)
        self.elements.add(line1)
        self.image.add(line1)

        line2 = Line(start=bound_right,
                     end = bound_right[0]*RIGHT+self.rect.get_bottom()[1]*UP)
        self.elements.add(line2)
        self.image.add(line2)

        line3 = Line(start=line2.end,end=line1.end)
        self.elements.add(line3)
        self.image.add(line3)

        line4 = Line(start=self.start,end=line3.start)
        self.elements.add(line4)
        self.image.add(line4)

        line5 = Line(start=line3.end,end=self.end)
        self.elements.add(line5)
        self.image.add(line5)

        # central detail lines
        line6 = line3.copy().scale(0.5).shift(UP*height/12)
        self.elements.add(line6)
        self.image.add(line6)

        line7 = line6.copy().shift(UP*height/12)
        self.elements.add(line7)
        self.image.add(line7)

        line8 = line7.copy().shift(UP*height/12)
        self.elements.add(line8)
        self.image.add(line8)
        
        self.elements.add(self.end)

