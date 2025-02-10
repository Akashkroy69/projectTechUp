from manim import *

class visPrint(Scene):
    def construct(self):
        # Title Scene
        title = Text("How printf() Works in C", font_size=48).shift(UP * 3)
        self.play(FadeIn(title), title.animate.scale(1.1))
        self.wait(1)
        
        # Creating Components
        printf_func = Text("printf()", font_size=36).shift(UP * 2)
        glibc_layer = Text("glibc (Standard Library)", font_size=32).shift(UP * 1)
        write_syscall = Text("write() System Call", font_size=32)
        kernel_layer = Text("Kernel", font_size=32).shift(DOWN * 1)
        stdout_layer = Text("Standard Output (Terminal)", font_size=32).shift(DOWN * 2)
        
        # Creating Boxes Around Components
        printf_box = SurroundingRectangle(printf_func, color=BLUE)
        glibc_box = SurroundingRectangle(glibc_layer, color=GREEN)
        write_box = SurroundingRectangle(write_syscall, color=YELLOW)
        kernel_box = SurroundingRectangle(kernel_layer, color=RED)
        stdout_box = SurroundingRectangle(stdout_layer, color=PURPLE)
        
        # Displaying Components with Boxes
        self.play(FadeIn(printf_func, printf_box))
        self.wait(0.5)
        self.play(FadeIn(glibc_layer, glibc_box))
        self.wait(0.5)
        self.play(FadeIn(write_syscall, write_box))
        self.wait(0.5)
        self.play(FadeIn(kernel_layer, kernel_box))
        self.wait(0.5)
        self.play(FadeIn(stdout_layer, stdout_box))
        self.wait(1)
        
        # Creating Arrows Between Layers
        printf_to_glibc = Arrow(printf_func.get_bottom(), glibc_layer.get_top(), buff=0.2)
        glibc_to_write = Arrow(glibc_layer.get_bottom(), write_syscall.get_top(), buff=0.2)
        write_to_kernel = Arrow(write_syscall.get_bottom(), kernel_layer.get_top(), buff=0.2)
        kernel_to_stdout = Arrow(kernel_layer.get_bottom(), stdout_layer.get_top(), buff=0.2)
        
        # Animating Arrows
        self.play(GrowArrow(printf_to_glibc))
        self.wait(0.3)
        self.play(GrowArrow(glibc_to_write))
        self.wait(0.3)
        self.play(GrowArrow(write_to_kernel))
        self.wait(0.3)
        self.play(GrowArrow(kernel_to_stdout))
        self.wait(1)
        
        # Summary Text
        summary = Text("printf() calls glibc -> write() -> Kernel -> Terminal", font_size=28).shift(DOWN * 3)
        self.play(FadeIn(summary))
        self.wait(2)
        
        # Fade Out Animation
        self.play(FadeOut(title, printf_func, glibc_layer, write_syscall, kernel_layer, stdout_layer,
                          printf_box, glibc_box, write_box, kernel_box, stdout_box,
                          printf_to_glibc, glibc_to_write, write_to_kernel, kernel_to_stdout, summary))
        self.wait(1)
