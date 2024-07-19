import random
import numpy as np
from manim import *
import charge

base_charge = 100*(10**(-12))
eps_0 = 8.85*10**(-12)
k_const = 1/(4*PI*eps_0)

def set_math_colors(*mobjects : MathTex):
    for mobject in mobjects:
        mobject.set_color_by_tex("{A}",GREEN)
        mobject.set_color_by_tex(r"d\vec{A}",GREEN_E)
        mobject.set_color_by_tex("dA",GREEN_E)
        mobject.set_color_by_tex("Delta", BLUE)
        mobject.set_color_by_tex("{E}", RED)
        mobject.set_color_by_tex("{q}", GREEN_B)
        mobject.set_color_by_tex("m_1", GREEN_B)
        mobject.set_color_by_tex("m_2", BLUE_B)
        mobject.set_color_by_tex("n",LIGHT_GRAY)
        mobject.set_color_by_tex("phi", BLUE_D)
        mobject.set_color_by_tex("q_1", GREEN_B)
        mobject.set_color_by_tex("q_2", BLUE_B)
        mobject.set_color_by_tex("{r}", RED)
        mobject.set_color_by_tex("r^2", RED_B)
        mobject.set_color_by_tex(r"\hat{r}", RED_C)

class AtomLabels(Scene):
    def construct(self):
        atom_label = Text("Atom")
        proton_label = Text("Proton (+)")
        neutron_label = Text("Neutron (N)")
        electron_label = Text("Electron (-)")

        labels = VGroup(atom_label,proton_label,neutron_label,electron_label)
        labels.scale(2)
        labels.to_edge(UP)

        self.play(Write(atom_label))
        self.wait()

        self.play(FadeOut(atom_label),run_time=0.5)
        self.play(FadeIn(proton_label),run_time=0.5)
        self.wait()
        
        self.play(FadeOut(proton_label),run_time=0.5)
        self.play(FadeIn(neutron_label),runt_time=0.5)
        self.wait()
        
        self.play(FadeOut(neutron_label),run_time=0.5)
        self.play(FadeIn(electron_label),run_time=0.5)
        self.wait()

# this code is garbage, but it works

class CoulombLaw(Scene):
    def construct(self):
        q1_propto = MathTex("{F}", r"\propto", "{q}_1")
        q2_propto = MathTex("{F}", r"\propto", "{q}_2")
        original_q1_propto = MathTex("{F}", r"\propto", "{q}_1")
        original_q2_propto = MathTex("{F}", r"\propto", "{q}_2")
        r2_propto = MathTex("{F}", r"\propto", "{1", r"\over", r"r^2}")

        set_math_colors(q1_propto,q2_propto,original_q1_propto,original_q2_propto,r2_propto)

        doubled_q1 = MathTex("2","{F}", r"\propto", "2{q}_1")
        doubled_q2 = MathTex("2","{F}", r"\propto", "2{q}_2")
        tripled_q2 = MathTex("3","{F}", r"\propto", "3{q}_2")
        ten_r2 = MathTex(r"\frac{1}{4}","{F}", r"\propto", "{1", r"\over", r"(2{r})^2}")
        hundred_r2 = MathTex(r"\frac{1}{100}","{F}", r"\propto", "{1", r"\over", r"(10{r})^2}")

        set_math_colors(doubled_q1,doubled_q2,tripled_q2)
        ten_r2.set_color_by_tex("2r", RED_B)
        hundred_r2.set_color_by_tex("10r", RED_B)

        q1_propto.scale(1.5)
        q2_propto.scale(1.5)
        original_q1_propto.scale(1.5)
        original_q2_propto.scale(1.5)
        r2_propto.scale(1.5)
        doubled_q1.scale(1.5)
        doubled_q2.scale(1.5)
        tripled_q2.scale(1.5)
        ten_r2.scale(1.5)
        hundred_r2.scale(1.5)
        
        q1_propto.next_to(q2_propto, UP)
        original_q1_propto.next_to(q2_propto, UP)
        r2_propto.next_to(q2_propto, DOWN)
        doubled_q1.next_to(q2_propto, UP)
        ten_r2.next_to(q2_propto, DOWN)
        hundred_r2.next_to(q2_propto, DOWN)

        proportions = VGroup(q1_propto, q2_propto, r2_propto)

        coulomb_law = MathTex(r"{F}", "=", "{k", "{q}_1", "{q}_2", r"\over", "r^2}")
        set_math_colors(coulomb_law)
        coulomb_law.scale(2)

        self.play(Write(q1_propto), Write(q2_propto), run_time=3)
        self.wait()
        self.play(Transform(q1_propto,doubled_q1), run_time=2)
        self.wait()
        self.play(Transform(q2_propto,doubled_q2), run_time=2)
        self.wait()
        self.play(Transform(q2_propto,tripled_q2), run_time=2)
        self.wait()

        self.play(Write(r2_propto), Transform(q1_propto, original_q1_propto), Transform(q2_propto, original_q2_propto), run_time=2)
        self.wait()
        self.play(Transform(r2_propto, ten_r2), run_time=2)
        self.wait()
        self.play(Transform(r2_propto, hundred_r2), run_time=2)
        self.wait()

        self.play(Transform(proportions, coulomb_law), run_time=2)
        self.wait()

        coulomb_header = Text(r"Coulomb's Law")
        coulomb_header.scale(2)
        coulomb_header.to_edge(UP)

        k_constant = Tex(r"$k = 8.99 \times 10^9$")
        k_constant.scale(1.5)
        k_constant.to_edge(DOWN)

        self.play(FadeIn(coulomb_header), FadeIn(k_constant), run_time=2)

        self.wait()

        coulomb_group = VGroup(coulomb_law, coulomb_header, k_constant, proportions)
        
        self.play(coulomb_group.animate.scale(0.6), run_time=1)
        self.play(coulomb_group.animate.to_edge(LEFT), run_time=1)

        gravity_law = MathTex(r"{F}", "=", "{G", "m_1", "m_2", r"\over", "r^2}")
        set_math_colors(gravity_law)
        gravity_law.scale(2)

        gravity_header = Text("Newton's Law of Gravitation")
        gravity_header.to_edge(UP)
        gravity_header.shift(DOWN*0.5)

        G_constant = Tex(r"$G = 6.67 \times 10^{-11}$")
        G_constant.scale(1.5)
        G_constant.to_edge(DOWN)

        gravity_group = VGroup(gravity_header, gravity_law, G_constant)
        gravity_group.scale(0.7)
        gravity_group.to_edge(RIGHT)

        divider = Line(start=3*UP, end=3*DOWN)

        self.play(FadeIn(gravity_group), FadeIn(divider), run_time=2)
        self.wait()

        k_box = SurroundingRectangle(k_constant, color=BLUE)
        G_box = SurroundingRectangle(G_constant, color=GREEN)

        self.play(Write(k_box), Write(G_box), run_time=2)

        self.play(coulomb_group.animate.shift(UP), divider.animate.shift(0.5*UP),
                   gravity_group.animate.shift(UP), FadeOut(k_box), FadeOut(G_box), run_time=1)

        difference = Tex(r"$\frac{k}{G} = 134,782,608,695,652,173,913$")
        difference.to_edge(DOWN)

        self.play(FadeIn(difference), run_time=2)

        self.wait()


class CoulombLawChargeDiagrams(Scene):
    def construct(self):
        CHARGE_RADIUS = 0.75

        charge1 = Circle(radius=CHARGE_RADIUS,color=WHITE)
        charge1.to_edge(UP).shift(LEFT*3)
        charge1.set_color(GREEN_B)

        charge2 = Circle(radius=CHARGE_RADIUS,color=WHITE)
        charge2.to_edge(UP).shift(RIGHT*3)
        charge2.set_color(BLUE_B)

        q1_label = Tex(r"$q_1$").move_to(charge1)
        q2_label = Tex(r"$q_2$").move_to(charge2)

        q1_arrow = Vector(RIGHT).move_to(charge1).shift(RIGHT*(1/2+CHARGE_RADIUS/2))
        q1_arrow.set_color(YELLOW)
        q1_original = q1_arrow.copy()

        q2_arrow = Vector(LEFT).move_to(charge2).shift(LEFT*(1/2+CHARGE_RADIUS/2))
        q2_arrow.set_color(YELLOW)
        q2_original = q2_arrow.copy()

        self.play(Write(charge1), Write(charge2))
        self.wait()
        self.play(FadeIn(q1_label,q2_label))
        self.wait()
        self.play(GrowArrow(q1_arrow), GrowArrow(q2_arrow))
        self.wait()
        
        q1_longer = Vector(1.5*RIGHT).move_to(charge1).shift(RIGHT*(1.5/2+CHARGE_RADIUS/2))
        q1_longer.set_color(YELLOW)

        q2_longer = Vector(1.5*LEFT).move_to(charge2).shift(LEFT*(1.5/2+CHARGE_RADIUS/2))
        q2_longer.set_color(YELLOW)
        
        self.play(Transform(q1_arrow, q1_longer), Transform(q2_arrow, q2_longer))
        self.wait()

        q1_longest = Vector(2*RIGHT).move_to(charge1).shift(RIGHT*(2/2+CHARGE_RADIUS/2))
        q1_longest.set_color(YELLOW)

        q2_longest = Vector(2*LEFT).move_to(charge2).shift(LEFT*(2/2+CHARGE_RADIUS/2))
        q2_longest.set_color(YELLOW)
        
        self.play(Transform(q1_arrow, q1_longest), Transform(q2_arrow, q2_longest))
        self.wait()

        radius_line = NumberLine(x_range=[0,1],length=6).move_to(charge1).shift(RIGHT*3).shift(DOWN*CHARGE_RADIUS)
        radius_label = Tex(r"$r$").next_to(radius_line, UP)

        self.play(Transform(q1_arrow,q1_original), Transform(q2_arrow,q2_original), FadeIn(radius_line,radius_label))
        self.wait()

        q1_shorter = Vector(0.75*RIGHT).move_to(charge1).shift(RIGHT*(0.75/2+CHARGE_RADIUS/2))
        q1_shorter.set_color(YELLOW)

        q2_shorter = Vector(0.75*LEFT).move_to(charge2).shift(LEFT*(0.75/2+CHARGE_RADIUS/2))
        q2_shorter.set_color(YELLOW)

        self.play(Transform(q1_arrow, q1_shorter), Transform(q2_arrow, q2_shorter))
        self.wait()

        q1_shortest = Vector(0.5*RIGHT).move_to(charge1).shift(RIGHT*(0.5/2+CHARGE_RADIUS/2))
        q1_shortest.set_color(YELLOW)

        q2_shortest = Vector(0.5*LEFT).move_to(charge2).shift(LEFT*(0.5/2+CHARGE_RADIUS/2))
        q2_shortest.set_color(YELLOW)

        self.play(Transform(q1_arrow, q1_shortest), Transform(q2_arrow, q2_shortest))
        self.wait()

        scene_elements = VGroup(charge1,charge2,q1_label,q2_label,q1_arrow,q2_arrow,radius_line,radius_label)

        self.play(FadeOut(scene_elements))
        self.wait()


class ElectricField(Scene):
    def construct(self):

        # Proton
        charges = []
        charges.append(charge.Charge(np.array([0,0]),10*base_charge,radius=0.5))
        
        for c in charges:
            c.image.set_z_index(5)
            c.text.set_z_index(5)
            self.play(DrawBorderThenFill(c.image), FadeIn(c.text), run_time=2)

        def get_electric_fields(pos):
            field = RIGHT*0
            for c in charges:
                field += c.get_electric_field(pos)
            
            return field

        vector_field = ArrowVectorField(get_electric_fields)
        vector_field.set_opacity(0.8)

        self.wait()

        single_vector = Vector(get_electric_fields(RIGHT+UP)*(1/8))
        single_vector.shift(RIGHT+UP)
        single_vector.set_color(RED)

        vector_point = Circle((1/16))
        vector_point.set_color(WHITE)
        vector_point.shift(RIGHT+UP)

        self.play(Write(vector_point), run_time=2)

        self.wait()

        # coulomb"s law
        coulomb_label = MathTex("{F}", "=", r"\displaystyle", r"{k", "{q}_1", "{q}_2", r"\over", "r^2}").to_edge(UP).shift(DOWN).set_z_index(10)
        set_math_colors(coulomb_label)
        self.play(FadeIn(coulomb_label), run_time=1)
        self.wait()

        # show r vector

        r_vector = Vector(RIGHT*(1/np.sqrt(2))+UP*(1/np.sqrt(2))).set_z_index(10).set_color(BLUE)
        original_r_vector = r_vector.copy().shift(UP+RIGHT)
        r_label = Tex(r"$\hat{r}$").next_to(r_vector, RIGHT).set_z_index(10).set_color(RED_C)

        self.play(GrowArrow(r_vector), run_time=1)
        self.play(FadeOut(original_r_vector), run_time=0)
        self.remove(original_r_vector)
        self.wait()
        self.play(FadeIn(r_label),run_time=1)
        self.play(r_vector.animate.shift(UP+RIGHT), r_label.animate.shift(UP+RIGHT), run_time=1)
        self.wait()

        negative_coulomb_label = MathTex("{{F}", "=", r"\displaystyle",  "{k", "{q}_1", "(-{q}_2)", r"\over", "r^2}").to_edge(UP).shift(DOWN).set_z_index(10)
        set_math_colors(negative_coulomb_label)
        
        positive_coulomb_label = MathTex("{F}", "=", r"\displaystyle",  "{k", "{q}_1", "{q}_2", r"\over", "r^2}").to_edge(UP).shift(DOWN).set_z_index(10)
        set_math_colors(positive_coulomb_label)
        
        reversed_r_vector = Vector(LEFT*(1/np.sqrt(2))+DOWN*(1/np.sqrt(2))).shift(UP+RIGHT).set_color(BLUE)

        self.play(Transform(coulomb_label, negative_coulomb_label),run_time=1)
        self.wait() 
        self.play(Transform(r_vector,reversed_r_vector),run_time=1)
        self.wait()
        self.play(Transform(r_vector, original_r_vector), Transform(coulomb_label, positive_coulomb_label))

        # introduce e field

        vector_coulomb_label = MathTex("{F}", "=", r"\displaystyle", r"{k", "{q}_1", "{q}_2", r"\over", "r^2}", r"\hat{r}").to_edge(UP).shift(DOWN)
        set_math_colors(vector_coulomb_label)

        self.play(Transform(coulomb_label, vector_coulomb_label),run_time=1)

        self.wait()
        
        vector_coulomb_label_set = MathTex("{F}", "=", r"\displaystyle", r"{k", "{q}_1", "(1)", r"\over", "r^2}", r"\hat{r}").to_edge(UP).shift(DOWN)
        set_math_colors(vector_coulomb_label)

        self.play(Transform(coulomb_label, vector_coulomb_label_set),run_time=1)

        self.wait()

        e_field_header = Text(r"Electric Field").scale(1.5).to_edge(UP).set_z_index(10)
        
        self.play(FadeIn(e_field_header))

        e_field = MathTex(r"\vec{E}", "=", r"\displaystyle", r"{\vec{F}", r"\over", "{q}}", "=", r"{k", "{q}", r"\over", "r^2}", r"\hat{r}").to_edge(UP).shift(DOWN).set_z_index(10)
        set_math_colors(e_field)
        self.play(Transform(coulomb_label,e_field))

        self.wait()


        e_label = Tex(r"$\vec{E}$").next_to(single_vector, LEFT).set_color(RED)
        self.play(GrowArrow(single_vector), FadeIn(e_label), FadeOut(r_label, r_vector)) 
        self.wait()
        
        # create electric field

        self.play(*[GrowArrow(vec) for vec in vector_field],
                   FadeOut(single_vector), FadeOut(vector_point),
                   FadeOut(e_label), FadeOut(coulomb_label), run_time=2)

        self.wait()
        # electron

        charges.append(charge.Charge(np.array([0,0]),charge=-10*base_charge,radius=0.5))
        proton = charges.pop(0)

        for c in charges:
            c.image.set_z_index(5)
            c.text.set_z_index(5)

        vector_field_2 = ArrowVectorField(get_electric_fields)
        vector_field_2.set_opacity(0.8)

        self.play(*[FadeOut(vec) for vec in vector_field],run_time=1)
        self.play(FadeOut(proton.image), FadeOut(proton.text), FadeIn(charges[0].image), FadeIn(charges[0].text),run_time=1)
        self.play(*[GrowArrow(vec) for vec in vector_field_2],run_time=1)

        self.wait()

        # both

        charges.append(proton)
        charges[1].move_to(3*RIGHT)
        theta_tracker = ValueTracker(0)

        def move_proton_charge():
            proton.move_to(np.array([3*np.cos(theta_tracker.get_value()),
                                      3*np.sin(theta_tracker.get_value()),0]))

        final_vector_field = ArrowVectorField(get_electric_fields)
        final_vector_field.set_opacity(0.8)
        animated_final_field = ArrowVectorField(get_electric_fields)
        animated_final_field.set_opacity(0.8)

        self.play(*[FadeOut(vec) for vec in vector_field_2],
                   *[FadeIn(vec) for vec in final_vector_field],
                    FadeIn(proton.image), FadeIn(proton.text), run_time=2)
        
        animated_final_field = always_redraw(lambda: ArrowVectorField(get_electric_fields).set_opacity(0.8))
        charges[1].image.add_updater(lambda m: move_proton_charge())

        self.wait()

        self.remove(final_vector_field)
        self.remove(vector_field_2)
        self.remove(vector_field)
        self.add(animated_final_field)
        self.play(*[FadeOut(vec) for vec in final_vector_field], run_time=0.1)
        self.play(theta_tracker.animate.set_value(2*PI), run_time=2)

        self.wait()


        self.play(FadeOut(e_field_header, coulomb_label),run_time=1)
        self.wait()

        # parametric curve (this took me like 4 hours please help)

        lines = VGroup()
        def get_parametric_curve(x,y,C):
            # dont divide by zero
            if (x == 0 and y == 0) or (x == 3 and y == 0):
                return 0
            # setting the change in voltage integral equal to zero and solving gives this
            # C is the integration constant
            curve_value = k_const*(-charges[0].q/(np.sqrt((charges[1].pos[0]-x)**2+(charges[1].pos[1]-y)**2))
                                    -charges[1].q/(np.sqrt(x**2+y**2)))-C
            return curve_value

        for C in range(-20,20,2):
            line = ImplicitFunction(
                lambda x, y: get_parametric_curve(x,y,C)   
            )
            line.set_color(YELLOW)
            lines.add(line)

        self.play(Write(lines), run_time=4)
        self.wait()

        # contour labels
        negative_contour_label = Tex(r"$-1 V$").shift(LEFT*3+DOWN*0.25)
        positive_contour_label = Tex(r"$+1 V$").shift(RIGHT*6+DOWN*0.25)
        self.play(FadeIn(negative_contour_label, positive_contour_label))
        self.wait()

class LineCharge(Scene):
    def construct(self):
        axes = Axes(axis_config={"include_ticks": False})
        labels = axes.get_axis_labels(x_label='x',y_label='y').shift(DOWN)
        self.play(FadeIn(axes,labels))
        self.wait(2)

        the_line = Rectangle(color=ORANGE,height=0.1,width=4,fill_opacity=1)
        self.play(Write(the_line))
        self.wait(2)

        broken_line = []
        n_rectangles = 10
        for i in np.linspace(-2,2,n_rectangles)[0:-1]:
            the_width = 4/n_rectangles
            new_line = Rectangle(color=ORANGE,height=0.1,width=the_width,fill_opacity=1).shift(RIGHT*the_width/2).shift(RIGHT*i)
            broken_line.append(new_line)
        
        for line in broken_line:
            self.add(line)
        self.remove(the_line)
        self.play(*[line.animate.shift((random.random()*2-1)*RIGHT+(random.random()*2-1)*UP) for line in broken_line])
        self.wait()

class FluxIntro(Scene):
    def construct(self):
        wind_field = ArrowVectorField(lambda pos: RIGHT,color=WHITE,
                                      x_range=[-7,0,1],y_range=[-2,2,1])

        wind_label = Tex("$W$ ").next_to(wind_field,UP) 

        net_mobject = SVGMobject("svg/net.svg").scale(2).shift(2*RIGHT)

        self.play(Write(wind_field))
        self.wait()
        self.play(FadeIn(wind_label))
        self.wait()
        self.play(Write(net_mobject))
        self.wait()

        area_circ = Circle(color=GREEN,fill_opacity=1).stretch(0.2,0)
        area_circ.shift(1.15*RIGHT+1*UP)
        self.play(Write(area_circ))
        self.wait()

        area_label = Tex(r"$A$").next_to(area_circ,UP).set_color(GREEN)
        self.play(Write(area_label))
        self.wait()

        area_vector = Vector(RIGHT).set_color(BLUE).move_to(area_circ).shift(0.5*RIGHT)
        self.play(GrowArrow(area_vector))
        self.wait()

        a_vec_label = Tex(r"$\vec{A}$").next_to(area_vector,LEFT,buff=0.2).set_color(GREEN)
        self.play(Write(a_vec_label))
        self.wait()

        flux_eqn1 = MathTex(r"\phi",'=','W','A',r'cos(\theta)')
        flux_eqn1.to_edge(UR).shift(LEFT)
        flux_eqn1.set_color_by_tex('A',GREEN)
        flux_eqn2 = MathTex(r"\phi",'=',r'\vec{W}',r'\cdot',r'\vec{A}')
        flux_eqn2.next_to(flux_eqn1,DOWN)
        flux_eqn2.set_color_by_tex('A',GREEN)

        self.play(FadeIn(flux_eqn1))
        self.wait()
        
        self.play(FadeIn(flux_eqn2))
        self.wait()

        self.play(FadeOut(net_mobject))
        self.wait()

        wiggle_mob = ArcBetweenPoints(area_circ.get_center(),area_circ.get_center()+4*DOWN+1.5*RIGHT)
        self.play(Write(wiggle_mob))
        self.wait()

        da_label = Tex(r"$d\vec{A}$").move_to(a_vec_label).set_color(GREEN)
        da_group = VGroup(a_vec_label,area_circ,area_vector)

        self.play(area_circ.animate.scale(0.5),Transform(a_vec_label,da_label))
        self.wait()
        self.play(da_group.animate.move_to(wiggle_mob.get_start()))
        self.play(MoveAlongPath(da_group,wiggle_mob))
        self.wait()

        flux_eqn3 = MathTex(r"\phi",'=', r"\int", r'\vec{W}',r'\cdot',r'\vec{dA}')
        flux_eqn3.next_to(flux_eqn2,DOWN)
        flux_eqn3.set_color_by_tex('A',GREEN)
        self.play(FadeIn(flux_eqn3))
        self.wait()

# This section is split into 3 scenes to make rendering faster
class GaussLaw(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(x_label="x",y_label="y",z_label="z")
        charge_surf = Sphere(radius=0.5).set_color(RED)
        gauss_surf = Sphere(radius=2).set_color(BLUE).set_opacity(0.5)
        
        self.play(FadeIn(charge_surf))
        self.wait()

        self.play(FadeIn(gauss_surf))
        self.wait()

        self.play(FadeIn(axes,labels))
        self.wait()

        self.move_camera(phi=2*PI,theta=3*PI/2,run_time=3)
        self.wait()

        gauss_circ = Circle(radius=2,color=BLUE)
        charge1 = charge.Charge(pos=np.array([0,0]),charge=100*(10**(-12)),radius=0.5)
        self.play(FadeOut(gauss_surf), FadeOut(charge_surf),
                  FadeIn(charge1.image), FadeIn(charge1.text), FadeIn(gauss_circ),
                  FadeOut(axes), FadeOut(labels))
        self.wait()

class GaussLaw2(Scene):
    def construct(self): 
        gauss_circ = Circle(radius=2,color=BLUE)
        charge1 = charge.Charge(pos=np.array([0,0]),charge=100*(10**(-12)),radius=0.5)

        self.add(gauss_circ,charge1.image,charge1.text)
        self.wait()        
        vector_field = ArrowVectorField(charge1.get_electric_field)
        self.play(FadeIn(vector_field))
        self.wait()

        vectors = []
        area_vectors = []
        radius = 2
        num_vectors = 10
        for i in range(num_vectors):
            theta = i * (2*PI)/(num_vectors)
            x = radius*np.cos(theta)
            y = radius*np.sin(theta)

            new_vector = Vector(2*charge1.get_electric_field(np.array([x,y])))
            new_area_vector = new_vector.copy()

            new_vector.shift(RIGHT*(x+np.sign(x)*new_vector.width/2)
                              + UP*(y+np.sign(y)*new_vector.height/2))
            new_vector.scale(2)
            new_vector.set_color(YELLOW)
            vectors.append(new_vector)

            new_area_vector.shift(RIGHT*(x)
                              + UP*(y))
            new_area_vector.set_color(GREEN_D)
            area_vectors.append(new_area_vector)

        e_label = Tex(r"$\vec{E}$")
        e_label.scale(2)
        e_label.next_to(gauss_circ,UR)
        e_label.set_color(YELLOW_E)

    
        self.play(FadeOut(vector_field),
                  *[GrowArrow(vec) for vec in vectors],
                  FadeIn(e_label))
        self.wait()

        dA_label = Tex(r"d$\vec{A}$")
        dA_label.scale(2)
        dA_label.next_to(gauss_circ,UL)
        dA_label.set_color(GREEN_E)

        # green circles

        dA_circs = []
        for i in range(num_vectors):
            new_circ = Circle(color=GREEN,fill_opacity=1).stretch(0.2,1).scale(0.33)
            new_circ.move_to(area_vectors[i].get_start())
            new_circ.rotate(np.arctan2(area_vectors[i].get_y(),area_vectors[i].get_x())+PI/2)
            dA_circs.append(new_circ)

        self.play(*[Write(circ) for circ in dA_circs],*[GrowArrow(vec) for vec in area_vectors],
                  FadeIn(dA_label))
        self.wait()

        gauss_setup = VGroup(charge1.image,charge1.text,gauss_circ)
        gauss_eqns_header = VGroup(dA_label,e_label)
        flux_eqn = MathTex(r"\phi_{","E}", "=", r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}")
        set_math_colors(flux_eqn)
        flux_eqn.set_color_by_tex(r"E", YELLOW_E)
        flux_eqn.set_color_by_tex(r"\vec{E}",YELLOW_E)
        flux_eqn.scale(2).to_edge(UR)

        self.play(*[vec.animate.shift(4*LEFT) for vec in vectors],
                  *[vec.animate.shift(4*LEFT) for vec in area_vectors],
                  *[circ.animate.shift(4*LEFT) for circ in dA_circs],
                  gauss_setup.animate.shift(4*LEFT),
                  Transform(gauss_eqns_header,flux_eqn))
        self.wait()

        self.play(*[Wiggle(vec,n_wiggles=2,rotation_angle=0.03*TAU) for vec in area_vectors],
                  *[Wiggle(vec,n_wiggles=2,rotation_angle=-0.015*TAU) for vec in vectors])
        self.wait()

        flux_pt2 = MathTex(r"\phi_{","E}", "=", r"\oint", r"{E}", r"dA")
        set_math_colors(flux_pt2)
        flux_pt2.set_color_by_tex(r"E", YELLOW_E)
        flux_pt2.scale(2).to_edge(UR)

        e_field_label = MathTex(r"E", "=", "{k","{q}" ,r"\over","r^2}")
        set_math_colors(e_field_label)
        e_field_label.set_color_by_tex("E", YELLOW_E)
        e_field_label.shift(4*RIGHT)

        e_field_function = MathTex(r"E", "(", "{r}", ")", "=", "{k","{q}" ,r"\over","r^2}")
        set_math_colors(e_field_function)
        e_field_function.set_color_by_tex("E", YELLOW_E)
        e_field_function.shift(4*RIGHT)

        flux_pt3 = MathTex(r"\phi_{","E}", "=", r"{E}", r"\oint", r"dA")
        set_math_colors(flux_pt3)
        flux_pt3.set_color_by_tex(r"E", YELLOW_E)
        flux_pt3.scale(2).to_edge(UR)

        self.play(Transform(gauss_eqns_header,flux_pt2))
        self.wait()

        self.play(FadeIn(e_field_label))
        self.wait()
        self.play(Transform(e_field_label, e_field_function))
        self.wait()
        self.play(FadeOut(e_field_label),Transform(gauss_eqns_header,flux_pt3))
        self.wait()

        dA_brace = Brace(VGroup(flux_pt3.get_parts_by_tex(r"\oint"),flux_pt3.get_parts_by_tex("dA")),sharpness=1)
        A_label = Tex(r"A").next_to(dA_brace,DOWN)
        A_label.set_color(GREEN_E)

        flux_pt4 = MathTex(r"\phi_{","E}", "=", r"{E}", r"{A}")
        set_math_colors(flux_pt4)
        flux_pt4.set_color_by_tex(r"E", YELLOW_E)
        flux_pt4.scale(2).move_to(flux_pt3)

        self.play(Write(dA_brace))
        self.wait()
        self.play(FadeIn(A_label))
        self.wait()
        self.play(Transform(gauss_eqns_header,flux_pt4),
                  FadeOut(dA_brace,A_label))
        self.wait()

        flux_solve1 = MathTex(r"\phi_{","E}", "=", "{k","q" ,r"\over","r^2}", r"4\pi", r"r^2")
        set_math_colors(flux_solve1)
        flux_solve1.set_color_by_tex(r"E", YELLOW_E)
        flux_solve1.set_color_by_tex("4",LIGHT_GRAY)
        flux_solve1.scale(2).next_to(flux_pt4,DOWN)

        self.play(FadeIn(flux_solve1))
        self.wait()

        flux_solve2 = MathTex(r"\phi_{","E}", "=", "k","q", r"4\pi")
        set_math_colors(flux_pt2)
        flux_solve2.set_color_by_tex("4",LIGHT_GRAY)
        flux_solve2.set_color_by_tex(r"E", YELLOW_E)
        flux_solve2.scale(2).next_to(flux_solve1,DOWN)

        self.play(FadeIn(flux_solve2))
        self.wait()

        flux_solve3 = MathTex(r"\phi_{","E}", "=", "{{q}", r"\over", r"\epsilon_0}")
        set_math_colors(flux_pt3)
        flux_solve3.set_color_by_tex(r"E", YELLOW_E)
        flux_solve3.scale(2).next_to(flux_solve2,DOWN)

        self.play(FadeIn(flux_solve3))
        self.wait()

        gauss_law_header = Text("Gauss's Law")
        gauss_law_header.scale(2).to_edge(UR)

        gauss_law = MathTex(r"\phi_{","E}", "=", r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}", "=", "{q", r"\over", r"\epsilon_0}")
        set_math_colors(gauss_law)
        gauss_law.set_color_by_tex(r"E", YELLOW_E)
        gauss_law.set_color_by_tex("A",GREEN_E)
        gauss_law.scale(1.5).next_to(gauss_law_header,DOWN)

        self.play(FadeOut(gauss_eqns_header,flux_solve1,flux_solve2,flux_solve3),
                  FadeIn(gauss_law_header,gauss_law))
        self.wait()

        self.play(*[FadeOut(vec) for vec in vectors],
                  *[FadeOut(vec) for vec in area_vectors],
                  *[FadeOut(circ) for circ in dA_circs],
                  charge1.image.animate.scale(0.5),
                  charge1.text.animate.scale(0.5),
                  gauss_circ.animate.scale(0.5))
        self.wait()

class GaussLaw3(Scene):
    def construct(self):
        charge1 = charge.Charge(pos=np.array([0,0]),charge=100*(10**(-12)),radius=0.5)
        charge1.elements.shift(4*LEFT).scale(0.5)
        charge1.elements.set_z_index(5)

        gauss_circ = Circle(radius=2,color=BLUE_D)
        gauss_circ.shift(4*LEFT).scale(0.5)

        general_surf = SVGMobject("svg/general-shape.svg").shift(4.25*LEFT).scale(2)

        gauss_law_header = Text("Gauss's Law")
        gauss_law_header.scale(2).to_edge(UR)

        gauss_law = MathTex(r"\phi_{","E}", "=", r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}", "=", "{{q}", r"\over", r"\epsilon_0}")
        set_math_colors(gauss_law)
        gauss_law.set_color_by_tex(r"E", YELLOW_E)
        gauss_law.scale(1.5).next_to(gauss_law_header,DOWN)

        self.add(charge1.image,charge1.text,gauss_circ,gauss_law_header,gauss_law)
        self.play(Write(general_surf))
        self.wait()

        ray1 = Line(start=charge1.image.get_center(),end=general_surf.get_top())
        ray2 = Line(start=charge1.image.get_center(),end=general_surf.get_top() + 0.55*RIGHT + 0.2*DOWN)
        self.play(Write(ray1))
        self.wait()

        self.play(Write(ray2))
        self.wait()

        a1 = Circle(color=GREEN,fill_opacity=1).scale(0.15).stretch(0.2,1)
        a1.move_to(charge1.image)
        a1.shift(UP+RIGHT*0.025)
        self.play(Write(a1))
        self.wait()

        a1_label = Tex(r"$A_1$")
        a1_label.move_to(a1).shift(0.5*LEFT+0.25*UP)
        a1_label.scale(0.5)
        a1_label.set_color(GREEN)
        self.play(FadeIn(a1_label))
        self.wait()

        a2 = Circle(color=GREEN,fill_opacity=1).scale(0.3).stretch(0.2,1)
        a2.move_to(charge1.image)
        a2.shift(1.8*UP+RIGHT*0.025).rotate(-PI/6)
        a2_original = a2.copy()
        self.play(Write(a2))
        self.wait()

        a2_label = Tex(r"$A_2$")
        a2_label.move_to(a2).shift(0.5*RIGHT+0.25*UP)
        a2_label.scale(0.5)
        a2_label.set_color(GREEN)
        a2_label_original = a2_label.copy()
        self.play(FadeIn(a2_label))
        self.wait()

        r_brace = Brace(ray1,LEFT).scale(0.25).rotate(PI/12).shift(0.4*DOWN+RIGHT*0.35)
        r_brace.set_color(RED)
        self.play(FadeIn(r_brace))
        self.wait()

        r_label = Tex(r"$r$")
        r_label.set_color(RED)
        r_label.next_to(r_brace,LEFT).shift(RIGHT*0.1+DOWN*0.1)
        self.play(FadeIn(r_label))
        self.wait()

        nr_brace = Brace(ray2,RIGHT,buff=0.05).scale(0.75).rotate(-PI/12).shift(LEFT*0.1+UP*0.1)
        nr_brace.set_color(RED)
        self.play(FadeIn(nr_brace))
        self.wait()

        nr_label = MathTex(r"n","{r}")
        set_math_colors(nr_label)
        nr_label.set_color_by_tex("n",LIGHT_GRAY)
        nr_label.next_to(nr_brace,RIGHT).shift(LEFT*0.1+DOWN*0.1)
        self.play(FadeIn(nr_label))
        self.wait()


        dot_prod_rewrite = MathTex(r"\phi_{","E","2}","=",r"\oint","E_2","cos(",r"\theta",")","dA_2")
        set_math_colors(dot_prod_rewrite)
        dot_prod_rewrite.set_color_by_tex("E",YELLOW_E)
        dot_prod_rewrite.set_color_by_tex(r"\theta",GRAY)
        dot_prod_rewrite.next_to(gauss_law,DOWN)
        self.play(FadeIn(dot_prod_rewrite))
        self.wait()

        radial_line = Line(start=a2.get_center(),end=a2.get_center()+UP)
        radial_line.set_color(YELLOW_E)
        radial_line_og = radial_line.copy()
        self.play(Write(radial_line))
        self.wait()

        a2_line = Line(start=a2.get_center(),end=a2.get_center()+UP).rotate(-PI/6)
        a2_line.shift(RIGHT*a2_line.width/2)
        a2_line.set_color(GREEN)
        a2_line_og = a2_line.copy()
        self.play(Write(a2_line))
        self.wait()

        theta_arc = Arc(radius=0.5,start_angle=PI/2,angle=-PI/6,arc_center=a2.get_center())
        theta_arc.set_color(GRAY)
        theta_arc_og = theta_arc.copy()
        self.play(Write(theta_arc))
        self.wait()

        theta_label = Tex(r"$\theta$").move_to(theta_arc).shift(UP*0.5+RIGHT*0.05)
        theta_label.set_color(GRAY)
        self.play(Write(theta_label))
        self.wait()
        
        a2_prime = Circle(color=BLUE,fill_opacity=0.5).scale(a2.width/2).stretch(0.2,1)
        a2_prime.move_to(a2).shift(UP*a2.height/2)
        self.play(Write(a2_prime))
        self.wait()

        a2_prime_label = Tex(r"$A_{\perp}$").set_color(BLUE).scale(0.5)
        a2_prime_label.move_to(a2_prime).shift(0.2*UP+0.5*LEFT)
        self.play(Write(a2_prime_label))
        self.wait()
        
        brace_vgroup = VGroup(dot_prod_rewrite.get_parts_by_tex(r"cos"),
                              dot_prod_rewrite.get_parts_by_tex("dA"),
                              dot_prod_rewrite.get_parts_by_tex("theta"),
                              dot_prod_rewrite.get_parts_by_tex(")"))
        a2_perp_brace = Brace(brace_vgroup,DOWN)
        self.play(Write(a2_perp_brace))
        self.wait()

        a2_brace_label = MathTex("dA_{\perp}").set_color(BLUE).next_to(a2_perp_brace,DOWN)
        self.play(Write(a2_brace_label))
        self.wait()

        a2_line_straight = Line(start=a2.get_center(),end=a2.get_center()+UP)
        a2_line_straight.set_color(GREEN)

        a2_straight = Circle(color=GREEN,fill_opacity=1).scale(0.3).stretch(0.2,1)
        a2_straight.move_to(charge1.image)
        a2_straight.shift(1.8*UP+RIGHT*0.025)
        
        theta_arc_straight = Arc(radius=0.5,start_angle=PI/2,angle=0,arc_center=a2.get_center())
        theta_arc_straight.set_color(GRAY)

        self.play(Transform(a2,a2_straight),
                   Transform(a2_line,a2_line_straight),
                   Transform(theta_arc,theta_arc_straight),
                   FadeOut(theta_label))
        self.wait()

        a2_line_perp = Line(start=a2.get_center(),end=a2.get_center()+UP)
        a2_line_perp.shift(DOWN*a2_line_perp.height/2+RIGHT*a2_line_perp.height/2)
        a2_line_perp.rotate(-PI/2)
        a2_line_perp.set_color(GREEN)

        a2_perp = Circle(color=GREEN,fill_opacity=1).scale(0.3).stretch(0.2,1)
        a2_perp.move_to(charge1.image)
        a2_perp.shift(1.8*UP+RIGHT*0.025).rotate(-PI/2)

        theta_arc_perp = Arc(radius=0.5,start_angle=PI/2,angle=-PI/2,arc_center=a2.get_center())
        theta_arc_perp.set_color(GRAY)

        self.play(Transform(a2,a2_perp),
                   Transform(a2_line,a2_line_perp),
                   Transform(theta_arc,theta_arc_perp),
                   FadeIn(theta_label),a2_label.animate.shift(0.5*RIGHT))
        self.wait()
        
        self.play(Transform(a2,a2_original),
                  Transform(a2_line,a2_line_og),
                  Transform(theta_arc,theta_arc_og),
                  a2_label.animate.shift(0.5*LEFT))
        self.wait()

        step3 = MathTex(r"\phi_{","E","2}","=",r"\oint","E_2",r"dA_{\perp}")
        step3.set_color_by_tex("E",YELLOW_E)
        step3.set_color_by_tex("dA",BLUE)
        step3.next_to(dot_prod_rewrite,DOWN)
        self.play(FadeIn(step3),FadeOut(a2_perp_brace),FadeOut(a2_brace_label))
        self.wait()

        e_field_label = MathTex(r"E", "=", "{k","{q}" ,r"\over","r^2}")
        set_math_colors(e_field_label)
        e_field_label.set_color_by_tex("E", YELLOW_E)
        e_field_label.next_to(step3,DOWN)

        self.play(FadeIn(e_field_label))
        self.wait()
        self.play(FadeOut(e_field_label))
        self.wait()

        step6 = MathTex(r"\phi_{","E","2}","=",r"\oint","{E_1", r"\over", "n^2}",r"dA_{\perp}")
        step6.set_color_by_tex("E",YELLOW_E)
        step6.set_color_by_tex("n",LIGHT_GRAY) 
        step6.set_color_by_tex("A",BLUE)
        step6.move_to(step3)
        self.play(Transform(step3,step6))
        self.wait()

        line1 = VGroup()
        line1.add(Line(start=a1.get_center()+LEFT*a1.width/2,end=a1.get_center()+RIGHT*a1.width/2).set_color(PURPLE))

        tri2 = VGroup()
        tri2.add(Line(start=a2_prime.get_center()+LEFT*a2_prime.width/2,end=a2_prime.get_center()+RIGHT*a2_prime.width/2).set_color(PURPLE))
        tri2.add(Line(start=a2_prime.get_center()+LEFT*a2_prime.width/2,end=ray1.get_start()).set_color(PURPLE))
        tri2.add(Line(start=a2_prime.get_center()+RIGHT*a2_prime.width/2,end=ray1.get_start()).set_color(PURPLE))
        self.play(Write(line1),Write(tri2))
        self.wait()

        tris = VGroup(line1,tri2)
        self.play(tris.animate.shift(2.5*RIGHT+DOWN))
        self.wait()

        shift_nr_label = nr_label.copy()
        shift_r_label = r_label.copy()
        self.play(shift_nr_label.animate.shift(2.25*RIGHT+DOWN),
                  shift_r_label.animate.shift(2.75*RIGHT+DOWN))
        self.wait()

        d_label = Tex("$d$").move_to(line1).shift(0.3*UP)
        nd_label = MathTex("n","d").next_to(tri2,UP).shift(0.15*DOWN)
        nd_label.set_color_by_tex("n",LIGHT_GREY)
        self.play(FadeIn(d_label,nd_label))
        self.wait()

        area_label = MathTex("{A}","=",r"\pi","r^2")
        set_math_colors(area_label)
        area_label.next_to(tri2,DOWN)
        area_label.shift(0.2*RIGHT)
        self.play(Write(area_label))
        self.wait()

        area_label2 = MathTex("{A}","=",r"\pi",r"({\frac{d}{2}})^2")
        set_math_colors(area_label2)
        area_label2.move_to(area_label)
        self.play(Transform(area_label,area_label2))
        self.wait()

        step7 = MathTex(r"\phi_{","E","2}","=",r"\oint","{E_1", r"\over", "n^2}","n^2",r"dA_1")
        step7.set_color_by_tex("E",YELLOW_E)
        step7.set_color_by_tex("n",LIGHT_GRAY) 
        step7.set_color_by_tex("A",BLUE)
        step7.move_to(step6)
        self.play(Transform(step3,step7))
        self.wait()

        step8 = MathTex(r"\phi_{","E","2}","=",r"\oint","E_1",r"dA_1")
        step8.set_color_by_tex("E",YELLOW_E)
        step8.set_color_by_tex("n",LIGHT_GRAY) 
        step8.set_color_by_tex("A",BLUE)
        step8.move_to(step7)
        self.play(Transform(step3,step8))
        self.wait()

        step9 = MathTex(r"\phi_{","E","2}","=","E_1",r"A_1","=",r"\phi_{","E","1}")
        step9.set_color_by_tex("E",YELLOW_E)
        step9.set_color_by_tex("n",LIGHT_GRAY) 
        step9.set_color_by_tex("A",BLUE)
        step9.move_to(step8,DOWN)
        self.play(Transform(step3,step9))
        self.wait()

        self.play(step3.animate.scale(1/0.75))
        self.wait()
        self.play(FadeOut(dot_prod_rewrite),step3.animate.next_to(gauss_law,DOWN))
        self.wait()

        triangle_diagram = VGroup(line1,tri2,shift_r_label,shift_nr_label,d_label,nd_label)
        ray_diagram =VGroup(ray1,ray2,r_brace,nr_brace,r_label,nr_label,a1_label,a1,a2,a2_label,a2_prime,a2_prime_label,theta_label,theta_arc,radial_line,a2_line)

        self.play(FadeOut(triangle_diagram),FadeOut(ray_diagram),FadeOut(area_label),lag_ratio=0.1)
        self.wait()

        self.play(gauss_circ.animate.scale(0.5))
        self.wait()

        c1_img_cpy = charge1.image.copy()
        c1_txt_cpy = charge1.text.copy()
        gauss_surf_cpy = gauss_circ.copy()
        charge_gauss_group = VGroup(c1_img_cpy,c1_txt_cpy,gauss_surf_cpy)
        self.play(charge_gauss_group.animate.shift(1.5*LEFT))
        self.wait()

        gauss_law_2 = MathTex(r"\phi_{","E}", "=", r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}", "=", "{q_{enc}", r"\over", r"\epsilon_0}")
        set_math_colors(gauss_law_2)
        gauss_law_2.set_color_by_tex(r"E", YELLOW_E)
        gauss_law_2.scale(1.5).next_to(gauss_law_header,DOWN) 

        self.play(Transform(gauss_law,gauss_law_2))
        self.wait()

        c1_img_cpy2 = c1_img_cpy.copy()
        c1_txt_cpy2 = c1_txt_cpy.copy()
        gauss_surf_cpy2 = gauss_surf_cpy.copy()
        charge_gauss_group2 = VGroup(c1_img_cpy2,c1_txt_cpy2,gauss_surf_cpy2)
        self.play(charge_gauss_group2.animate.shift(0.5*LEFT+1.5*DOWN))
        self.wait()

        in_out_flux_arrow = Vector(1.25*(4*RIGHT+0.5*UP))
        in_out_flux_arrow.move_to(c1_img_cpy2).shift((2.625*RIGHT+0.375*UP))
        self.play(GrowArrow(in_out_flux_arrow))
        self.wait()

        self.play(FadeOut(c1_img_cpy2,c1_txt_cpy2),FadeOut(gauss_surf_cpy2),FadeOut(in_out_flux_arrow))
        self.wait()

        self.play(FadeOut(c1_img_cpy,c1_txt_cpy,gauss_surf_cpy))
        self.wait()

class GaussExample(Scene):
    def construct(self):
        gauss_law = MathTex(r"\phi_{","{E}}", "=", r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}", "=", "{q_{enc}", r"\over", r"\epsilon_0}")
        set_math_colors(gauss_law)
        gauss_law.to_edge(UL)

        lhs = MathTex(r"\oint", r"\vec{E}", r"\cdot", r"d\vec{A}",":").next_to(gauss_law,DOWN)
        lhs.set_color_by_tex(r"E", YELLOW_E)
        lhs.set_color_by_tex('A',GREEN_E)

        step2 = MathTex(r"=",r"\oint",r"E",r"dA").next_to(lhs,DOWN)
        step2.set_color_by_tex(r"E", YELLOW_E)
        step2.set_color_by_tex('A',GREEN_E)

        step3 = MathTex(r"=",r"E",r"\oint",r"dA").next_to(step2,DOWN)
        step3.set_color_by_tex(r"E", YELLOW_E)
        step3.set_color_by_tex('A',GREEN_E)

        step4 = MathTex(r"=","E","A").next_to(step3,DOWN)
        step4.set_color_by_tex("E",YELLOW_E)
        step4.set_color_by_tex("A",GREEN_E)

        step5 = MathTex("=","E","2",r"\pi","r^2").next_to(step4,DOWN)
        step5.set_color_by_tex("E",YELLOW_E)
        step5.set_color_by_tex("r",RED)
        step5.set_color_by_tex("pi",LIGHT_GRAY)

        rhs = Tex(r"Charge: ", "$Q$", ", ", "Area: ", "${A}$").to_edge(UR)
        rhs.set_color_by_tex('Q', BLUE_D)
        rhs.set_color_by_tex('{A}',GREEN_E)

        q2 = MathTex("Q","=","(","{Q",r"\over","A}",")","A").next_to(rhs,DOWN)
        q2.set_color_by_tex("Q",BLUE_D)
        q2.set_color_by_tex("A",GREEN_E)

        q3 = MathTex("Q","=",r"\sigma","A").next_to(q2,DOWN)
        q3.set_color_by_tex("Q",BLUE_D)
        q3.set_color_by_tex("A",GREEN_E)
        
        q4 = MathTex("Q","=",r"\sigma",r"\pi","r^2").next_to(q3,DOWN)
        q4.set_color_by_tex("Q",BLUE_D)
        q4.set_color_by_tex(r"pi",LIGHT_GRAY)
        q4.set_color_by_tex("r^2",RED)
        
        q5 = MathTex("{Q",r"\over",r"\epsilon_0}","=",r"{\sigma",r"\pi","r^2",r"\over",r"\epsilon_0}").next_to(q4,DOWN)
        q5.set_color_by_tex("Q",BLUE_D)
        q5.set_color_by_tex("A",GREEN_E)
        q5.set_color_by_tex("Q",BLUE_D)
        q5.set_color_by_tex(r"pi",LIGHT_GRAY)
        q5.set_color_by_tex("r^2",RED)

        combo = MathTex(r"\Rightarrow","E","2",r"\pi","r^2","=",r"{\sigma",r"\pi","r^2",r"\over",r"\epsilon_0}").to_edge(DL).shift(4*RIGHT)
        combo.set_color_by_tex("Q",BLUE_D)
        combo.set_color_by_tex("A",GREEN_E)
        combo.set_color_by_tex("Q",BLUE_D)
        combo.set_color_by_tex(r"pi",LIGHT_GRAY)
        combo.set_color_by_tex("r^2",RED)

        combo2 = MathTex(r"\Rightarrow","E","=","{\sigma",r"\over","2",r"\epsilon_0}").next_to(combo,RIGHT,buff=0.2).set_color(YELLOW)
        combo2.set_color_by_tex("Q",BLUE_D)
        combo2.set_color_by_tex("A",GREEN_E)
        combo2.set_color_by_tex("Q",BLUE_D)
        combo2.set_color_by_tex(r"pi",LIGHT_GRAY)
        combo2.set_color_by_tex("r^2",RED)

        mobs = VGroup(gauss_law,lhs,step2,step3,step4,step5,rhs,q2,q3,q4,q5,combo,combo2)

        for mob in mobs:
            self.play(Write(mob))
            self.wait()

class Voltage(Scene):
    def construct(self):
        # square
        square = Square()
        self.play(Write(square),run_time=1)
        self.wait()

        # original

        force_vec = Vector(4*RIGHT+3*UP).set_color(RED)
        force_label = Tex(r"$\vec{F}$").next_to(force_vec, RIGHT+UP).set_color(RED)
        distance_vec = Vector(4*RIGHT).set_color(BLUE)
        distance_label = Tex(r"$\Delta \vec{s}$").next_to(distance_vec, RIGHT).set_color(BLUE)
        theta_arc = Arc(radius=1, start_angle=0, angle=np.arctan2(3,4)).set_color(PURPLE)
        theta_label = Tex(r"$\theta$").next_to(theta_arc, RIGHT).shift(UP*0.25).set_color(PURPLE)

        self.play(Write(force_label), Write(force_vec), run_time=1)
        self.wait()
        self.play(Write(distance_label), Write(distance_vec),run_time=1)
        self.wait()

        force_theta = VGroup(force_vec, force_label, theta_arc, theta_label)
        original_force_theta = force_theta.copy()
        # avoid double-drawing
        self.play(FadeOut(original_force_theta), run_time=0.0)
        self.remove(original_force_theta)


        original_work_label = Tex(r"W", "=", "{F}", r"$\Delta s$", r"$cos(\theta)$")
        set_math_colors(original_work_label)
        original_work_label.set_color_by_tex("theta", PURPLE)
        original_work_label.to_edge(DOWN)
        work_label = original_work_label.copy()

        self.play(Write(work_label),run_time=1)
        self.play(Write(theta_arc), Write(theta_label),run_time=1)

        self.wait()

        # parallel

        parallel_force_vec = Vector(3*RIGHT).set_color(RED)
        parallel_force_label = Tex(r"$\vec{F}$").next_to(parallel_force_vec, RIGHT+UP).set_color(RED)
        para_theta_arc = Arc(radius=1, start_angle=0, angle=0).set_color(PURPLE)


        para_work_label = Tex(r"$W$", "$=$", "${F}$", r"$\Delta s$", r"$(1)$", "$=$", "$F$", r"$\Delta s$").to_edge(DOWN)
        set_math_colors(para_work_label)
        para_work_label.set_color_by_tex("1", PURPLE)

        parallel_force_theta = VGroup(parallel_force_vec, parallel_force_label, para_theta_arc)

        self.play(Transform(force_theta, parallel_force_theta), Transform(work_label, para_work_label),run_time=1)
        
        self.wait()

        # perpendicular

        perp_force_vec = Vector(3*UP).set_color(RED)
        perp_force_label = Tex(r"$\vec{F}$").next_to(perp_force_vec, RIGHT).set_color(RED)
        perp_theta_arc = Arc(radius=1, start_angle=0, angle=PI/2).set_color(PURPLE)
        perp_theta_label = Tex(r"$\theta$").next_to(perp_theta_arc, RIGHT).set_color(PURPLE)

        perp_force_theta = VGroup(perp_force_vec, perp_force_label, perp_theta_arc, perp_theta_label)
        perp_work_label = Tex("W", "=", "{F}", r"$\Delta s$", "(0)", "=", "0").to_edge(DOWN)
        set_math_colors(perp_work_label)
        perp_work_label.set_color_by_tex("(0)", PURPLE)

        self.play(Transform(force_theta, perp_force_theta), Transform(work_label, perp_work_label),run_time=1)
        self.wait()

        # opposite
        opp_force_vec = Vector(3*LEFT).set_color(RED)
        opp_force_label = Tex(r"$\vec{F}$").next_to(opp_force_vec, UP).set_color(RED)
        opp_theta_arc = Arc(radius=1, start_angle=0, angle=PI).set_color(PURPLE)
        opp_theta_label = Tex(r"$\theta$").next_to(opp_theta_arc, UP+RIGHT).set_color(PURPLE)

        opp_force_theta = VGroup(opp_force_vec, opp_force_label, opp_theta_arc, opp_theta_label)
        opp_work_label = Tex("W", "=", "{F}", r"$\Delta s$", "(-1)", "=", "$-F$", r"$\Delta s$").to_edge(DOWN)
        set_math_colors(opp_work_label)
        opp_work_label.set_color_by_tex("-1", PURPLE)

        self.play(Transform(force_theta, opp_force_theta), Transform(work_label, opp_work_label),run_time=1)
        self.wait()

        # Original

        self.play(Transform(force_theta, original_force_theta), Transform(work_label, original_work_label),run_time=1)
        self.wait()

        # This is where you could cut for the in person part about how
        # u = -W = -F dot Delta s
        self.wait()
        # potential

        u_label = Tex("U", "=", "$-F$", r"$\Delta s$", r"$cos(\theta)$").to_edge(DOWN).scale(0.75)
        set_math_colors(u_label)
        u_label.set_color_by_tex("theta", PURPLE)
        self.play(Transform(work_label, u_label), run_time=2)
        self.wait()

        u_label_dot = Tex("U", "=", r"$-\vec{F}$", r"$\cdot$", r"$\vec{\Delta s}$").to_edge(DOWN).scale(0.75)
        set_math_colors(u_label_dot)
        u_label_dot.set_color_by_tex("theta", PURPLE)
        self.play(Transform(work_label, u_label_dot), run_time=2)
        self.wait()

        self.play(work_label.animate.shift(1.5*UP),run_time=1)
        self.wait()

        self.wait()

        u_label_sum = Tex("U", "=", "$(-$", r"$\vec{F_1}$", r"$\cdot$", r"$\vec{\Delta s_1}$", ") + (", r"$-\vec{F_2}$", r"$\cdot$", r"$\vec{\Delta s_2}$", ") + (", r"$-\vec{F_3}$", r"$\cdot$", r"$\vec{\Delta s_3}$", ") +",  r"$\cdots$").next_to(work_label, DOWN).scale(0.75)
        set_math_colors(u_label_sum)
        u_label_sum.set_color_by_tex("theta", PURPLE)
        self.play(Write(u_label_sum), run_time=3)
        self.wait()

        sum_label_copy = u_label_sum.copy()
        integral_sum_label = Tex(r"$U = -\displaystyle \int$", r"$\vec{F}$", r"$\cdot$", r"$d\vec{s} $").next_to(u_label_sum, DOWN).scale(0.75)
        set_math_colors(integral_sum_label)
        integral_sum_label.set_color_by_tex(r"\vec{s}", BLUE)
        self.play(Transform(sum_label_copy, integral_sum_label),run_time=1)
        self.wait()

        # move potential up
        self.play(FadeOut(square), FadeOut(force_theta), FadeOut(theta_arc),
                  FadeOut(theta_label), FadeOut(work_label), FadeOut(u_label_sum),
                  FadeOut(sum_label_copy), FadeOut(distance_vec), FadeOut(distance_label),
                  integral_sum_label.animate.to_edge(UP), run_time=2)
        self.wait()

        coulomb_force_label = MathTex(r"\vec{F}", "=", r"\displaystyle", "{k", "{q}_1", "{q}_2", r"\over", "r^2}", r"\hat{r}").next_to(integral_sum_label, DOWN).scale(0.75)
        set_math_colors(coulomb_force_label)
        self.play(FadeIn(coulomb_force_label))
        self.wait()

        ds_force_label = Tex(r"$d\vec{s}$", "$=$", "$d{r}$", r"$\hat{r}$").next_to(coulomb_force_label, DOWN).scale(0.75)
        set_math_colors(ds_force_label)
        ds_force_label.set_color_by_tex(r"\vec{s}", BLUE_C)
        ds_force_label.set_color_by_tex("dr", RED_D)
        self.play(FadeIn(ds_force_label))
        self.wait()


        coulomb_potential_label = MathTex("U", "=",  r"-\displaystyle \int", "{k", "{q}_1", "{q}_2", r"\over", "r^2}", r"\hat{r}", r"\cdot", "dr" r"\hat{r}").scale(0.75)
        set_math_colors(coulomb_potential_label)
        coulomb_potential_label.set_color_by_tex("dr", RED_D)


        coulomb_potential_label.next_to(ds_force_label, DOWN).shift(DOWN)
        combined_eqs_copy = VGroup(integral_sum_label, coulomb_force_label, ds_force_label).copy()
        self.play(Transform(combined_eqs_copy, coulomb_potential_label))
        
        coulomb_potential_limits = MathTex("U", "=",  r"-\displaystyle \int_{\infty}^{r'}", "{k", "{q}_1", "{q}_2", r"\over", "r^2}", r"\hat{r}", r"\cdot", "dr", r"\hat{r}").scale(0.75)
        set_math_colors(coulomb_potential_limits)
        coulomb_potential_limits.set_color_by_tex("dr", RED_D)

        # move charges

        proton1 = charge.Charge(np.array([0,0]),charge=100*(10**(-12)), radius=0.5)
        proton1.move_to(DOWN*2+RIGHT*5)
        proton2 = charge.Charge(np.array([0,0]),charge=100*(10**(-12)), radius=0.5)
        proton2.move_to(DOWN*2+LEFT*5)
        self.play(FadeIn(proton1.image, proton1.text), 
                  FadeIn(proton2.image, proton2.text),run_time=1)

        self.wait()

        r_prime_radius = NumberLine(x_range=[0,1], length=1).move_to(DOWN*2)
        r_prime_label = Tex(r"$r'$").scale(0.75).next_to(r_prime_radius, UP)
        self.play(proton1.image.animate.move_to(DOWN*2+RIGHT),
                  proton1.text.animate.move_to(DOWN*2+RIGHT),
                  proton2.text.animate.move_to(DOWN*2+LEFT),
                  proton2.image.animate.move_to(DOWN*2+LEFT),
                  FadeIn(r_prime_radius), FadeIn(r_prime_label))
        self.wait()

        proton_vgroup = VGroup(proton1.image, proton1.text, proton2.image, proton2.text,
                               r_prime_radius, r_prime_label)
        self.play(FadeOut(proton_vgroup), Transform(combined_eqs_copy, coulomb_potential_limits))
        self.wait()

        # Solving for potential
        potential_step2 = MathTex("U", "=",  r"-\displaystyle \int_{\infty}^{r'}", "{k", "{q}_1", "{q}_2", r"\over", "r^2}" "d{r}").scale(0.75).next_to(coulomb_potential_limits, DOWN)
        set_math_colors(potential_step2)
        potential_step2.set_color_by_tex("dr", RED_D)
        self.play(FadeIn(potential_step2),run_time=0.5)

        
        potential_step3 = MathTex("U", "=",  r"\displaystyle", "{k", "{q}_1", "{q}_2", r"\over", "{r}}", r"\biggr \rvert _{\infty}^{{r}'}").scale(0.75).next_to(potential_step2, DOWN)
        set_math_colors(potential_step3)
        potential_step3.set_color_by_tex("r}", RED_B)
        self.play(FadeIn(potential_step3),run_time=0.5)

        potential_step4 = MathTex("U", "=",  r"\displaystyle", "{k", "{q}_1", "{q}_2", r"\over", "{r}'}").scale(0.75).next_to(potential_step3, DOWN).shift(UP*0.25)
        set_math_colors(potential_step4)

        zero_term = MathTex(r"-\displaystyle", "{k", "{q}_1", "{q}_2", r"\over", r"\infty}").scale(0.75).next_to(potential_step4, RIGHT)
        set_math_colors(zero_term)

        self.play(FadeIn(potential_step4, zero_term),run_time=0.5)

        zero = Tex(r"$-0$").scale(0.75).next_to(potential_step4, RIGHT)
        self.play(Transform(zero_term,zero),run_time=0.5)
        self.play(FadeOut(zero_term),run_time=1)
        self.wait()

        # in-person shot here

        self.play(FadeOut(combined_eqs_copy, potential_step2, potential_step3,
                          coulomb_force_label, ds_force_label),
                  potential_step4.animate.next_to(integral_sum_label, DOWN))

        voltage_label = MathTex("V", "=", r"\displaystyle", r"{U", r"\over", "{q}_2}", "=", r"{k", "{q}_1", r"\over", "{r}}").scale(0.75).next_to(potential_step4, DOWN)
        set_math_colors(voltage_label)

        voltage_label_final = MathTex("V", "=", r"\displaystyle", "{U", r"\over", "{q}}", "=", "{k", "{q}", r"\over", "{r}}").scale(0.75).next_to(potential_step4, DOWN)
        set_math_colors(voltage_label_final)

        self.play(FadeIn(voltage_label))
        self.wait()
        self.play(Transform(voltage_label, voltage_label_final))

        self.wait()

        voltage_final_equations = VGroup(integral_sum_label, potential_step4, voltage_label)
        self.play(voltage_final_equations.animate.shift(DOWN*2))

        voltage_header = Text(r"Voltage").scale(0.75).scale(2).to_edge(UP)
        self.play(FadeIn(voltage_header))
        self.wait()

        u_int_rect = SurroundingRectangle(integral_sum_label)
        self.play(DrawBorderThenFill(u_int_rect), voltage_label.animate.move_to(potential_step4),
                   FadeOut(potential_step4), run_time=2)
        self.wait()

        u_integral_step1 = MathTex("{U", r"\over", "{q}}", "=",  "-{1", r"\over", "{q}}", r"\displaystyle \int", r"\vec{F}", r"\cdot", r"d\vec{s}").scale(0.75).move_to(integral_sum_label)
        set_math_colors(u_integral_step1)
        u_integral_step1.set_color_by_tex(r"\vec{s}", BLUE)
            
        self.play(Transform(integral_sum_label, u_integral_step1), FadeOut(u_int_rect))
        self.wait()
        voltage_integral = MathTex("V", "=", r"-\displaystyle \int", r"\vec{E}", r"\cdot", r"d\vec{s}").scale(0.75).move_to(integral_sum_label)
        set_math_colors(voltage_integral)
        voltage_integral.set_color_by_tex(r"\vec{s}", BLUE)

        self.play(Transform(integral_sum_label, voltage_integral))
        self.wait()

        voltage_integral_limits = MathTex("V", "=", r"-\displaystyle \int_{\infty}^{r'}", r"\vec{E}", r"\cdot", r"d\vec{s}").scale(0.75).move_to(integral_sum_label)
        set_math_colors(voltage_integral_limits)
        voltage_integral_limits.set_color_by_tex(r"\vec{s}", BLUE)
        self.play(Transform(integral_sum_label, voltage_integral_limits))
        self.wait()

        
        delta_voltage_integral = MathTex(r"\Delta V", "=", r"-\displaystyle \int_{a}^{b}", r"\vec{E}", r"\cdot", r"d\vec{s}").scale(0.75).next_to(integral_sum_label, DOWN)
        set_math_colors(delta_voltage_integral)
        delta_voltage_integral.set_color_by_tex(r"\vec{s}", BLUE)

        self.play(FadeIn(delta_voltage_integral), voltage_label.animate.next_to(delta_voltage_integral, DOWN))
        self.wait()

class FourQuantities(Scene):
    def construct(self):

        f_circ = Circle().to_edge(UL).set_color(WHITE)
        e_circ = f_circ.copy().to_edge(DL).set_color(RED)
        v_circ = f_circ.copy().to_edge(DR).set_color(BLUE)
        u_circ = f_circ.copy().to_edge(UR).set_color(GREEN)

        force_label = Tex(r"$F$").move_to(f_circ).set_color(WHITE)
        e_label = Tex(r"$E$").move_to(e_circ).set_color(RED)
        voltage_label = Tex(r"$V$").move_to(v_circ).set_color(BLUE)
        potential_label = Tex(r"$U$").move_to(u_circ).set_color(GREEN)

        f_eqn = Tex(r"$\frac{kq_1q_2}{r^2}$").scale(0.75).next_to(force_label,DOWN,buff=0.2)
        e_eqn = Tex(r"$\frac{kq}{r^2}$").scale(0.75).next_to(e_label,DOWN,buff=0.2).set_color(RED)
        v_eqn = Tex(r"$\frac{kq}{r}$").scale(0.75).next_to(voltage_label,DOWN,buff=0.2).set_color(BLUE)
        u_eqn = Tex(r"$\frac{kq_1q_2}{r}$").scale(0.75).next_to(potential_label,DOWN,buff=0.2).set_color(GREEN)

        f_to_e = Vector(2*DOWN).shift(LEFT*5+UP)
        e_to_f = Vector(2*UP).shift(LEFT*6+DOWN)

        e_to_v = Vector(8*RIGHT).shift(2*DOWN+4*LEFT)
        v_to_e = Vector(8*LEFT).shift(3*DOWN+4*RIGHT)

        u_to_v = Vector(2*DOWN).shift(RIGHT*6+UP)
        v_to_u = Vector(2*UP).shift(RIGHT*5+DOWN)

        f_to_u = Vector(8*RIGHT).shift(3*UP+4*LEFT)
        u_to_f = Vector(8*LEFT).shift(2*UP+4*RIGHT)

        divide_q_symbol = Tex(r"$\div q$")
        multiply_q_symbol = Tex(r"$\times q$")

        fe_label = divide_q_symbol.copy().shift(4.5*LEFT)
        uv_label = divide_q_symbol.copy().shift(6.5*RIGHT)

        ef_label = multiply_q_symbol.copy().shift(6.5*LEFT)
        vu_label = multiply_q_symbol.copy().shift(4.5*RIGHT)

        ev_label = Tex(r"$- \int \vec{E} \cdot d\vec{s}$").shift(1.5*DOWN)
        ve_label = Tex(r"$-\frac{dV}{ds}$").shift(3.5*DOWN)

        fu_label = Tex(r"$- \int \vec{F} \cdot d\vec{s}$").shift(3.5*UP)
        uf_label = Tex(r"$-\frac{dU}{ds}$").shift(1.5*UP)

        self.play(Write(f_circ))
        self.wait()
        self.play(FadeIn(force_label)) 
        self.wait()
        self.play(FadeIn(f_eqn))
        self.wait()

        self.play(Write(e_circ))
        self.wait()
        self.play(FadeIn(e_label)) 
        self.wait()
        self.play(FadeIn(e_eqn))
        self.wait()

        self.play(Write(v_circ))
        self.wait()
        self.play(FadeIn(voltage_label)) 
        self.wait()
        self.play(FadeIn(v_eqn))
        self.wait()

        self.play(Write(u_circ))
        self.wait()
        self.play(FadeIn(potential_label)) 
        self.wait()
        self.play(FadeIn(u_eqn))
        self.wait()

        self.play(FadeIn(f_to_e,e_to_f,fe_label,ef_label))
        self.wait()

        self.play(FadeIn(u_to_v,v_to_u,uv_label,vu_label))
        self.wait()

        self.play(FadeIn(e_to_v,v_to_e,ev_label,ve_label))
        self.wait()
        
        self.play(FadeIn(f_to_u,fu_label,u_to_f,uf_label))
        self.wait()
