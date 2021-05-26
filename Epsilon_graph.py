from manim import *
import math


class graph(Scene):
    def construct(self):

        ############################## Setup ############################################################################################################

        x_axes_min = 0

        x_axes_max = 10

        y_axes_min = -5

        y_axes_max = 5

        axes_color = BLUE # Can use default colors or use hex colors in quotation marks

        dot_radius = 0.1

        dot_color = YELLOW

        function = lambda x: math.cos(x) + math.sin(2*x)   # This is the funtion to plot

        function_color = WHITE # Set the color of the graph of the function

        epsilon_seperation_y_axis = 1 # Seperation of the y axis epsilons

        epsilon_seperation_x_axis = 1 # Seperation fo the x axis epsilons

        Epsilon_y_bottom = " - \\epsilon"

        Epsilon_y_top = " + \\epsilon"

        Epsilon_x_left = " - \\epsilon"
        
        Epsilon_x_right = " + \\epsilon"

        Horizontal_line_opacity = 0.8 # set to a value between 1 and 0

        Horizontal_line_color = WHITE # set to a default color or Hexidecimal color in quotation marks

        Vertical_line_opacity = 0.8

        Vertical_line_color = WHITE

        Horizontal_box_color = BLUE

        Vertical_box_color = BLUE

        Horizontal_box_opacity = 0.2
        
        Vertical_box_opacity = 0.2


        

        ############################## Code #############################################################################################################
        
        axes = Axes(x_range = [x_axes_min,x_axes_max],y_range= [y_axes_min,y_axes_max])

        axes.set_color(axes_color)

        dot = Dot(radius = dot_radius).set_color(dot_color)

        x_position = ValueTracker(0)

        graph = axes.get_graph(function).set_color(function_color)

        MathTex_Epsilon_y_bottom = MathTex(Epsilon_y_bottom)
        MathTex_Epsilon_y_top = MathTex(Epsilon_y_top)
        MathTex_Epsilon_x_left = MathTex(Epsilon_x_left)
        MathTex_Epsilon_x_right = MathTex(Epsilon_x_right)

        #Horizontal lines

        Epsilon_y_top_line = DashedLine([0,function(x_position.get_value()) + (0.5 * epsilon_seperation_y_axis),0],[x_axes_max,function(x_position.get_value()) + (0.5 * epsilon_seperation_y_axis),0]).set_opacity(0.8)
        Epsilon_y_bottom_line = DashedLine([0,function(x_position.get_value()) - (0.5 * epsilon_seperation_y_axis),0],[x_axes_max,function(x_position.get_value()) - (0.5 * epsilon_seperation_y_axis),0]).set_opacity(0.8)
        
        # Vertical lines

        Epsilon_x_left_line = DashedLine([MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(Vertical_line_opacity).set_color(Vertical_line_color)
        Epsilon_x_right_line = DashedLine([MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(Vertical_line_opacity).set_color(Vertical_line_color)

        Horizontal_polygon = Polygon([axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_bottom.get_center()[1],0],[axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_top.get_center()[1],0],[axes.coords_to_point(x_axes_max,0)[1],MathTex_Epsilon_y_top.get_center()[1],0],[axes.coords_to_point(x_axes_max,0)[0],MathTex_Epsilon_y_bottom.get_center()[1],0]).set_opacity(0.2)
        Vertical_polygon = Polygon([MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0],[MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(0.2)
        #Vertical_polygon = Polygon([MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[])

        def Vertical_Polygon_updater(obj):
            obj.become(Polygon([MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0],[MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(Vertical_box_opacity).set_color(Vertical_box_color))

        
        def Horizontal_polygon_updater(obj):
            obj.become(Polygon([axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_bottom.get_center()[1],0],[axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_top.get_center()[1],0],[axes.coords_to_point(x_axes_max,0)[0],MathTex_Epsilon_y_top.get_center()[1],0],[axes.coords_to_point(x_axes_max,0)[0],MathTex_Epsilon_y_bottom.get_center()[1],0]).set_opacity(Horizontal_box_opacity).set_color(Horizontal_box_color))
       
        def Epsilon_x_left_line_updater(obj):
            obj.become(DashedLine([MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_left.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(Vertical_line_opacity).set_color(Vertical_line_color))

        def Epsilon_x_right_line_updater(obj):
            obj.become(DashedLine([MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_min)[1],0],[MathTex_Epsilon_x_right.get_center()[0],axes.coords_to_point(0,y_axes_max)[1],0]).set_opacity(Vertical_line_opacity).set_color(Vertical_line_color))

        def Epsilon_y_top_line_updater(obj):
            #obj.become(DashedLine([0,function(x_position.get_value()) + (0.5 * epsilon_seperation_y_axis),0],[x_axes_max,function(x_position.get_value()) + (0.5 * epsilon_seperation_y_axis),0]).set_opacity(0.8))
            obj.become(DashedLine([axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_top.get_center()[1],0],[x_axes_max,MathTex_Epsilon_y_top.get_center()[1],0]).set_opacity(Horizontal_line_opacity).set_color(Horizontal_line_color))

        def Epsilon_y_bottom_line_updater(obj):
            #obj.become(DashedLine([0,function(x_position.get_value()) - (0.5 * epsilon_seperation_y_axis),0],[x_axes_max,function(x_position.get_value()) - (0.5 * epsilon_seperation_y_axis),0]).set_opacity(0.8))
            obj.become(DashedLine([axes.coords_to_point(0,0)[0],MathTex_Epsilon_y_bottom.get_center()[1],0],[x_axes_max,MathTex_Epsilon_y_bottom.get_center()[1],0]).set_opacity(Horizontal_line_opacity).set_color(Horizontal_line_color))
        
        def dot_updater(obj):
            reference_dot = Dot(radius = dot_radius).set_color(dot_color).move_to(axes.coords_to_point(0,function(0)))
            obj.become(reference_dot.move_to(axes.coords_to_point(x_position.get_value(),function(x_position.get_value()))))

        def Epsilon_y_bottom_updater(obj):
            reference = MathTex(Epsilon_y_bottom)
            obj.become(reference.move_to(axes.coords_to_point(-0.25,function(x_position.get_value()) - (0.5 * epsilon_seperation_y_axis))))

        def Epsilon_y_top_updater(obj):
            reference = MathTex(Epsilon_y_top)
            obj.become(reference.move_to(axes.coords_to_point(-0.25,function(x_position.get_value()) + (0.5 * epsilon_seperation_y_axis))))

        def Epsilon_x_left_updater(obj):
            reference = MathTex(Epsilon_x_left)
            obj.become(reference.move_to(axes.coords_to_point(x_position.get_value() - (0.5 * epsilon_seperation_x_axis),-0.25)))

        def Epsilon_x_right_updater(obj):
            reference = MathTex(Epsilon_x_right)
            obj.become(reference.move_to(axes.coords_to_point(x_position.get_value() + (0.5 * epsilon_seperation_x_axis),-0.25)))




        # add updaters

        dot.add_updater(dot_updater)

        
        MathTex_Epsilon_y_bottom.add_updater(Epsilon_y_bottom_updater)

        MathTex_Epsilon_y_top.add_updater(Epsilon_y_top_updater)

        MathTex_Epsilon_x_left.add_updater(Epsilon_x_left_updater)

        MathTex_Epsilon_x_right.add_updater(Epsilon_x_right_updater)

        Epsilon_y_top_line.add_updater(Epsilon_y_top_line_updater)

        Epsilon_y_bottom_line.add_updater(Epsilon_y_bottom_line_updater)

        Epsilon_x_left_line.add_updater(Epsilon_x_left_line_updater)

        Epsilon_x_right_line.add_updater(Epsilon_x_right_line_updater)

        Horizontal_polygon.add_updater(Horizontal_polygon_updater)

        Vertical_polygon.add_updater(Vertical_Polygon_updater)



        

        # Animations

        self.play(Create(axes))

        self.wait(1)





        self.play(Create(graph),Write(MathTex_Epsilon_x_left),Write(MathTex_Epsilon_x_right),Write(MathTex_Epsilon_y_top),Write(MathTex_Epsilon_y_bottom),Create(dot),Create(Epsilon_y_bottom_line),Create(Epsilon_y_top_line),Create(Epsilon_x_right_line),Create(Epsilon_x_left_line),Create(Vertical_polygon),Create(Horizontal_polygon))
        self.add(MathTex_Epsilon_y_bottom,MathTex_Epsilon_y_top,MathTex_Epsilon_x_right,MathTex_Epsilon_x_left,dot,Epsilon_y_top_line,Epsilon_y_bottom_line,Epsilon_x_left_line,Epsilon_x_right_line,Horizontal_polygon,Vertical_polygon)

        self.wait(1)

############################################################# Make your own animations ############################################################################################################################################################################################################################################################################

    # To move the dot, lines, and rectangles use self.play(x_position.animate.set_value(What I want x to be),run_time(How long I want it to take in seconds))
    # Unfortunatly indicate doesn't seem to do anything for Polygons


        self.play(x_position.animate.set_value(9),run_time = 10)
        self.wait(1)
        # self.play(Indicate(Horizontal_polygon))
        # self.wait(1)
        # self.play(Indicate(Vertical_polygon))
        # self.wait(1)
        



