from manim import *

class MultiprocessingOS(Scene):
    def construct(self):
        # Title
        title = Text("Multiprocessing OS Visualization").to_edge(UP)
        self.play(Write(title))

        # CPUs
        cpu_1 = Rectangle(width=2, height=1, color=BLUE).shift(LEFT * 4 + UP * 2)
        cpu_2 = Rectangle(width=2, height=1, color=BLUE).shift(LEFT * 4 + DOWN * 2)
        cpu_text_1 = Text("CPU 1").move_to(cpu_1.get_center())
        cpu_text_2 = Text("CPU 2").move_to(cpu_2.get_center())
        self.play(Create(cpu_1), Write(cpu_text_1))
        self.play(Create(cpu_2), Write(cpu_text_2))

        # Ready Queue
        ready_queue = VGroup(
            Rectangle(width=1.5, height=0.8, color=YELLOW).shift(LEFT * 2 + UP * 2),
            Rectangle(width=1.5, height=0.8, color=YELLOW).shift(LEFT * 2),
            Rectangle(width=1.5, height=0.8, color=YELLOW).shift(LEFT * 2 + DOWN * 2),
        )
        queue_labels = VGroup(
            Text("P1").move_to(ready_queue[0].get_center()),
            Text("P2").move_to(ready_queue[1].get_center()),
            Text("P3").move_to(ready_queue[2].get_center()),
        )
        self.play(Create(ready_queue), Write(queue_labels))

        # Distribute Processes to CPUs
        # CPU 1 executes P1
        cpu_1_arrow = Arrow(start=queue_labels[0].get_right(), end=cpu_1.get_left(), buff=0.1, color=RED)
        self.play(GrowArrow(cpu_1_arrow))
        self.play(FadeOut(queue_labels[0]), FadeOut(ready_queue[0]))
        executed_p1 = Text("P1").move_to(cpu_1.get_center())
        self.play(Write(executed_p1))

        # CPU 2 executes P2
        cpu_2_arrow = Arrow(start=queue_labels[1].get_right(), end=cpu_2.get_left(), buff=0.1, color=RED)
        self.play(GrowArrow(cpu_2_arrow))
        self.play(FadeOut(queue_labels[1]), FadeOut(ready_queue[1]))
        executed_p2 = Text("P2").move_to(cpu_2.get_center())
        self.play(Write(executed_p2))

        # P3 goes to CPU 1 after P1
        self.wait(1)
        self.play(FadeOut(executed_p1), FadeOut(cpu_1_arrow))
        cpu_1_arrow_next = Arrow(start=queue_labels[2].get_right(), end=cpu_1.get_left(), buff=0.1, color=RED)
        self.play(GrowArrow(cpu_1_arrow_next))
        self.play(FadeOut(queue_labels[2]), FadeOut(ready_queue[2]))
        executed_p3 = Text("P3").move_to(cpu_1.get_center())
        self.play(Write(executed_p3))

        # Simulate Waiting and Resource Sharing
        io_device = Rectangle(width=2.5, height=1, color=ORANGE).shift(RIGHT * 3 + UP * 2)
        io_text = Text("I/O Device").move_to(io_device.get_center())
        self.play(Create(io_device), Write(io_text))

        io_arrow = Arrow(start=cpu_2.get_right(), end=io_device.get_left(), buff=0.2, color=PURPLE)
        self.play(GrowArrow(io_arrow))
        self.play(FadeOut(executed_p2))
        p2_waiting = Text("P2 (Waiting)").move_to(io_device.get_center())
        self.play(Write(p2_waiting))
        self.wait(1)

        # End Scene
        end_text = Text("Multiprocessing OS Visualization Complete").to_edge(DOWN)
        self.play(Write(end_text))
        self.wait(2)
