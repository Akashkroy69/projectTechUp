from manim import *

class OSstr(Scene):
    def construct(self):
        # Title Scene
        title = Text("Operating System Structure", font_size=48).shift(UP * 3)
        self.play(FadeIn(title), title.animate.scale(1.1))
        self.wait(1)
        
        # Creating OS Structure Components
        user_layer = Text("User", font_size=32).shift(UP * 2)
        application_layer = Text("Applications", font_size=32).shift(UP * 1)
        os_layer = Text("Operating System", font_size=32)
        kernel_layer = Text("Kernel", font_size=32).shift(DOWN * 1)
        hardware_layer = Text("Hardware", font_size=32).shift(DOWN * 2)
        
        # Creating Boxes Around Components
        user_box = SurroundingRectangle(user_layer, color=BLUE)
        application_box = SurroundingRectangle(application_layer, color=GREEN)
        os_box = SurroundingRectangle(os_layer, color=YELLOW)
        kernel_box = SurroundingRectangle(kernel_layer, color=RED)
        hardware_box = SurroundingRectangle(hardware_layer, color=PURPLE)
        
        # Displaying Components with Boxes
        self.play(FadeIn(user_layer, user_box))
        self.wait(0.5)
        self.play(FadeIn(application_layer, application_box))
        self.wait(0.5)
        self.play(FadeIn(os_layer, os_box))
        self.wait(0.5)
        self.play(FadeIn(kernel_layer, kernel_box))
        self.wait(0.5)
        self.play(FadeIn(hardware_layer, hardware_box))
        self.wait(1)
        
        # Creating Arrows Between Layers
        user_to_app = Arrow(user_layer.get_bottom(), application_layer.get_top(), buff=0.2)
        app_to_os = Arrow(application_layer.get_bottom(), os_layer.get_top(), buff=0.2)
        os_to_kernel = Arrow(os_layer.get_bottom(), kernel_layer.get_top(), buff=0.2)
        kernel_to_hardware = Arrow(kernel_layer.get_bottom(), hardware_layer.get_top(), buff=0.2)
        
        # Animating Arrows
        self.play(GrowArrow(user_to_app))
        self.wait(0.3)
        self.play(GrowArrow(app_to_os))
        self.wait(0.3)
        self.play(GrowArrow(os_to_kernel))
        self.wait(0.3)
        self.play(GrowArrow(kernel_to_hardware))
        self.wait(1)
        
        # Summary Text
        summary = Text("OS Structure: Layers for efficient management and interaction.", font_size=28).shift(DOWN * 3)
        self.play(FadeIn(summary))
        self.wait(2)
        
        # Fade Out Animation
        self.play(FadeOut(title, user_layer, application_layer, os_layer, kernel_layer, hardware_layer,
                          user_box, application_box, os_box, kernel_box, hardware_box,
                          user_to_app, app_to_os, os_to_kernel, kernel_to_hardware, summary))
        self.wait(1)
