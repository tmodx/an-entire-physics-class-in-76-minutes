from manim import *
import numpy as np

eps_0 = 8.85*(10**(-12))
k = 1/(4*PI*eps_0)

class Charge:
    def __init__(self, pos=np.array([0,0]), charge=100*(10**(-12)), radius=1):
        self.pos = pos
        self.q = charge
        self.radius = radius
        self.opacity = 0.9

        if charge > 0:
            self.color = RED
        elif charge < 0:
            self.color = BLUE
        else:
            self.color = GRAY

        self.image = Circle(radius=self.radius,color=WHITE,fill_color=self.color,fill_opacity=self.opacity)
        self.image.shift(RIGHT*pos[0] + UP*pos[1])

        if (charge > 0):
            self.text = Tex(r"\textbf{+}")
        elif(charge < 0):
            self.text = Tex(r"\textbf{-}")
        else:
            self.text = Tex(r"\textbf{=}")

        self.text.font_size = 100*radius
        self.text.shift(RIGHT*pos[0] + UP*pos[1])

        self.elements = VGroup(self.image,self.text)
     
    def move_to(self,pos):
        self.pos = pos
        self.image.move_to(pos)
        self.text.move_to(pos)    

    def get_electric_field(self,pos):
        delta_x = pos[0] - self.pos[0]
        delta_y = pos[1] - self.pos[1]
        distance= np.sqrt(delta_x**2 + delta_y**2)

        # don't divide by zero
        if distance == 0:
            distance = 1

        return RIGHT * (k*self.q*delta_x/(distance**3)) + UP * (k*self.q*delta_y/(distance**3))