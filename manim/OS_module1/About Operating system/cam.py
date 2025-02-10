from manim import *

class cam(Scene):
    def construct(self):
        # Title
        title = Text("Taking a Picture: OS Communication Flow", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create components
        user = Text("User", font_size=24).to_edge(UP)
        app = Text("Camera App", font_size=24).next_to(user, DOWN, buff=1)
        os = Text("Operating System", font_size=24).next_to(app, DOWN, buff=1)
        driver = Text("Device Driver", font_size=24).next_to(os, DOWN, buff=1)
        hardware = Text("Camera Hardware", font_size=24).next_to(driver, DOWN, buff=1)

        # Arrows for flow
        arrow1 = Arrow(user.get_bottom(), app.get_top(), buff=0.1)
        arrow2 = Arrow(app.get_bottom(), os.get_top(), buff=0.1)
        arrow3 = Arrow(os.get_bottom(), driver.get_top(), buff=0.1)
        arrow4 = Arrow(driver.get_bottom(), hardware.get_top(), buff=0.1)
        arrow5 = Arrow(hardware.get_top(), driver.get_bottom(), buff=0.1)
        arrow6 = Arrow(driver.get_top(), os.get_bottom(), buff=0.1)
        arrow7 = Arrow(os.get_top(), app.get_bottom(), buff=0.1)
        arrow8 = Arrow(app.get_top(), user.get_bottom(), buff=0.1)

        # Animate components and arrows
        self.play(FadeIn(user), FadeIn(app), FadeIn(os), FadeIn(driver), FadeIn(hardware))
        self.wait(1)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4))
        self.wait(1)
        self.play(Create(arrow5), Create(arrow6), Create(arrow7), Create(arrow8))
        self.wait(2)

        # Highlight OS role
        os_box = SurroundingRectangle(os, color=YELLOW)
        self.play(Create(os_box))
        self.wait(1)
        os_text = Text("OS Manages Communication", font_size=24).next_to(os_box, DOWN)
        self.play(Write(os_text))
        self.wait(2)

        # Fade out
        self.play(FadeOut(user), FadeOut(app), FadeOut(os), FadeOut(driver), FadeOut(hardware),
                  FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3), FadeOut(arrow4),
                  FadeOut(arrow5), FadeOut(arrow6), FadeOut(arrow7), FadeOut(arrow8),
                  FadeOut(os_box), FadeOut(os_text))
        self.wait(1)

# # Run the scene
# if __name__ == "__main__":
#     scene = CameraAppFlow()
#     scene.render()