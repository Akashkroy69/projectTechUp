from manim import *

class MultiProgrammingOS(Scene):
   def construct(self):
        # Title
        title = Text("Multi-Programming OS with Waiting State").to_edge(UP)
        self.play(Write(title))

        # Represent the CPU
        cpu = Rectangle(width=2, height=1, color=BLUE).shift(LEFT * 4)
        cpu_text = Text("CPU").move_to(cpu.get_center())
        self.play(Create(cpu), Write(cpu_text))

        # Ready Queue (Processes)
        ready_queue = VGroup(
            Rectangle(width=1.5, height=0.8, color=YELLOW).shift(LEFT * 2),
            Rectangle(width=1.5, height=0.8, color=YELLOW),
            Rectangle(width=1.5, height=0.8, color=YELLOW).shift(RIGHT * 2),
        )
        queue_labels = VGroup(
            Text("P1").move_to(ready_queue[0].get_center()),
            Text("P2").move_to(ready_queue[1].get_center()),
            Text("P3").move_to(ready_queue[2].get_center()),
        )
        queue_group = VGroup(ready_queue, queue_labels)
        self.play(Create(ready_queue), Write(queue_labels))

        # Resource Sharing (Memory and I/O Devices)
        io_device = Rectangle(width=2.5, height=1, color=ORANGE).shift(RIGHT * 3 + DOWN * 2)
        io_text = Text("I/O Device").move_to(io_device.get_center())
        self.play(Create(io_device), Write(io_text))

        # Simulate CPU Execution and I/O Waiting
        # Step 1: P1 moves to CPU
        cpu_arrow_p1 = Arrow(start=queue_labels[0].get_right(), end=cpu.get_left(), buff=0.1, color=RED)
        self.play(GrowArrow(cpu_arrow_p1))
        self.play(FadeOut(queue_labels[0]), FadeOut(ready_queue[0]))
        p1 = Text("P1").move_to(cpu.get_center())
        self.play(Write(p1))
        self.wait(1)

        # Step 2: P1 goes into I/O waiting
        io_arrow_p1 = Arrow(start=cpu.get_right(), end=io_device.get_left(), buff=0.2, color=PURPLE)
        self.play(GrowArrow(io_arrow_p1))
        self.play(FadeOut(p1), FadeOut(cpu_arrow_p1))
        p1_waiting = Text("P1 (Waiting)").move_to(io_device.get_center()+20)
        self.play(Write(p1_waiting))
        self.wait(1)

        # Step 3: P2 moves to CPU
        cpu_arrow_p2 = Arrow(start=queue_labels[1].get_right(), end=cpu.get_left(), buff=0.1, color=RED)
        self.play(GrowArrow(cpu_arrow_p2))
        self.play(FadeOut(queue_labels[1]), FadeOut(ready_queue[1]))
        p2 = Text("P2").move_to(cpu.get_center())
        self.play(Write(p2))
        self.wait(1)

        # Step 4: P1 completes I/O and returns to ready queue
        self.play(FadeOut(io_arrow_p1))
        self.play(FadeOut(p1_waiting))
        p1_ready = Rectangle(width=1.5, height=0.8, color=YELLOW).shift(LEFT * 2)
        p1_ready_label = Text("P1").move_to(p1_ready.get_center())
        self.play(Create(p1_ready), Write(p1_ready_label))
        ready_queue.add(p1_ready)
        queue_labels.add(p1_ready_label)
        self.wait(1)

        # End Scene
        end_text = Text("").to_edge(DOWN)
        self.play(Write(end_text))
        self.wait(2)