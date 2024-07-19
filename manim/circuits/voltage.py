from manim import *

from circuits import component

class DCVoltage(component.Component):
    """ A direct current source diagram, multiple parallel plates
    """
    def __init__(self, bounding_rect=Rectangle(width=1,height=1), num_lines=6, color=WHITE):
        super().__init__(bounding_rect=bounding_rect)

        self.num_lines = num_lines
        self.color = color

        self.create_lines()

    def create_lines(self):
        self.elements.add(self.rect)
        self.elements.add(self.start)
        
        step_size = self.rect.width / (self.num_lines-1)

        for i in range(self.num_lines):
            if i%2 == 0:
                start_point = self.rect.get_bottom() + self.rect.get_left() + RIGHT*i*step_size
                end_point = self.rect.get_top() + self.rect.get_left() + RIGHT*i*step_size
                new_line = Line(start=start_point,end=end_point,color=self.color)
            else:
                start_point = self.rect.get_bottom() + UP*self.rect.height/4 + self.rect.get_left() + RIGHT*i*step_size
                end_point = self.rect.get_top() - UP*self.rect.height/4 + self.rect.get_left() + RIGHT*i*step_size
                new_line = Line(start=start_point,end=end_point,color=self.color)
            self.elements.add(new_line)
            self.image.add(new_line)
        
        self.elements.add(self.end)

class ACVoltage(component.Component):
    """ An alternative current source diagram, a sine wave and a circle
    """
    def __init__(self, bounding_rect=Rectangle(), num_lines=6, color=WHITE):
        super().__init__(bounding_rect=bounding_rect)

        self.num_lines = num_lines
        self.color = color

        self.create_lines()

    def create_lines(self):
        self.elements.add(self.rect)
        # circle
        if (self.rect.width < self.rect.height):
            circ_radius = self.rect.width/2
        else :
            circ_radius = self.rect.height/2
        bounding_circ = Circle(radius=circ_radius,color=self.color)

        self.elements.add(bounding_circ)
        self.image.add(bounding_circ)

        # sine wave
        axes = Axes(x_range=[0,2*PI,1],
                    y_range=[-1,1,1],
                    x_length = circ_radius,
                    y_length=0.5*circ_radius)
        sin_graph = axes.plot(lambda x: circ_radius*np.sin(x),color=self.color)
        

        self.radius = circ_radius
        
        self.elements.add(sin_graph)
        self.image.add(sin_graph)


        self.elements.add(self.start)
        
        self.elements.add(self.end)
