from manim import *
import numpy as np

from circuits import component

class Resistor(component.Component):
    """ A squiggly ANSI resistor diagram
    """
    def __init__(self, bounding_rect=None, num_lines=7, color=WHITE):
        if bounding_rect is None:
            bounding_rect = Rectangle(width=1,height=1)
        super().__init__(bounding_rect=bounding_rect)

        self.num_lines = num_lines
        self.color = color
        
        self.create_lines()

    def create_lines(self):
        self.elements.add(self.rect)
        self.elements.add(self.start)

        step_size = self.rect.width / (self.num_lines-1)

        # first line
        second_position = self.start.get_center()+RIGHT*step_size/2+UP*(self.rect.height/2)
        first_line = Line(start=self.start.get_center(),end=second_position,color=self.color)
        self.elements.add(first_line)
        self.image.add(first_line)

        previous_position = second_position
        # Add in the middle lines
        for i in range(self.num_lines-2):
            end_position = previous_position+RIGHT*step_size+UP*(self.rect.height)*np.power(-1,i+1)
            new_line = Line(start=previous_position,
                                   end=end_position,
                                   color=self.color)
            self.elements.add(new_line)
            self.image.add(new_line)
            previous_position = end_position

        # Last line
        final_line = Line(start=previous_position,end=self.end.get_center(),color=self.color)
        self.elements.add(final_line)
        self.image.add(final_line)
        
        self.elements.add(self.end)

