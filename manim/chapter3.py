from manim import *
from manim_physics import *
import random
import charge
from circuits import capacitor, inductor, resistor, voltage, wire 

class MiniDipole(ThreeDScene):
    def construct(self):
        wire1 = Wire(Circle(2))
        mag_field = MagneticField(
            wire1,
            x_range=[0,0],
            y_range=[-7, 7],
            z_range=[-4,4]
        )
        # stream = StreamLines(mag_field.func,x_range=[-6,6],y_range=[-4,4],max_anchors_per_line=30)
        self.set_camera_orientation(PI/2,0)
        self.play(*[GrowArrow(vec) for vec in mag_field])
        self.wait(2)

class MovingChargeMagneticField(ThreeDScene):
    def construct(self):
        c1 = Charge(magnitude=2)
        c1.move_to(LEFT)
        move_vector = Vector(2*RIGHT).shift(LEFT)
        w1 = Wire(stroke=move_vector)
        mag_field = MagneticField(
            w1,
            x_range=[0,0],
            y_range=[-4,4],
            z_range=[-4,4]
        )

        self.play(Write(c1))
        self.wait()
        self.play(c1.animate.shift(2*RIGHT),GrowArrow(move_vector))
        self.wait()
        self.move_camera(phi=PI/4,theta=PI/4)
        self.play(FadeIn(mag_field))
        self.wait()

class BiotSavartLaw(Scene):
    def construct(self):
        biot_savart = MathTex(r"d",r"\vec{B}","=",r"{\mu_0",r"\over",r"4\pi}","{I",r"d\vec{l}",r"\times",r"\hat{r}",r"\over","{r}^2}")
        cross_prod_magnitude = MathTex(r"|d\vec{l}",r"\times",r"\vec{r}|","=","dl","r",r"sin(\theta)").to_edge(UR)
        vector_a = Vector(2*UP+LEFT).next_to(cross_prod_magnitude,DOWN).shift(0.5*DOWN+LEFT)
        vector_a.set_color(RED)
        vector_b = Vector(2*UP+2*RIGHT).put_start_and_end_on(start=vector_a.get_start(),end=vector_a.get_start()+2*UP+2*RIGHT)
        vector_b.set_color(RED)

        theta_arc = Arc(radius=1,start_angle = PI/4,angle = np.arctan2(2,-1)-PI/4).move_arc_center_to(vector_a.get_start())
        theta_label = Tex(r"$\theta$").next_to(theta_arc,UP)

        math_eqns = [biot_savart,cross_prod_magnitude]
        for eqn in math_eqns:
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("{r}",RED)

        self.play(Write(biot_savart))
        self.play(Write(cross_prod_magnitude))
        self.play(GrowArrow(vector_a),GrowArrow(vector_b),Write(theta_arc),Write(theta_label))

class RightHandRule(Scene):
    def construct(self):
        hand = SVGMobject("svg/right-hand-rule.svg").scale(2)
        a_vector = Vector(3*LEFT+0.75*UP).set_color(GREEN)
        a_label = Tex(r"$\vec{A}$").move_to(a_vector.get_end()).shift(UL*0.5).set_color(GREEN)

        b_vector = Vector(2.5*LEFT+1*DOWN).set_color(BLUE)
        b_label = Tex(r"$\vec{B}$").move_to(b_vector.get_end()).shift(DL*0.5).set_color(BLUE)

        c_vector = Vector(0.5*RIGHT+2.5*UP).set_color(RED)
        c_label = Tex(r"$\vec{C}$").set_color(RED).next_to(c_vector,UP)

        cross_eqn = MathTex(r"\vec{A}",r"\times",r"\vec{B}","=",r"\vec{C}").to_edge(UR)
        sin_eqn = MathTex("|",r"\vec{A}",r"\times",r"\vec{B}","|","=","|",r"\vec{A}","|","|",r"\vec{B}","|",r"sin(\theta)")
        sin_eqn.to_edge(UR).shift(DOWN)

        math_eqns = [cross_eqn,sin_eqn]
        for eqn in math_eqns:
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("C",RED)

        self.play(Write(hand))
        self.play(Write(a_vector),Write(b_vector))
        self.play(FadeIn(a_label,b_label))
        self.play(Write(c_vector))
        self.play(FadeIn(c_label))
        self.play(Write(cross_eqn))
        self.wait()
        self.play(Write(sin_eqn))
        self.play(FadeOut(a_label,b_label,c_label,cross_eqn,sin_eqn))

class RightHandRuleCurrentBField(ThreeDScene):
    def construct(self):

        biot_savart = MathTex(r"d",r"\vec{B}","=",r"{\mu_0",r"\over",r"4\pi}","{I",r"d\vec{l}",r"\times",r"\hat{r}",r"\over","{r}^2}")
        biot_savart.to_edge(UR).shift(0.5*LEFT)
        
        math_eqns = [biot_savart]
        for eqn in math_eqns:
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("{r}",RED)

        hand = SVGMobject("svg/right-hand-rule.svg").scale(2)
        wire1 = Vector(10*LEFT+3*UP).shift(5*RIGHT+1.5*DOWN).set_color(YELLOW_A)
        wire1_label = Tex(r"$I$").next_to(wire1.get_end(),UL).set_color(YELLOW_E)

        r_vector = Vector(0.75*(5*LEFT+2*DOWN)).set_color(RED)
        r_label = Tex(r"$r$").next_to(r_vector.get_end(),UL).set_color(RED)

        b_vector = Vector(1.25*(0.5*RIGHT+2.5*UP)).set_color(BLUE)
        b_label = Tex(r"$B$").next_to(b_vector.get_end(),UL).set_color(BLUE_D)

        b_point = Dot().move_to(r_vector.get_end()).shift(0.33*(5*LEFT+2*DOWN))

        b_copy = b_vector.copy()

        charge_imgs = []
        for i in range(7):
            new_charge = charge.Charge(radius=0.25)
            
            charge_imgs.append(VGroup(new_charge.image,new_charge.text).move_to(wire1.get_start()))
        
        self.play(Write(hand),Write(wire1))
        self.play(FadeIn(wire1_label))
        self.play(AnimationGroup(*[MoveAlongPath(c1,wire1) for c1 in charge_imgs],lag_ratio=0.1))
        self.play(*[FadeOut(c1) for c1 in charge_imgs])
        self.wait()
        self.play(Write(biot_savart))
        self.play(Write(r_vector),Write(b_vector))
        self.play(FadeIn(r_label,b_label))
        self.play(Write(b_point))
        self.play(b_copy.animate.shift(1.08*(5*LEFT+2*DOWN)))
        # self.play(FadeOut(r_label,b_vector,b_label))
        rotation_mobs = VGroup(b_copy,b_point,hand,r_label,r_vector,b_label,b_vector)
        # self.play(rotation_mobs.animate.shift(0.25*(10*RIGHT+3*DOWN)))
        self.play(Rotate(rotation_mobs,2*PI,axis=10*LEFT+3*UP+3*IN,
                         about_point=ORIGIN),run_time=2)

class StraightLineCurrent(ThreeDScene):
    def construct(self):
        mag_wire1 = Wire(Line(start=DOWN,end=UP))
        mag_field = MagneticField(mag_wire1,
                                  x_range=[-4,4],
                                  y_range=[0,0],
                                  z_range=[-4,4])
        visual_wire1 = Vector(4*UP).shift(2*DOWN).set_color(YELLOW_A)

        self.move_camera(phi=PI/4,theta=3*PI/4)
        self.play(GrowArrow(visual_wire1))
        self.play(FadeIn(mag_field))
        self.wait()
        self.move_camera(theta=2*PI+3*PI/4)
        self.wait()

class LoopOfCurrent(ThreeDScene):
    def construct(self):
        loop = Wire(Circle(radius=2).rotate(PI/2,UP))
        mag_field = MagneticField(loop)

        self.move_camera(phi=PI/4,theta=PI/4)
        self.play(Write(loop))
        self.play(Write(mag_field))

class BiotSavartIntegral(Scene):
    def construct(self):
        biot_savart = MathTex(r"\vec{B}","=",r"\int",r"d",r"\vec{B}","=",r"\int",r"{\mu_0",r"\over",r"4\pi}","{I",r"d\vec{l}",r"\times",r"\hat{r}",r"\over","{r}^2}")
        biot_savart.to_edge(UP).shift(1*DOWN)
        
        math_eqns = [biot_savart]
        for eqn in math_eqns:
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("{r}",RED)
        
        self.play(Write(biot_savart))

class LorenzForce(Scene):
    def construct(self):
        main_eqn = MathTex(r"\vec{F}","=","q",r"\vec{v}",r"\times",r"\vec{B}")
        main_eqn.scale(1.5)

        zero_velocity = MathTex(r"\vec{0}","=","q",r"\vec{0}",r"\times",r"\vec{B}")
        zero_velocity.scale(1.5)

        parallel = MathTex("0","=","q","v","B",r"sin(0)").scale(1.5)

        all_eqns = [main_eqn,zero_velocity,parallel]
        for eqn in all_eqns:
            eqn.set_color_by_tex("F",RED)
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("{v}",GREEN_A)
            eqn.set_color_by_tex("B",BLUE)

        main_copy = main_eqn.copy()

        self.play(Write(main_eqn))
        self.wait()
        self.play(Transform(main_eqn,zero_velocity))
        self.wait()
        self.play(Transform(main_eqn,parallel))
        self.wait()
        self.play(Transform(main_eqn,main_copy))
        self.wait()
        self.play(Wiggle(main_eqn.get_parts_by_tex("times")))
        self.wait()

class LorenzForceIntro(Scene):
    def construct(self):
        main_eqn = MathTex(r"\vec{F}","=","q",r"\vec{v}",r"\times",r"\vec{B}")
        main_eqn.scale(1.5)

        zero_velocity = MathTex(r"\vec{0}","=","q",r"\vec{0}",r"\times",r"\vec{B}")
        zero_velocity.scale(1.5)

        parallel = MathTex("0","=","q","v","B",r"sin(0)").scale(1.5)

        all_eqns = [main_eqn,zero_velocity,parallel]
        for eqn in all_eqns:
            eqn.set_color_by_tex("F",RED)
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("{v}",GREEN_A)
            eqn.set_color_by_tex("B",BLUE)

        main_copy = main_eqn.copy()

        self.play(Write(main_eqn))
        self.wait()
        self.play(Transform(main_eqn,zero_velocity))
        self.wait()
        self.play(Transform(main_eqn,parallel))
        self.wait()
        self.play(Transform(main_eqn,main_copy))
        self.wait()
        self.play(Wiggle(main_eqn.get_parts_by_tex("times")))
        self.wait()

class VectorsInOut(Scene):
    def construct(self):
        in_vector = VGroup(Circle(radius=0.5,color=WHITE),Line(start=0.25*DL,end=0.25*UR,color=WHITE),Line(start=0.25*DR,end=0.25*UL,color=WHITE))
        out_vector = VGroup(Circle(radius=0.5,color=WHITE),Dot(color=WHITE))

        self.play(Write(out_vector))
        self.wait()
        self.play(FadeOut(out_vector))
        self.wait()
        self.play(Write(in_vector))
        self.wait()
        self.play(FadeOut(in_vector))
        self.wait()

class LorenzDirectionExample(ThreeDScene):
    def construct(self):
        c1 = charge.Charge(pos=np.array([0,0]),charge=-1,radius=0.5)
        c1_things = VGroup(c1.image,c1.text).set_z_index(5)
        b_field = ArrowVectorField(lambda pos: 2*RIGHT,
                                   x_range=[-4,4],
                                   y_range=[-2,2]).set_color(BLUE_D).set_opacity(0.7)
        b_label = Tex(r"$\vec{B}$").set_color(BLUE).next_to(b_field,UR)
        velocity = Vector(2*OUT)

        velocity_out_circles = VGroup(Dot(color=WHITE).shift(2*LEFT),Circle(radius=0.5,color=WHITE).shift(2*LEFT))
        v_label = Tex(r"$\vec{v}$").set_color(GREEN).next_to(velocity_out_circles,UR)

        self.play(FadeIn(c1.image,c1.text))
        self.play(*[GrowArrow(vec) for vec in b_field])
        self.play(GrowArrow(velocity))
        self.wait()
        self.play(velocity.animate.shift(2*LEFT))
        self.play(Write(velocity_out_circles),FadeOut(velocity))
        self.play(Write(b_label),Write(v_label))
        self.wait()

class RHRWrite1(Scene):
    def construct(self):
        rhr = SVGMobject("svg/right-hand-rule-ex1.svg").scale(2)

        self.play(Write(rhr))
        self.wait()

class VCrossBPointsUp(Scene):
    def construct(self):
        up_arrow = Vector(2*UP).set_color(GREEN_B)
        down_arrow = Vector(DOWN).set_color(RED)

        label = MathTex(r"\vec{v}",r"\times",r"\vec{B}").next_to(up_arrow,UR)
        label.set_color_by_tex("v",GREEN)
        label.set_color_by_tex("B",BLUE)

        label2 = MathTex("q",r"\vec{v}",r"\times",r"\vec{B}").next_to(down_arrow,RIGHT)
        label2.set_color_by_tex("q",GREEN_A)
        label2.set_color_by_tex("v",GREEN)
        label2.set_color_by_tex("B",BLUE)

        self.play(GrowArrow(up_arrow),FadeIn(label))
        self.wait()
        self.play(Transform(up_arrow,down_arrow),FadeOut(label),FadeIn(label2))
        self.wait()

class PathTracingExample(Scene):
    def construct(self):
        mag_field = VGroup(Circle(radius=0.5,color=BLUE),Line(start=0.25*DL,end=0.25*UR,color=BLUE),Line(start=0.25*DR,end=0.25*UL,color=BLUE))
        b_label = Tex(r"$\vec{B}$").next_to(mag_field,UR).shift(0.25*DL).set_color(BLUE)

        c1 = charge.Charge(radius=0.5)
        c1_stuff = VGroup(c1.image,c1.text)
        c1_stuff.shift(3*DOWN+2.5*RIGHT)

        velocity1 = Vector(UP).set_color(GREEN).next_to(c1_stuff,UP)
        v1_label = Tex(r"$\vec{v}$").next_to(velocity1,UR).set_color(GREEN)

        force1 = Vector(LEFT).set_color(RED).next_to(c1_stuff,LEFT)
        f1_label = Tex(r"$\vec{F}$").next_to(force1,UL).set_color(RED).scale(0.75)

        c1_and_arrow = VGroup(c1_stuff,velocity1,v1_label)

        theta = ValueTracker(0)


        self.play(Write(mag_field))
        self.play(FadeIn(b_label))
        self.play(Write(c1_stuff))
        self.play(GrowArrow(velocity1))
        self.play(FadeIn(v1_label))
        self.wait()
        self.play(c1_and_arrow.animate.shift(3*UP))
        self.wait()

        c1_stuff.add_updater(lambda mobject: mobject.move_to(2.5*np.cos(theta.get_value())*RIGHT+2.5*np.sin(theta.get_value())*UP))
        velocity1.add_updater(lambda mobject: mobject.put_start_and_end_on(2.5*np.cos(theta.get_value())*RIGHT+2.5*np.sin(theta.get_value())*UP +
                                                                           -0.7*np.sin(theta.get_value())*RIGHT+0.7*np.cos(theta.get_value())*UP,
                                                                           2.5*np.cos(theta.get_value())*RIGHT+2.5*np.sin(theta.get_value())*UP +
                                                                           -1.7*np.sin(theta.get_value())*RIGHT+1.7*np.cos(theta.get_value())*UP))
        v1_label.add_updater(lambda mobject: mobject.move_to(velocity1.get_end()).shift(0.2*np.cos(theta.get_value())*RIGHT+0.2*np.sin(theta.get_value())*UP
                                                                                        -0.2*np.sin(theta.get_value())*RIGHT+0.2*np.cos(theta.get_value())*UP))
        force1.add_updater(lambda mobject: mobject.put_start_and_end_on(1.8*np.cos(theta.get_value())*RIGHT+1.8*np.sin(theta.get_value())*UP,
                                                                        0.8*np.cos(theta.get_value())*RIGHT+0.8*np.sin(theta.get_value())*UP))
        f1_label.add_updater(lambda mobject: mobject.move_to(force1.get_end()).shift(0.2*np.cos(theta.get_value())*RIGHT+0.2*np.sin(theta.get_value())*UP
                                                                                        -0.5*np.sin(theta.get_value())*RIGHT+0.5*np.cos(theta.get_value())*UP))

        self.play(FadeIn(force1,f1_label))

        self.play(theta.animate.set_value(PI/2))
        self.wait()

        self.play(theta.animate.set_value(PI))
        self.wait()

        self.play(theta.animate.set_value(3*PI/2))
        self.wait()

        self.play(theta.animate.set_value(2*PI))
        self.wait()

        self.play(theta.animate.set_value(4*PI),run_time=2)
        self.wait()

class DrawRHR2(Scene):
    def construct(self):
        hand = SVGMobject("svg/rhr_ex2.svg").scale(2)
        self.play(Write(hand))
        self.wait()

class NorthernLights(ThreeDScene):
    def construct(self):

        b_arrow = Vector(12*RIGHT,color=BLUE).shift(6*LEFT)
        self.play(GrowArrow(b_arrow))
        self.wait()

        c1 = charge.Charge(radius=0.5)
        c1.elements.to_edge(DL).shift(0.5*UR+2*RIGHT)
        v1 = Vector(0.33*(4*UP+RIGHT),color=RED).next_to(c1.image,UR).shift(0.2*DL)
        v_para = Vector().put_start_and_end_on(start=v1.get_start(),end=v1.get_start()+0.33*RIGHT)
        v_perp = Vector().put_start_and_end_on(start=v_para.get_end(),end=v_para.get_end()+0.33*4*UP)

        self.play(Write(c1.image),Write(c1.text))
        self.play(GrowArrow(v1))
        self.play(GrowArrow(v_para),GrowArrow(v_perp))
        self.wait()

        cork_speed = 0.2
        radius = 2
        corkscrew = ParametricFunction(lambda t:
                                       cork_speed*t*RIGHT+
                                       radius*np.sin(t)*UP+
                                       radius*np.cos(t)*OUT,
                                        t_range=[-25,25])
        corkscrew.set_color_by_gradient(BLUE,PURPLE)

        self.play(Write(corkscrew),FadeOut(c1.elements,v1,v_para,v_perp),run_time=4)
        self.wait()
        self.move_camera(theta=0,phi=PI/2,run_time=2)
        self.move_camera(theta=PI/2,phi=PI,run_time=2)
        self.wait()

class wire1OfChargeLorenzDefinition(Scene):
    def construct(self):
        wire1 = Vector(8*RIGHT).shift(4*LEFT).set_color(YELLOW_A)
        w_label = Tex(r"$I$").set_color(YELLOW_A).next_to(wire1.get_end(),UR)
        w_and_label = VGroup(wire1,w_label)

        self.play(GrowArrow(wire1),FadeIn(w_label))
        self.wait()
        self.play(w_and_label.animate.to_edge(UP))
        self.wait()

        lorenz_law = MathTex(r"\vec{F}","=",r"Q_{\text{total}}",r"\vec{v}",r"\times",r"\vec{B}")
        lorenz_law.scale(1.25).next_to(w_and_label,DOWN)

        eqn2 = MathTex(r"\vec{F}","=","{n}","q","A","l",r"\vec{v}",r"\times",r"\vec{B}")
        eqn2.scale(1.25).next_to(lorenz_law,DOWN)

        eqn3 = MathTex(r"\vec{F}","=","{n}","q","A","{v}",r"\vec{l}",r"\times",r"\vec{B}")
        eqn3.scale(1.25).next_to(eqn2,DOWN)

        eqn4 = MathTex(r"\vec{F}","=","I",r"\vec{l}",r"\times",r"\vec{B}")
        eqn4.scale(1.25).next_to(eqn3,DOWN)

        eqn5 = MathTex(r"\vec{F}","=",r"\int","I",r"d\vec{l}",r"\times",r"\vec{B}")
        eqn5.scale(1.25).next_to(eqn4,DOWN)

        all_eqns = [lorenz_law,eqn2,eqn3,eqn4,eqn5]
        for eqn in all_eqns:
            eqn.set_color_by_tex("F",RED)
            eqn.set_color_by_tex("{v}",GREEN_A)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("{n}",LIGHT_GRAY)
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("A",GREEN_A)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("Q",GREEN)
            eqn.set_color_by_tex("I",YELLOW_E)

        for eqn in all_eqns:
            self.play(Write(eqn))
            self.wait()

# (This is the part where we measure magnetic field using voltage)
class HallVoltage(Scene):
    def construct(self):
        b_field = VGroup(Circle(radius=0.5,color=BLUE),Line(start=0.25*DL,end=0.25*UR,color=BLUE),Line(start=0.25*DR,end=0.25*UL,color=BLUE))
        b_field.shift(2*UP)
        b_label = Tex(r"$\vec{B}$").next_to(b_field,UR).shift(0.25*DL).set_color(BLUE)

        wire1 = Vector(8*RIGHT).shift(4*LEFT+DOWN).set_color(YELLOW_A)
        w_label = Tex(r"$I$").set_color(YELLOW_A).next_to(wire1.get_end(),UR)

        c1 = charge.Charge(radius=0.5)
        c1.elements.shift(DOWN+4*LEFT)

        c2 = charge.Charge(radius=0.5)
        c2.elements.shift(DOWN)

        e_field = Vector(DOWN).shift(0.7*DOWN).set_color(RED)
        e_label = Tex(r"$\vec{E}$").next_to(e_field.get_end(),DR).shift(0.25*UL).set_color(RED)

        eqn0 = MathTex("q","E","=","q",r"\vec{v}",r"\times",r"\vec{B}")
        eqn0.to_edge(UR).shift(LEFT)

        eqn1 = MathTex("q","E","=","q","v","B",r"sin(\theta)")
        eqn1.move_to(eqn0)

        eqn2 = MathTex("q","E","=","q","v","B")
        eqn2.move_to(eqn1)

        eqn3 = MathTex("E","=","v","B")
        eqn3.next_to(eqn2,DOWN)

        eqn4 = MathTex("V","=",r"-\oint",r"\vec{E}",r"\cdot",r"d\vec{l}")
        eqn4.to_edge(UL)

        eqn5 = MathTex("V","=","-""E","l")
        eqn5.next_to(eqn4,DOWN)

        eqn6 = MathTex("E","=","-","{V",r"\over","l}")
        eqn6.next_to(eqn5,DOWN)

        eqn7 = MathTex("-","{V",r"\over","l}","=","v","B")
        eqn7.next_to(eqn3,DOWN)

        eqn8 = MathTex("-","{V",r"\over","v","l}","=","B")
        eqn8.next_to(eqn7,DOWN)

        eqns = [eqn0,eqn1,eqn2,eqn3,eqn4,eqn5,eqn6,eqn7,eqn8]
        for eqn in eqns:
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("v",GREEN_A)
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("theta",LIGHT_GRAY)
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("l",RED)


        self.play(Write(b_field),FadeIn(b_label))
        self.wait()
        self.play(Write(wire1),FadeIn(w_label))
        self.wait()
        self.play(FadeIn(c1.elements))
        self.play(MoveAlongPath(c1.elements,wire1))
        self.play(FadeOut(c1.elements))
        self.play(FadeIn(c2.elements))
        self.play(c2.elements.animate.shift(UP))
        self.wait()
        self.play(GrowArrow(e_field),FadeIn(e_label))
        self.wait()

        self.play(Write(eqn0))
        self.wait()
        self.play(Transform(eqn0,eqn1))
        self.wait()
        self.play(Transform(eqn0,eqn2))
        self.wait()
        self.play(Write(eqn3))
        self.wait()
        self.play(Write(eqn4))
        self.wait()
        self.play(Write(eqn5))
        self.wait()
        self.play(Write(eqn6))
        self.wait()
        self.play(Write(eqn7))
        self.wait()
        self.play(Write(eqn8))
        self.wait()

        v_brace = Brace(VGroup(c2.image,e_field),RIGHT)

        self.play(FadeIn(v_brace))
        self.wait()

class Parallelwire1sExample(ThreeDScene):
    def construct(self):
        top_wire1 = Vector(6*RIGHT).shift(3*LEFT+UP).set_color(YELLOW_A)
        bottom_wire1 = Vector(6*RIGHT).shift(3*LEFT+DOWN).set_color(YELLOW_A)

        top_mag_field = MagneticField(Wire(top_wire1),
                                        x_range=[0,0],
                                         y_range=[-3,3],
                                         z_range=[-3,3])

        bottom_mag_field = MagneticField(Wire(bottom_wire1),
                                         x_range=[0,0],
                                         y_range=[-3,3],
                                         z_range=[-3,3])

        mag_field = top_mag_field+bottom_mag_field


        top_b_field = VGroup(Circle(radius=0.5,color=BLUE),
                            Dot(color=BLUE))
        top_b_field.shift(2*UP)

        top_b_label = Tex(r"$\vec{B}$").set_color(BLUE).next_to(top_b_field,UR)

        force1_vec = Vector(DOWN,color=RED).shift(0.7*UP+0.2*RIGHT)
        f1_label = Tex(r"$\vec{F}$").set_color(RED).next_to(force1_vec.get_end(),RIGHT)

        bottom_b_field = VGroup(Circle(radius=0.5,color=BLUE),
                                Line(start=0.25*DL,end=0.25*UR,color=BLUE),
                                Line(start=0.25*DR,end=0.25*UL,color=BLUE))
        bottom_b_field.shift(2*DOWN)
        bottom_b_label = Tex(r"$\vec{B}$").set_color(BLUE).next_to(bottom_b_field,DL)



        force2_vec = Vector(UP,color=RED).shift(0.7*DOWN+0.2*LEFT)
        f2_label = Tex(r"$\vec{F}$").set_color(RED).next_to(force2_vec.get_end(),LEFT)

        self.play(Write(top_wire1))
        self.play(Write(bottom_wire1))
        self.move_camera(phi=2*PI,run_time=2)
        # self.play(Write(mag_field),run_time=1)
        # self.move_camera(theta=0,phi=2*PI+PI/2,run_time=2)
        # self.move_camera(theta=-PI/2,phi=2*PI,run_time=2)
        # self.wait()
        # self.play(FadeOut(bottom_mag_field,top_mag_field))
        # self.wait()
        self.play(FadeIn(top_b_field,top_b_label))
        self.wait()
        self.play(GrowArrow(force1_vec),FadeIn(f1_label))
        self.wait()
        self.play(Write(bottom_b_field),FadeIn(bottom_b_label))
        self.wait()
        self.play(GrowArrow(force2_vec),FadeIn(f2_label))
        self.wait()

class RailgunExample(Scene):
    def construct(self):
        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))
        c1.elements.move_to(3*RIGHT).rotate(-PI/2)

        c1_plus = Tex(r"$+$").next_to(c1.image,RIGHT).shift(0.5*UP)
        c1_minus = Tex(r"$-$").next_to(c1.image,RIGHT).shift(0.5*DOWN)

        w1 = wire.Wire()
        w1.add_point(c1.get_start_point())
        w1.add_point(Point(c1.get_start_pos()+0.5*UP))
        w1.add_point(Point(c1.get_start_pos()+0.5*UP+6*LEFT))

        w2 = wire.Wire()
        w2.add_point(c1.get_end_point())
        w2.add_point(Point(c1.get_end_pos()+0.5*DOWN))
        w2.add_point(Point(c1.get_end_pos()+0.5*DOWN+6*LEFT))

        circuit = VGroup(w1.image,c1.image,w2.image)
        circuit.set_color_by_gradient(GREEN,BLUE)

        b_arrow = VGroup(Circle(radius=0.5,color=BLUE),Dot(color=BLUE))
        b_arrow.shift(0.2*DOWN)
        b_label = Tex(r"$\vec{B}$").next_to(b_arrow,UR).shift(0.25*DL).set_color(BLUE)

        gray_metal = Line(start=UP,end=DOWN).shift(RIGHT).set_color(GRAY)

        wire1_arrow = Vector(DOWN).next_to(gray_metal,RIGHT).set_color(YELLOW_A)
        i_label = Tex("$I$").next_to(wire1_arrow.get_end(),RIGHT).set_color(YELLOW_E)

        force_arrow = Vector(LEFT).set_color(RED).next_to(gray_metal,LEFT)
        f_label = Tex(r"$\vec{F}$").next_to(force_arrow,LEFT).set_color(RED)

        moving_stuff = VGroup(gray_metal,force_arrow,f_label,wire1_arrow,i_label)

        header = Text("Railgun").scale(1.5).to_edge(UP)

        ohm_law = MathTex("V","=","I","R")
        ohm_law.to_edge(UR).shift(LEFT)
        lorenz_wire1 = MathTex(r"\vec{F}","=",r"\int","I",r"d\vec{l}",r"\times",r"\vec{B}")
        lorenz_wire1.next_to(ohm_law,DOWN)

        eqns = [ohm_law,lorenz_wire1]
        for eqn in eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)
            eqn.set_color_by_tex("F",RED)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("B",BLUE)

        self.play(Write(c1.image),FadeIn(c1_plus,c1_minus))
        self.play(Write(w1.image),Write(w2.image))
        self.wait()
        self.play(Write(b_arrow),FadeIn(b_label))
        self.wait()
        self.play(Write(gray_metal))
        self.wait()
        self.play(Write(wire1_arrow),FadeIn(i_label))
        self.wait()
        self.play(Write(ohm_law))
        self.play(Write(lorenz_wire1))
        self.wait()
        self.play(VGroup(b_arrow,b_label).animate.shift(2.3*DOWN))
        self.wait()
        self.play(Write(force_arrow),FadeIn(f_label))
        self.wait()
        self.play(moving_stuff.animate.shift(25*LEFT),rate_func=rate_functions.ease_in_quart)
        self.wait()
        self.play(FadeIn(header))
        self.wait()

class Motor3DExample(ThreeDScene):
    def construct(self):
        loop = VGroup(Line(start=DOWN,end=DOWN+2*OUT),
                      Line(start=DOWN+2*OUT,end=2*DOWN+2*OUT),
                      Line(start=2*DOWN+2*OUT,end=2*DOWN+4*OUT),
                      Line(start=2*DOWN+4*OUT,end=2*UP+4*OUT),
                      Line(start=2*UP+4*OUT,end=2*UP+2*OUT),
                      Line(start=2*UP+2*OUT,end=UP+2*OUT),
                      Vector(2*IN).shift(UP+2*OUT)).shift(2*IN).set_color(YELLOW_A)

        i_label = Tex(r"$I$",color=YELLOW_E).next_to(loop[-1].get_end(),UP+IN).rotate(PI/2,RIGHT).rotate(PI/2,OUT)

        ax = Vector(6*OUT).shift(3*IN)
        tau = Tex(r"$\tau$").next_to(ax.get_end(),UR).rotate(PI/2,RIGHT)
        tau.set_color_by_tex("tau",BLUE_B)

        self.wait()
        self.move_camera(phi=PI/2,theta=-PI/4)
        self.play(Write(loop),FadeIn(i_label))
        self.wait()
        self.move_camera(theta=2*PI-PI/4)
        self.wait()
        self.play(Write(ax),FadeIn(tau))
        self.wait()
        self.move_camera(phi=0)
        self.wait()

class Motor2DExample(Scene):
    def construct(self):
        eqn1 = MathTex(r"\vec{\tau}","=",r"\vec{r}",r"\times",r"\vec{F}")
        eqn1.to_edge(UL)

        eqn2 = MathTex(r"\vec{\tau}","=","{r}","F",r"sin(\theta)")
        eqn2.next_to(eqn1,DOWN)

        eqn3 = MathTex(r"\vec{\tau_{\text{loop}}}","=","(","{w",r"\over","2}","F",r"sin(\theta)",")","2")
        eqn3.next_to(eqn2,DOWN)
        eqn3.shift(0.75*RIGHT)

        eqn4 = MathTex(r"\vec{\tau_{\text{loop}}}","=","w","F",r"sin(\theta)")
        eqn4.next_to(eqn3,DOWN).shift(0.3*LEFT)

        eqn5 = MathTex(r"\vec{F}","=","I",r"{l}","{B}",r"sin(\theta)").to_edge(UR)
        eqn6 = MathTex(r"\vec{F}","=","I",r"{l}","{B}")
        eqn6.next_to(eqn5,DOWN)

        eqn7 = MathTex(r"\vec{\tau_{\text{loop}}}","=","w","I","{l}","{B}",r"sin(\theta)")
        eqn7.next_to(eqn4,DOWN).shift(0.4*DOWN+0.2*RIGHT)

        eqn8 = MathTex(r"\vec{\tau_{\text{loop}}}","=","I","A","B",r"sin(\theta)")
        eqn8.next_to(eqn7,DOWN)

        eqn9 = MathTex(r"\vec{\tau_{\text{loop}}}","=",r"\vec{\mu}",r"\times",r"\vec{B}")
        eqn9.next_to(eqn8,DOWN)

        mu_def = MathTex(r"|\vec{\mu}|","=","N","I","A")
        mu_def.next_to(eqn9,DOWN)

        eqns = [eqn1,eqn2,eqn3,eqn4,eqn5,eqn6,eqn7,eqn8,eqn9,mu_def]
        for eqn in eqns:
            eqn.set_color_by_tex("tau",BLUE_B)
            eqn.set_color_by_tex("{r}",RED)
            eqn.set_color_by_tex("F",RED)
            eqn.set_color_by_tex("{l}",RED)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("mu",BLUE)

        top_wire1 = Line(start=1.575*DL,end=1.575*UR,color=YELLOW_A)

        b_field = Vector(8*RIGHT).shift(4*LEFT).set_color(BLUE).set_z_index(-5)
        b_label = Tex(r"$\vec{B}$").next_to(b_field.get_end(),UP).set_color(BLUE)

        current_in = VGroup(Circle(radius=0.5).set_color(YELLOW_C),
                            Dot().set_color(YELLOW_C)).move_to(top_wire1.get_start())

        current_out = VGroup(Circle(radius=0.5).set_color(YELLOW_C),
                             Line(start=0.25*DL,end=0.25*UR,color=YELLOW_C),
                             Line(start=0.25*UL,end=0.25*DR,color=YELLOW_C)).move_to(top_wire1.get_end())

        f1 = Vector(2.5*UP,color=RED).put_start_and_end_on(current_in.get_center(),current_in.get_center()+2.5*UP)
        f2 = Vector(2.5*DOWN,color=RED).put_start_and_end_on(current_out.get_center(),current_out.get_center()+2.5*DOWN)

        f1_label = Tex(r"$\vec{F}$",color=RED).next_to(f1.get_end(),UP)
        f2_label = Tex(r"$\vec{F}$",color=RED).next_to(f2.get_end(),DOWN)

        t1_arc = Arc(radius=1,start_angle=PI/4,angle=PI/4).move_arc_center_to(f1.get_start())
        t2_arc = Arc(radius=1,start_angle=3*PI/2-PI/4,angle=PI/4).move_arc_center_to(f2.get_start())
        t3_arc = Arc(radius=1,start_angle=3*PI/2+PI/4,angle=PI/4)

        mu_vec = Vector(color=BLUE).put_start_and_end_on(ORIGIN,DR)        
        mu_label = Tex(r"$\mu$",color=BLUE).next_to(mu_vec.get_end(),DOWN)

        spinny_stuff = VGroup(top_wire1,t1_arc,t2_arc,t3_arc,f1,f2,f1_label,f2_label,
                              mu_vec,mu_label,current_in,current_out)

        self.play(FadeIn(eqn1))
        self.wait()
        self.play(FadeIn(top_wire1))
        self.play(GrowArrow(b_field),FadeIn(b_label))
        self.play(Write(current_in))
        self.play(Write(current_out))
        self.play(FadeIn(eqn2))
        self.wait()
        self.play(GrowArrow(f1),GrowArrow(f2),FadeIn(f1_label,f2_label))
        self.play(Write(t1_arc),Write(t2_arc))
        self.play(FadeIn(eqn3))
        self.wait()
        self.play(FadeIn(eqn4))
        self.wait()
        self.play(FadeIn(eqn5))
        self.wait()
        self.play(FadeIn(eqn6))
        self.wait()
        self.play(FadeIn(eqn7))
        self.wait()
        self.play(FadeIn(eqn8))
        self.wait()
        self.play(FadeIn(eqn9))
        self.wait()
        self.play(FadeIn(mu_def))
        self.play(GrowArrow(mu_vec),Write(mu_label),Write(t3_arc))
        self.wait()
        self.play(Rotate(spinny_stuff,2*PI),run_time=2)
        self.wait()

class GaussLawMagnetic(Scene):
    def construct(self):
        header = Text("Gauss's Law for Magnetism").scale(1.25).to_edge(UP)        

        law_eqn = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}","=","0").scale(1.5)
        law_eqn.set_color_by_tex("B",BLUE)
        law_eqn.set_color_by_tex("A",GREEN)
        
        self.play(Write(law_eqn))
        self.play(FadeIn(header))        
        self.wait()

class PathIntegral(Scene):
    def construct(self):

        def wiggle_func(t):
            return np.array([t,np.sin(3*t) + np.sin(5*t),0])
        
        def stretch_func(pos):
            x,y,z = pos
            angle = np.arctan2(y,x)
            radius = np.sqrt(x*x+y*y)
            new_x = radius*np.cos(angle+0.1*radius)*2
            new_y = radius*np.sin(angle+0.1*radius)

            return np.array([new_x,new_y,z])
        
        wiggly_line = ParametricFunction(
            wiggle_func,
            t_range = np.array([-PI, PI]),
            color = BLUE
        )

        stretched_points = np.array([stretch_func(point) for point in wiggly_line.points])
        wiggly_line.set_points(stretched_points)

        vector_field = ArrowVectorField(lambda pos: RIGHT).set_opacity(0.75)

        dl_vector = Vector(0.5*(3*RIGHT+1.5*DOWN)).shift(1.9*UP+0*RIGHT)
        dl_label = Tex(r"$d\vec{l}$").next_to(dl_vector.get_end(),RIGHT)

        that_one_field_vector = Vector(RIGHT).move_to(dl_vector.get_start()).shift(0.5*RIGHT)
        that_one_field_vector.set_color(YELLOW)

        theta_arc = Arc(radius=0.5,start_angle=-PI/6,angle=0)
        theta_arc.move_arc_center_to(that_one_field_vector.get_start())

        radius = 0.05
        vec1_angle = 3*PI/2 + PI/6
        vec2_angle = 0
        vec1 = Vector(RIGHT,color=BLUE).put_start_and_end_on(ORIGIN,ORIGIN+radius*np.cos(vec1_angle)*RIGHT+radius*np.sin(vec1_angle)*UP)
        vec1.move_to(UR)
        vec2 = Vector(RIGHT,color=BLUE).put_start_and_end_on(ORIGIN,ORIGIN+radius*np.cos(vec2_angle)*RIGHT+radius*np.sin(vec2_angle)*UP)
        vec2.move_to(3.1*LEFT+0.25*DOWN)
        
        self.play(FadeIn(wiggly_line,vec1,vec2))
        self.play(*[FadeIn(vec) for vec in vector_field],run_time=2)
        self.play(*[FadeOut(vec) for vec in vector_field],run_time=2)
        self.play(GrowArrow(dl_vector),FadeIn(dl_label))
        self.play(GrowArrow(that_one_field_vector),Write(theta_arc))
        self.wait()

class QuickCircle(ThreeDScene):
    def construct(self):
        circ = Circle().rotate(PI/6,UP)
        self.play(Create(circ))
        self.wait()

class AmperesLaw(Scene):
    def construct(self):
        header = Text("Ampere's Law").scale(1.5)

        the_law = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"I_{\text{thru}}")
        colored_law = the_law.copy()

        colored_law.set_color_by_tex("B",BLUE)
        colored_law.set_color_by_tex("mu",GRAY)
        colored_law.set_color_by_tex("l",RED)
        colored_law.set_color_by_tex("I",YELLOW_E)

        self.play(FadeIn(header))
        self.play(header.animate.to_edge(UP))
        self.play(Write(the_law))
        self.play(Transform(the_law,colored_law))
        self.wait()
        self.play(the_law.animate.scale(1.5))
        self.wait()

class AmpereExample(ThreeDScene):
    def construct(self):
        mag_wire1 = Wire(Line(start=DOWN,end=UP))
        mag_field = MagneticField(mag_wire1,
                                  x_range=[-4,4],
                                  y_range=[0,0],
                                  z_range=[-4,4])
        visual_wire1 = Vector(4*UP).shift(2*DOWN).set_color(YELLOW_A)
        loop = Circle(radius=2).rotate(PI/2,RIGHT)

        self.move_camera(phi=PI/4,theta=3*PI/4)
        self.play(GrowArrow(visual_wire1))
        self.play(FadeIn(mag_field))
        self.wait()
        self.play(Write(loop))
        self.wait()

class AmpereExampleEqns(Scene):
    def construct(self):
        the_law = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"I_{\text{thru}}")
        the_law.to_edge(UL)

        eqn2 = MathTex(r"\oint",r"{B}",r"dl","=",r"\mu_0",r"I_{\text{thru}}")
        eqn2.next_to(the_law,DOWN)

        eqn3 = MathTex("B",r"\oint",r"dl","=",r"\mu_0",r"I_{\text{thru}}")
        eqn3.next_to(eqn2,DOWN)

        eqn4 = MathTex("B","2",r"\pi","{r}","=",r"\mu_0",r"I_{\text{thru}}")
        eqn4.next_to(eqn3,DOWN)

        eqn5 =  MathTex("B","=",r"{\mu_0",r"I_{\text{thru}}",r"\over","2",r"\pi","{r}}")
        eqn5.next_to(eqn4,DOWN)

        eqns = [the_law,eqn2,eqn3,eqn4,eqn5]
        for eqn in eqns:
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("pi",LIGHT_GRAY)
            eqn.set_color_by_tex("{r}",RED)
            eqn.set_color_by_tex("I",YELLOW_E)

        for eqn in eqns:
            self.play(Write(eqn))
            self.wait()
    
class MagneticFieldStrengthGraph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0,50],y_range=[-2,2],
            x_length=8,y_length=6,
            tips=True,
            axis_config={"include_ticks": False}
        )

        labels = ax.get_axis_labels(y_label=Tex("$B$").set_color(BLUE),x_label=Tex("$r$").set_color(RED))

        curve = ax.plot(lambda t: 2/(t+1)).set_color(BLUE).set_z_index(-3)

        self.play(FadeIn(ax,labels))
        self.play(Write(curve),run_time=2)
        self.wait()

class FaradaysLaw(Scene):
    def construct(self):
        header = Text("Faraday's Law").scale(1.5)
        the_law = MathTex("V","=","-","{d",r"\phi_B",r"\over","d","t}")
        colored_law = the_law.copy()
        colored_law.set_color_by_tex("V",BLUE_D)
        colored_law.set_color_by_tex("phi",GREEN)
        colored_law.set_color_by_tex("t",LIGHT_GRAY)

        self.play(FadeIn(header))
        self.play(header.animate.to_edge(UP))
        self.play(Write(the_law))
        self.play(Transform(the_law,colored_law))
        self.wait()
        self.play(the_law.animate.next_to(header,DOWN))

        raw_flux = MathTex("V","=","-","{d",r"\over","d","t}",r"\int",r"\vec{B}",r"\cdot",r"d\vec{A}")
        raw_flux.next_to(the_law,DOWN)
        raw_flux2 = MathTex(r"\int",r"\vec{E}",r"\cdot",r"d\vec{l}","=","-","{d",r"\over","d","t}",r"\int",r"\vec{B}",r"\cdot",r"d\vec{A}")
        raw_flux2.next_to(raw_flux,DOWN)
        raw_flux3 = MathTex(r"\int","(",r"\vec{E}","+",r"\vec{v}",r"\times",r"\vec{B}",")",r"\cdot",r"d\vec{l}","=","-","{d",r"\over","d","t}",r"\int",r"\vec{B}",r"\cdot",r"d\vec{A}")
        raw_flux3.next_to(raw_flux2,DOWN)

        flux_eqns = [raw_flux,raw_flux2,raw_flux3]
        for eqn in flux_eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("t",LIGHT_GRAY)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("{v}",GREEN)

        self.play(Write(raw_flux))
        self.wait()
        self.play(Write(raw_flux2))
        self.wait()
        self.play(Write(raw_flux3))
        self.wait()
        self.play(FadeOut(raw_flux,raw_flux2,raw_flux3),the_law.animate.move_to(ORIGIN))
        self.play(the_law.animate.scale(1.5))
        self.wait()

        flux = MathTex(r"\phi_B", "=", r"\int",r"\vec{B}",r"\cdot",r"d\vec{A}")
        flux.scale(1.5).next_to(the_law,DOWN)
        flux.set_color_by_tex("phi",GREEN)
        flux.set_color_by_tex("B",BLUE)
        flux.set_color_by_tex("A",GREEN)

        self.play(FadeIn(flux))
        self.play(VGroup(the_law,flux).animate.move_to(ORIGIN))
        self.wait()
        self.play(Wiggle(flux.get_parts_by_tex("{B}")))
        self.wait()
        self.play(Wiggle(flux.get_parts_by_tex("{A}")))
        self.wait()
        self.play(Wiggle(flux.get_parts_by_tex("cdot"),scale_value=1.5))
        self.wait()
        self.play(FadeOut(flux))
        self.wait()

class LenzsLaw(Scene):
    def construct(self):
        flux1 = Vector(2.5*UP,color=GREEN).shift(2.75*DOWN)
        f1_label = Tex(r"$\phi_B$",color=GREEN).next_to(flux1.get_end(),LEFT)
        
        voltage1 = Vector(2*DOWN,color=BLUE_D).shift(2.25*UP)

        circle1 = Circle().stretch(0.2,1).move_to(voltage1)
        v1_label = Tex(r"$V$",color=BLUE_D).next_to(circle1,RIGHT)

        header = Text("Lenz's Law").scale(1.5).to_edge(UP)

        flux2 = Vector(2.5*UP,color=GREEN).shift(0.2*DOWN)
        f2_label = Tex(r"$\phi_B$",color=GREEN).next_to(flux2.get_end(),LEFT)

        voltage2 = Vector(2*UP,color=BLUE_D).shift(2.25*DOWN)
        circle2 = Circle().stretch(0.2,1).move_to(voltage2)
        v2_label = Tex(r"$V$",color=BLUE_D).next_to(circle2,RIGHT)

        self.play(GrowArrow(flux1),GrowArrow(voltage1),FadeIn(f1_label,v1_label))
        self.play(FadeIn(circle1))
        self.wait()
        self.play(FadeIn(header))
        self.wait(2)
        self.play(FadeOut(flux1,f1_label,voltage1,v1_label,circle1))
        self.wait()
        self.play(GrowArrow(flux2),FadeIn(f2_label))
        self.play(Uncreate(flux2),FadeOut(f2_label),GrowArrow(voltage2),FadeIn(v2_label),Write(circle2))
        self.wait()

class EddyCurrents(Scene):
    def construct(self):
        header = Text("Eddy Currents").scale(1.5).to_edge(UP)
        field_area = Square(color=BLUE_D,side_length=3).set_opacity(0.7)

        b_arrow = VGroup(Circle(radius=0.5),Line(start=0.25*DL,end=0.25*UR),Line(start=0.25*UL,end=0.25*DR))
        b_arrow.set_color(BLUE)

        metal = Rectangle(color=GRAY,height=2,width=3).set_fill(color=color_gradient([BLACK,GRAY],2)).set_opacity(0.7)
        metal.shift(4*LEFT)


        self.add(header)
        self.wait()
        self.play(FadeIn(field_area))
        self.play(Write(b_arrow))
        self.wait()
        self.play(Write(metal))
        self.wait()
        self.play(metal.animate.shift(1.5*RIGHT))
        self.wait()

        circ_arrow = SVGMobject("svg/arrow-circle.svg").set_color(YELLOW).scale(0.5).move_to(metal)
        move_up = Vector(0.75*UP).shift(1.25*LEFT+(0.75/2)*DOWN).set_color(WHITE)
        f_left = Vector(color=RED).put_start_and_end_on(metal.get_left()+0.2*LEFT,metal.get_left()+1.2*LEFT)

        self.play(Write(circ_arrow))
        self.wait()
        self.play(Write(move_up))
        self.wait()
        self.play(Write(f_left))
        self.wait()
        self.play(FadeOut(circ_arrow,move_up,f_left),metal.animate.shift(5*RIGHT))
        self.wait()

        circ_arrow2 = SVGMobject("svg/arrow-circle.svg").set_color(YELLOW).scale(-0.5).stretch(-1,1).move_to(metal)
        move_up2 = Vector(0.75*UP).shift(1.25*RIGHT+(0.75/2)*DOWN).set_color(WHITE)
        f_left2 = Vector(color=RED).put_start_and_end_on(metal.get_right()+1.2*RIGHT,metal.get_right()+0.2*RIGHT)

        self.play(Write(circ_arrow2))
        self.wait()
        self.play(Write(move_up2))
        self.wait()
        self.play(Write(f_left2))
        self.wait()

class Transformer(Scene):
    def construct(self):
        header = Text("Transformer").scale(1.5)

        iron = Rectangle(color=GRAY,height=4,width=1).set_fill(color=color_gradient([BLACK,GRAY],2)).set_opacity(0.7)
        coil1 = VGroup(Line(start=1.5*UP,end=1.5*UP+3*LEFT),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(1.3*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(1.1*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(0.9*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(0.7*UP),
                       Line(start=0.5*UP,end=0.5*UP+3*LEFT))
        
        coil2 = coil1.copy().rotate(PI).shift(2*DOWN+2*RIGHT)


        self.play(FadeIn(header))
        self.wait()
        self.play(header.animate.to_edge(UP))
        self.wait()
        self.play(Write(iron),Write(coil1),Write(coil2))
        self.wait()
        self.play(iron.animate.shift(3*LEFT),
                  coil1.animate.shift(3*LEFT),
                  coil2.animate.shift(3*LEFT))
        self.wait()

        b_arrow = Vector(color=BLUE).put_start_and_end_on(start=coil1[0].get_start()+UP,end=coil2[0].get_start()+DOWN)
        b_label = Tex(r"$\vec{B}$",color=BLUE).next_to(b_arrow.get_end(),DR)

        eqn1 = MathTex(r"\vec{B_1}","=",r"\vec{B_2}").shift(2*UP+3*RIGHT)
        eqn2 = MathTex(r"\phi_{1,\text{loop}}","=",r"\phi_{2,\text{loop}}")
        eqn2.next_to(eqn1,DOWN)
        eqn3 = MathTex(r"{d",r"\phi_{1,\text{loop}}",r"\over","d","t}","=",r"{d",r"\phi_{2,\text{loop}}",r"\over","d","t}")
        eqn3.next_to(eqn2,DOWN)
        eqn4 = MathTex(r"|V_1|","=","N_1",r"{d",r"\phi_{1,\text{loop}}",r"\over","d","t}")
        eqn4.next_to(eqn3,DOWN)
        eqn5 = MathTex(r"{|V_1|",r"\over","N_1}","=",r"{d",r"\phi_{1,\text{loop}}",r"\over","d","t}")
        eqn5.move_to(eqn4)
        eqn6 = MathTex(r"|V_2|","=","N_2",r"{d",r"\phi_{2,\text{loop}}",r"\over","d","t}")
        eqn6.next_to(eqn5,DOWN)
        eqn7 = MathTex(r"|V_2|","=","N_2",r"{d",r"\phi_{1,\text{loop}}",r"\over","d","t}")
        eqn7.move_to(eqn6)
        eqn8 = MathTex(r"|V_2|","=",r"{N_2",r"\over","N_1}","|V_1|")
        eqn8.move_to(eqn6)
        eqn9 = MathTex("P","=","I","V")
        eqn9.shift(2*UP+3*RIGHT)

        eqns = [eqn1,eqn2,eqn3,eqn4,eqn5,eqn6,eqn7,eqn8,eqn9]
        for eqn in eqns:
            eqn.set_color_by_tex("P",PURPLE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("phi",GREEN)
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("N",LIGHT_GRAY)

        self.play(GrowArrow(b_arrow),FadeIn(b_label))
        self.wait()

        for i in range(4):
            self.play(Write(eqns[i]))
            self.wait()
        
        self.play(Write(eqn6))
        self.wait()
        self.play(Transform(eqn4,eqn5))
        self.wait()
        self.play(Transform(eqn6,eqn7))
        self.wait()
        self.play(Transform(eqn6,eqn8))
        self.wait()
        self.play(FadeOut(eqn1,eqn2,eqn3,eqn4,eqn6))
        self.play(Write(eqn9))
        self.wait()

class MagnetismTypes(Scene):
    def construct(self):
        h1 = Text("Ferromagnetic").scale(1.5)
        self.play(FadeIn(h1))
        self.wait()
        self.play(h1.animate.to_edge(UP))
        self.wait()

        mm1 = SVGMobject("svg/magnetic-material.svg").scale(2)
        self.play(Write(mm1))

        def get_random_vec():
            return Vector((random.random()-0.5)*RIGHT+(random.random()-0.5)*UP)

        domains = VGroup(get_random_vec(),
                         get_random_vec().shift(LEFT+0.5*UP),
                         get_random_vec().shift(1.2*LEFT+0.4*DOWN),
                         get_random_vec().shift(DOWN+0.5*LEFT),
                         get_random_vec().shift(2*LEFT+1.4*DOWN),
                         get_random_vec().shift(2.2*LEFT+0.4*DOWN),
                         get_random_vec().shift(2.2*LEFT),
                         get_random_vec().shift(3*LEFT+0.3*UP),
                         get_random_vec().shift(2.4*LEFT+0.4*UP),
                         get_random_vec().shift(2*LEFT+0.75*UP),
                         get_random_vec().shift(1.8*LEFT+UP),
                         get_random_vec().shift(2.5*LEFT+UP),
                         get_random_vec().shift(1.8*LEFT+1.4*UP),
                         get_random_vec().shift(LEFT+1.5*UP),
                         get_random_vec().shift(UP),
                         get_random_vec().shift(DOWN+0.5*RIGHT),
                         get_random_vec().shift(RIGHT+0.5*UP),
                         get_random_vec().shift(UR),
                         get_random_vec().shift(2*RIGHT+UP),
                         get_random_vec().shift(2*RIGHT),
                         get_random_vec().shift(RIGHT+0.5*DOWN),
                         get_random_vec().shift(1.5*DR),
                         get_random_vec().shift(3*RIGHT),
                         get_random_vec().shift(3*RIGHT+DOWN),
                         get_random_vec().shift(3*RIGHT+UP))
        
        domains2 = VGroup(get_random_vec(),
                         get_random_vec().shift(LEFT+0.5*UP),
                         get_random_vec().shift(1.2*LEFT+0.4*DOWN),
                         get_random_vec().shift(DOWN+0.5*LEFT),
                         get_random_vec().shift(2*LEFT+1.4*DOWN),
                         get_random_vec().shift(2.2*LEFT+0.4*DOWN),
                         get_random_vec().shift(2.2*LEFT),
                         get_random_vec().shift(3*LEFT+0.3*UP),
                         get_random_vec().shift(2.4*LEFT+0.4*UP),
                         get_random_vec().shift(2*LEFT+0.75*UP),
                         get_random_vec().shift(1.8*LEFT+UP),
                         get_random_vec().shift(2.5*LEFT+UP),
                         get_random_vec().shift(1.8*LEFT+1.4*UP),
                         get_random_vec().shift(LEFT+1.5*UP),
                         get_random_vec().shift(UP),
                         get_random_vec().shift(DOWN+0.5*RIGHT),
                         get_random_vec().shift(RIGHT+0.5*UP),
                         get_random_vec().shift(UR),
                         get_random_vec().shift(2*RIGHT+UP),
                         get_random_vec().shift(2*RIGHT),
                         get_random_vec().shift(RIGHT+0.5*DOWN),
                         get_random_vec().shift(1.5*DR),
                         get_random_vec().shift(3*RIGHT),
                         get_random_vec().shift(3*RIGHT+DOWN),
                         get_random_vec().shift(3*RIGHT+UP))
                    
        self.play(*[GrowArrow(vec) for vec in domains])
        self.wait()

        b_field = Vector(10*RIGHT,color=BLUE).shift(5*LEFT).set_z_index(-3)
        b_label = Tex(r"$\vec{B}$",color=BLUE).next_to(b_field.get_end(),UR)

        self.play(GrowArrow(b_field),FadeIn(b_label))
        self.play(*[vec.animate.set_angle(0) for vec in domains])
        self.wait()

        self.play(FadeOut(b_field,b_label))
        self.wait()
        self.play(FadeOut(h1,domains,mm1))
        self.wait()

        h2 = Text("Paramagnetism").scale(1.5).to_edge(UP)
        self.play(FadeIn(h2))
        self.wait()

        mm2 = SVGMobject("svg/magnetic-material2.svg").scale(2)
        d2_cpy = domains2.copy()
        self.play(Write(mm2))
        self.play(*[GrowArrow(vec) for vec in domains2])
        self.play(GrowArrow(b_field),FadeIn(b_label))
        self.play(*[vec.animate.set_angle(0) for vec in domains2])
        self.wait()

        self.play(FadeOut(b_field,b_label))
        self.play(Transform(domains2,d2_cpy))
        self.wait()
        self.play(FadeOut(h2,mm2,domains2))
        self.wait()

        h3 = Text("Diamagnetism").scale(1.5).to_edge(UP)
        self.play(FadeIn(h3))
        self.wait()

        loop1 = Circle().stretch(0.2,0).shift(0.5*LEFT)
        loop2 = Circle().stretch(0.2,0).rotate(PI).shift(0.5*RIGHT)

        mag1 = Vector(color=BLUE).put_start_and_end_on(loop1.get_center(),loop1.get_center()+LEFT)
        mag2 = Vector(color=BLUE).put_start_and_end_on(loop2.get_center(),loop2.get_center()+RIGHT)

        self.play(Write(loop1),Write(loop2),GrowArrow(mag1),GrowArrow(mag2))
        self.wait()
        self.play(GrowArrow(b_field.copy().shift(UP)),GrowArrow(b_field.shift(DOWN)),FadeIn(b_label.shift(DOWN)))
        self.wait()
        self.play(VGroup(loop1,mag1).animate.scale(1.5),
                  VGroup(loop2,mag2).animate.scale(0.5))
        self.wait()

        self.play(FadeOut(h3))
        self.wait()

class Inductor(Scene):
    def construct(self):
        iron = Rectangle(color=GRAY,height=4,width=1).set_fill(color=color_gradient([BLACK,GRAY],2)).set_opacity(0.7)
        coil1 = VGroup(Line(start=1.5*UP,end=1.5*UP+3*LEFT),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(1.3*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(1.1*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(0.9*UP),
                       Circle(radius=1,color=WHITE).stretch(0.2,1).shift(0.7*UP),
                       Line(start=0.5*UP,end=0.5*UP+3*LEFT)).move_to(LEFT)

        eqn1 = MathTex(r"\phi_B","=","L","I").shift(2*UP+3*RIGHT)
        eqn2 = MathTex(r"V","=","-","L","{d","I",r"\over","d","t}").next_to(eqn1,DOWN)

        header = Text("Inductor").scale(1.5).to_edge(UP)

        eqns = [eqn1,eqn2]
        for eqn in eqns:
            eqn.set_color_by_tex("phi",GREEN)
            eqn.set_color_by_tex("V",BLUE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("L",PURPLE_D)
            eqn.set_color_by_tex("t",LIGHT_GRAY)

        self.play(FadeIn(iron))
        self.play(Write(coil1))
        self.wait()
        self.play(VGroup(iron,coil1).animate.to_edge(LEFT))
        self.wait()
        self.play(Write(eqn1))
        self.wait()
        self.play(Write(eqn2))
        self.wait()
        self.play(FadeIn(header))
        self.wait()

class InductorWaves(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2.5,10],
            y_range=[-3,3],
            tips=True,
            axis_config={"include_ticks": False}
        )

        voltage_graph = ax.plot(lambda t: np.sin(t),color=BLUE)
        amps_graph = ax.plot(lambda t: 2*np.sin(t),color=YELLOW_A)
        amps_graph2 = ax.plot(lambda t: 2*np.sin(t-PI/2),color=YELLOW_A)

        v0_ticks = VGroup(Line(start=3.8*LEFT+UP,end=3.4*LEFT+UP),
                          Line(start=3.8*LEFT+DOWN,end=3.4*LEFT+DOWN))
        v0_labels = VGroup(Tex("$V_0$").next_to(v0_ticks[0],LEFT),
                           Tex("$-V_0$").next_to(v0_ticks[1],RIGHT))

        i0_ticks = VGroup(Line(start=3.8*LEFT+2*UP,end=3.4*LEFT+2*UP),
                          Line(start=3.8*LEFT+2*DOWN,end=3.4*LEFT+2*DOWN))
        i0_labels = VGroup(Tex("$I_0$").next_to(i0_ticks[0],LEFT),
                           Tex("$-I_0$").next_to(i0_ticks[1],RIGHT))
        
        self.add(ax)
        self.play(Write(voltage_graph),Write(v0_ticks),Write(v0_labels))
        self.wait()
        self.play(Write(amps_graph),Write(i0_ticks),Write(i0_labels))
        self.wait()
        self.play(Transform(amps_graph,amps_graph2),i0_labels[1].animate.shift(1.5*LEFT),
                  v0_labels[1].animate.shift(1.5*LEFT))
        self.wait()

class InductorReactance(Scene):
    def construct(self):
        header = Text("Reactance").scale(1.5)

        the_eqn = MathTex("X","=","\\omega","L")
        the_eqn.set_color_by_tex("X",RED)
        the_eqn.set_color_by_tex("omega",GREEN)
        the_eqn.set_color_by_tex("L",PURPLE_D)
        
        self.play(FadeIn(header))
        self.play(header.animate.to_edge(UP))
        self.wait()
        self.play(Write(the_eqn))
        self.play(the_eqn.animate.scale(2))
        self.wait()

class InductorPhasor(Scene):
    def construct(self):
        main_circle = Circle(color=GREEN,radius=3)
        y_axis = Vector(7.5*UP).shift((7.5/2)*DOWN)
        x_axis = Vector(8*RIGHT).shift(4*LEFT)
        y_axis_label = Tex("$V$").next_to(y_axis,RIGHT).shift((7/2)*UP)

        time = ValueTracker(PI/4)
        phasor_radii = 2
        # v_phasor = Vector(phasor_radii*np.cos(time.get_value())*RIGHT+phasor_radii*np.sin(time.get_value())*UP).set_color(BLUE)
        # v_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()))

        x_c_phasor = Vector(-phasor_radii*np.sin(time.get_value())*RIGHT+phasor_radii*np.cos(time.get_value())*UP).set_color(ORANGE)
        x_c_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()+PI/2))

        x_c_label = Tex(r"$X_C$").next_to(x_c_phasor.get_end(),UR).set_color(ORANGE)
        x_c_label.add_updater(lambda mobject: mobject.next_to(x_c_phasor.get_end(),UR))

        x_l_phasor = Vector(0.5*phasor_radii*np.sin(time.get_value())*RIGHT-0.5*phasor_radii*np.cos(time.get_value())*UP).set_color(PURPLE)
        x_l_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()-PI/2))

        x_l_label = Tex(r"$X_L$").next_to(x_l_phasor.get_end(),UR).set_color(ORANGE)
        x_l_label.add_updater(lambda mobject: mobject.next_to(x_l_phasor.get_end(),DL))

        r_phasor = Vector((phasor_radii/1.5)*np.cos(time.get_value())*RIGHT+(phasor_radii/1.5)*np.sin(time.get_value())*UP).set_color(RED)
        r_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()))

        r_height_line = Line().set_color(ORANGE)
        r_height_line.add_updater(lambda mobject: mobject.put_start_and_end_on(r_phasor.get_end(),r_phasor.get_end()[1]*UP))

        r_label = Tex(r"$R$").next_to(r_phasor.get_end(),UR).set_color(RED)
        r_label.add_updater(lambda mobject: mobject.next_to(r_phasor.get_end(),UR))

        z_phasor = Vector((phasor_radii/1.5)*RIGHT+phasor_radii*UP).set_color(YELLOW_A)
        z_phasor.add_updater(lambda mobject: mobject.set_angle(np.arctan2(x_c_phasor.get_y()+x_l_phasor.get_y()+r_phasor.get_y(),
                                                                                  x_c_phasor.get_x()+x_l_phasor.get_x()+r_phasor.get_x())))

        z_label = Tex(r"$Z$").next_to(z_phasor.get_end(),UR).set_color(YELLOW_A)
        z_label.add_updater(lambda mobject: mobject.next_to(z_phasor.get_end(),UR).shift(0.25*DL))

        impedance_eqn = MathTex("Z","=",r"\sqrt{","X^2","+","R^2","}").to_edge(UR).shift(DOWN)
        impedance_eqn.set_color_by_tex("Z",YELLOW_A)
        impedance_eqn.set_color_by_tex("X",ORANGE)
        impedance_eqn.set_color_by_tex("R",RED)

        impedance_eqn2 = MathTex("Z","=",r"\sqrt{","(","X_C","-","X_L",")^2","+","R^2","}").move_to(impedance_eqn)
        impedance_eqn2.scale(0.75)
        impedance_eqn2.set_color_by_tex("Z",YELLOW_A)
        impedance_eqn2.set_color_by_tex("X",ORANGE)
        impedance_eqn2.set_color_by_tex("R",RED)

        impedance_header = Text("Impedance").to_edge(UR)

        ohm_law_ac = MathTex(r"V_{\text{rms}}","=",r"I_{\text{rms}}","Z").next_to(impedance_eqn2,DOWN)
        ohm_law_ac.set_color_by_tex("V",BLUE_D)
        ohm_law_ac.set_color_by_tex("I",YELLOW_E)
        ohm_law_ac.set_color_by_tex("Z",YELLOW_A)

        
        self.play(Write(x_axis),Write(y_axis),FadeIn(y_axis_label))
        self.wait()
        self.play(Write(main_circle))
        self.play(Write(r_phasor),Write(x_c_phasor),Write(x_l_phasor),FadeIn(r_label,x_c_label,x_l_label))
        self.wait()
        self.play(time.animate.set_value(2*PI))
        self.wait()
        self.play(Write(z_phasor),FadeIn(z_label))
        self.wait()
        self.play(time.animate.set_value(4*PI))
        self.wait()
        self.play(Write(impedance_header),Write(impedance_eqn),Write(ohm_law_ac))
        self.wait()
        self.play(Transform(impedance_eqn,impedance_eqn2))
        self.wait()

class InductorEnergy(Scene):
    def construct(self):
        v1 = voltage.DCVoltage()
        v1.elements.move_to(3*LEFT)
        r1 = resistor.Resistor()
        r1.elements.move_to(4*LEFT+2*UP)
        i1 = inductor.Inductor(bounding_rect=Rectangle(width=1,height=1)) 
        i1.elements.move_to(2*LEFT+2*UP)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(r1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(r1.get_end_point())
        w2.add_point(i1.get_start_point())

        w3 = wire.Wire()
        w3.add_point(i1.get_end_point())
        w3.add_point(Point(i1.get_end_pos()+2*DOWN))
        w3.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,w1.image,r1.image,w2.image,i1.image,w3.image)
        circuit.set_color_by_gradient(RED,BLUE)
        circuit.move_to(ORIGIN)

        eqn1 = MathTex("V","-","I","R","-","L","{dI","\\over","dt}","=","0")
        eqn1.to_edge(UR).shift(2*LEFT)

        eqn2 = MathTex("I","V","-","I^2","R","-","L","I","{dI","\\over","dt}","=","0")
        eqn2.next_to(eqn1,DOWN)

        eqn3 = MathTex("P","=","{dU","\over","dt}","=","L","I","{dI","\over","dt}")
        eqn3.next_to(eqn2,DOWN)

        eqn4 = MathTex("dU","=","L","I","dI")
        eqn4.next_to(eqn3,DOWN)

        eqn5 = MathTex("U","=","\\int","dU","=","\\int","^L","_0","L","I","dI")
        eqn5.scale(0.75).next_to(eqn4,DOWN)

        eqn6 = MathTex("U","_L","=","\\frac{1}{2}","L","I^2")
        eqn6.next_to(eqn5,DOWN)

        eqns = [eqn1,eqn2,eqn3,eqn4,eqn5,eqn6]
        for eqn in eqns:
            eqn.set_color_by_tex("V",BLUE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)
            eqn.set_color_by_tex("P",PURPLE)
            eqn.set_color_by_tex("L",PURPLE_D)
            eqn.set_color_by_tex("t",LIGHT_GRAY)
            eqn.set_color_by_tex("U",YELLOW_A)

        self.play(Write(v1.image),Write(r1.image),Write(i1.image))
        self.play(Write(w1.image),Write(w2.image),Write(w3.image))
        self.play(circuit.animate.scale(1.5))
        self.play(circuit.animate.to_edge(UL))
        self.wait()
        for eqn in eqns:
            self.play(Write(eqn))
            self.wait()
        self.play(circuit.animate.scale(1/1.5))
        self.play(circuit.animate.to_edge(UL))

        graph = FunctionGraph(
            lambda t: (1-np.e**(-t)),
            x_range=[-1,4,1],
            color=GREEN
        ).next_to(circuit,DOWN).shift(DOWN+2*RIGHT)

        y_axis = Line(start=graph.get_start()+0.2*DOWN,end=graph.get_start()+3*UP)
        x_axis = Line(start =graph.get_start()+0.2*LEFT,end= graph.get_start()+5*RIGHT)

        y_label = Tex(r"$I$",color=YELLOW_E).next_to(y_axis,UP)
        x_label = Tex(r"$t$",color=LIGHT_GRAY).next_to(x_axis,RIGHT)

        q_tick = Line(start=graph.get_start()+2.75*UP+0.25*LEFT,
                      end=graph.get_start()+2.75*UP+0.25*RIGHT)
        q_tick_label = MathTex("{V","\\over","R}")
        q_tick_label.set_color_by_tex("V",BLUE)
        q_tick_label.set_color_by_tex("R",RED)
        q_tick_label.next_to(q_tick,LEFT,buff=0.2)

        self.play(Write(x_axis),Write(y_axis),Write(graph))
        self.play(Write(y_label),Write(x_label),Write(q_tick),Write(q_tick_label))
        self.wait()
