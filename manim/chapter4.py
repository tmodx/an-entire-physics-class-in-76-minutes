from manim import *
import numpy as np
import charge
import random

class MaxwellsEquations(Scene):
    def construct(self):
        gauss_header = Text("Gauss's Law").to_edge(UP)
        gauss_eqn = MathTex(r"\oint",r"\vec{E}",r"\cdot",r"d\vec{A}","=",r"{q_{\text{enc}}",r"\over",r"\epsilon_0}")
        gauss_eqn.next_to(gauss_header,DOWN)

        gauss_magnetic = Text("Gauss's Law for Magnetism").next_to(gauss_eqn,DOWN)
        gauss_mag_eqn = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}","=","0")
        gauss_mag_eqn.next_to(gauss_magnetic,DOWN)

        ampere_header = Text("Ampere's Law").next_to(gauss_mag_eqn,DOWN)
        ampere_eqn = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"I_{\text{enc}}","+",r"\mu_0",r"\epsilon_0","{d",r"\phi_E",r"\over","d","{t}}")
        ampere_eqn.next_to(ampere_header,DOWN)

        faraday_header = Text("Faraday's Law").next_to(ampere_eqn,DOWN)
        faraday_eqn = MathTex(r"\oint","(",r"\vec{E}","+",r"\vec{v}",r"\times",r"\vec{B}",")",r"\cdot",r"d\vec{l}","=","-","{d",r"\phi_B",r"\over","d","t}")
        faraday_eqn.next_to(faraday_header,DOWN)

        headers = [gauss_header,gauss_magnetic,ampere_header,faraday_header]
        eqns = [gauss_eqn,gauss_mag_eqn,ampere_eqn,faraday_eqn]
        for eqn in eqns:
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("{v}",GREEN)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("epsilon",GRAY)
            eqn.set_color_by_tex("{t}",LIGHT_GRAY)

        maxwell_header = Text("Maxwell's Equations").to_edge(UP)
        
        maxwell_eqns1 = VGroup(*[header for header in headers],
                               *[eqn for eqn in eqns])
        maxwell_eqns1.scale(0.6).next_to(maxwell_header,DOWN)

        self.play(Write(maxwell_header),run_time=1)
        self.wait()
        self.play(FadeIn(maxwell_eqns1),run_time=1)
        self.wait()

class DisplacementCurrent(Scene):
    def construct(self):
        ampere_eqn1 = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0","(",r"I_{\text{enc}}","+","I_d",")") #,"+",r"\mu_0",r"\epsilon_0","{d",r"\phi_E",r"\over","d","{t}}")
        # ampere_eqn2 = MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"I_{\text{enc}}","+",r"\mu_0",r"\epsilon_0","{d",r"\phi_E",r"\over","d","{t}}")
        ampere_eqn1.to_edge(UR)
        # ampere_eqn2.move_to(ampere_eqn1)
        d_current = MathTex("I_d","=",r"\epsilon_0","{d",r"\phi_E",r"\over","d","{t}}")
        d_current.next_to(ampere_eqn1,DOWN)

        eqns = [ampere_eqn1,d_current]
        for eqn in eqns:
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("l",RED)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("mu",GRAY)
            eqn.set_color_by_tex("epsilon",GRAY)
            eqn.set_color_by_tex("{t}",LIGHT_GRAY)

        self.play(Write(ampere_eqn1))
        self.wait()
        self.play(Write(d_current))
        self.wait()

class ACLightWave(Scene):
    def construct(self):
        pole = Line(start=3*LEFT+3*DOWN,end=3*LEFT+3*UP)
        pole.set_color(GRAY)

        c1 = charge.Charge(radius=0.5)
        c1.elements.move_to(pole.get_start())

        charge_height = ValueTracker(3)
        c1.elements.add_updater(lambda mobject: mobject.move_to(pole.get_start()+
                                                                UP*charge_height.get_value()))

        circ1 = Circle().stretch(0.2,1).set_color(BLUE).shift(3*LEFT)

        circs = []
        for i in range(10):
            new_circ = Circle().stretch(0.2,(i+1)%2).shift(3*LEFT+i*RIGHT)

            if (i%2 == 0):
                new_circ.set_color(BLUE)
            else:
                new_circ.set_color(RED)

            circs.append(new_circ)
            

        self.play(Write(pole))
        self.wait()
        self.play(FadeIn(c1.elements))
        self.wait()
        self.play(charge_height.animate.set_value(6),rate_func=rate_functions.wiggle,run_time=2)
        self.play(charge_height.animate.set_value(2))
        self.wait()

        wave_direction = Vector(13*RIGHT).set_color(WHITE).shift(6*LEFT)

        for i in range(3):
            self.play(Write(circs[i]))
            self.wait()
        
        self.play(AnimationGroup(*[Write(circs[i+3]) for i in range(len(circs)-3)],lag_ratio=0.2))
        self.wait()
        self.play(Write(wave_direction))
        self.wait()

class ThreeFieldsAndWaves(Scene):
    def construct(self):
        c1 = charge.Charge(radius=0.5)
        c1.elements.move_to(4*LEFT)

        e_arrows = []
        d_theta = PI/6
        for i in range(round(2*PI/d_theta)):
            new_arrow = Vector(RIGHT).set_angle(i*d_theta).move_to(c1.elements)
            new_arrow.set_color(RED)
            new_arrow.shift(1.2*np.cos(i*d_theta)*RIGHT+1.2*np.sin(i*d_theta)*UP)
            e_arrows.append(new_arrow)
        
        wire = Vector(4*UP,color=YELLOW_A).shift(2*DOWN)
        b_field = Circle(color=BLUE).stretch(0.2,1)

        arrow = Circle(color=YELLOW_A).shift(4*RIGHT).set_color(YELLOW_A)

        wave = ParametricFunction(lambda t: (t,np.sin(t),0),
                                  t_range=(0,4*PI))
        wave.set_color([RED,BLUE])
        wave.scale(0.5).rotate(PI/2).shift(2*LEFT)

        self.play(Write(c1.elements),*[GrowArrow(arrow) for arrow in e_arrows])
        self.wait()
        self.play(Write(wire),Write(b_field),lag_ratio=0.4)
        self.wait()
        self.play(Write(arrow),Write(wave))
        self.wait()

class SpeedOfLight(MovingCameraScene):
    def construct(self):

        # The arrays are split
        # If an array is too large, you get issues with size compression
        text_array1 = [Text("1. Gauss's Law"),
                      MathTex(r"\oint",r"\vec{E}",r"\cdot",r"d\vec{A}","=",r"{q_{\text{enc}}",r"\over",r"\epsilon_0}"),
                      Text("2. Gauss's Law for Magnetism"),
                      MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}","=","0"),
                      Text("3. Ampere's Law"),
                      MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"I_{\text{enc}}","+",r"\mu_0",r"\epsilon_0","{d",r"\phi_E",r"\over","d","t}"),
                      Text("4. Faraday's Law"),
                      MathTex(r"\oint","(",r"\vec{E}","+",r"\vec{v}",r"\times",r"\vec{B}",")",r"\cdot",r"d\vec{l}","=","-","{d",r"\phi_B",r"\over","d","t}"),

                      Text("Assume Free Space (No Charges or Currents)").scale(0.75),
                      MathTex("1. ",r"\oint",r"\vec{E}",r"\cdot",r"d\vec{A}","=","0"),
                      MathTex("2. ",r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}","=","0"),
                      MathTex("3. ","\oint",r"\vec{B}",r"\cdot",r"d\vec{l}","=",r"\mu_0",r"\epsilon_0","{d",r"\phi_E",r"\over","d","t}"),
                      MathTex("4. ",r"\oint","(",r"\vec{E}",")",r"\cdot",r"d\vec{l}","=","-","{d",r"\phi_B",r"\over","d","t}"),
                      
                      Text("Transform with Stokes' Theorem"),
                      MathTex(r"\int_C", r"\vec{F}", r"\cdot", r"d\vec{l}", "=", r"\iint_A", "(", r"\nabla", r"\times", r"\vec{F}", ")", r"\cdot", r"d\vec{A}"),
                      Text("and the Divergence Theorem"),
                      MathTex(r"\iint_A", r"\vec{F}", r"\cdot", r"d\vec{A}", "=", r"\iiint_V", "(", r"\nabla", r"\cdot", r"\vec{F}", ")", r"\cdot", "d{V}"),\
                      Text("(note each integral is closed across the entire curve/surface/volume)").scale(0.5),
                      
                      Text("1. "),
                      MathTex(r"\oint",r"\vec{E}",r"\cdot",r"d\vec{A}","=","0"),
                      MathTex(r"\iiint_V", r"\nabla", r"\cdot", r"\vec{E}", r"\,", "dV", "=", "0"),
                      MathTex(r"\nabla", r"\cdot", r"\vec{E}", "=", "0"),
                      Text("2. "),
                      MathTex(r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}","=","0"),
                      MathTex(r"\iiint_V", r"\nabla", r"\cdot", r"\vec{B}", r"\,", "dV", "=", "0"),
                      MathTex(r"\nabla", r"\cdot", r"\vec{B}", "=", "0"),
                      Text("3. "),
                      MathTex(r"\oint", r"\vec{B}", r"\cdot", r"d\vec{l}", "=", r"\mu_0", r"\epsilon_0", "{d", r"\phi_E", r"\over", "dt}"),
                      MathTex(r"\iint_A", "(", r"\nabla", r"\times", r"\vec{B}", ")", r"\cdot", r"d\vec{A}", "=", r"\mu_0", r"\epsilon_0", "{d", r"\over", "dt}", r"\int", r"\vec{E}", r"\cdot", r"d\vec{A}"),
                      MathTex(r"\iint_A", "(", r"\nabla", r"\times", r"\vec{B})", r"\cdot", r"d\vec{A}", "=", r"\int", "(", r"\mu_0", r"\epsilon_0", "{d", r"\over", "dt}", r"\vec{E}", ")", r"\cdot", r"d\vec{A}"),
                      MathTex(r"\nabla", r"\times", r"\vec{B}", "=", r"\mu_0", r"\epsilon_0", "{d", r"\vec{E}", r"\over", "dt}"),
                      MathTex(r"\nabla", r"\times", r"\vec{B}", "=", r"\mu_0", r"\epsilon_0", "{d", r"\vec{E}", r"\over", "dt}"),
                      Text("4. "),
                      MathTex(r"\oint", r"\vec{E}", r"\cdot", r"d\vec{l}", "=", "-{d", r"\phi_B", r"\over", "dt}"),
                      MathTex(r"\iint_A", "(", r"\nabla", r"\times", r"\vec{E}", ")", r"\cdot", r"d\vec{A}", "=", "-{d", r"\over", "dt}", r"\int", r"\vec{B}", r"\cdot", r"d\vec{A}"),
                      MathTex(r"\iint_A", "(", r"\nabla", r"\times", r"\vec{E}", ")", r"\cdot", r"d\vec{A}", "=", r"\int", "-{d", r"\vec{B}", r"\over", "dt}", r"\cdot", r"d\vec{A}"),
                      MathTex(r"\nabla", r"\times", r"\vec{E}", "=", "-{d", r"\vec{B}", r"\over", "dt}")]

        text_array2 = [Text("Maxwell's Equations in Differential Form"),
                       Text("1. Gauss's Law"),
                       MathTex(r"\nabla", r"\cdot", r"\vec{E}", "=", "0"),
                       Text("2. Gauss's Law for Magnetism"),
                       MathTex(r"\nabla", r"\cdot", r"\vec{B}", "=", "0"),
                       Text("3. Ampere's Law"),
                       MathTex(r"\nabla", r"\times", r"\vec{B}", "=", r"\mu_0", r"\epsilon_0", "{d", r"\vec{E}", r"\over", "dt}"),
                       Text("4. Faraday's Law"),
                       MathTex(r"\nabla", r"\times", r"\vec{E}", "=", "-{d", r"\vec{B}", r"\over", "dt}"),
                      
                       Text("Take the curl of Faraday's Law:"),
                       MathTex(r"\nabla", r"\times", "(", r"\nabla", r"\times", r"\vec{E}", ")", "=", r"\nabla", r"\times", r"\left(", "-{d", r"\vec{B}", r"\over", "dt}", r"\right)"),
                       MathTex(r"\nabla", r"\times", "(", r"\nabla", r"\times", r"\vec{E}", ")", "=", "-{d", r"\over", "dt}", "(", r"\nabla", r"\times", r"\vec{B}", ")"),
                       Text("Substitute in Ampere's Law:"),
                       MathTex(r"\nabla", r"\times", "(", r"\nabla", r"\times", r"\vec{E}", ")", "=", "-{d", r"\over", "dt}", r"\left(", r"\mu_0", r"\epsilon_0", "{d", r"\vec{E}", r"\over", "dt}", r"\right)"),
                       Text("Use the curl of curl identity:"),
                       MathTex(r"\nabla", r"\times", "(", r"\nabla", r"\times", r"\vec{F}", ")", "=", r"\nabla", "(", r"\nabla", r"\cdot", r"\vec{F}", ")", "-", r"\nabla^2", r"\vec{F}", ")"),
                       MathTex(r"\nabla", r"\cdot", "(", r"\nabla", r"\cdot", r"\vec{E}", ")" "-", r"\nabla^2", r"\vec{E}", "=", "-{d", r"\over", "dt}", r"\left(", r"\mu_0", r"\epsilon_0", "{d", r"\vec{E}", r"\over", "dt}", r"\right)"),
                       Text("The first term goes away because of Gauss's Law:"),
                       MathTex("-", r"\nabla^2", r"\vec{E}", "=", r"-\mu_0", r"\epsilon_0", "{d^2", r"\vec{E}", r"\over", "dt^2}"),
                       Text("Assume E only goes in the x-direction:"),
                       MathTex("-", r"{\partial^2", r"\vec{E}", r"\over", r"\partial", "x^2}", "=", r"-\mu_0", r"\epsilon_0", "{d^2", r"\vec{E}", r"\over", "dt^2}"),
                       MathTex(r"{\partial^2", r"\vec{E}", r"\over", r"\partial", "x^2}", "=", r"\mu_0", r"\epsilon_0", "{d^2", r"\vec{E}", r"\over", "dt^2}")]

        for lst in [text_array1,text_array2]:
            for eqn in lst:
                if not isinstance(eqn,MathTex):
                    continue

                eqn.set_color_by_tex("A", GREEN)
                eqn.set_color_by_tex("B", BLUE)
                eqn.set_color_by_tex("dA", GREEN)
                eqn.set_color_by_tex("E", RED)
                eqn.set_color_by_tex("F", RED)
                eqn.set_color_by_tex("l", RED)
                eqn.set_color_by_tex("t", LIGHT_GRAY)
                eqn.set_color_by_tex("{v}", BLUE)
                eqn.set_color_by_tex("{V}", BLUE)
                eqn.set_color_by_tex(r"\epsilon_0", GRAY)
                eqn.set_color_by_tex(r"\mu_0", GRAY)
                eqn.set_color_by_tex(r"\phi", GREEN)
                eqn.set_color_by_tex(r"q_{\text{enc}}", GREEN)
                eqn.set_color_by_tex(r"I_{\text{enc}}", YELLOW)

        text_mobjects = VGroup(*text_array1,*text_array2).scale(0.75).arrange(DOWN,buff=0.2).to_edge(UP).shift(8*DOWN)
        
        self.play(AnimationGroup(FadeIn(text_mobjects),self.camera.frame.animate.move_to(text_mobjects.get_bottom()),lag_ratio=0.2,run_time=5),rate_func=rate_functions.smooth)
        self.wait(0.5)
        self.play(FadeOut(*text_array1,*text_array2[0:-1]),text_array2[-1].animate.scale(2))
        self.wait()

class WaveForm(Scene):
    def construct(self):
        c = 1.0 
        amplitude = 1.0

        def wave_func(x, t):
            return amplitude * np.sin(x - c * t)

        time = ValueTracker(0)

        wave_graph = always_redraw(lambda: FunctionGraph(lambda x: wave_func(x,time.get_value()),
                                                         x_range=[-5,5]))

        start_line = Line(start=5*LEFT,end=5*RIGHT,color=YELLOW)
        endpoints = VGroup(Dot(color=YELLOW).move_to(start_line.get_start()),
                           Dot(color=YELLOW).move_to(start_line.get_end()))
        
        line_copy = start_line.copy()

        wave_start_dot = Dot(color=YELLOW).move_to(line_copy.get_start())
        follow_line_start = wave_start_dot.add_updater(lambda mobject: mobject.move_to(line_copy.get_start()))

        wave_end_dot = Dot(color=YELLOW).move_to(line_copy.get_end())
        follow_line_end = wave_end_dot.add_updater(lambda mobject: mobject.move_to(line_copy.get_end()))

        wave_start_line = Line(start=start_line.get_start(), end=wave_start_dot.get_center()+0.01*RIGHT)
        wave_start_line.add_updater(lambda mobject: mobject.put_start_and_end_on(start_line.get_start(),wave_start_dot.get_center()+0.01*RIGHT))

        wave_end_line = Line(start=start_line.get_end(), end=wave_end_dot.get_center()+0.01*RIGHT)
        wave_end_line.add_updater(lambda mobject: mobject.put_start_and_end_on(start_line.get_end(),wave_end_dot.get_center()+0.01*RIGHT))

        self.play(Write(start_line),Write(endpoints))

        self.add(wave_start_dot,wave_end_dot,wave_start_line,wave_end_line)
        self.play(start_line.animate.set_opacity(0.5),Transform(line_copy,wave_graph))
        self.add(wave_graph)
        self.remove(line_copy)

        wave_start_dot.remove_updater(follow_line_start)
        wave_end_dot.remove_updater(follow_line_end)

        wave_start_dot.add_updater(lambda mobject: mobject.move_to(wave_graph.get_start()))
        wave_end_dot.add_updater(lambda mobject: mobject.move_to(wave_graph.get_end()))

        self.wait()
        self.play(time.animate.set_value(13),run_time=5)
        self.wait()

class WaveEquation(Scene):
    def construct(self):
        equation = MathTex(r"\frac{\partial^2 u}{dt^2} = c^2 \frac{\partial^2 u}{\partial x^2}").shift(UP)
        equation2 = MathTex("c","=","{1",r"\over",r"\sqrt{",r"\mu_0",r"\epsilon_0}}","=","3",r"\times","10^8",r"\frac{m}{s}").shift(3*DOWN)
        equation2.set_color_by_tex("mu",GRAY)
        equation2.set_color_by_tex("epsilon",GRAY)
        self.play(FadeIn(equation))
        self.wait(2)
        self.play(FadeIn(equation2))
        self.wait(2)

class WaveEquationSolution(Scene):
    def construct(self):
        wave_solution = MathTex("E","(","t",")","=","E_0","sin(","k","x","-",r"\omega","t","+",r"\Delta",")")
        wave_number = MathTex("k","=","{2",r"\pi",r"\over",r"\lambda}").next_to(wave_solution,DOWN)
        frequency = MathTex("f","=",r"\frac{\text{cycles}}{\text{second}}").to_edge(UP).shift(2.5*DOWN)
        angular_frequency = MathTex(r"\omega","=","2",r"\pi","f").to_edge(UP).shift(4*DOWN)
        speed = MathTex("c","=",r"\lambda","f").to_edge(UP).shift(5*DOWN)

        eqns = [wave_solution,wave_number,frequency,angular_frequency,speed]
        for eqn in eqns:
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("t",LIGHT_GRAY)
            eqn.set_color_by_tex("f",PURPLE)
            eqn.set_color_by_tex("k",GRAY)
            eqn.set_color_by_tex("omega",GREEN)
            eqn.set_color_by_tex("Delta",BLUE)
            eqn.set_color_by_tex("lambda",ORANGE)

        self.play(Write(wave_solution))
        self.wait(2)
        self.play(Write(wave_number))
        self.wait()
        self.play(wave_solution.animate.to_edge(UP),
                  wave_number.animate.to_edge(UP).shift(DOWN))
        self.wait(2)
        self.play(Write(frequency))
        self.wait()
        self.play(Write(angular_frequency))
        self.wait()
        self.play(Write(speed))
        self.wait()
        self.play(FadeOut(wave_solution,wave_number,frequency,angular_frequency,speed))

class Intensity(Scene):
    def construct(self):
        header = Text("Intensity")

        self.play(FadeIn(header),run_time=2)
        self.play(header.animate.to_edge(UP))
        self.wait()

        equation1 = MathTex("I","=","{P",r"\over","A}").next_to(header,DOWN)
        equation2 = MathTex("I","=","{U",r"\over","t","A}").next_to(equation1,DOWN)

        equation3 = MathTex("I","=",r"|\vec{S}|","=","|",r"{\vec{E}",r"\times",r"\vec{B}",r"\over",r"\mu_0}","|")
        equation3.next_to(equation2,DOWN)

        equation4 = MathTex("=",r"\frac{1}{2}","c",r"\epsilon_0","E_0^2")
        equation4.next_to(equation3,DOWN)

        eqns = [equation1,equation2,equation3,equation4]
        for eqn in eqns:
            eqn.set_color_by_tex("I",ORANGE)
            eqn.set_color_by_tex("P",PURPLE)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("U",YELLOW)
            eqn.set_color_by_tex("t",GRAY)
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("mu",LIGHT_GRAY)
            eqn.set_color_by_tex("epsilon",LIGHT_GRAY)

        self.play(Write(equation1))
        self.wait()
        self.play(Write(equation2))
        self.wait()
        self.play(Write(equation3))
        self.wait()
        self.play(Write(equation4))
        self.wait()

class AntennaTransmitter(Scene):
    def construct(self):
        cell_tower = SVGMobject("svg/cell-tower.svg").scale(2)

        power_p = Tex("Power: ","${P}$").scale(0.75)
        frequency_f = Tex("Frequency: ","$f$").scale(0.75)
        distance_d = Tex("Distance: ","$d$").scale(0.75)
        length_l = Tex("Length: ","$l$").scale(0.75)


        eqns1 = [power_p,frequency_f,distance_d,length_l]
        for eqn in eqns1:
            eqn.set_color_by_tex("{P}",PURPLE)
            eqn.set_color_by_tex("f",PURPLE)
            eqn.set_color_by_tex("d",RED)
            eqn.set_color_by_tex("l",RED)

        eqns_mobject = VGroup(*eqns1).arrange_submobjects(DOWN).to_corner(UL)

        self.play(Write(cell_tower))
        self.wait()
        for eqn in eqns1:
            self.play(Write(eqn))
            self.wait()
        self.play(cell_tower.animate.scale(0.5))
        self.play(cell_tower.animate.next_to(eqns_mobject,RIGHT))
        self.wait()

        intensity_1 = MathTex("I","=","{P",r"\over","A}").next_to(cell_tower,RIGHT)
        intensity_2 = MathTex("I","=","{P",r"\over","A}","=","{P",r"\over","4",r"\pi","d^2}").next_to(cell_tower,RIGHT)
        intensity_3 = MathTex("I","=","{P",r"\over","A}","=","{P",r"\over","4",r"\pi","d^2}","=",r"\frac{1}{2}",r"\epsilon_0","{c}","E_0^2").next_to(cell_tower,RIGHT)

        e_0_solved = MathTex(r"\displaystyle","E_0","=",r"\sqrt{","{P",r"\over","2",r"\pi","d^2",r"\epsilon_0","{c}}}").next_to(cell_tower,RIGHT).shift(1.5*DOWN)

        voltage_def = MathTex("|V|","=",r"\int",r"\vec{E}",r"\cdot",r"d\vec{l}").next_to(e_0_solved,DOWN)
        v_max = MathTex(r"|V_{\text{max}}|","=","E_0","{l}").next_to(voltage_def,DOWN)
        v_max2 = MathTex(r"|V|_{\text{max}}","=","E_0","{l}","=","{l}",r"\displaystyle",r"\sqrt{","{P",r"\over","2",r"\pi","d^2",r"\epsilon_0","{c}}}").move_to(v_max)

        eqns2 = [intensity_1,intensity_2,intensity_3,e_0_solved,voltage_def,v_max,v_max2]
        for eqn in eqns2:
            eqn.set_color_by_tex("I",ORANGE)
            eqn.set_color_by_tex("P",PURPLE)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("d",RED)
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("epsilon",LIGHT_GRAY)
            eqn.set_color_by_tex("{c}",GREEN_C)
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("{l}",RED)

        self.play(Write(intensity_1))
        self.wait()
        self.play(Transform(intensity_1,intensity_2))
        self.wait()
        self.play(Transform(intensity_1,intensity_3))
        self.wait()
        self.play(Write(e_0_solved))
        self.wait()
        self.play(Write(voltage_def))
        self.wait()
        self.play(Write(v_max))
        self.wait()
        self.play(Transform(v_max,v_max2))
        self.wait()
        self.play(FadeOut(intensity_1,e_0_solved,voltage_def,v_max))
        self.wait()

        radius_r = Tex("Radius: ","$r$").scale(0.75).next_to(length_l,DOWN)
        radius_r.set_color_by_tex("$r$",RED)

        self.play(Write(radius_r))
        self.wait()

        e_b_planewave = MathTex("{E_0",r"\over","B_0}","=","{c}").scale(0.75).to_edge(UP)
        b_wave_eqn = MathTex("B","(t)","=","B_0","sin(","k","x","-",r"\omega","t","+",r"\Delta",")").next_to(e_b_planewave,DOWN).shift(RIGHT)
        b_wave_eqn2 = MathTex("B","(t)","=","{E_0",r"\over","c}","sin(","k","x","-",r"\omega","t","+",r"\Delta",")").next_to(e_b_planewave,DOWN).shift(RIGHT)
        faraday_voltage = MathTex("|V|","=","{d",r"\phi_B",r"\over","d","t}","=","{d",r"\over","d","t}",r"\oint",r"\vec{B}",r"\cdot",r"d\vec{A}").next_to(b_wave_eqn2,DOWN)
        max_voltage = MathTex(r"|V|_{\text{max}}","=","{d",r"\over","d","t}","[","B","(t)",r"\pi","{r}^2",r"]_{\text{max}}").next_to(faraday_voltage,DOWN)
        max2 = MathTex("=","{E_0",r"\over","c}",r"\omega","cos","(","k","x","-",r"\omega","t","+",r"{\Delta",")",r"\pi","{r}^2",r"_\text{max}").next_to(max_voltage,DOWN)
        max3 = MathTex("=","{E_0",r"\over","c}","2",r"\pi","f",r"\pi","{r}^2").next_to(max2,DOWN)

        eqns3 = [e_b_planewave,b_wave_eqn,b_wave_eqn2,faraday_voltage,max_voltage,max2,max3]
        for eqn in eqns3:
            eqn.set_color_by_tex("E",RED)
            eqn.set_color_by_tex("B",BLUE)
            eqn.set_color_by_tex("omega",GREEN)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("Delta",BLUE)
            eqn.set_color_by_tex("{c}",GREEN)
            eqn.set_color_by_tex("{r}",GREEN)
            eqn.set_color_by_tex("pi",GRAY)
        
        self.play(Write(e_b_planewave))
        self.wait()
        self.play(Write(b_wave_eqn))
        self.wait()
        self.play(Transform(b_wave_eqn,b_wave_eqn2))
        self.wait()
        self.play(Write(faraday_voltage))
        self.wait()
        self.play(Write(max_voltage))
        self.wait()
        self.play(Write(max2))
        self.wait()
        self.play(Write(max3))
        self.wait()

class WaveMomentum(Scene):
    def construct(self):
        momentum_equation = MathTex(r"{U}_{\text{per\_volume}}", "=", r"{p}_{\text{per\_volume}}", "{c}")
        p_mv = MathTex("{p}","=","{m}","{v}")
        n2l = MathTex("{F}","=","{m}","{a}")
        n2l2 = MathTex("{F}","=","{m}","{a}","=","{d","{p}",r"\over","d","{t}}")
        p_accumulate = MathTex("{p}","=",r"\int","{F}","dt")
        u_int = MathTex("|{U}|","=",r"\int",r"\vec{F}",r"\cdot",r"d\vec{s}",r"\Rightarrow",r"\int","{F}","d{s}")
        u_int2 = MathTex("=",r"\int","{F}","{d{s}",r"\over","dt}","dt")
        u_int3 = MathTex("=",r"\int","{F}","{v}","dt")
        u_int4 = MathTex("=","{v}",r"\int","{F}","dt")
        u_int5 = MathTex("{U}","=","{v}","{p}")

        derivation_mobjects = VGroup(p_mv,n2l,n2l2,p_accumulate,u_int,u_int2,u_int3,u_int4,u_int5).arrange_submobjects(DOWN).to_edge(UP)

        momentum_eqn2 = MathTex(r"\epsilon_0","{E}_0^2","=",r"{p}_{\text{per\_volume}}","{c}")
        momentum_eqn3 = MathTex(r"{\epsilon_0","{E}_0^2",r"\over","{c}}","=",r"{p}_{\text{per\_volume}}")
        momentum_eqn3_v2 = MathTex(r"{\epsilon_0","{E}_0^2",r"\over","{c}}","=",r"{p}_{\text{per\_volume}}","=","{d{p}",r"\over","d{V}}")
        momentum_eqn4 = MathTex("{d{p}",r"\over","d{V}}",r"\cdot","{d{V}",r"\over","dt}","=",r"{\epsilon_0","{E}_0^2","{A}","{c}",r"\over","{c}}")
        momentum_eqn4_v2 = MathTex("{d{p}",r"\over","d{V}}",r"\cdot","{d{V}",r"\over","dt}","=",r"{\epsilon_0","{E}_0^2","{A}","{c}",r"\over","{c}}","=","{d{p}",r"\over","dt}","=","F")
        momentum_eqn5 = MathTex("{P}","=",r"\epsilon_0","{E}_0^2")

        volume1 = MathTex("{V}","=","{A}","{c}","dt").to_corner(UR).shift(LEFT)
        volume2 = MathTex("{d{V}",r"\over","dt}","=","{A}","{c}").next_to(volume1,DOWN)

        pressure_eqns = VGroup(momentum_eqn2,momentum_eqn3,momentum_eqn3_v2,momentum_eqn4,momentum_eqn4_v2,momentum_eqn5)
        pressure_eqns.scale(0.75).arrange(DOWN).next_to(momentum_equation.copy().to_corner(UL).shift(RIGHT),DOWN)

        cube_polygons = [
            # top face
            [
                [0,0.5,0],
                [-1,1,0],
                [0,1.5,0],
                [1,1,0]
            ],
            # left face
            [
                [0,0.5,0],
                [0,-0.75,0],
                [-1,-0.25,0],
                [-1,1,0]
            ],
            # right face
            [
                [0,0.5,0],
                [1,1,0],
                [1,-0.25,0],
                [0,-0.75,0]
            ]
        ]
        cube = VGroup(*[Polygon(*polygon,color=WHITE) for polygon in cube_polygons])
        cube.next_to(volume2,DOWN)

        eqns = [momentum_equation,p_mv,n2l,n2l2,p_accumulate,u_int,u_int2,
                u_int3,u_int4,u_int5,momentum_eqn2,momentum_eqn3,momentum_eqn3_v2,momentum_eqn4,momentum_eqn4_v2,
                momentum_eqn5,volume1,volume2]

        for eqn in eqns:
            eqn.set_color_by_tex("{U}",YELLOW_A)
            eqn.set_color_by_tex("{p}",TEAL)
            eqn.set_color_by_tex("{c}",GREEN)
            eqn.set_color_by_tex("{m}",RED)
            eqn.set_color_by_tex("{v}",GREEN)
            eqn.set_color_by_tex("{V}",BLUE)
            eqn.set_color_by_tex("{A}",GREEN_A)
            eqn.set_color_by_tex("{F}",RED)
            eqn.set_color_by_tex("{a}",BLUE)
            eqn.set_color_by_tex("{s}",RED)
            eqn.set_color_by_tex("{E}",RED)
            eqn.set_color_by_tex("epsilon",GRAY)

        self.play(Write(momentum_equation))
        self.wait()
        self.play(momentum_equation.animate.scale(1.5))
        self.wait()
        self.play(FadeOut(momentum_equation))
        self.wait()
        self.wait()
        
        for i in range(6):
            self.play(Write(derivation_mobjects[i]))
            self.wait()
        
        self.play(derivation_mobjects[0:6].animate.shift(5.5*UP))
        derivation_mobjects[6:].shift(5.5*UP)
        self.wait()

        for i in range(len(derivation_mobjects)-6):
            self.play(Write(derivation_mobjects[i+6]))
            self.wait()

        self.play(FadeOut(derivation_mobjects),FadeIn(momentum_equation))
        self.wait()
        self.play(momentum_equation.animate.scale(0.5))
        self.play(momentum_equation.animate.to_corner(UL).shift(RIGHT))
        self.wait()

        for i in range(3):
            self.play(Write(pressure_eqns[i]))
            self.wait()
        
        self.play(Write(volume1))
        self.play(Write(cube))
        self.play(cube[2].animate.set_fill(GREEN,opacity=0.5))
        self.wait()
        self.play(Write(volume2))
        self.wait()

        for i in range(len(pressure_eqns)-3):
            self.play(Write(pressure_eqns[i+3]))
            self.wait()

# BONK
# A single particle very quickly bouncing around the screen
class Bonk(MovingCameraScene):
    def construct(self):
        screen_top = self.camera.frame.get_top()[1]
        screen_bottom = self.camera.frame.get_bottom()[1]
        screen_left = self.camera.frame.get_left()[0]
        screen_right = self.camera.frame.get_right()[0]

        light = Dot(color=WHITE).move_to(
            screen_right * random.random() * RIGHT + screen_top * random.random() * UP
        )
        speed = 300
        angle = random.random() * 2 * PI
        light_velocity = speed * np.cos(angle) * RIGHT + speed * np.sin(angle) * UP

        run_time = 3
        delta_t = 0.01
        epsilon = 0.000001

        for i in range(round(run_time / delta_t)):
            self.play(light.animate.shift(light_velocity*delta_t),run_time=delta_t/2)
            self.play(Write(Line(start=light.get_center() - light_velocity*delta_t,end=light.get_center(),color=WHITE)),run_time=delta_t/2)

            # Collision detection and handling
            if light.get_x() > screen_right:
                # self.play(light.animate.shift(-light_velocity*delta_t),run_time=epsilon)
                light_velocity = -light_velocity[0]*RIGHT + light_velocity[1]*UP
            if light.get_x() < screen_left:
                # self.play(light.animate.shift(-light_velocity*delta_t),run_time=epsilon)
                light_velocity = -light_velocity[0]*RIGHT + light_velocity[1]*UP
            if light.get_y() > screen_top:
                # self.play(light.animate.shift(-light_velocity*delta_t),run_time=epsilon)
                light_velocity = light_velocity[0]*RIGHT -light_velocity[1]*UP
            if light.get_y() < screen_bottom:
                # self.play(light.animate.shift(-light_velocity*delta_t),run_time=epsilon)
                light_velocity = light_velocity[0]*RIGHT -light_velocity[1]*UP
            

        self.wait()



class Reflect(Scene):
    def construct(self):
        interface_material = Rectangle(width=16,height=4,color=WHITE).shift(4*UP).set_fill(color=color_gradient([BLUE,BLACK],2),opacity=0.4)
        perp_line = DashedLine(start=2*UP,end=4*DOWN,color=WHITE)
        incident_vector = Vector(4*UR,color=RED).shift(2.2*DL+2*LEFT)
        outgoing_vector = Vector(4*DR,color=BLUE).shift(1.8*UL+2*RIGHT)

        theta_i_arc = Arc(radius=1,start_angle=5*PI/4, angle= PI/4+0.2).move_arc_center_to(incident_vector.get_end())
        theta_o_arc = Arc(radius=1.5,start_angle = 3*PI/2 - 0.1,angle=PI/4+0.1).move_arc_center_to(outgoing_vector.get_start())

        theta_i_label = Tex(r"$\theta_i$").next_to(theta_i_arc,DOWN).shift(0.5*LEFT)
        theta_o_label = Tex(r"$\theta_o$").next_to(theta_o_arc,DOWN).shift(0.5*RIGHT)


        self.play(AnimationGroup(Write(interface_material),Write(perp_line),lag_ratio=0.2,run_time=1))
        self.play(AnimationGroup(Write(incident_vector),Write(outgoing_vector),lag_ratio=0.2),run_time=1)
        self.wait()
        self.play(AnimationGroup(Write(theta_i_arc),Write(theta_o_arc),
                                 Write(theta_i_label),Write(theta_o_label)))
        self.wait()

class Scatter(Scene):
    def construct(self):
        scatter_light = SVGMobject("svg/scatter-light.svg").scale(3).shift(4*UP)
        self.play(Write(scatter_light))

        incoming_vecs = VGroup(*[Vector(2*RIGHT+3*UP,color=RED).shift((i+1)*LEFT+3*DOWN) for i in range(5)])
        outgoing_vecs = VGroup(*[Vector(3*RIGHT,color=BLUE).set_angle(PI+random.random()*PI).shift((i-1)*LEFT+UP) for i in range(5)])

        self.play(AnimationGroup(Write(incoming_vecs),Write(outgoing_vecs),lag_ratio=0.2))
        self.wait()

class Corner(Scene):
    def construct(self):
        corner = VGroup(Line(start=2*LEFT,end=ORIGIN),
                        Line(start=ORIGIN,end=2*UP),
                        Line(start=0.25*LEFT,end=0.25*UL),
                        Line(start=0.25*UL,end=0.25*UP),
                        DashedLine(start=UP+0.75*RIGHT,end=UP+0.75*LEFT),
                        DashedLine(start=LEFT+0.75*DOWN,end=LEFT+0.75*UP)).rotate(PI/4).scale(2).shift(3*RIGHT+DOWN)
        
        incoming_vec = Vector().put_start_and_end_on(4*LEFT+2*UP,corner[1].get_center())
        middle_vec = Vector().put_start_and_end_on(incoming_vec.get_end(),corner[0].get_center())
        outgoing_vec = Vector().put_start_and_end_on(corner[0].get_center(),incoming_vec.get_start()+middle_vec.height*DOWN)

        vecs = VGroup(incoming_vec,middle_vec,outgoing_vec).set_color_by_gradient(RED,BLUE)

        self.play(Write(corner[0:4]))
        self.play(AnimationGroup(Write(incoming_vec),Write(corner[4]),lag_ratio=0.4),run_time=1)
        self.play(AnimationGroup(Write(middle_vec),Write(corner[5]),lag_ratio=0.4),run_time=1)
        self.play(Write(outgoing_vec))
        self.wait()

class Refract(Scene):
    def construct(self):
        interface_material = Rectangle(width=16,height=4,color=WHITE).shift(3*UP).set_fill(color=color_gradient([BLUE,BLACK],2),opacity=0.4)
        perp_line = DashedLine(start=4*UP,end=4*DOWN,color=WHITE)
        incident_vector = Vector(4*UR,color=RED).shift(2.2*DL+2*LEFT+DOWN)
        outgoing_vector = Vector(5*RIGHT+2*UP,color=BLUE).shift(1.2*UP+0.2*RIGHT)

        theta_i_arc = Arc(radius=1,start_angle=5*PI/4, angle= PI/4+0.2).move_arc_center_to(incident_vector.get_end())
        theta_o_arc = Arc(radius=1,start_angle=np.arctan2(2,5),angle=PI/2-np.arctan2(2,5)+0.2).move_arc_center_to(outgoing_vector.get_start())
        theta_i_label = Tex(r"$\theta_i$").next_to(theta_i_arc,DOWN).shift(0.5*LEFT).set_color(GRAY)
        theta_o_label = Tex(r"$\theta_o$").next_to(theta_o_arc,UP).shift(0.5*RIGHT).set_color(GRAY)

        n1 = Tex("$n_1$",color=BLUE).to_edge(LEFT).shift(0.5*UP)
        n2 = Tex("$n_2$",color=BLUE).to_edge(LEFT).shift(1.5*UP)

        snells_law = MathTex("n_1","sin(",r"\theta_i",")","=","n_2","sin(",r"\theta_o",")")
        snells_law.to_corner(UL)

        snell_header = Text("Snell's Law").to_edge(UR)

        snells_law.set_color_by_tex("n_",BLUE)
        snells_law.set_color_by_tex("theta",GRAY)

        self.play(AnimationGroup(Write(interface_material),Write(perp_line),lag_ratio=0.2))
        self.play(AnimationGroup(Write(incident_vector),Write(outgoing_vector),lag_ratio=0.5))
        self.play(Write(theta_i_arc),Write(theta_o_arc))
        self.play(Write(theta_i_label),Write(theta_o_label))
        self.wait()
        self.play(Write(n1),Write(n2))
        self.wait()
        self.play(Write(snells_law))
        self.wait()
        self.play(FadeIn(snell_header))
        self.play(snell_header.animate.shift(0.33*UR))
        self.wait()

class TotalInternalRefraction(Scene):
    def construct(self):
        interface_material = Rectangle(width=16,height=4,color=WHITE).shift(3*UP).set_fill(color=color_gradient([BLUE,BLACK],2),opacity=0.4)
        perp_line = DashedLine(start=4*UP,end=4*DOWN,color=WHITE)
        incident_vector = Vector(4*UR,color=RED).shift(2.2*DL+2*LEFT+DOWN)
        outgoing_vector = Vector(5*RIGHT+2*UP,color=BLUE).shift(1.2*UP+0.2*RIGHT)


        self.play(Write(interface_material),Write(perp_line))
        self.play(Write(incident_vector),Write(outgoing_vector))
        self.wait()
        self.play(incident_vector.animate.rotate(-PI/6-0.2,OUT,UP),
                  outgoing_vector.animate.rotate(-PI/6-0.2,OUT,UP),run_time=3)
        self.wait()

class IndexOfRefraction(Scene):
    def construct(self):
        equation = MathTex(r"\mu_0",",",r"\epsilon_0").scale(1.5)
        equation2 = MathTex("n","=","{c",r"\over","v}").scale(1.5).next_to(equation,DOWN)
        self.play(Write(equation))
        self.wait()
        self.play(Write(equation2))
        self.wait(2)

class UnderwaterExample(Scene):
    def construct(self):
        sine_wave = FunctionGraph(lambda x: 0.2*np.sin(x)+1,x_range=[-7,7],color=BLUE)

        surface_icon = SVGMobject("svg/water-surface.svg").scale(0.5).set_color(BLUE)
        surface_icon.shift(5*RIGHT+1.1*UP)

        water_IOR = Tex("$n=1.33$",color=BLUE_D).to_edge(LEFT,buff=0.2).shift(0.5*UP)
        air_IOR = Tex("$n=1$",color=BLUE_D).to_edge(LEFT,buff=0.2).shift(1.5*UP)

        central_line = DashedLine(start=3*UP,end=2*DOWN)
        incident_vector = Vector(3.8*UR,color=BLUE).shift(4*LEFT+3*DOWN)
        outgoing_vector = Vector(3.8*DR,color=RED).shift(UP+0.2*DR)

        theta_i_arc = Arc(radius=1,start_angle=PI+PI/4,angle=PI/4+0.2).move_arc_center_to(incident_vector.get_end())
        theta_o_arc = Arc(radius=1.2,start_angle=3*PI/2-0.2,angle=PI/4+0.2).move_arc_center_to(outgoing_vector.get_start())

        theta_i_label = Tex(r"$\theta_i$").next_to(theta_i_arc,DOWN).shift(0.2*LEFT)
        theta_o_label = Tex(r"$\theta_o$").next_to(theta_o_arc,DOWN).shift(0.2*RIGHT)

        snells_law = MathTex(r"\displaystyle","1.33","sin(",r"\theta_i",")","=","1",r"\cdot","sin(",r"\theta_o",")")
        snells_law.to_corner(UL)
        snells_law2 = MathTex(r"\displaystyle","1.33","sin(",r"\theta_i",")","=","1",r"\cdot","sin(","90",")").move_to(snells_law)
        snells_law3 = MathTex(r"\displaystyle","1.33",r"\cdot","sin(",r"\theta_i",")","=","1").move_to(snells_law2)
        snells_law4 = MathTex(r"\displaystyle","sin(",r"\theta_i",")","=",r"\frac{1}{1.33}").move_to(snells_law2)
        snells_law5 = MathTex(r"\displaystyle",r"\theta_i","=",r"arcsin(\frac{1}{1.33})",r"\approx",r"48.6 ^{\circ}").move_to(snells_law)
        snells_law_flip = MathTex(r"\displaystyle",r"\theta_i","=",r"arcsin(\frac{1.33}{1})").move_to(snells_law)

        self.play(Write(VGroup(sine_wave,surface_icon)))
        self.play(Write(VGroup(water_IOR,air_IOR)))
        self.wait()
        self.play(Write(VGroup(central_line,incident_vector,outgoing_vector)))
        self.play(Write(VGroup(theta_i_arc,theta_o_arc,theta_i_label,theta_o_label)))
        self.wait()
        
        self.play(Write(snells_law))
        snell_laws_extra = [snells_law2,snells_law3,snells_law4,snells_law5]
        for law in snell_laws_extra:
            self.play(Transform(snells_law,law))
            self.wait()
        self.wait()

        self.play(air_IOR.animate.shift(DOWN),
                  water_IOR.animate.shift(UP),
                  Transform(snells_law,snells_law_flip),
                  sine_wave.animate.flip(RIGHT),
                  surface_icon.animate.flip(RIGHT)) 
        self.play(surface_icon.animate.shift(0.2*DOWN))
        self.wait()

class ConstructiveInterference(Scene):
    def construct(self):
        wave1 = FunctionGraph(lambda x: 0.8*np.sin(x),x_range=[-7,7],color=WHITE).shift(2*UP)
        wave2 = FunctionGraph(lambda x: 0.8*np.sin(x),x_range=[-7,7],color=WHITE).shift(2*DOWN)
        wave3 = FunctionGraph(lambda x: 2.4*np.sin(x),x_range=[-7,7],color=WHITE) # technical lie but easier to see

        self.play(Write(wave1),Write(wave2))
        self.wait()
        self.play(Transform(VGroup(wave1,wave2),wave3))
        self.wait()
        self.play(FadeOut(wave3))
        self.wait()

class DestructiveInterference(Scene):
    def construct(self):
        wave1 = FunctionGraph(lambda x: 0.8*np.sin(x),x_range=[-7,7],color=WHITE).shift(2*UP)
        wave2 = FunctionGraph(lambda x: 0.8*np.sin(x+PI),x_range=[-7,7],color=WHITE).shift(2*DOWN)
        wave3 = FunctionGraph(lambda x: 0,x_range=[-7,7],color=WHITE) # technical lie but easier to see

        self.play(Write(wave1),Write(wave2))
        self.wait()
        self.play(Transform(VGroup(wave1,wave2),wave3))
        self.wait()
        self.play(FadeOut(wave3))
        self.wait()

class DoubleSlit(Scene):
    def construct(self):
        central_line = Line(start=UP,end=DOWN)
        up_line = Line(start=4*UP,end=2*UP)
        down_line = Line(start=2*DOWN,end=4*DOWN)

        top_path = Vector(5*RIGHT+UP,color=WHITE).shift(1.5*UP)
        bottom_path = Vector(5*RIGHT+4*UP,color=WHITE).shift(1.5*DOWN)

        hit_line = Line(start=3*UP+5*RIGHT,end=2*UP+5*RIGHT)

        r1_label = Tex("$r_1$").shift(2.5*RIGHT+2.3*UP)
        r2_label = Tex("$r_2$").shift(2.5*RIGHT)

        delta_r = Tex(r"$\Delta r = r_1 - r_2$").to_edge(UR).shift(LEFT)
        constructive = Tex(r"Constructive: $\Delta r = m \lambda$").next_to(delta_r,DOWN)
        destructive = Tex(r"Destructive: $\Delta r = (m+ \frac{1}{2}) \lambda$").next_to(constructive,DOWN)
        destructive.shift(0.75*LEFT)

        m_set_element = Tex(r"$m \in \mathbb{Z}$").scale(0.5).to_corner(DR,buff=0.75)

        VGroup(delta_r,constructive,destructive).move_to(UP).to_edge(RIGHT)

        wave = SVGMobject("svg/wave-curve.svg").set_color(BLUE)

        waves_inc = VGroup(wave.copy().scale(0.5).shift(4*LEFT),
                       wave.copy().scale(0.75).shift(3.5*LEFT),
                       wave.copy().shift(3*LEFT),
                       wave.copy().scale(1.25).shift(2.5*LEFT),
                       wave.copy().scale(1.5).shift(2*LEFT),
                       wave.copy().scale(1.75).shift(1.5*LEFT),
                       wave.copy().scale(2).shift(LEFT)).scale(1.25).shift(0.45*LEFT)
        waves_out1 = VGroup(wave.copy().scale(0.5).shift(1.5*UP+0.45*RIGHT),
                            wave.copy().scale(0.75).shift(1.5*UP+0.7*RIGHT))
        waves_out2 = VGroup(wave.copy().scale(0.5).shift(1.5*DOWN+0.45*RIGHT),
                            wave.copy().scale(0.75).shift(1.5*DOWN+0.7*RIGHT))

        self.play(Write(VGroup(up_line,central_line,down_line)))
        self.wait()
        self.play(Write(waves_inc))
        self.play(Write(waves_out1))
        self.play(Write(waves_out2))
        self.wait()
        self.play(Write(VGroup(top_path,bottom_path,hit_line)))
        self.play(Write(VGroup(r1_label,r2_label)))
        self.wait()
        self.play(VGroup(up_line,central_line,down_line,top_path,bottom_path,
                         r1_label,r2_label,hit_line,waves_out1,
                         waves_out2)
                  .animate.to_edge(LEFT),
                  FadeOut(waves_inc))
        self.wait()
        self.play(Write(delta_r))
        self.wait()
        self.play(Write(constructive))
        self.wait()
        self.play(Write(destructive))
        self.wait()
        self.play(FadeIn(m_set_element))
        self.wait()

class BraggDiffraction(Scene):
    def construct(self):
        dots = [Dot(color=WHITE).set_z_index(10),
                Dot(color=WHITE).shift(2*DOWN),
                Dot(color=WHITE).shift(2*RIGHT),
                Dot(color=WHITE).shift(2*UP),
                Dot(color=WHITE).shift(2*LEFT),
                Dot(color=WHITE).shift(2*DR),
                Dot(color=WHITE).shift(2*DL),
                Dot(color=WHITE).shift(2*UR),
                Dot(color=WHITE).shift(2*UL)]

        incoming_vecs = VGroup(Vector(4*RIGHT+2*DOWN,color=BLUE).shift(4.1*LEFT+2.1*UP),
                               Vector((4*RIGHT+2*DOWN),color=BLUE).shift(4.1*LEFT+0.1*UP))
        outgoing_vecs = incoming_vecs.copy().flip(RIGHT).shift(4.2*RIGHT)

        d_label = Tex("$d$").shift(1.3*DOWN+0.3*RIGHT)
        d_line = Line(start=ORIGIN,end=2*DOWN).set_z_index(-5)

        dotted_lines = VGroup(DashedLine(start=ORIGIN,end=0.75*(LEFT+2*DOWN)),
                              DashedLine(start=ORIGIN,end=0.75*(RIGHT+2*DOWN)))

        theta_arcs = VGroup(Arc(radius=0.5,start_angle=3*PI/2-np.arctan2(1,2),angle=np.arctan2(1,2)),
                            Arc(radius=0.75,start_angle=3*PI/2,angle=np.arctan2(1,2)))
        
        delta_r = MathTex(r"\Delta","r","=","d",r"\sin","(",r"\theta_1",")","+","d",r"\sin","(",r"\theta_2",")").to_edge(UL)
        
        self.play(*[Write(dot) for dot in dots])
        self.wait()
        self.play(AnimationGroup(Write(incoming_vecs),Write(outgoing_vecs),lag_ratio=0.2))
        self.play(*[dot.animate.set_color(BLUE_E) for dot in dots[0:2]])
        self.play(Write(d_line),Write(d_label))
        self.play(AnimationGroup(Write(dotted_lines),Write(theta_arcs),lag_ratio=0.4))
        self.wait()
        self.play(Write(delta_r))
        self.wait()


