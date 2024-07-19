from manim import *
import numpy as np

from circuits import component

class Inductor(component.Component):
    def __init__(self, bounding_rect=None, num_lines=7, color=WHITE):
        if bounding_rect is None:
            bounding_rect = Rectangle(width=2,height=1)
        super().__init__(bounding_rect=bounding_rect)

        self.color = color
        
        self.create_lines()

    def create_lines(self):
        self.elements.add(self.rect)
        self.elements.add(self.start)

        radius = self.rect.width/6
        if self.rect.height/2 < radius:
            radius = self.rect.height/2

        arc1 = Arc(radius=self.rect.width/6,start_angle=0,angle=PI,color=self.color).move_arc_center_to(self.rect.get_center()).shift(LEFT*self.rect.width/3)
        arc2 = Arc(radius=self.rect.width/6,start_angle=0,angle=PI,color=self.color).move_arc_center_to(self.rect.get_center())
        arc3 = Arc(radius=self.rect.width/6,start_angle=0,angle=PI,color=self.color).move_arc_center_to(self.rect.get_center()).shift(RIGHT*self.rect.width/3)

        self.elements.add(arc1)
        self.image.add(arc1)

        self.elements.add(arc2)
        self.image.add(arc2)
        
        self.elements.add(arc3)
        self.image.add(arc3)
        
        self.elements.add(self.end)

