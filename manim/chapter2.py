from manim import *
from circuits import capacitor,resistor,voltage,wire,light
import charge

class ResistanceFlowPropto(Scene):
    def construct(self):
        prop = MathTex("R","=","{V",r"\over","flow}").scale(3)
        self.add(prop)
        self.wait()
        self.play(prop.animate.scale(1/3))
        self.wait()
        self.play(prop.animate.to_edge(UL))

        loop = Circle().stretch(0.2,0)
        self.play(Write(loop))
        self.wait()

        charge1 = charge.Charge(radius=0.5)
        charge1.elements.shift(LEFT)
        self.play(FadeIn(charge1.image,charge1.text))
        self.wait()

        arrow = Vector(2*RIGHT).shift(LEFT)
        self.play(GrowArrow(arrow),charge1.elements.animate.shift(2*RIGHT))
        self.wait()

        flow_label = MathTex(r"flow =", r"{\Delta Q",r"\over",r"\Delta t}").next_to(loop,UP)
        flow_label.set_color_by_tex('Q',BLUE)
        self.play(FadeIn(flow_label))
        self.wait()

        self.play(loop.animate.shift(LEFT))

        loop2=loop.copy().shift(3*RIGHT)
        tube_line_top = Line(start=loop.get_center()+UP*loop.height/2,
                             end=loop2.get_center()+UP*loop2.height/2).set_color(RED)
        tube_line_bottom = Line(start=loop.get_center()+DOWN*loop.height/2,
                             end=loop2.get_center()+DOWN*loop2.height/2).set_color(RED)
        tube = VGroup(loop,loop2,tube_line_bottom,tube_line_top)
        self.play(FadeOut(arrow),FadeIn(loop2,tube_line_bottom,tube_line_top),charge1.elements.animate.scale(0.5),
                  charge1.elements.animate.shift(0.5*LEFT))
        self.wait()

        geo_current1 = MathTex(r"Q","=(","{Q",r"\over","V}",")","V")
        geo_current1.scale(0.7)
        geo_current1.set_color_by_tex("Q",BLUE)
        geo_current1.set_color_by_tex("V",GREEN)
        geo_current1.next_to(tube,DOWN)
        self.play(FadeIn(geo_current1))
        self.wait()

        geo_current2 = MathTex(r"Q","=(","n","q",")","V")
        geo_current2.scale(0.7)
        geo_current2.set_color_by_tex("Q",BLUE)
        geo_current2.set_color_by_tex("q",GRAY)
        geo_current2.set_color_by_tex("n",BLUE)
        geo_current2.set_color_by_tex("V",GREEN)
        geo_current2.next_to(geo_current1,DOWN)
        self.play(FadeIn(geo_current2))
        self.wait()

        mob_moves = VGroup(flow_label,tube,charge1.elements,geo_current1,geo_current2)
        self.play(mob_moves.animate.shift(1.5*UP))
        self.wait()

        self.play(loop.animate.set_opacity(0.5))
        self.wait()

        area_label = Tex(r"$A$").move_to(loop)
        self.play(Write(area_label))
        self.wait()

        l_arrow = Vector(3*RIGHT+UP).shift(3*LEFT+0.5*DOWN)
        l_label = Tex(r"$l$").move_to(l_arrow).shift(2*LEFT+0.5*DOWN)
        self.play(FadeIn(l_arrow,l_label))
        self.wait()

        geo_current3 = MathTex(r"Q","=(","n","q",")","A","l")
        geo_current3.scale(0.7)
        geo_current3.set_color_by_tex("Q",BLUE)
        geo_current3.set_color_by_tex("q",GRAY)
        geo_current3.set_color_by_tex("n",BLUE)
        geo_current3.set_color_by_tex("A",GREEN)
        geo_current3.next_to(geo_current2,DOWN)
        self.play(FadeIn(geo_current3))
        self.wait()

        velocity_arrow = Vector(1.5*RIGHT).move_to(charge1.image).shift(0.5*1.5*RIGHT).set_color(GRAY)
        velocity_label = Tex(r"$\vec{v}$").next_to(velocity_arrow,UP,buff=0.2).set_color(GRAY)
        self.play(GrowArrow(velocity_arrow),FadeIn(velocity_label))
        self.wait()

        geo_current4 = MathTex(r"Q","=(","n","q",")","A","v",r"\Delta t")
        geo_current4.scale(0.7)
        geo_current4.set_color_by_tex("Q",BLUE)
        geo_current4.set_color_by_tex("q",GRAY)
        geo_current4.set_color_by_tex("n",BLUE)
        geo_current4.set_color_by_tex("A",GREEN)
        geo_current4.set_color_by_tex("v",GRAY)
        geo_current4.next_to(geo_current3,DOWN)
        self.play(FadeIn(geo_current4))
        self.wait()

        geo_current5 = MathTex(r"flow","=",r"{Q",r"\over",r"\Delta t}","=(","n","q",")","A","v")
        geo_current5.scale(0.7)
        geo_current5.set_color_by_tex("Q",BLUE)
        geo_current5.set_color_by_tex("q",GRAY)
        geo_current5.set_color_by_tex("n",BLUE)
        geo_current5.set_color_by_tex("A",GREEN)
        geo_current5.set_color_by_tex("v",GRAY)
        geo_current5.next_to(geo_current4,DOWN)
        self.play(FadeIn(geo_current5))
        self.wait()

        fadeout_mobs = VGroup(geo_current1,geo_current2,geo_current3,geo_current4)
        self.play(FadeOut(fadeout_mobs),geo_current5.animate.next_to(tube,DOWN))

        geo_current5_rewrite = MathTex(r"I","=","(","n","q",")","A","v")
        geo_current5_rewrite.set_color_by_tex("Q",BLUE)
        geo_current5_rewrite.set_color_by_tex("q",GRAY)
        geo_current5_rewrite.set_color_by_tex("n",BLUE)
        geo_current5_rewrite.set_color_by_tex("A",GREEN)
        geo_current5_rewrite.set_color_by_tex("v",GRAY)
        geo_current5_rewrite.move_to(geo_current5)

        current_label = MathTex(r"Current = I = ",r"{\Delta Q",r"\over",r"\Delta t}").move_to(flow_label)
        current_label.set_color_by_tex("Q",BLUE)
        ohm_law_r_equals = Tex(r"$R = \frac{V}{I}$").to_edge(UL)
        self.play(Transform(flow_label,current_label),Transform(prop,ohm_law_r_equals),
                  Transform(geo_current5,geo_current5_rewrite))
        self.wait()

        current_header = Text("Current").scale(1.5).to_edge(UR)
        self.play(FadeIn(current_header))
        self.wait()

        velocity_arrow = Vector(UP+RIGHT).shift(1.3*DOWN+0.5*RIGHT)
        self.play(Write(velocity_arrow))
        self.wait()

        self.play(FadeOut(velocity_arrow))
        self.wait()

        solved_for_velocity = MathTex(r"{I",r"\over","(","n","q",")","A}","=","v")
        solved_for_velocity.set_color_by_tex("Q",BLUE)
        solved_for_velocity.set_color_by_tex("q",GRAY)
        solved_for_velocity.set_color_by_tex("n",BLUE)
        solved_for_velocity.set_color_by_tex("A",GREEN)
        solved_for_velocity.set_color_by_tex("v",GRAY)
        solved_for_velocity.next_to(geo_current5_rewrite,DOWN)
        self.play(FadeIn(solved_for_velocity))
        self.wait()
    
class OhmsLawIntro(Scene):
    def construct(self):
        eqn = MathTex("R","=","{V",r"\over","I}")
        eqn.set_color_by_tex("I",YELLOW_A)
        eqn.set_color_by_tex("V",BLUE_D)
        eqn.set_color_by_tex("R",RED)
        eqn_og = eqn.copy()

        eqn_filled = MathTex("2","=","{2",r"\over","1}")

        ohm_law = MathTex("V","=","I","R")
        ohm_law.set_color_by_tex("I",YELLOW_A)
        ohm_law.set_color_by_tex("V",BLUE_D)
        ohm_law.set_color_by_tex("R",RED)

        header = Text("Ohm's Law").scale(2).to_edge(UP)

        self.play(Write(eqn))
        self.wait()
        self.play(Transform(eqn,eqn_filled))
        self.wait()
        self.play(Transform(eqn,eqn_og))
        self.wait()
        self.play(Transform(eqn,ohm_law))
        self.wait()
        self.play(eqn.animate.scale(2))
        self.wait()
        self.play(FadeIn(header))
        self.wait()

class GeometricResistor(Scene):
    def construct(self):
        circ1 = Circle(color=WHITE).stretch(0.2,0).shift(LEFT)
        circ2 = circ1.copy().shift(2*RIGHT)
        line1 = Line(start=circ1.get_center()+UP*circ1.height/2,end=circ2.get_center()+UP*circ1.height/2)
        line2 = Line(start=circ1.get_center()+DOWN*circ1.height/2,end=circ2.get_center()+DOWN*circ1.height/2)

        r1 = VGroup(circ1,circ2,line1,line2)
        r1_copy = r1.copy()

        r1_label = Tex(r"$R_1$").next_to(r1,UP).set_color(RED)

        charge1 = charge.Charge(radius=0.5)
        charge1.elements.shift(LEFT*2)

        move_arrow = Vector(4*RIGHT).move_to(charge1.image.get_center()).shift(2*RIGHT)

        circ2_long = circ2.copy().shift(RIGHT)
        line1_long = Line(start=circ1.get_center()+UP*circ1.height/2,end=circ2_long.get_center()+UP*circ1.height/2)
        line2_long = Line(start=circ1.get_center()+DOWN*circ1.height/2,end=circ2_long.get_center()+DOWN*circ1.height/2)
        r1_long = VGroup(circ1,circ2_long,line1_long,line2_long)

        l_label = Tex("$l$").next_to(r1,DOWN)

        circ1_wide = Circle(radius=2,color=WHITE).stretch(0.1,0).shift(LEFT)
        circ2_wide = circ1_wide.copy().shift(2*RIGHT)
        line1_wide = Line(start=circ1_wide.get_center()+UP*circ1_wide.height/2,end=circ2_wide.get_center()+UP*circ2_wide.height/2)
        line2_wide = Line(start=circ1_wide.get_center()+DOWN*circ1_wide.height/2,end=circ2_wide.get_center()+DOWN*circ2_wide.height/2)

        r1_wide = VGroup(circ1_wide,circ2_wide,line1_wide,line2_wide)

        charge1_and_arrow = VGroup(charge1.image,charge1.text,move_arrow)
        charge2_and_arrow = charge1_and_arrow.copy()
        charge3_and_arrow = charge1_and_arrow.copy()

        a_label = Tex(r"$A$").next_to(circ2_wide,RIGHT,buff=0.2).shift(0.5*DOWN)

        r1_prop_l = Tex(r"$R_1$", r"$\propto l$").to_edge(UL)
        r1_prop_l.set_color_by_tex("R",RED)
        r1_prop_a = MathTex(r"R_1", r"\propto", r"{1",r"\over",r"A}").next_to(r1_prop_l,DOWN)
        r1_prop_a.set_color_by_tex("A",GRAY)
        r1_prop_a.set_color_by_tex("R",RED)

        final_eqn = MathTex(r"R_1", "=", r"{\rho l",r"\over",r"A")
        final_eqn.set_color_by_tex("R",RED)
        final_eqn.set_color_by_tex("A",GRAY)
        final_eqn.next_to(r1_prop_a,DOWN)

        integral_eqn = MathTex(r"R","=",r"\int",r"{\rho","dl",r"\over","A}")
        integral_eqn.set_color_by_tex("R",RED)
        integral_eqn.set_color_by_tex("A",GRAY)
        integral_eqn.next_to(final_eqn,DOWN)

        self.play(Write(r1),Write(r1_label))
        self.wait()
        self.play(Write(charge1.image),Write(charge1.text))
        self.wait()
        self.play(GrowArrow(move_arrow))
        self.wait()
        self.play(Transform(r1,r1_long))
        self.wait()
        self.play(FadeIn(l_label),Transform(r1,r1_copy))
        self.wait()
        self.play(Transform(r1,r1_wide),r1_label.animate.shift(UP),l_label.animate.shift(DOWN))
        self.wait()
        self.play(charge2_and_arrow.animate.shift(DOWN*1.25),charge3_and_arrow.animate.shift(UP*1.25))
        self.wait()
        self.play(circ2_wide.animate.set_fill(WHITE,opacity=0.5),FadeIn(a_label))
        self.wait()
        self.play(FadeIn(r1_prop_l))
        self.play(FadeIn(r1_prop_a))
        self.wait()
        self.play(FadeIn(final_eqn))
        self.wait()
        self.play(FadeIn(integral_eqn))
        self.wait()
        self.play(Transform(VGroup(r1_prop_l,r1_prop_a).copy(),final_eqn))
        self.wait()

class SeriesResistors(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(height=1,width=1))
        v1.elements.to_edge(DOWN).shift(UP)
        v1_label = Text("Voltage").next_to(v1.image,DOWN)

        r1 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r1.elements.to_edge(UP).shift(DOWN+LEFT)
        r1_label = Text("Resistor").scale(0.5).next_to(r1.image,DOWN)

        r2 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r2.elements.to_edge(UP).shift(DOWN+RIGHT)
        r2_label = Text("Resistor").scale(0.5).next_to(r2.image,DOWN)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+2*LEFT))
        w1.add_point(Point(r1.get_start_pos()+LEFT))
        w1.add_point(r1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(r1.get_end_point())
        w2.add_point(r2.get_start_point())

        w3 = wire.Wire()
        w3.add_point(r2.get_end_point())
        w3.add_point(Point(r2.get_end_pos()+RIGHT))
        w3.add_point(Point(v1.get_end_pos()+2*RIGHT))
        w3.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,w1.image,r1.image,w2.image,r2.image,w3.image)
        
        circuit.set_color_by_gradient(BLUE,GREEN)
        V_label = Tex("V").move_to(v1_label).set_color(BLUE_D)
        r1_label2 = Tex(r"$R_1$").move_to(r1_label).set_color(RED)
        r2_label2 = Tex(r"$R_2$").move_to(r2_label).set_color(RED)

        w1_rewrite = wire.Wire()
        w1_rewrite.add_point(v1.get_start_point())
        w1_rewrite.add_point(Point(v1.get_start_pos()+2*LEFT))
        w1_rewrite.add_point(Point(r1.get_start_pos()+LEFT))
        w1_rewrite.add_point(Point(r1.get_start_pos()+0.5*RIGHT))

        w2_rewrite = wire.Wire()
        w2_rewrite.add_point(Point(r1.get_end_pos()+0.5*RIGHT))
        w2_rewrite.image.move_to(w2.image)

        w3_rewrite = wire.Wire()
        w3_rewrite.add_point(Point(r2.get_end_pos()+0.5*LEFT))
        w3_rewrite.add_point(Point(r2.get_end_pos()+RIGHT))
        w3_rewrite.add_point(Point(v1.get_end_pos()+2*RIGHT))
        w3_rewrite.add_point(v1.get_end_point())

        series_header = Text("Series").scale(1.5).to_edge(UR).shift(LEFT)

        circuit2 = VGroup(v1.image,w1_rewrite.image,r1.image,w2_rewrite.image,r2.image,w3_rewrite.image)
        circuit2.set_color_by_gradient(BLUE,GREEN)

        r_eff_label = MathTex(r"R_{\text{eff}}", "=", "R_1", "+", "R_2").next_to(circuit2,UP)
        r_eff_label.set_color_by_tex("R",RED)

        ohm_law = MathTex("V=","I","R").to_edge(UL)
        ohm_law2 = MathTex(r"{V",r"\over",r"R}","=","I").next_to(ohm_law,DOWN)
        ohm_law3 = Tex(r"$\frac{9}{1+2}=3=$","$I$").next_to(ohm_law2,DOWN).shift(0.5*RIGHT)

        ohm_law.set_color_by_tex("I",YELLOW_A)
        ohm_law.set_color_by_tex("V",BLUE_D)
        ohm_law.set_color_by_tex("R",RED)

        ohm_law2.set_color_by_tex("I",YELLOW_A)
        ohm_law2.set_color_by_tex("V",BLUE_D)
        ohm_law2.set_color_by_tex("R",RED)

        ohm_law3.set_color_by_tex("I",YELLOW_A)

        nine_volt_label = Tex(r"$V:9$").move_to(V_label).set_color(BLUE_D)
        one = Tex(r"$1$").next_to(r1_label,DOWN).shift(0.5*RIGHT)
        two = Tex(r"$2$").next_to(r2_label,DOWN).shift(0.5*LEFT)

        self.play(Write(v1.image),Write(v1_label))
        self.wait()
        self.play(Write(VGroup(w1.image,r1.image,w2.image,r2.image,w3.image)),FadeIn(r1_label,r2_label))
        self.wait()

        self.play(Transform(v1_label,V_label),Transform(r1_label,r1_label2),Transform(r2_label,r2_label2))
        self.wait()

        self.play(FadeIn(series_header))
        self.wait()

        self.play(r1.image.animate.shift(0.5*RIGHT),r2.image.animate.shift(0.5*LEFT),
                  r1_label.animate.shift(0.5*RIGHT),r2_label.animate.shift(0.5*LEFT),
                  Transform(w1.image,w1_rewrite.image),Transform(w2.image,w2_rewrite.image),
                  Transform(w3.image,w3_rewrite.image))
        self.wait()
        self.play(FadeIn(r_eff_label))
        self.wait()

        self.play(Transform(v1_label,nine_volt_label),FadeIn(one,two))
        self.wait()
        self.play(Write(ohm_law))
        self.wait()
        self.play(Write(ohm_law2))
        self.wait()
        self.play(Write(ohm_law3))
        self.wait()

class ParallelResistors(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(width=1,height=1))
        v1.elements.to_edge(DOWN).shift(UP)

        v1_label = Tex("$V$").next_to(v1.elements,DOWN).set_color(BLUE_D)

        r1 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r1.elements.shift(0.5*UP)
        r2 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r2.elements.next_to(r1.image,UP).shift(UP)

        r1_label = Tex(r"$R_1$").next_to(r1.image,DOWN).set_color(RED)
        r2_label = Tex(r"$R_2$").next_to(r2.image,DOWN).set_color(RED)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+2*LEFT))
        w1.add_point(Point(r1.get_start_pos()+2*LEFT+UP))
        w1.add_point(Point(r1.get_start_pos()+LEFT+UP))

        w2 = wire.Wire()
        w2.add_point(Point(r1.get_start_pos()+LEFT+UP))
        w2.add_point(Point(r2.get_start_pos()+LEFT))
        w2.add_point(r2.get_start_point())

        w3 = wire.Wire()
        w3.add_point(Point(r1.get_start_pos()+LEFT+UP))
        w3.add_point(Point(r1.get_start_pos()+LEFT))
        w3.add_point(r1.get_start_point())

        w4 = wire.Wire()
        w4.add_point(r2.get_end_point())
        w4.add_point(Point(r2.get_end_pos()+RIGHT))
        w4.add_point(Point(r1.get_end_pos()+RIGHT+UP))

        w5 = wire.Wire()
        w5.add_point(r1.get_end_point())
        w5.add_point(Point(r1.get_end_pos()+RIGHT))
        w5.add_point(Point(r1.get_end_pos()+RIGHT+UP))

        w6 = wire.Wire()
        w6.add_point(Point(r1.get_end_pos()+RIGHT+UP))
        w6.add_point(Point(r1.get_end_pos()+2*RIGHT+UP))
        w6.add_point(Point(v1.get_end_pos()+2*RIGHT))
        w6.add_point(v1.get_end_point())

        r1_cpy = r1.image.copy()
        r2_cpy = r2.image.copy()
        w2_cpy = w2.image.copy()
        w3_cpy = w3.image.copy()
        w4_cpy = w4.image.copy()
        w5_cpy = w5.image.copy()

        circuit = VGroup(v1.image,r1.image,r2.image,w1.image,
                 w2.image,w3.image,w4.image,w5.image,w6.image)
        circuit.set_color_by_gradient(BLUE,GREEN)

        fat_resistor = resistor.Resistor(bounding_rect=Rectangle(width=1,height=3))
        fat_resistor.elements.shift(1.5*UP)

        fat_w2 = wire.Wire()
        fat_w2.add_point(Point(r1.get_start_pos()+LEFT+UP))
        fat_w2.add_point(fat_resistor.get_start_point())

        fat_w3 = wire.Wire()
        fat_w3.add_point(fat_resistor.get_end_point())
        fat_w3.add_point(Point(r1.get_end_pos()+RIGHT+UP))

        fat_circuit = VGroup(v1.image,w1.image,fat_w2.image,fat_resistor.image,fat_w3.image,
                             w6.image)
        fat_circuit.set_color_by_gradient(BLUE,GREEN)

        propto1 = MathTex("R",r"\propto","{1",r"\over","A}")
        propto1.set_color_by_tex("R",RED)
        propto1.set_color_by_tex("A",GRAY)
        propto1.to_edge(UL).shift(RIGHT)

        propto2 = MathTex("{1",r"\over","R}",r"\propto","A")
        propto2.set_color_by_tex("R",RED)
        propto2.set_color_by_tex("A",GRAY)
        propto2.next_to(propto1,DOWN)

        r_eff_label = MathTex(r"R_{\text{eff}}").next_to(fat_circuit,UP).set_color(RED)
        r_eff_2 = MathTex("{1",r"\over",r"R_{\text{eff}}}","=","{1",r"\over",r"R_1}","+","{1",r"\over",r"R_2}")
        r_eff_2.set_color_by_tex("R",RED)
        r_eff_2.move_to(r_eff_label).shift(0.5*DOWN)
        r_eff_3 = MathTex(r"R_{\text{eff}}}","=","{1",r"\over","{{1",r"\over",r"R_1}","+","{1",r"\over",r"R_2}}}")
        r_eff_3.set_color_by_tex("R",RED)
        r_eff_3.move_to(r_eff_label).shift(0.5*DOWN)

        og_r1_r2 = VGroup(r1.image,r2.image)
        og_w4_w5 = VGroup(w4.image,w5.image)
        og_w2_w3 = VGroup(w2.image,w3.image)

        parallel_header = Text("Parallel").scale(1.5).to_edge(UR)

        self.play(Write(circuit),FadeIn(r1_label,r2_label,v1_label))
        self.wait()
        self.play(FadeIn(parallel_header))
        self.wait()
        self.play(Transform(og_r1_r2,fat_resistor.image),
                  FadeOut(r1_label,r2_label),Transform(og_w2_w3,fat_w2.image),
                  Transform(og_w4_w5,fat_w3.image),FadeIn(r_eff_label))
        self.wait()
        self.play(FadeIn(r_eff_label))
        self.wait()
        self.play(FadeIn(propto1))
        self.play(FadeIn(propto2))
        self.wait()
        self.play(fat_circuit.animate.shift(DOWN),og_r1_r2.animate.shift(DOWN),
                  v1_label.animate.shift(UP),r_eff_label.animate.shift(0.5*DOWN),
                  og_w2_w3.animate.shift(DOWN),og_w4_w5.animate.shift(DOWN))
        self.play(FadeOut(og_r1_r2))
        self.wait()
        self.play(Transform(r_eff_label,r_eff_2))
        self.wait()
        self.play(Transform(r_eff_label,r_eff_3))
        self.wait()

class ManyResistorsAnalysis(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(width=1,height=1))
        v1.elements.to_edge(DL).shift(UP+2*RIGHT)

        r1 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r1.elements.move_to(v1.image).shift(3*UP)


        r2 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r2.elements.move_to(r1.image).shift(3*RIGHT+UP)

        r3 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r3.elements.move_to(r2.image).shift(2*DOWN)

        r6 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r6.elements.rotate(-PI/2)
        r6.elements.move_to(r3.image).shift(0.5*DOWN+3*RIGHT)

        r5 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r5.elements.rotate(PI)
        r5.elements.move_to(r6.image).shift(1.5*DOWN+2*RIGHT)

        r4 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r4.elements.move_to(r5.image).shift(3*UP)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(r1.get_start_pos()+LEFT))
        w1.add_point(r1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(r1.get_end_point())
        w2.add_point(Point(r1.get_end_pos()+RIGHT))
        
        w3 = wire.Wire()
        w3.add_point(Point(r1.get_end_pos()+RIGHT))
        w3.add_point(Point(r1.get_end_pos()+RIGHT+UP))
        w3.add_point(r2.get_start_point())

        w4 = wire.Wire()
        w4.add_point(Point(r1.get_end_pos()+RIGHT))
        w4.add_point(Point(r1.get_end_pos()+RIGHT+DOWN))
        w4.add_point(r3.get_start_point())

        w5 = wire.Wire()
        w5.add_point(r2.get_end_point())
        w5.add_point(Point(r2.get_end_pos()+RIGHT))
        w5.add_point(Point(r2.get_end_pos()+RIGHT+DOWN))

        w6 = wire.Wire()
        w6.add_point(r3.get_end_point())
        w6.add_point(Point(r3.get_end_pos()+RIGHT))
        w6.add_point(Point(r3.get_end_pos()+RIGHT+UP))

        w7 = wire.Wire()
        w7.add_point(Point(r3.get_end_pos()+RIGHT+UP))
        w7.add_point(r4.get_start_point())

        w8 = wire.Wire()
        w8.add_point(Point(r3.get_end_pos()+2.5*RIGHT+UP))
        w8.add_point(r6.get_start_point())

        w9 = wire.Wire()
        w9.add_point(r4.get_end_point())
        w9.add_point(Point(r4.get_end_pos()+RIGHT))
        w9.add_point(Point(r5.get_start_pos()+RIGHT))
        w9.add_point(r5.get_start_point())

        w10 = wire.Wire()
        w10.add_point(r5.get_end_point())
        w10.add_point(Point(r5.get_end_pos()+1.5*LEFT))
        w10.add_point(r6.get_end_point())

        w11 = wire.Wire()
        w11.add_point(Point(r5.get_end_pos()+1.5*LEFT))
        w11.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,w1.image,r1.image,w2.image,w3.image,w4.image,r2.image,r3.image,
                         w5.image,w6.image,w7.image,w8.image,r6.image,r4.image,w9.image,r5.image,
                         w10.image,w11.image)
        circuit.set_color_by_gradient(RED,BLUE)

        r1_label = Tex(r"$R_1$").set_color(RED).next_to(r1.image,DOWN)
        r2_label = Tex(r"$R_2$").set_color(RED).next_to(r2.image,UP)
        r3_label = Tex(r"$R_3$").set_color(RED).next_to(r3.image,DOWN)
        r4_label = Tex(r"$R_4$").set_color(RED).next_to(r4.image,DOWN)
        r5_label = Tex(r"$R_5$").set_color(RED).next_to(r5.image,DOWN)
        r6_label = Tex(r"$R_6$").set_color(RED).next_to(r6.image,LEFT)

        labels = VGroup(r1_label,r2_label,r3_label,r4_label,r5_label,r6_label)

        r45 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r45.elements.rotate(-PI/2).move_to(r6.image).shift(2*RIGHT)
        r45_label = Tex(r"$R_{45}$").set_color(RED).next_to(r45.image,RIGHT)

        w45 = wire.Wire()
        w45.add_point(Point(r2.get_end_pos()+RIGHT+DOWN))
        w45.add_point(Point(r2.get_end_pos()+4.5*RIGHT+DOWN))
        w45.add_point(r45.get_start_point())

        w45_2 = wire.Wire()
        w45_2.add_point(r45.get_end_point())
        w45_2.add_point(Point(r45.get_end_pos()+DOWN))
        w45_2.add_point(v1.get_end_point())

        r456_label = Tex(r"$R_{456}$").set_color(RED).next_to(r6.image,LEFT)

        circuit2 = VGroup(v1.image,w1.image,r1.image,w2.image,w3.image,w4.image,r2.image,r3.image,
                         w5.image,w6.image,w8.image,r6.image,w45.image,r45.image,w45_2.image,w10.image,w11.image)
        circuit2.set_color_by_gradient(RED,BLUE)

        w456 = wire.Wire()
        w456.add_point(Point(r2.get_end_pos()+RIGHT+DOWN))
        w456.add_point(Point(r2.get_end_pos()+2.5*RIGHT+DOWN))

        w456_2 = wire.Wire()
        w456_2.add_point(r6.get_end_point())
        w456_2.add_point(Point(r6.get_end_pos()+DOWN))
        w456_2.add_point(v1.get_end_point())

        circuit3 = VGroup(v1.image,w1.image,r1.image,w2.image,w3.image,w4.image,r2.image,r3.image,w456.image,r6.image,w456_2.image)
        circuit3.set_color_by_gradient(RED,BLUE)

        r23 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r23.elements.move_to(r3.image).shift(UP)

        w23 = wire.Wire()
        w23.add_point(Point(r1.get_end_pos()+RIGHT))
        w23.add_point(r23.get_start_point())

        w23_2 = wire.Wire()
        w23_2.add_point(r23.get_end_point())
        w23_2.add_point(Point(r23.get_end_pos()+RIGHT))

        r23_label = Tex(r"$R_{23}$").next_to(r23.image,UP).set_color(RED)

        circuit4 = VGroup(v1.image,w1.image,r1.image,w23.image,w23_2.image,r23.image,w456.image,r6.image,w456_2.image)
        circuit4.set_color_by_gradient(RED,BLUE)

        w_eff = wire.Wire()
        w_eff.add_point(r1.get_end_point())
        w_eff.add_point(Point(r1.get_end_pos()+RIGHT))
        w_eff.add_point(Point(v1.get_end_pos()+RIGHT))
        w_eff.add_point(v1.get_end_point())


        r_eff_label = Tex(r"$R_{\text{eff}}$")
        r_eff_label.move_to(r1_label).set_color(RED)

        circuit5 = VGroup(v1.image,w1.image,r1.image,w_eff.image)
        circuit5.set_color_by_gradient(RED,BLUE)

        transformed_to_w_eff_group = VGroup(w2.image,r23.image,w456.image,w456_2.image,
                                   r23_label,r6_label,w23.image,w23_2.image,
                                   r6.image,w8.image)
        final_mobs = VGroup(circuit5,r1_label,transformed_to_w_eff_group)

        self.play(Write(circuit))
        self.play(Write(labels))
        self.wait()
        self.play(FadeOut(r4.image,r5.image,w9.image),FadeOut(r4_label,r5_label),FadeIn(r45_label),
                  Transform(w7.image,w45.image),Transform(w11.image,w45_2.image),FadeIn(r45.image))
        self.wait()
        self.play(FadeOut(w7.image,w45_2.image,r45.image,r45_label,w11.image,w45.image,w10.image),
                  Transform(r6_label,r456_label),FadeIn(w456.image,w456_2.image))
        self.wait()
        self.play(FadeOut(r2_label,r3_label,r2.image,r3.image,w3.image,w4.image,w5.image,w6.image),
                  FadeIn(w23.image,w23_2.image,r23.image,r23_label))
        self.wait()
        self.play(Transform(transformed_to_w_eff_group,w_eff.image),
                  Transform(r1_label,r_eff_label))
        self.wait()
        self.play(final_mobs.animate.move_to(ORIGIN))
        self.wait()

class OhmPower(Scene):
    def construct(self):
        power = Text("Power").scale(1.5).to_edge(UP)

        power_eqn = MathTex("P","=","{dU",r"\over","dt},",r"\quad","U","=",r"\int","P","dt").next_to(power,DOWN).shift(0.5*DOWN)
        power_eqn.set_color_by_tex("P",PURPLE)

        piv_eqn = MathTex("P","=","I","V").next_to(power_eqn,DOWN)
        piv_eqn.set_color_by_tex("P",PURPLE)
        piv_eqn.set_color_by_tex("I",YELLOW_E)
        piv_eqn.set_color_by_tex("V",BLUE_D)

        piv_breakdown = MathTex("P","=","{Q",r"\over","t}","{U",r"\over","Q}").next_to(piv_eqn,DOWN)
        piv_breakdown.set_color_by_tex("P",PURPLE)
        piv_breakdown.set_color_by_tex("Q",LIGHT_GRAY)

        piv_breakdown2 = MathTex("P","=","{U",r"\over","t}").move_to(piv_breakdown)
        piv_breakdown2.set_color_by_tex("P",PURPLE)

        ohm_mini_header = Text("Ohm's Law").to_edge(DL).shift(2*UP)
        ohm_law = MathTex("V","=","I","R").next_to(ohm_mini_header,DOWN)
        ohm_law.set_color_by_tex("V",BLUE_D)
        ohm_law.set_color_by_tex("I",YELLOW_E)
        ohm_law.set_color_by_tex("R",RED)

        ohm_law2 = MathTex("I","=","{V",r"\over","R}").next_to(ohm_law,DOWN)
        ohm_law2.set_color_by_tex("V",BLUE_D)
        ohm_law2.set_color_by_tex("I",YELLOW_E)
        ohm_law2.set_color_by_tex("R",RED)

        ohm_arrow = Vector(piv_eqn.get_left()-ohm_mini_header.get_right()-0.25)
        ohm_arrow.move_to((ohm_mini_header.get_right()+piv_eqn.get_left())/2)

        ohm_power = MathTex("P","=","I","V","=","I^2","R","=","{V^2",r"\over","R}").next_to(piv_eqn,DOWN).shift(0.5*RIGHT)
        ohm_power.set_color_by_tex("P",PURPLE)
        ohm_power.set_color_by_tex("I",YELLOW_E)
        ohm_power.set_color_by_tex("V",BLUE_D)
        ohm_power.set_color_by_tex("R",RED)

        ohm_power_brace = Brace(ohm_power,RIGHT)

        power_example = MathTex("P","=",r"\frac{5}{5}","=1").next_to(power_eqn,DOWN)
        power_example.set_color_by_tex("P",PURPLE)

        self.play(Write(power))
        self.wait()
        self.play(Write(power_eqn))
        self.wait()
        self.play(FadeIn(power_example))
        self.wait()
        self.play(FadeOut(power_example),Write(piv_eqn))
        self.wait()
        self.play(Write(piv_breakdown))
        self.wait()
        self.play(Transform(piv_breakdown,piv_breakdown2))
        self.wait()
        self.play(FadeIn(ohm_mini_header,ohm_law,ohm_law2))
        self.wait()
        self.play(GrowArrow(ohm_arrow))
        self.wait()
        self.play(FadeOut(piv_breakdown),FadeIn(ohm_power))
        self.wait()
        self.play(FadeIn(ohm_power_brace))
        self.wait()

class CircuitVoltageDrops(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(width=1,height=1))
        v1.elements.to_edge(DOWN).shift(UP)

        v1_label = Tex("$V$").next_to(v1.elements,DOWN).set_color(BLUE_D)

        r1 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r1.elements.shift(0.5*UP)
        r2 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r2.elements.next_to(r1.image,UP).shift(UP)

        r1_label = Tex(r"$R_1$").next_to(r1.image,DOWN).set_color(RED)
        r2_label = Tex(r"$R_2$").next_to(r2.image,DOWN).set_color(RED)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+2*LEFT))
        w1.add_point(Point(r1.get_start_pos()+2*LEFT+UP))
        w1.add_point(Point(r1.get_start_pos()+LEFT+UP))

        w2 = wire.Wire()
        w2.add_point(Point(r1.get_start_pos()+LEFT+UP))
        w2.add_point(Point(r2.get_start_pos()+LEFT))
        w2.add_point(r2.get_start_point())

        w3 = wire.Wire()
        w3.add_point(Point(r1.get_start_pos()+LEFT+UP))
        w3.add_point(Point(r1.get_start_pos()+LEFT))
        w3.add_point(r1.get_start_point())

        w4 = wire.Wire()
        w4.add_point(r2.get_end_point())
        w4.add_point(Point(r2.get_end_pos()+RIGHT))
        w4.add_point(Point(r1.get_end_pos()+RIGHT+UP))

        w5 = wire.Wire()
        w5.add_point(r1.get_end_point())
        w5.add_point(Point(r1.get_end_pos()+RIGHT))
        w5.add_point(Point(r1.get_end_pos()+RIGHT+UP))

        w6 = wire.Wire()
        w6.add_point(Point(r1.get_end_pos()+RIGHT+UP))
        w6.add_point(Point(r1.get_end_pos()+2*RIGHT+UP))
        w6.add_point(Point(v1.get_end_pos()+2*RIGHT))
        w6.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,r1.image,r2.image,w1.image,
                 w2.image,w3.image,w4.image,w5.image,w6.image)
        circuit.set_color_by_gradient(BLUE,GREEN)

        charge1 = charge.Charge(radius=0.5)
        charge_img = VGroup(charge1.image,charge1.text)
        charge2_img = charge_img.copy()
        charge_img.move_to(w1.image[0].get_start())

        current_in = Tex(r"$I_{\text{in}}$").set_color(YELLOW_E).move_to(w1.image[2]).shift(3*LEFT)
        I_in_arrow1 = Vector(RIGHT).next_to(current_in,RIGHT)

        current_out = Tex(r"$I_{\text{out}}$").set_color(YELLOW_E).move_to(w6.image[0]).shift(3*RIGHT)
        I_out_arrow1 = Vector(RIGHT).next_to(current_out,LEFT)

        delta_v = Tex(r"$\Delta$", "$V$")
        delta_v.set_color(BLUE_D)
        delta_v.move_to((r1.image.get_center()+r2.image.get_center())/2)
        dv_right_arrow = Vector(0.75*RIGHT).next_to(delta_v,RIGHT)
        dv_left_arrow = Vector(0.75*LEFT).next_to(delta_v,LEFT)

        self.play(Write(circuit))
        self.wait()
        self.play(FadeIn(v1_label,r1_label,r2_label))
        self.wait()
        self.play(FadeIn(charge_img))
        self.wait()

        for line in w1.image:
            self.play(MoveAlongPath(charge_img,line))
        for line,line2 in zip(w2.image,w3.image):
            self.play(MoveAlongPath(charge_img,line),
                      MoveAlongPath(charge2_img,line2))
        for line,line2 in zip(r2.image,r1.image):
            self.play(MoveAlongPath(charge_img,line),
                      MoveAlongPath(charge2_img,line2),run_time=0.2)
        for line,line2 in zip(w4.image,w5.image):
            self.play(MoveAlongPath(charge_img,line),
                      MoveAlongPath(charge2_img,line2))
        for line in w6.image:
            self.play(MoveAlongPath(charge_img,line),
                      MoveAlongPath(charge2_img,line))
        self.wait()

        self.play(FadeOut(charge_img,charge2_img))
        self.wait()

        self.play(FadeIn(current_in,I_in_arrow1),FadeIn(current_out,I_out_arrow1))
        self.wait()
        self.play(r2_label.animate.next_to(r2.image,UP))
        self.play(FadeIn(delta_v),FadeIn(dv_left_arrow,dv_right_arrow))
        self.wait()

class KirchhoffIntro(Scene):
    def construct(self):
        header = Text("Kirchhoff").scale(1.5).to_edge(UP)
        junction_header = Text("Junction Rule").next_to(header,DOWN)
        dot = Dot()

        in1 = Vector(RIGHT).shift(1.2*LEFT).set_color(RED)
        in2 = Vector(UP).shift(1.2*DOWN).set_color(RED)

        in1_label = Tex(r"$I_{1}$").set_color(YELLOW_E).next_to(in1,LEFT)
        in2_label = Tex(r"$I_{2}$").set_color(YELLOW_E).next_to(in2,DOWN)

        out1 = Vector(RIGHT).shift(0.2*RIGHT).set_color(BLUE)
        out2 = Vector(UP).shift(0.2*UP).set_color(BLUE)

        out1_label = Tex(r"$I_3$").set_color(YELLOW_E).next_to(out1,RIGHT) 
        out2_label = Tex(r"$I_4$").set_color(YELLOW_E).next_to(out2,UP)

        junction_thing = VGroup(dot,in1,in2,out1,out2,in1_label,in2_label,out1_label,out2_label) 

        eqn_label = MathTex("I_1","+","I_2","=","I_3","+","I_4")
        eqn_label.set_color_by_tex("I",YELLOW_E)
        eqn_label.shift(3*RIGHT)

        loop_header = Text("Loop Rule").next_to(header,DOWN)

        unit_rect = Rectangle(height=1,width=1)

        v1 = voltage.DCVoltage(bounding_rect=unit_rect)
        v1.elements.to_edge(DOWN).shift(UP)

        r1 = resistor.Resistor(bounding_rect=unit_rect)
        
        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(r1.get_start_pos()+LEFT))
        w1.add_point(r1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(r1.get_end_point())
        w2.add_point(Point(r1.get_end_pos()+RIGHT))
        w2.add_point(Point(v1.get_end_pos()+RIGHT))
        w2.add_point(v1.get_end_point())

        v_label = Tex("$V$").set_color(BLUE_D).next_to(v1.image,DOWN)
        r_label = Tex("$R$").set_color(RED).next_to(r1.image,UP)

        voltage_positive_end = Tex(r"$+$").next_to(v1.image,LEFT).shift(0.5*DOWN)
        voltage_negative_end = Tex(r"$-$").next_to(v1.image,RIGHT).shift(0.5*DOWN)

        circuit = VGroup(v1.image,r1.image,w1.image,w2.image)
        circuit.set_color_by_gradient(RED,BLUE)

        ohm_law = MathTex("V","=","I","R")
        ohm_law.set_color_by_tex("V",BLUE_D)
        ohm_law.set_color_by_tex("I",YELLOW_E)
        ohm_law.set_color_by_tex("R",RED)
        ohm_law.shift(3*RIGHT)

        loop_eqn1 = Tex("$V$").set_color(BLUE).next_to(ohm_law,DOWN).shift(DOWN)
        loop_eqn2 = MathTex("V","-","I","R").move_to(loop_eqn1)
        loop_eqn2.set_color_by_tex("V",BLUE)
        loop_eqn2.set_color_by_tex("I",YELLOW_E)
        loop_eqn2.set_color_by_tex("R",RED)
        loop_eqn3 = MathTex("V","-","I","R","=","0").move_to(loop_eqn1)
        loop_eqn3.set_color_by_tex("V",BLUE)
        loop_eqn3.set_color_by_tex("I",YELLOW_E)
        loop_eqn3.set_color_by_tex("R",RED)

        loopy_stuff = VGroup(circuit,v_label,r_label,voltage_positive_end,voltage_negative_end)

        self.play(FadeIn(header))
        self.wait()
        self.play(FadeIn(junction_header))
        self.wait()
        self.play(Write(junction_thing))
        self.play(junction_thing.animate.shift(3*LEFT))
        self.wait()
        self.play(Write(eqn_label))
        self.wait()
        self.play(FadeOut(eqn_label,junction_thing,junction_header))
        self.wait()

        self.play(FadeIn(loop_header),Write(loopy_stuff))
        self.wait()
        self.play(loopy_stuff.animate.shift(3*LEFT))
        self.wait()

        # the yellow loop

        line1 = Line(start=w2.points[2].get_center()+3*LEFT,
                     end=w1.points[1].get_center()+3*LEFT,color=YELLOW_A)
        line2 = Line(start=w1.points[1].get_center()+3*LEFT,
                     end=w1.points[2].get_center()+3*LEFT,color=YELLOW_A)
        line3 = Line(start=w1.points[2].get_center()+3*LEFT,
                     end=w2.points[1].get_center()+3*LEFT,color=YELLOW_A)

        final_vector = Vector(v1.image.get_right()-r1.image.get_right())
        final_vector.move_to((w2.points[2].get_center()+w2.points[1].get_center())/2)
        final_vector.shift(3*LEFT)
        final_vector.set_color(YELLOW_A)

        self.play(FadeIn(ohm_law))
        self.wait()
        self.play(Write(line1))
        self.play(FadeIn(loop_eqn1))
        self.wait()
        self.play(Write(line2))
        self.play(Write(line3))
        self.play(Transform(loop_eqn1,loop_eqn2))
        self.wait()
        self.play(Write(final_vector))
        self.play(Transform(loop_eqn1,loop_eqn3))
        self.wait()

class LightBulb(Scene):
    def construct(self):
        bulb = light.Light()
        v1 = voltage.DCVoltage()
        v1.elements.to_edge(DOWN).shift(UP)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(bulb.get_start_pos()+LEFT))
        w1.add_point(bulb.get_start_point())

        w2 = wire.Wire()
        w2.add_point(bulb.get_end_point())
        w2.add_point(Point(bulb.get_end_pos()+RIGHT))
        w2.add_point(Point(v1.get_end_pos()+RIGHT))
        w2.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,w1.image,bulb.image,w2.image)
        circuit.set_color_by_gradient(PURPLE,BLUE)

        self.add(circuit)

class CapacitorIntro(Scene):
    def construct(self):
        c1 = capacitor.Capacitor()
        
        c1.elements.shift(UP)

        v1 = voltage.DCVoltage()
        v1.elements.to_edge(DOWN).shift(UP)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(c1.get_start_pos()+LEFT))
        w1.add_point(c1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(c1.get_end_point())
        w2.add_point(Point(c1.get_end_pos()+RIGHT))
        w2.add_point(Point(v1.get_end_pos()+RIGHT))
        w2.add_point(v1.get_end_point())

        plus_label = Tex(r"+").next_to(v1.image,LEFT).shift(0.5*DOWN)
        minus_label = Tex(r"-").next_to(v1.image,RIGHT).shift(0.5*DOWN)
        

        charge1 = charge.Charge(radius=0.25)
        charge1.elements.move_to(w1.image[0].get_start())
        charge2 = charge.Charge(radius=0.25)
        charge2.elements.move_to(w2.image[0].get_start())

        charge3 = charge.Charge(radius=0.25,charge=-1)
        charge3.elements.move_to(w2.image[0].get_start())

        plus_q_label = Tex(r"+Q").next_to(c1.image,UL)
        minus_q_label = Tex(r"-Q").next_to(c1.image,UR)

        capacitor_header = Tex("Capacitor").scale(1.5).to_edge(UP)

        circuit = VGroup(v1.image,w1.image,c1.image,w2.image)
        circuit.set_color_by_gradient(PINK,ORANGE)
        m_object_stuff = VGroup(c1.image,v1.image,w1.image,w2.image,plus_label,minus_label,plus_q_label,minus_q_label)

        r1 = resistor.Resistor()
        r1.elements.rotate(-PI/2)
        r1.elements.move_to((w2.points[1].get_center()+w2.points[2].get_center())/2)

        wr1 = wire.Wire()
        wr1.add_point(c1.get_end_point())
        wr1.add_point(Point(c1.get_end_pos()+RIGHT))
        wr1.add_point(r1.get_start_point())
        wr1.image.shift(3*LEFT)

        wr2 = wire.Wire()
        wr2.add_point(r1.get_end_point())
        wr2.add_point(Point(v1.get_end_pos()+RIGHT))
        wr2.add_point(v1.get_end_point())
        wr2.image.shift(3*LEFT)

        r1.elements.shift(3*LEFT)

        circuit2 = VGroup(v1.image,w1.image,r1.image,wr1.image,r1.image,wr2.image)
        circuit2.set_color_by_gradient(PINK,ORANGE)

        cqv_stuff = MathTex("C","=","{Q",r"\over","V}",r"\Rightarrow","V","=",r"{Q",r"\over","C}")
        cqv_stuff.set_color_by_tex("C",ORANGE)
        cqv_stuff.set_color_by_tex("Q",GREEN)
        cqv_stuff.set_color_by_tex("V",BLUE_D)
        cqv_stuff.to_edge(UP).shift(3*RIGHT+DOWN)

        kirchhoff = MathTex("V","-","{Q",r"\over","C}","-","I","R","=","0")
        kirchhoff.set_color_by_tex("V",BLUE_D)
        kirchhoff.set_color_by_tex("Q",GREEN)
        kirchhoff.set_color_by_tex("C",ORANGE)
        kirchhoff.set_color_by_tex("I",YELLOW_E)
        kirchhoff.set_color_by_tex("R",RED)

        kirchhoff.next_to(cqv_stuff,DOWN).shift(DOWN)

        kirchhoff2 = MathTex("V","-","{Q",r"\over","C}","-","{d","Q",r"\over dt}","R","=","0")
        kirchhoff2.set_color_by_tex("V",BLUE_D)
        kirchhoff2.set_color_by_tex("Q",GREEN)
        kirchhoff2.set_color_by_tex("C",ORANGE)
        kirchhoff2.set_color_by_tex("I",YELLOW_E)
        kirchhoff2.set_color_by_tex("R",RED)
        kirchhoff2.next_to(kirchhoff,DOWN)

        final_eqn = MathTex(r"\displaystyle","Q","(t)","=","Q_f","[1-",r"e^{-t",r"\over","R","C}","]").move_to(cqv_stuff)
        final_eqn.set_color_by_tex("V",BLUE_D)
        final_eqn.set_color_by_tex("Q",GREEN)
        final_eqn.set_color_by_tex("C",ORANGE)
        final_eqn.set_color_by_tex("I",YELLOW_E)
        final_eqn.set_color_by_tex("R",RED)

        current_final = MathTex(r"\displaystyle","I","(t)","=","{Q_f",r"\over","R","C}",r"e^{-t",r"\over","R","C}").next_to(final_eqn,DOWN)
        current_final.set_color_by_tex("V",BLUE_D)
        current_final.set_color_by_tex("Q",GREEN)
        current_final.set_color_by_tex("C",ORANGE)
        current_final.set_color_by_tex("I",YELLOW_E)
        current_final.set_color_by_tex("R",RED)


        graph = FunctionGraph(
            lambda t: (1-np.e**(-t)),
            x_range=[-1,4,1],
            color=GREEN
        ).next_to(current_final,DOWN).shift(0.5*DOWN)

        current_graph = FunctionGraph(
            lambda t: np.e**(-t),
            x_range=[-1,4,1],
            color=YELLOW_E
        ).next_to(current_final,DOWN).shift(0.5*DOWN)

        y_axis = Line(start=graph.get_start()+0.2*DOWN,end=graph.get_start()+3*UP)
        x_axis = Line(start =graph.get_start()+0.2*LEFT,end= graph.get_start()+5*RIGHT)

        y_label = Tex(r"$Q$").next_to(y_axis,UP)
        y_i_label = Tex(r"$I$").next_to(y_axis,UP)
        x_label = Tex(r"$t$").next_to(x_axis,RIGHT)

        q_tick = Line(start=graph.get_start()+2.75*UP+0.25*LEFT,
                      end=graph.get_start()+2.75*UP+0.25*RIGHT)
        q_tick_label = Tex(r"$Q_f$").next_to(q_tick,LEFT,buff=0.2)
        q_tick_label2 = Tex(r"$I_i$").next_to(q_tick,LEFT,buff=0.2)

        self.play(FadeIn(c1.image.rotate(-PI/2)))
        self.wait()
        self.play(c1.image.animate.rotate(PI/2))
        self.wait()
        self.play(FadeIn(v1.image,w1.image,w2.image,plus_label,minus_label))
        self.play(FadeIn(capacitor_header))
        self.wait()
        self.play(FadeIn(charge1.elements))
        self.wait()
        self.play(MoveAlongPath(charge1.elements,w1.image[0]))
        self.play(MoveAlongPath(charge1.elements,w1.image[1]))
        self.play(MoveAlongPath(charge1.elements,w1.image[2]),FadeIn(charge2.elements))
        self.wait()
        self.play(MoveAlongPath(charge2.elements,w2.image[0]))
        self.play(MoveAlongPath(charge2.elements,w2.image[1]))
        self.play(MoveAlongPath(charge2.elements,w2.image[2]))
        self.play(FadeOut(charge2.elements),FadeIn(charge3.elements))
        self.wait()
        self.play(FadeIn(plus_q_label,minus_q_label))
        self.wait()
        self.play(Wiggle(plus_q_label),Wiggle(minus_q_label))
        self.wait()
        self.play(m_object_stuff.animate.shift(3*LEFT),FadeOut(charge1.elements,charge3.elements))
        self.wait()
        self.play(FadeIn(r1.image),Transform(w2.image,wr1.image),FadeIn(wr2.image))
        self.wait()
        self.play(Write(cqv_stuff))
        self.wait()
        self.play(Write(kirchhoff))
        self.wait()
        self.play(FadeIn(kirchhoff2))
        self.wait()
        self.play(FadeOut(kirchhoff,kirchhoff2,cqv_stuff))
        self.wait()
        self.play(Write(final_eqn),Write(graph),Write(y_axis),Write(x_axis),FadeIn(x_label,y_label))
        self.wait()
        self.play(Write(q_tick),Write(q_tick_label))
        self.wait()
        self.play(FadeOut(graph,y_label,q_tick_label),Write(current_graph),FadeIn(current_final,y_i_label,q_tick_label2))
        self.wait()

class CapacitanceDefinition(Scene):
    def construct(self):
        eqn = MathTex("C","=","{Q",r"\over","V}")
        eqn.set_color_by_tex("C",ORANGE)
        eqn.set_color_by_tex("Q",GREEN)
        eqn.set_color_by_tex("V",BLUE_D)

        header = Text('Capacitance').scale(1.5).to_edge(UP)

        self.play(Write(eqn),FadeIn(header))
        self.wait()
        self.play(eqn.animate.scale(2))
        self.wait()

class RCDifferentialEquation(Scene):
    def construct(self):
        eqns = []
        eqn1 = MathTex("V","-","{Q",r"\over","C}","-","{d","Q",r"\over dt}","R","=","0").scale(0.75)
        eqn1.to_edge(UP).shift(0.5*DOWN)
        eqn2 = MathTex("-","R","{d","Q",r"\over dt}","-","{t",r"\over","C}","Q","+","V","=","0").scale(0.75)
        eqn2.next_to(eqn1,DOWN)
        eqn3 = MathTex("{d","Q",r"\over dt}","+","{t",r"\over","R","C}","Q","-","{V",r"\over","R}","=","0").scale(0.75)
        eqn3.next_to(eqn2,DOWN)
        eqn4 = MathTex("{d","Q",r"\over dt}","+","{t",r"\over","R","C}","Q","=","{V",r"\over","R}").scale(0.75)
        eqn4.next_to(eqn3,DOWN)
        eqn5_label = Tex(r"Multiply both sides by $\mu = e^{\frac{t}{RC}}$").scale(0.75).next_to(eqn4,DOWN)
        eqn5 = MathTex("{d","Q",r"\over dt}",r"e^{t",r"\over","R","C}","+","{t",r"\over","R","C}","Q",r"e^{t",r"\over","R","C}","=","{V",r"\over","R}",r"e^{t",r"\over","R","C}").scale(0.75)
        eqn5.next_to(eqn5_label,DOWN)
        eqns.append(eqn1)
        eqns.append(eqn2)
        eqns.append(eqn3)
        eqns.append(eqn4)
        eqns.append(eqn4)
        eqns.append(eqn5_label)
        eqns.append(eqn5)
        eqns.append(eqn4)

        lookup_label = Text("Look up \"Integrating Factor Method\"").scale(0.25).to_edge(UR)
        
        for eqn in eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("Q",GREEN)
            eqn.set_color_by_tex("C",ORANGE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)
        
        eqn5_label.set_color(WHITE)

        eqn5_stuff = VGroup(eqn5_label,eqn5)

        self.play(*[Write(eqn) for eqn in eqns],run_time=0.5)
        self.play(eqn5_stuff.animate.to_edge(UP),FadeIn(lookup_label),FadeOut(eqn1,eqn2,eqn3,eqn4),run_time=0.5)

        new_eqns = []
        reverse_prod = Tex(r"Reverse Product Rule").next_to(eqn5,DOWN).scale(0.75)
        eqn6 = MathTex(r"\displaystyle \frac{d}{dt}[","Q",r"e^{t",r"\over","R","C}","]","=","{V",r"\over","R}",r"e^{t",r"\over","R","C}").scale(0.75)
        eqn6.next_to(reverse_prod,DOWN)
        integrate = Tex(r"Integrate Both Sides").next_to(eqn6,DOWN).scale(0.75)
        eqn7 = MathTex(r"\displaystyle","Q",r"e^{t",r"\over","R","C}","=","V","C",r"e^{t",r"\over","R","C}","+","C_1").scale(0.75)
        eqn7.next_to(integrate,DOWN)
        eqn8 = MathTex(r"\displaystyle","Q","(t)","=","V","C","+","C_1",r"e^{-t",r"\over","R","C}").scale(0.75).next_to(eqn7,DOWN)

        new_eqns.append(eqn6)
        new_eqns.append(eqn7)
        new_eqns.append(eqn8)

        for eqn in new_eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("Q",GREEN)
            eqn.set_color_by_tex("C",ORANGE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)
        
        self.play(*[Write(eqn) for eqn in new_eqns],
                  Write(reverse_prod),Write(integrate),run_time=0.5)
        stuff_to_move = VGroup(integrate,eqn7,eqn8)
        self.play(stuff_to_move.animate.to_edge(UP),FadeOut(eqn5,eqn6,reverse_prod,eqn5_label))

        ic = Tex(r"Initial Condition: $Q(0) = 0$").next_to(eqn8,DOWN).scale(0.75)
        eqn9 = MathTex("0","=","V","C","+","C_1",r"e^{-0",r"\over","R","C}").scale(0.75).next_to(ic,DOWN)
        eqn10 = MathTex("0","=","V","C","+","C_1").scale(0.75).next_to(eqn9,DOWN)
        eqn11 = MathTex("C_1","=","-","V","C").scale(0.75).next_to(eqn10,DOWN)
        final = Tex(r"Final Equation").scale(0.75).next_to(eqn11,DOWN)
        eqn12 = MathTex(r"\displaystyle","Q","(t)","=","V","C","-","V","C",r"e^{-t",r"\over","R","C}").scale(0.75).next_to(final,DOWN)
        eqn13 = MathTex(r"\displaystyle","Q","(t)","=","V","C","[1-",r"e^{-t",r"\over","R","C}","]").scale(0.75).next_to(eqn12,DOWN)
        eqn14 = MathTex(r"\displaystyle","Q","(t)","=","Q_f","[1-",r"e^{-t",r"\over","R","C}","]").scale(0.75).next_to(eqn13,DOWN)


        new_eqns2 = [eqn9,eqn10,eqn11,eqn12,eqn13,eqn14]
        for eqn in new_eqns2:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("Q",GREEN)
            eqn.set_color_by_tex("C",ORANGE)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)
        
        self.play(Write(ic),*[Write(eqn) for eqn in new_eqns2],Write(final),
                  FadeOut(lookup_label),run_time=0.5)

class CapacitorAcrossCircuit(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(width=1,height=1))
        v1.elements.to_edge(DOWN).shift(UP)

        v1_label = Tex("$V$").next_to(v1.elements,DOWN).set_color(BLUE_D)

        r1 = resistor.Resistor(bounding_rect=Rectangle(width=1,height=1))
        r1.elements.shift(2*UP)
        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))

        r1_label = Tex(r"$R_1$").next_to(r1.image,DOWN).set_color(RED)
        r2_label = Tex(r"$R_2$").next_to(c1.image,DOWN).set_color(RED)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(c1.get_start_pos()+LEFT))

        w2 = wire.Wire()
        w2.add_point(Point(c1.get_start_pos()+LEFT))
        w2.add_point(Point(r1.get_start_pos()+LEFT))
        w2.add_point(r1.get_start_point())

        w3 = wire.Wire()
        w3.add_point(Point(c1.get_start_pos()+LEFT))
        w3.add_point(c1.get_start_point())

        w4 = wire.Wire()
        w4.add_point(r1.get_end_point())
        w4.add_point(Point(r1.get_end_pos()+RIGHT))
        w4.add_point(Point(c1.get_end_pos()+RIGHT))

        w5 = wire.Wire()
        w5.add_point(c1.get_end_point())
        w5.add_point(Point(c1.get_end_pos()+RIGHT))

        w6 = wire.Wire()
        w6.add_point(Point(c1.get_end_pos()+RIGHT))
        w6.add_point(Point(v1.get_end_pos()+RIGHT))
        w6.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,r1.image,c1.image,w1.image,
                 w2.image,w3.image,w4.image,w5.image,w6.image)
        circuit.set_color_by_gradient(BLUE,GREEN)

        positive_terminal = Tex(r"$+$").next_to(v1.elements,LEFT).shift(0.5*DOWN)
        negative_terminal = Tex(r"$-$").next_to(v1.elements,RIGHT).shift(0.5*DOWN)

        charges1 = []
        charges2 = []
        charges3_anim2 = []
        charges4 = []
        for i in range(5):
            new_charge = charge.Charge(radius=0.25)
            new_charge.elements.move_to(w1.points[0].get_center())
            charges1.append(new_charge)

            new_charge2 = charge.Charge(radius=0.25)
            new_charge2.elements.move_to(w5.points[0].get_center())
            charges2.append(new_charge2)
        
        for i in range(10):

            new_charge3 = charge.Charge(radius=0.25)
            new_charge3.elements.move_to(w1.points[0].get_center())
            charges3_anim2.append(new_charge3)

            new_charge4 = charge.Charge(radius=0.25)
            new_charge4.elements.move_to(w3.points[1].get_center())
            charges4.append(new_charge4)

        traced_path = VMobject().set_points_as_corners([w1.points[0].get_center(),w1.points[1].get_center(),
                                                        w1.points[2].get_center(),w3.points[1].get_center()])
        traced_path2 = VMobject().set_points_as_corners([w5.points[0].get_center(),w5.points[1].get_center(),
                                                        w6.points[0].get_center(),w6.points[1].get_center(),
                                                        w6.points[2].get_center()])
        path3 = VMobject().set_points_as_corners([w1.points[0].get_center(),w1.points[1].get_center(),
                                                        w2.points[1].get_center(),w4.points[1].get_center(),
                                                        w6.points[1].get_center(),w6.points[2].get_center()])
        path4 = VMobject().set_points_as_corners([w3.points[1].get_center(),w3.points[0].get_center(),
                                                        w2.points[1].get_center(),w4.points[1].get_center(),
                                                        w4.points[2].get_center(),w5.points[0].get_center()])


        self.play(Write(circuit),FadeIn(negative_terminal,positive_terminal))
        
        animation1 = AnimationGroup(*[MoveAlongPath(c1.elements,traced_path) for c1 in charges1],lag_ratio=0.05)
        animation2 = AnimationGroup(*[MoveAlongPath(c2.elements,traced_path2) for c2 in charges2],lag_ratio=0.05)

        charge_labels = VGroup(Tex("$+$").next_to(c1.image,LEFT).shift(0.25*RIGHT+0.5*UP),
                               Tex("$-$").next_to(c1.image,RIGHT).shift(0.25*LEFT+0.5*UP))

        stuff_to_move = VGroup(circuit,charge_labels,negative_terminal,positive_terminal)

        kirchhoff_line1 = Line(start=w5.points[1].get_center(),end=w3.points[0].get_center()).set_color(YELLOW_E).shift(3*LEFT)
        kirchhoff_line2 = Line(start=w3.points[0].get_center(),end=w2.points[1].get_center()).set_color(YELLOW_E).shift(3*LEFT)
        kirchhoff_line3 = Line(start=w2.points[1].get_center(),end=w4.points[1].get_center()).set_color(YELLOW_E).shift(3*LEFT)
        kirchhoff_arrow = Vector(2*DOWN).move_to((w4.points[1].get_center()+w5.points[1].get_center())/2).set_color(YELLOW_E).shift(3*LEFT)

        capacitor_discharge = MathTex("Q","(t)","=","Q_f","e^{-t",r"\over","R","C}").shift(2*UP+3*RIGHT)
        capacitor_discharge.set_color_by_tex("Q",GREEN)
        capacitor_discharge.set_color_by_tex("R",RED)
        capacitor_discharge.set_color_by_tex("C",ORANGE)

        # graph
        graph = FunctionGraph(
            lambda t: (np.e**(-t)),
            x_range=[-1,4,1],
            color=GREEN
        ).next_to(capacitor_discharge,DOWN).shift(0.5*DOWN)

        bound_line_graph = FunctionGraph(
            lambda t: np.e**(-1),
            x_range=[-1,4,1],
            color=GREEN
        ).next_to(capacitor_discharge,DOWN).shift(0.5*DOWN)
 

        graph_bottom_left = graph.get_start()+2.75*DOWN

        y_axis = Line(start=graph_bottom_left+0.2*DOWN,end=graph_bottom_left+3*UP)
        x_axis = Line(start =graph_bottom_left+0.2*LEFT,end= graph_bottom_left+5*RIGHT)
        ax = Axes().move_to(y_axis.get_start()+0.2*UP)
        
        rects = ax.get_riemann_rectangles(graph,[0,5.83],dx=0.01).set_color_by_gradient(RED,YELLOW).set_opacity(0.4).set_z_index(-3)
        rects_2 = ax.get_riemann_rectangles(bound_line_graph,
                                            x_range=[0,5.83],
                                            dx=0.01).set_color_by_gradient(BLUE,GREEN).set_opacity(0.2).set_z_index(-3)
        i_r_label = Tex("$I_R$").move_to(rects)
        i_c_label = Tex("$I_c$").move_to(i_r_label).shift(2*LEFT+0.5*DOWN)

        y_label = Tex(r"$Q$").next_to(y_axis,UP)
        y_i_label = Tex(r"$I$").next_to(y_axis,UP)
        x_label = Tex(r"$t$").next_to(x_axis,RIGHT)

        q_tick = Line(start=graph_bottom_left+2.75*UP+0.25*LEFT,
                      end=graph_bottom_left+2.75*UP+0.25*RIGHT)
        q_tick_label = Tex(r"$Q_i$").next_to(q_tick,LEFT,buff=0.2)
        q_tick_i_total = Tex(r"$I_{\text{total}}$").next_to(q_tick,LEFT,buff=0.2)

        dotted_line = DashedLine(start=q_tick.get_center(),end=q_tick.get_center()+5*RIGHT)

        self.play(AnimationGroup(animation1,
                              animation2,
                              lag_ratio=0.2))
        self.play(*[FadeOut(c.elements) for c in charges2],
                  *[FadeOut(c.elements) for c in charges1])
        self.wait()
        self.play(FadeIn(charge_labels))
        self.wait()
        self.play(AnimationGroup(*[MoveAlongPath(c3.elements,path3) for c3 in charges3_anim2],lag_ratio=0.2))
        self.wait()
        self.play(*[FadeOut(c.elements) for c in charges3_anim2])
        self.wait()
        self.play(v1.image.animate.shift(DOWN))
        self.wait()
        self.play(AnimationGroup(*[MoveAlongPath(c4.elements,path4) for c4 in charges4],lag_ratio=0.2))
        self.play(*[FadeOut(c4.elements) for c4 in charges4])
        self.wait()
        self.play(stuff_to_move.animate.shift(3*LEFT))
        self.wait()
        self.play(Write(kirchhoff_line1))
        self.play(Write(kirchhoff_line2))
        self.play(Write(kirchhoff_line3))
        self.play(Write(kirchhoff_arrow))
        self.play(Write(capacitor_discharge))
        self.play(Write(graph),Write(y_axis),Write(x_axis),Write(q_tick),FadeIn(y_label,x_label,q_tick_label))
        self.wait()
        self.play(Write(rects),Write(rects_2),FadeOut(y_label,q_tick_label),Write(dotted_line),FadeIn(y_i_label,q_tick_i_total),
                  v1.image.animate.shift(UP),FadeOut(kirchhoff_line1,kirchhoff_line2,kirchhoff_line3,kirchhoff_arrow,capacitor_discharge))
        self.play(Write(i_r_label),Write(i_c_label))
        self.wait()

class GeometricCapacitor(Scene):
    def construct(self):
        c1 = capacitor.Capacitor()
        c1.elements.scale(2)

        a_label = Tex(r"$A$").set_color(GREEN).next_to(c1.image,RIGHT).shift(0.5*UP)
        d_label = Tex(r"$d$").set_color(RED).move_to(c1.image)

        capacitor_thing = VGroup(c1.image,a_label,d_label)

        e_field = MathTex("E","=",r"{\sigma",r"\over",r"\epsilon_0}").to_edge(UP).shift(DOWN+3*RIGHT)
        e_field.set_color_by_tex("E",RED)
        e_field_2 = MathTex("E","=",r"{Q",r"\over","A",r"\epsilon_0}").next_to(e_field,DOWN)
        e_field_2.set_color_by_tex("E",RED)
        e_field_2.set_color_by_tex("A",GREEN_E)
        e_field_2.set_color_by_tex("Q",GREEN)

        v_label = MathTex("|V|","=",r"\int_0","^d",r"\vec{E}",r"\cdot",r"{d}\vec{s}").next_to(e_field_2,DOWN)
        v_label.set_color_by_tex("V",BLUE_D)
        v_label.set_color_by_tex("{d}",RED)
        v_label.set_color_by_tex("E",RED)

        v_label_2 = MathTex("|V|","=",r"\int","_0","^{d}",r"{Q",r"\over","A",r"\epsilon_0}",r"{d}l").next_to(e_field_2,DOWN)
        v_label_2.set_color_by_tex("V",BLUE_D)
        v_label_2.set_color_by_tex("{d}",RED)
        v_label_2.set_color_by_tex("E",RED)
        v_label_2.set_color_by_tex("Q",GREEN)
        v_label_2.set_color_by_tex("A",GREEN_E)

        v_label_3 = MathTex("|V|","=",r"{Q","d",r"\over","A",r"\epsilon_0}").next_to(e_field_2,DOWN)
        v_label_3.set_color_by_tex("V",BLUE_D)
        v_label_3.set_color_by_tex("Q",GREEN)
        v_label_3.set_color_by_tex("A",GREEN_E)
        v_label_3.set_color_by_tex("d",RED)
        v_label_3.set_color_by_tex("E",RED)

        capacitance_1 = MathTex("C","=","{Q",r"\over","V}","=","{Q",r"\over",r"{Q","d",r"\over","A",r"\epsilon_0}}").next_to(v_label,DOWN)
        capacitance_1.set_color_by_tex("V",BLUE_D)
        capacitance_1.set_color_by_tex("d",RED)
        capacitance_1.set_color_by_tex("E",RED)
        capacitance_1.set_color_by_tex("C",ORANGE)
        capacitance_1.set_color_by_tex("Q",GREEN)
        capacitance_1.set_color_by_tex("A",GREEN_E)

        capacitance_2 = MathTex("C","=","{Q",r"\over","V}","=","{Q",r"\over",r"{Q","d",r"\over","A",r"\epsilon_0}}","=",r"{\epsilon_0","A",r"\over","d}").move_to(capacitance_1)
        capacitance_2.set_color_by_tex("V",BLUE_D)
        capacitance_2.set_color_by_tex("d",RED)
        capacitance_2.set_color_by_tex("E",RED)
        capacitance_2.set_color_by_tex("C",ORANGE)
        capacitance_2.set_color_by_tex("Q",GREEN)
        capacitance_2.set_color_by_tex("A",GREEN_E)
        
        self.play(FadeIn(c1.image))
        self.play(c1.image.animate.rotate(3*PI/2))
        self.play(Write(a_label),Write(d_label))
        self.wait()
        self.play(capacitor_thing.animate.shift(3*LEFT))
        self.play(Write(e_field))
        self.wait()
        self.play(Write(e_field_2))
        self.wait()
        self.play(Write(v_label))
        self.wait()
        self.play(Transform(v_label,v_label_2))
        self.wait()
        self.play(Transform(v_label,v_label_3))
        self.wait()
        self.play(Write(capacitance_1))
        self.wait()
        self.play(Transform(capacitance_1,capacitance_2))
        self.wait()

class CapacitorSeriesParallel(Scene):
    def construct(self):
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(width=1,height=1))
        v1.elements.to_edge(DOWN).shift(UP)

        v1_label = Tex("$V$").next_to(v1.elements,DOWN).set_color(BLUE_D)

        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))
        c1.elements.shift(2*UP)
        c2 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))

        r1_label = Tex(r"$R_1$").next_to(c1.image,DOWN).set_color(RED)
        r2_label = Tex(r"$R_2$").next_to(c2.image,DOWN).set_color(RED)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(c2.get_start_pos()+LEFT))

        w2 = wire.Wire()
        w2.add_point(Point(c2.get_start_pos()+LEFT))
        w2.add_point(Point(c1.get_start_pos()+LEFT))
        w2.add_point(c1.get_start_point())

        w3 = wire.Wire()
        w3.add_point(Point(c2.get_start_pos()+LEFT))
        w3.add_point(c2.get_start_point())

        w4 = wire.Wire()
        w4.add_point(c1.get_end_point())
        w4.add_point(Point(c1.get_end_pos()+RIGHT))
        w4.add_point(Point(c2.get_end_pos()+RIGHT))

        w5 = wire.Wire()
        w5.add_point(c2.get_end_point())
        w5.add_point(Point(c2.get_end_pos()+RIGHT))

        w6 = wire.Wire()
        w6.add_point(Point(c2.get_end_pos()+RIGHT))
        w6.add_point(Point(v1.get_end_pos()+RIGHT))
        w6.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,c1.image,c2.image,w1.image,
                 w2.image,w3.image,w4.image,w5.image,w6.image)
        circuit.set_color_by_gradient(BLUE,GREEN)

        capacitance_1 = MathTex("C","=",r"{\epsilon_0","A",r"\over","d}").to_edge(UL).shift(RIGHT+DOWN)
        capacitance_1.set_color_by_tex("V",BLUE_D)
        capacitance_1.set_color_by_tex("d",RED)
        capacitance_1.set_color_by_tex("E",RED)
        capacitance_1.set_color_by_tex("C",ORANGE)
        capacitance_1.set_color_by_tex("Q",GREEN)
        capacitance_1.set_color_by_tex("A",GREEN_E)

        transform_mobs = VGroup(c1.image,c2.image,w3.image,w5.image)
        c3 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=2))
        c3.elements.move_to(c1.image)

        c_eff = Tex(r"$C_{\text{eff}}$").next_to(c3.image,UP)
        c_eff.set_color(ORANGE)
        c_eff_label = MathTex(r"C_{\text{eff}}","=","C_1","+","C_2").next_to(capacitance_1,DOWN)
        c_eff_label.set_color_by_tex("C",ORANGE).shift(DOWN)
        c_eff_label2 = MathTex(r"{1",r"\over",r"C_{\text{eff}}}","=","{1",r"\over","C_1}","+","{1",r"\over","C_2}").next_to(capacitance_1,DOWN)
        c_eff_label2.set_color_by_tex("C",ORANGE).shift(DOWN)
        c_eff_label2_solve = MathTex(r"C_{\text{eff}}}","=","{1",r"\over","{1",r"\over","C_1}","+","{1",r"\over","C_2}}").next_to(capacitance_1,DOWN)
        c_eff_label2_solve.set_color_by_tex("C",ORANGE).shift(DOWN)

        
        circuit2 = VGroup(v1.image,w1.image,w2.image,c3.image,w4.image,w6.image)
        circuit2.set_color_by_gradient(BLUE,GREEN)

        parallel_stuff = VGroup(circuit2,c_eff,c_eff_label,capacitance_1)
    
        self.play(Write(circuit),run_time=1)
        self.play(FadeIn(capacitance_1))
        self.wait()
        self.play(Transform(transform_mobs,c3.image),FadeIn(c_eff))
        self.wait()
        self.play(Write(c_eff_label))
        self.wait()
        self.play(FadeOut(parallel_stuff,transform_mobs))

         # series
        v1 = voltage.DCVoltage(bounding_rect=Rectangle(height=1,width=1))
        v1.elements.to_edge(DOWN).shift(UP)

        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))
        c1.elements.to_edge(UP).shift(DOWN+LEFT)

        c2 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))
        c2.elements.to_edge(UP).shift(DOWN+RIGHT)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+2*LEFT))
        w1.add_point(Point(c1.get_start_pos()+LEFT))
        w1.add_point(c1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(c1.get_end_point())
        w2.add_point(c2.get_start_point())

        w3 = wire.Wire()
        w3.add_point(c2.get_end_point())
        w3.add_point(Point(c2.get_end_pos()+RIGHT))
        w3.add_point(Point(v1.get_end_pos()+2*RIGHT))
        w3.add_point(v1.get_end_point())

        circuit3 = VGroup(v1.image,w1.image,c1.image,w2.image,c2.image,w3.image)
        circuit3.set_color_by_gradient(BLUE,GREEN)

        wide_cap = capacitor.Capacitor(bounding_rect=Rectangle(width=3,height=1))
        wide_cap.elements.shift(2*UP)
        
        circuit_series = VGroup(v1.image,w1.image,wide_cap.image,w3.image)
        circuit_series.set_color_by_gradient(BLUE,GREEN)


        transform_mobs2 = VGroup(c1.image,c2.image,w2.image)

        self.play(FadeIn(circuit3))
        self.wait()
        self.play(FadeIn(capacitance_1))
        self.wait()
        self.play(Transform(transform_mobs2,wide_cap.image))
        self.play(FadeIn(c_eff))
        self.wait()
        self.play(Write(c_eff_label2))
        self.wait()
        self.play(Transform(c_eff_label2,c_eff_label2_solve))
        self.wait()

class CapacitorEnergy(Scene):
    def construct(self):
        potential_eqn1 = MathTex("U","=",r"\int","V","dq").to_edge(UP)
        potential_eqn2 = MathTex("U","=",r"\int","_0","^{Q}","{q",r"\over","C}","dq").next_to(potential_eqn1,DOWN)
        potential_eqn3 = MathTex("U","=","{Q^2",r"\over","2","C}").next_to(potential_eqn2,DOWN)
        potential_eqn4 = MathTex("U","=",r"\frac{1}{2}","C","V^2").next_to(potential_eqn3,DOWN)

        field_energy1 = MathTex("U","=",r"\frac{1}{2}","(",r"{\epsilon_0","A",r"\over","d}",")","(","E","d",")^2").next_to(potential_eqn4,DOWN).shift(0.5*DOWN)
        field_energy2 = MathTex("U","=",r"\frac{1}{2}",r"\epsilon_0","E^2","(","A","d",")").next_to(field_energy1,DOWN)
        field_energy3 = MathTex("{U",r"\over","V}","=",r"\frac{1}{2}",r"\epsilon_0" ,"E^2").next_to(field_energy2,DOWN)

        cqv = MathTex("C","=","{q",r"\over","V}").to_edge(UR).shift(DL)
        cqv2 = MathTex("V","=","{q",r"\over","C}").next_to(cqv,DOWN)

        equations = [potential_eqn1,potential_eqn2,cqv,cqv2,potential_eqn3,potential_eqn4,field_energy1,field_energy2,field_energy3]
        for eqn in equations:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("Q",GREEN)
            eqn.set_color_by_tex("q",GREEN)
            eqn.set_color_by_tex("C",ORANGE)
            eqn.set_color_by_tex("A",GREEN)
            eqn.set_color_by_tex("d",RED)
            eqn.set_color_by_tex("E",RED)
        
        for i in range(7):
            self.play(Write(equations[i]))
            self.wait()
        
        self.play(*[FadeOut(equations[i]) for i in range(6)],field_energy1.animate.to_edge(UP))
        field_energy2.next_to(field_energy1,DOWN)
        field_energy3.next_to(field_energy2,DOWN)

        self.play(Write(field_energy2))
        self.wait()
        self.play(Write(field_energy3))
        self.wait()

class DielectricInsulator(Scene):
    def construct(self):
        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=8,height=4))
        plus_label = Tex(r"$+$").next_to(c1.image,UP).shift(2*LEFT)
        minus_label = Tex(r"$-$").next_to(c1.image,UP).shift(2*RIGHT)


        charges1 = []
        for i in range(5):
            for j in range(9):
                new_charge = charge.Charge(pos=[-1+i*0.5,2-0.5*j],
                                           charge=(i % 2)*2-1,
                                           radius=0.2)
                charges1.append(new_charge)
        
        charges2 = []
        for i in range(6):
            for j in range(11):
                new_charge = charge.Charge(pos=[-1+i*0.4,2-0.4*j],
                                           charge=(i % 2)*2-1,
                                           radius=0.2)
                charges2.append(new_charge)
        
        
        central_box = Rectangle(width=2,height=4,color=YELLOW,fill_opacity=0.6)
        zero = Tex(r"0").scale(3).set_color(BLUE)

        e_vectors = []
        short_e_vectors = []
        for i in range(5):
            new_vec = Vector(4*RIGHT) 
            new_vec.shift(2*UP+i*DOWN+2*LEFT)
            new_vec.set_color(YELLOW)
            e_vectors.append(new_vec)
        
            new_vec2 = Vector(3*RIGHT) 
            new_vec2.shift(2*UP+i*DOWN+1.5*LEFT)
            new_vec2.set_color(YELLOW)
            short_e_vectors.append(new_vec2) 
        
        return_e_vec = Vector(2*LEFT).next_to(c1.image,DOWN)

        c1_stuff = VGroup(*[c1.image for c1 in charges1],
                          *[c1.text for c1 in charges1])
        
        c2_stuff = VGroup(*[c2.image for c2 in charges2],
                          *[c2.text for c2 in charges2])

        vec_stuff = VGroup(*[vec for vec in e_vectors])

        vec2_stuff = VGroup(*[vec for vec in short_e_vectors])

        my_mobs = VGroup(c1_stuff,
                 vec_stuff,
                 plus_label,minus_label,c1.image)

        voltage_stuff = MathTex("|V|","=",r"\int",r"\vec{E}",r"\cdot",r"d\vec{l}")
        voltage_stuff.set_color_by_tex("V",BLUE_D)
        voltage_stuff.set_color_by_tex("E",BLUE_D)
        voltage_stuff.set_color_by_tex("l",RED)
        voltage_stuff.to_edge(UP).shift(DOWN) 

        cqv = MathTex("C","=","{Q",r"\over","V}").next_to(voltage_stuff,DOWN)
        cqv.set_color_by_tex("C",ORANGE)
        cqv.set_color_by_tex("Q",GREEN)
        cqv.set_color_by_tex("V",BLUE_D)

        e_to_kappa_thing = MathTex("E",r"\rightarrow",r"\kappa","E").next_to(cqv,DOWN)
        e_to_kappa_thing.set_color_by_tex("E",RED)

        eps_to_kappa_thing = MathTex(r"\epsilon_0",r"\rightarrow",r"\kappa",r"\epsilon_0")
        eps_to_kappa_thing.next_to(e_to_kappa_thing,DOWN)

        self.play(FadeIn(c1.image,plus_label,minus_label))
        self.wait()
        self.play(Write(c1_stuff))
        self.wait()
        self.play(Transform(c1_stuff,c2_stuff))
        self.wait()
        self.play(Write(vec_stuff))
        self.wait()
        self.play(Write(return_e_vec))
        self.wait()
        self.play(Transform(vec_stuff,vec2_stuff),FadeOut(return_e_vec))
        self.wait()
        self.play(FadeOut(my_mobs))
        self.wait()
        self.play(Write(voltage_stuff))
        self.play(Write(cqv))
        self.wait()
        self.play(Write(e_to_kappa_thing))
        self.play(Write(eps_to_kappa_thing))
        self.wait()

class ACSineWaves(Scene):
    def construct(self):
        plane = NumberPlane()
        ax = Axes()
        dc_graph = ax.plot(lambda t: 1).set_color(BLUE_D)
        ac_graph = ax.plot(lambda t: np.sin(t)).set_color(BLUE_D)
        scaled_ac_graph = ax.plot(lambda t: 2*np.sin(t)).set_color(BLUE_D)
        speed_ac_graph = ax.plot(lambda t: 3*np.sin(3*t)).set_color(BLUE_D)
        shift_ac_graph = ax.plot(lambda t: 3*np.sin(3*t+2)).set_color(BLUE_D)

        labels = ax.get_axis_labels(x_label='t',y_label='V')

        voltage_sine_wave = MathTex("V","=","sin(t)").to_edge(UR).shift(LEFT)
        vsin2 = MathTex("V","=","V_0","sin(t)").move_to(voltage_sine_wave)
        vsin3 = MathTex("V","=","V_0","sin(",r"\omega","t)").move_to(voltage_sine_wave)
        vsin4 = MathTex("V","=","V_0","sin(",r"\omega","t","+",r"\delta",")").move_to(voltage_sine_wave)
        
        graph_mobs = VGroup(ax,ac_graph,labels)

        ohm_law = MathTex("V","=","I","R").to_edge(UP).shift(0.5*DOWN)
        
        current_eqn = MathTex("I","=","{V",r"\over","R}","=","{V_0",r"\over","R}","sin(",r"\omega","t)").next_to(ohm_law,DOWN)

        wall_voltage = Tex(r"Wall Voltage: $100V - 300V$").next_to(current_eqn,DOWN)
        
        the_eqns = [voltage_sine_wave,vsin2,vsin3,vsin4,ohm_law,current_eqn]
        for eqn in the_eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("omega",GREEN)
            eqn.set_color_by_tex("delta",RED)
            eqn.set_color_by_tex("I",YELLOW_E)
            eqn.set_color_by_tex("R",RED)

        self.play(FadeIn(ax,labels,dc_graph))
        self.wait()
        self.play(FadeOut(dc_graph),Write(ac_graph))
        self.wait()
        self.play(Write(voltage_sine_wave))
        self.wait()
        self.play(Transform(voltage_sine_wave,vsin2),
                  Transform(ac_graph,scaled_ac_graph))
        self.wait()
        self.play(Transform(voltage_sine_wave,vsin3),
                  Transform(ac_graph,speed_ac_graph))
        self.wait()
        self.play(Transform(voltage_sine_wave,vsin4),
                  Transform(ac_graph,shift_ac_graph))
        self.wait()
        self.play(Transform(voltage_sine_wave,vsin3),
                  Transform(ac_graph,speed_ac_graph))
        self.wait()
        self.play(graph_mobs.animate.scale(0.5))
        self.play(graph_mobs.animate.to_edge(DOWN),voltage_sine_wave.animate.move_to(UP*3.5))
        self.wait()

        current_graph = ax.plot(lambda t: 1.5*np.sin(3*t)).set_color(YELLOW_E)

        self.play(Write(ohm_law))
        self.wait()
        self.play(Write(current_eqn),Write(current_graph))
        self.wait()
        self.play(Write(wall_voltage))
        self.wait()

class RMSVoltage(Scene):
    def construct(self):
        header = Text("Average").scale(2).to_edge(UP)

        ax = Axes().scale(0.66).to_edge(DOWN)
        voltage_graph = ax.plot(lambda t: 1.5*np.sin(t))
        voltage_square = ax.plot(lambda t: 1.5*np.sin(t)*1.5*np.sin(t))
        mean_square = ax.plot(lambda t: (1.5*1.5)/2).set_z_index(5)
        rms = ax.plot(lambda t: 1.5/np.sqrt(2) * 0.5).set_z_index(5) # multiplying by 0.5 is a technical lie but it makes the animation visible

        voltage_graph_riemann = ax.get_riemann_rectangles(voltage_graph,dx=0.01).set_color_by_gradient(BLUE,GREEN).set_opacity(0.5)
        voltage_square_riemann = ax.get_riemann_rectangles(voltage_square,dx=0.01).set_color_by_gradient(PINK,ORANGE).set_opacity(0.5)

        labels = ax.get_axis_labels(x_label='t',y_label='V')

        used_graph = voltage_graph.copy()

        rms_tex = Tex(r"Root Mean Square: $\sqrt{(I^2)_{\text{avg}}}$").scale(0.75).to_edge(UP)
        also_called_rms = Text("(Also called rms)").scale(0.33).next_to(rms_tex,DOWN)
        ohm_law_rms = MathTex(r"V_{\text{rms}}","=",r"I_{\text{rms}}","R").scale(0.75).next_to(also_called_rms,DOWN)
        ohm_law_rms.set_color_by_tex("V",BLUE_D)
        ohm_law_rms.set_color_by_tex("I",YELLOW_E)
        ohm_law_rms.set_color_by_tex("R",RED)

        piv_rms = MathTex(r"P_{\text{rms}}","=",r"I_{\text{rms}}",r"V_{\text{rms}}").scale(0.75).next_to(ohm_law_rms,DOWN)
        piv_rms.set_color_by_tex("P",PURPLE)
        piv_rms.set_color_by_tex("I",YELLOW_E)
        piv_rms.set_color_by_tex("V",BLUE_D)

        self.play(Write(header),Write(ax),Write(labels),Write(used_graph),FadeIn(voltage_graph_riemann))
        self.wait()
        self.play(Transform(used_graph,voltage_square),FadeOut(voltage_graph_riemann),FadeIn(voltage_square_riemann))
        self.wait()
        self.play(Write(mean_square))
        self.wait()
        self.play(Transform(mean_square,rms),Transform(used_graph,voltage_graph),FadeOut(voltage_square_riemann),FadeIn(voltage_graph_riemann))
        self.wait()
        self.play(FadeOut(header),Write(rms_tex))
        self.wait()
        self.play(FadeIn(also_called_rms))
        self.wait()
        self.play(FadeIn(ohm_law_rms))
        self.wait()
        self.play(FadeIn(piv_rms))
        self.wait()

class ACCapacitor(Scene):
    def construct(self):
        v1 = voltage.ACVoltage()
        v1.elements.to_edge(DOWN).shift(UP)
        v1_label = Text("AC Voltage").next_to(v1.image,DOWN)

        c1 = capacitor.Capacitor(bounding_rect=Rectangle(width=1,height=1))
        c1.elements.to_edge(UP).shift(DOWN)

        w1 = wire.Wire()
        w1.add_point(v1.get_start_point())
        w1.add_point(Point(v1.get_start_pos()+LEFT))
        w1.add_point(Point(c1.get_start_pos()+LEFT))
        w1.add_point(c1.get_start_point())

        w2 = wire.Wire()
        w2.add_point(c1.get_end_point())
        w2.add_point(Point(c1.get_end_pos()+RIGHT))
        w2.add_point(Point(v1.get_end_pos()+RIGHT))
        w2.add_point(v1.get_end_point())

        circuit = VGroup(v1.image,w1.image,c1.image,w2.image)
        circuit.set_color_by_gradient(BLUE,GREEN)
        V_label = Tex("V").move_to(v1_label).set_color(BLUE_D)

        

        self.play(Write(v1.image),Write(v1_label))
        self.wait()
        self.play(Write(VGroup(w1.image,c1.image,w2.image)))
        self.wait()
        self.play(Transform(v1_label,V_label))
        self.wait()
        self.play(circuit.animate.shift(3*LEFT),
                  v1_label.animate.shift(3*LEFT))
        self.wait()

        charges1 = []
        charges2 = []
        for i in range(10):
            new_charge1 = charge.Charge(radius=0.25)
            new_charge1.elements.move_to(v1.get_start_pos()).shift(3*LEFT)
            charges1.append(new_charge1)

            new_charge2 = charge.Charge(radius=0.25)
            new_charge2.elements.move_to(c1.get_end_pos()).shift(3*LEFT)
            charges2.append(new_charge2)
        
        path1 = VGroup().set_points_as_corners([v1.get_start_pos()+3*LEFT,w1.points[1].get_center()+3*LEFT,
                                                w1.points[2].get_center()+3*LEFT,w1.points[3].get_center()+3*LEFT])

        path2 = VGroup().set_points_as_corners([c1.get_end_pos()+3*LEFT,w2.points[1].get_center()+3*LEFT,
                                                w2.points[2].get_center()+3*LEFT,w2.points[3].get_center()+3*LEFT])
        path3 = path2.copy().reverse_direction()
        path4 = path1.copy().reverse_direction()

        path1_shortened = VGroup().set_points_as_corners([v1.get_start_pos()+3*LEFT,w1.points[1].get_center()+3*LEFT,
                                                w1.points[2].get_center()+3*LEFT+2*DOWN])
        # path2_shortened = VGroup().set_points_as_corners([c1.get_end_pos()+3*LEFT,w2.points[1].get_center()+3*LEFT,
        #                                         w2.points[2].get_center()+3*LEFT+2*UP])
        # path3_shortened = path2_shortened.copy().reverse_direction()
        path4_shortened = path1_shortened.copy().reverse_direction()

        opposition_frequency = MathTex(r"\text{Opposition}",r"\propto","{1",r"\over",r"\omega}").scale(0.75).shift(3*UP+3*RIGHT)
        opposition_capacitance = MathTex(r"\text{Opposition}",r"\propto","{1",r"\over",r"C}").shift(2*UP+3*RIGHT).scale(0.75).next_to(opposition_frequency,DOWN)
        opposition_frequency.set_color_by_tex("omega",GREEN)
        opposition_capacitance.set_color_by_tex("C",ORANGE)

        voltage_sol1 = MathTex("C","=","{Q",r'\over','V}',r'\Rightarrow','Q','=','V','C').scale(0.75).next_to(opposition_capacitance,DOWN)
        voltage_sol2 = MathTex('Q','=','V_0','C',r'sin(',r'\omega','t)').scale(0.75).next_to(voltage_sol1,DOWN)
        voltage_sol3 = MathTex('I','=','V_0','C',r'\omega',r'cos(',r'\omega','t)').scale(0.75).next_to(voltage_sol2,DOWN)
        voltage_sol4 = MathTex('I_0','=','V_0','C',r'\omega').scale(0.75).next_to(voltage_sol3,DOWN)
        voltage_sol5 = MathTex('V_0','=','I_0','({1',r'\over',r'\omega','C','})').scale(0.75).next_to(voltage_sol4,DOWN)

        vir_sols = [voltage_sol1,voltage_sol2,voltage_sol3,voltage_sol4,voltage_sol5]
        for sol in vir_sols:
            sol.set_color_by_tex("V",BLUE_D)
            sol.set_color_by_tex("Q",GREEN)
            sol.set_color_by_tex("omega",GREEN)
            sol.set_color_by_tex("C",ORANGE)
            sol.set_color_by_tex("I",YELLOW_E)

        self.play(LaggedStart(AnimationGroup(*[MoveAlongPath(c1.elements,path1) for c1 in charges1],
                                             lag_ratio=0.2),
                              AnimationGroup(*[MoveAlongPath(c2.elements,path2) for c2 in charges2],
                                             lag_ratio=0.2),
                              lag_ratio=0.2))
        self.wait()
        self.play(LaggedStart(AnimationGroup(*[MoveAlongPath(c2.elements,path3) for c2 in charges2],
                                    lag_ratio=0.2),
                              AnimationGroup(*[MoveAlongPath(c1.elements,path4) for c1 in charges1],
                                             lag_ratio=0.2),
                              lag_ratio=0.2))
        self.wait()
        self.play(*[FadeOut(c2.elements) for c2 in charges2])

        self.play(AnimationGroup(*[MoveAlongPath(c1.elements,path1_shortened) for c1 in charges1],
                                             lag_ratio=0.2))
        self.wait()
        self.play(AnimationGroup(*[MoveAlongPath(c1.elements,path4_shortened) for c1 in charges1],
                                    lag_ratio=0.2))
        self.wait()
        self.play(*[FadeOut(c1.elements) for c1 in charges1])
        self.wait()
        self.play(Write(opposition_frequency))
        self.wait()
        self.play(Write(opposition_capacitance))
        self.wait()
        self.play(*[Write(sol) for sol in vir_sols])
        self.wait()

class CapacitorLeadsVoltage(Scene):
    def construct(self):
        true_axes = Axes(
            x_range=[-2.5,10],
            y_range=[-3,3],
            tips=True,
            axis_config={"include_ticks": False}
        )
        true_axes.shift(4*LEFT - true_axes.get_origin())
        axes_origin = true_axes.get_origin()

        I_0_tick = Line(start=axes_origin+2*UP+0.25*LEFT,end=axes_origin+2*UP+0.25*RIGHT)
        I_0_tick_label = Tex(r"$I_0$").next_to(I_0_tick,LEFT).set_color(ORANGE)

        I_0_tick_and_label_down = VGroup(I_0_tick,I_0_tick_label).copy().shift(4*DOWN)

        V_0_tick = Line(start=axes_origin+1.5*UP+0.25*LEFT,end=axes_origin+1.5*UP+0.25*RIGHT)
        V_0_tick_label = Tex(r"$V_0$").next_to(V_0_tick,LEFT).set_color(BLUE)

        V_0_tick_and_label_down = VGroup(V_0_tick,V_0_tick_label).copy().shift(3*DOWN)

        voltage_graph = true_axes.plot(lambda t: 1.5*np.sin(t),color=BLUE,
                                      x_range=[0,3*PI])
        capacitor_graph = true_axes.plot(lambda t: 2*np.cos(t),color=ORANGE,
                                      x_range=[0,3*PI])

        max_q_riemann = true_axes.get_riemann_rectangles(capacitor_graph,
                                                         x_range=[0,PI/2],
                                                         dx=0.01).set_color_by_gradient(BLUE,GREEN).set_z_index(-1)
        cancel_q_riemann = true_axes.get_riemann_rectangles(capacitor_graph,
                                                         x_range=[0,PI],
                                                         dx=0.01).set_color_by_gradient(BLUE,GREEN).set_z_index(-1)

        self.play(Write(true_axes))
        self.play(Write(voltage_graph),Write(capacitor_graph),run_time=2)
        self.play(Write(V_0_tick),Write(V_0_tick_label),Write(I_0_tick),Write(I_0_tick_label),
                  Write(I_0_tick_and_label_down),Write(V_0_tick_and_label_down))
        self.wait()
        self.play(Write(max_q_riemann))
        self.wait()
        self.play(FadeOut(max_q_riemann))
        self.wait()
        self.play(Write(cancel_q_riemann))
        self.wait()
        self.play(FadeOut(cancel_q_riemann))
        self.wait()

class UnitCircleSineWave(Scene):
    def construct(self):
        x_begin = 6.5*LEFT
        x_end = 6.5*RIGHT
        
        y_begin = 4*LEFT+3*DOWN
        y_end = 4*LEFT+3*UP

        x_axis = Arrow(start=x_begin,end=x_end)
        y_axis = Arrow(start=y_begin,end=y_end)

        axes_origin = 4*LEFT

        ax = VGroup(x_axis,y_axis)

        circ_radius = 2
        unit_circle = Circle(color=RED,radius=circ_radius).move_to(axes_origin).set_x_index(3)

        omega_speed_change=2

        time = ValueTracker(0)
        circle_dot = Dot(color=YELLOW,radius=0.1).set_z_index(5).shift(LEFT)
        circle_dot.add_updater(lambda mobject: mobject.move_to(axes_origin+
                                                               RIGHT*circ_radius*np.cos(omega_speed_change*time.get_value())
                                                               +UP*circ_radius*np.sin(omega_speed_change*time.get_value())))
            

        radius_line = Line(start=axes_origin,end=circle_dot.get_center()).set_z_index(4).set_color(BLUE)
        radius_line.add_updater(lambda mobject: mobject.put_start_and_end_on(axes_origin,circle_dot.get_center()))

        def sine_function(t):
            return circ_radius*np.sin(omega_speed_change*t)

        sine_graph = always_redraw(lambda: FunctionGraph(sine_function,x_range=[0,time.get_value()]).shift(axes_origin+RIGHT*circ_radius))

        secondary_line = Line(start=circle_dot.get_center(),end=axes_origin+circ_radius*RIGHT+time.get_value()*RIGHT+sine_function(time.get_value())*UP).set_z_index(4).set_color(YELLOW_E)
        # tiny shift right to avoid a zero-length line
        secondary_line.add_updater(lambda mobject: mobject.put_start_and_end_on(start=circle_dot.get_center(),end=axes_origin+circ_radius*RIGHT+time.get_value()*RIGHT+sine_function(time.get_value())*UP+0.01*RIGHT))


        final_time_value = TAU
        self.play(Write(ax))
        self.wait()
        self.play(Write(unit_circle))
        self.wait()
        self.play(FadeIn(circle_dot,radius_line,sine_graph,secondary_line))
        self.wait()
        self.play(time.animate.set_value(final_time_value),run_time=5,rate_func=linear)
        self.wait()

class PhasorDiagram(Scene):
    def construct(self):
        main_circle = Circle(color=GREEN,radius=3)
        y_axis = Vector(7.5*UP).shift((7.5/2)*DOWN)
        x_axis = Vector(8*RIGHT).shift(4*LEFT)
        y_axis_label = Tex("$V$").next_to(y_axis,RIGHT).shift((7/2)*UP)

        time = ValueTracker(PI/4)
        phasor_radii = 2
        v_phasor = Vector(phasor_radii*np.cos(time.get_value())*RIGHT+phasor_radii*np.sin(time.get_value())*UP).set_color(BLUE)
        v_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()))

        c_phasor = Vector(-phasor_radii*np.sin(time.get_value())*RIGHT+phasor_radii*np.cos(time.get_value())*UP).set_color(ORANGE)
        c_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()+PI/2))

        theta_arc = always_redraw(lambda: Arc(radius=0.5,start_angle=0,angle=time.get_value()) )
        theta_label = Tex(r"$\omega$","$t$").next_to(theta_arc,RIGHT).shift(0.25*UP)
        theta_label.set_color_by_tex("omega",GREEN)

        v_label = Tex(r"$V_0$").next_to(v_phasor.get_end(),UR).set_color(BLUE_D)
        v_label.add_updater(lambda mobject: mobject.next_to(v_phasor.get_end(),UR))

        c_label = Tex(r"$I_0$").next_to(c_phasor.get_end(),UR).set_color(ORANGE)
        c_label.add_updater(lambda mobject: mobject.next_to(c_phasor.get_end(),UR))

        x_label = Tex(r"$X$").next_to(c_phasor.get_end(),UR).set_color(ORANGE)
        x_label.add_updater(lambda mobject: mobject.next_to(c_phasor.get_end(),UR))

        voltage_height_line = Line().set_color(BLUE)
        voltage_height_line.add_updater(lambda mobject: mobject.put_start_and_end_on(v_phasor.get_end(),v_phasor.get_end()[1]*UP))

        vertical_voltage_height = Line().set_color(BLUE)
        vertical_voltage_height.add_updater(lambda mobject: mobject.put_start_and_end_on(v_phasor.get_end()[0]*RIGHT,v_phasor.get_end()))

        voltage_opp_label = Tex(r"$V$").next_to(vertical_voltage_height,RIGHT).set_color(BLUE).set_z_index(5)
        voltage_opp_label.add_updater(lambda mobject: mobject.next_to(vertical_voltage_height,RIGHT))

        c_height_line = Line().set_color(ORANGE)
        c_height_line.add_updater(lambda mobject: mobject.put_start_and_end_on(c_phasor.get_end(),c_phasor.get_end()[1]*UP))

        v_eqn_label = MathTex("V_0",r"\sin(",r"\omega","t)")
        v_eqn_label.set_color_by_tex("V_0",BLUE_D) 
        v_eqn_label.set_color_by_tex("omega",GREEN) 
        v_eqn_label.add_updater(lambda mobject: mobject.next_to(voltage_height_line.get_end(),UL))

        sine_definition = MathTex("sin(",r"\omega","t)","=",r"{\text{opp}",r"\over",r"\text{hyp}}").to_edge(UR).shift(DOWN)
        sine_eqn1 = MathTex("sin(",r"\omega","t)","=","{V",r"\over","V_0}").next_to(sine_definition,DOWN)
        sine_eqn2 = MathTex("V_0","sin(",r"\omega","t)","=","V").next_to(sine_eqn1,DOWN).shift(0.5*DOWN)

        r_phasor = Vector((phasor_radii/1.5)*np.cos(time.get_value())*RIGHT+(phasor_radii/1.5)*np.sin(time.get_value())*UP).set_color(RED)
        r_phasor.add_updater(lambda mobject: mobject.set_angle(time.get_value()))

        r_height_line = Line().set_color(ORANGE)
        r_height_line.add_updater(lambda mobject: mobject.put_start_and_end_on(r_phasor.get_end(),r_phasor.get_end()[1]*UP))

        r_label = Tex(r"$R$").next_to(r_phasor.get_end(),UR).set_color(RED)
        r_label.add_updater(lambda mobject: mobject.next_to(r_phasor.get_end(),UR))

        impedance_phasor = Vector((phasor_radii/1.5)*RIGHT+phasor_radii*UP).set_color(YELLOW_A)
        impedance_phasor.add_updater(lambda mobject: mobject.set_angle(np.arctan2(c_phasor.get_y()+r_phasor.get_y(),c_phasor.get_x()+r_phasor.get_x())))

        z_label = Tex(r"$Z$").next_to(impedance_phasor.get_end(),UR).set_color(YELLOW_A)
        z_label.add_updater(lambda mobject: mobject.next_to(impedance_phasor.get_end(),UR).shift(0.25*DL))

        sine_eqns = [sine_eqn1,sine_eqn2,sine_definition]
        for eqn in sine_eqns:
            eqn.set_color_by_tex("V",BLUE_D)
            eqn.set_color_by_tex("omega",GREEN)

        impedance_eqn = MathTex("Z","=",r"\sqrt{","X^2","+","R^2","}").to_edge(UR).shift(DOWN)
        impedance_eqn.set_color_by_tex("Z",YELLOW_A)
        impedance_eqn.set_color_by_tex("X",ORANGE)
        impedance_eqn.set_color_by_tex("R",RED)

        impedance_header = Text("Impedance").to_edge(UR)

        ohm_law_ac = MathTex(r"V_{\text{rms}}","=",r"I_{\text{rms}}","Z").next_to(impedance_eqn,DOWN)
        ohm_law_ac.set_color_by_tex("V",BLUE_D)
        ohm_law_ac.set_color_by_tex("I",YELLOW_E)
        ohm_law_ac.set_color_by_tex("Z",YELLOW_A)

        self.play(FadeIn(x_axis,y_axis,y_axis_label,main_circle,v_phasor,theta_arc,theta_label,v_label,v_label))
        self.wait()
        self.play(FadeIn(voltage_height_line,vertical_voltage_height,voltage_opp_label))
        self.wait()
        self.play(time.animate.set_value(PI/2))
        self.wait()
        self.play(time.animate.set_value(0))
        self.wait()
        self.play(time.animate.set_value(PI/4))
        self.wait()
        self.play(Write(sine_definition))
        self.wait()
        self.play(Write(sine_eqn1))
        self.wait()
        self.play(Write(sine_eqn2))
        self.wait()
        self.play(FadeIn(v_eqn_label))
        self.wait()
        self.play(FadeOut(voltage_opp_label,vertical_voltage_height))
        self.wait()
        self.play(time.animate.set_value(2*PI),run_time=2)
        self.play(FadeOut(theta_arc,theta_label,v_eqn_label,sine_eqn1,sine_eqn2,sine_definition),FadeIn(c_phasor,c_label,c_height_line))
        self.wait()
        self.play(time.animate.set_value(4*PI),run_time=2)
        self.wait()
        self.play(FadeOut(v_phasor,voltage_height_line,v_label,c_label),FadeIn(x_label,r_phasor,r_label,r_height_line))
        self.wait()
        self.play(FadeIn(impedance_phasor,z_label),FadeOut(c_height_line,r_height_line))
        self.wait()
        self.play(FadeIn(impedance_header))
        self.wait()
        self.play(time.animate.set_value(6*PI),run_time=2)
        self.wait()

        c_phasor2 = c_phasor.copy()

        self.play(c_phasor2.animate.shift((phasor_radii/1.5)*RIGHT))
        self.wait()
        self.play(Write(impedance_eqn))
        self.wait()
        self.play(Write(ohm_law_ac))
        self.wait()
        self.play(FadeOut(c_phasor2))
        self.wait()

class ReactanceXEquals(Scene):
    def construct(self):
        equation = MathTex("X","=","{1",r"\over",r"\omega","C}")
        equation.set_color_by_tex("omega",GREEN)
        equation.set_color_by_tex("C",ORANGE)

        self.play(Write(equation))
        self.play(FadeOut(equation))

class ReactanceSineWave(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2.5,10],
            y_range=[-3,3],
            tips=True,
            axis_config={"include_ticks": False}
        )
        ax.shift(4*LEFT - ax.get_origin())
        axes_origin = ax.get_origin()

        sine_v = ax.plot(lambda t: 2*np.sin(t)).set_color(BLUE)
        sine_i = ax.plot(lambda t: 0.75*np.sin(t-1)).set_color(YELLOW_A)

        v_label = Text("V").set_color(BLUE).move_to(axes_origin).shift(2*UP+0.5*LEFT)
        i_label = Text("I").set_color(YELLOW_A).move_to(axes_origin).shift(0.5*UP+0.5*LEFT)

        self.play(Write(ax))
        self.wait()
        self.play(Write(sine_v),Write(v_label))
        self.wait()
        self.play(Write(sine_i),Write(i_label))
        self.wait()
