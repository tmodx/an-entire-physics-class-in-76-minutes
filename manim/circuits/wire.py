from manim import *
from circuits import component

class Wire():
    """ A wire connecting circuit components
    """
    def __init__(self):
        self.points = Group()
        self.image = VGroup()

    def update_image(self):
        self.image = VGroup()
        previous_point = 0
        for point in self.points:
            if previous_point == 0:
                previous_point = point
                continue

            self.image.add(Line(start=previous_point.get_center(),end=point.get_center()))

            previous_point = point
            

    def add_point(self,point: Point):
        """ Adds a point to the wire, which will be connected to the previous line

        Parameters:
        -----
        point
            The point added to the wire
        """
        self.points.add(point)
        self.update_image()
    
    def connect_components(self, component1: component.Component, component2: component.Component,
                            connection_order: list =[1,0], horiztonal_first=True):
        """ Connects two components with a three-point line

        Parameters:
        -----
        component1
            The first component to connect
        component2
            The second component to connect
        connection_order
            The order to connect them in. 0=start, 1=end
        horizontal_first
            If the connecting wire should run horizontally or vertically first
        
        Example
        -----
        
            class Example(Scene):
                def construct(self):
                    comp1 = Resistor()
                    comp1.elements.shift(RIGHT*3)
                    comp2 = Resistor()
                    wire1 = Wire()
                    wire1.connect_components(comp1,comp2,[0,1])

                    self.add(comp1.image,comp2.image,wire1.image)

        """
        if connection_order[0] == 0:
            pos_1 = component1.get_start_point()
        else:
           pos_1 = component1.get_end_point() 

        if connection_order[1] == 0:
            pos_2 = component2.get_start_point()
        else:
            pos_2 = component2.get_end_point()

        self.add_point(pos_1)

        if horiztonal_first:
            self.add_point(Point(pos_2.get_x()*RIGHT+pos_1.get_y()*UP))
        else:
            self.add_point(Point(pos_1.get_x()*RIGHT+pos_2.get_y()*UP))
                
        self.add_point(pos_2)
