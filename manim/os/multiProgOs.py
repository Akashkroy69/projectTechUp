from manim import *

class MultiprogrammingOS(Scene):
    def construct(self):
        # Title
        title = Text("Multiprogramming Operating System", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create CPU and Processes
        cpu = Rectangle(width=3, height=1, color=BLUE).to_edge(UP)
        cpu_label = Text("CPU", font_size=24).next_to(cpu, DOWN)
        self.play(Create(cpu), Write(cpu_label))

        # Process queues
        ready_queue = VGroup(*[
            Rectangle(width=2, height=0.5, color=GREEN) for _ in range(3)
        ]).arrange(DOWN, buff=0.2).to_edge(LEFT)
        ready_label = Text("Ready Queue", font_size=20).next_to(ready_queue, DOWN)

        waiting_queue = VGroup(*[
            Rectangle(width=2, height=0.5, color=RED) for _ in range(2)
        ]).arrange(DOWN, buff=0.2).to_edge(RIGHT)
        waiting_label = Text("Waiting Queue", font_size=20).next_to(waiting_queue, DOWN)

        self.play(
            Create(ready_queue),
            Write(ready_label),
            Create(waiting_queue),
            Write(waiting_label)
        )
        self.wait(1)

        # Process labels
        process_labels = [Text(f"P{i+1}", font_size=18) for i in range(5)]
        for label, rect in zip(process_labels[:3], ready_queue):
            label.move_to(rect.get_center())
        for label, rect in zip(process_labels[3:], waiting_queue):
            label.move_to(rect.get_center())

        self.play(*[Write(label) for label in process_labels])
        self.wait(1)

        # Simulate CPU scheduling
        for i in range(3):
            # Move process from ready queue to CPU
            process = ready_queue[i]
            process_label = process_labels[i]
            self.play(
                process.animate.move_to(cpu.get_center()),
                process_label.animate.move_to(cpu.get_center())
            )
            self.wait(1)

            # Simulate execution
            execution_text = Text("Executing...", font_size=20).next_to(cpu, DOWN)
            self.play(Write(execution_text))
            self.wait(1)
            self.play(FadeOut(execution_text))

            # Move process back to ready queue or waiting queue
            if i < 2:
                self.play(
                    process.animate.move_to(ready_queue[i].get_center()),
                    process_label.animate.move_to(ready_queue[i].get_center())
                )
            else:
                self.play(
                    process.animate.move_to(waiting_queue[0].get_center()),
                    process_label.animate.move_to(waiting_queue[0].get_center())
                )
            self.wait(1)

        # End scene
        self.play(FadeOut(cpu), FadeOut(cpu_label), FadeOut(ready_queue), FadeOut(waiting_queue),
                  FadeOut(ready_label), FadeOut(waiting_label), *[FadeOut(label) for label in process_labels])
        self.wait(1)

# Run the scene
# if __name__ == "__main__":
#     scene = MultiprogrammingOS()
#     scene.render()