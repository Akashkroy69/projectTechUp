from manim import *

class OSAsMiddleman(Scene):
    def construct(self):
        # Title Scene
        title = Text("Operating System: The Middleman", font_size=48).shift(UP * 2)
        self.play(FadeIn(title), title.animate.scale(1.1))
        self.wait(1)
        
        # Main Elements
        user = Text("User").shift(LEFT * 4 + UP * 1.5)
        application = Text("Application").shift(LEFT * 4)
        hardware = Text("Hardware").shift(LEFT * 4 + DOWN * 1.5)
        os_box = Text("Operating System", font_size=32).shift(RIGHT * 1.5)
        
        # Arrows Showing Interaction
        user_to_os = Arrow(user.get_right(), os_box.get_left(), buff=0.3, color=WHITE)
        app_to_os = Arrow(application.get_right(), os_box.get_left(), buff=0.3, color=WHITE)
        os_to_hardware = Arrow(os_box.get_right(), hardware.get_left(), buff=0.3, color=WHITE)
        
        # Display Elements
        self.play(Write(user), Write(application), Write(hardware), FadeIn(os_box))
        self.play(GrowArrow(user_to_os), GrowArrow(app_to_os), GrowArrow(os_to_hardware))
        self.wait(1)
        
        # OS Highlighting
        self.play(os_box.animate.scale(1.2).set_color(YELLOW), run_time=0.5)
        self.wait(1)
        
        # Summary Text
        summary = Text("OS acts as a bridge between User, Applications, and Hardware.", font_size=28).shift(DOWN * 2)
        self.play(FadeIn(summary))
        self.wait(2)
        
        # Fade Out Animation
        self.play(FadeOut(title, user, application, hardware, os_box, user_to_os, app_to_os, os_to_hardware, summary))
        self.wait(1)
