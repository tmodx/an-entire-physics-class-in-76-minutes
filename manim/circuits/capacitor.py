from manim import *
import numpy as np

from circuits import component

class Capacitor(component.Component):
    def __init__(self, bounding_rect=None, num_lines=7, color=WHITE):
        if bounding_rect is None:
            bounding_rect = Rectangle(width=1,height=1)
        super().__init__(bounding_rect=bounding_rect)

        self.color = color
        
        self.create_lines()

    def create_lines(self):
        self.elements.add(self.rect)
        self.elements.add(self.start)

        step_size = self.rect.width / (3)

        # first line
        second_position = self.start.get_center()+RIGHT*step_size
        first_line = Line(start=self.start.get_center(),end=second_position,color=self.color)
        self.elements.add(first_line)
        self.image.add(first_line)

        # middle lines
        middle_line_1 = Line(start=second_position+UP*self.rect.height/2, end=second_position+DOWN*self.rect.height/2,color=self.color)
        self.elements.add(middle_line_1)
        self.image.add(middle_line_1)

        third_position = second_position+RIGHT*step_size

        middle_line_2 = Line(start=third_position+UP*self.rect.height/2, end=third_position+DOWN*self.rect.height/2,color=self.color)
        self.elements.add(middle_line_2)
        self.image.add(middle_line_2)

        # Last line
        final_line = Line(start=third_position,end=self.end.get_center(),color=self.color)
        self.elements.add(final_line)
        self.image.add(final_line)
        
        self.elements.add(self.end)

