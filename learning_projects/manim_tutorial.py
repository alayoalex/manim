from manimlib.imports import *
import os
import pyclbr
import numpy as np

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.add(line)
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.play(Transform(line,triangle))


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)
        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))


class TryShapes(Scene):
    #My own scenes.
    def construct(self):
        pol = Polygon(np.array([0,0,0]),np.array([1,0,0]),np.array([1,1,0]), np.array([0,1,0]))
        self.play(GrowFromCenter(pol))
        self.play(Rotate(pol))


class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)
        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
        ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))


class TryAddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Christ Lives")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("God is Good")
        quote2.set_color(YELLOW)
        author=TextMobject("-Holly Bible")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(Transform(quote,quote2),
        ApplyMethod(author.to_corner,quote2.get_corner(DOWN+RIGHT)+DOWN+2*RIGHT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))


class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=.5)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=.5)
        label_group=VGroup(label.bg,label) #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)
        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))
        self.play(Rotate(label.bg))


class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)
        self.play(Write(eq1))
        self.play(Write(eq2))


class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject(r"\text{ The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }", 
        r"\text{of an objet of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ". ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))


class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
    },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
        ])
        
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()
    
    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)
    
    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
        
        self.Positron().move_to(point)
            for point in points
        ])
        
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)
    
    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield
    
    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
            "radius" : 0.2,
            "stroke_width" : 3,
            "color" : RED,
            "fill_color" : RED,
            "fill_opacity" : 0.5,
        }
        
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
    "color" : RED_B
    },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)
        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
        ])        
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)
    
    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001: #Prevent divide by zero ##Note: This won't work - fix this
            efield = np.array((0,0,0))
        else:
            efield = (observation_point - source_point)/r**3
        return efield

    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
    
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
    
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())
        
            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)
    
    class Positron(Circle):
        CONFIG = {
            "radius" : 0.2,
            "stroke_width" : 3,
            "color" : RED,
            "fill_color" : RED,
            "fill_opacity" : 0.5,
        }
    
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)