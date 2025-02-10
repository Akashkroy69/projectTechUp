from manim import *

class TimeSharingRailwayImproved(Scene):
    def construct(self):
        # Config
        num_users = 4
        initial_seats = 8
        user_colors = [BLUE, YELLOW, GREEN, RED]
        
        # Setup Users (Left Side)
        users = VGroup(*[
            VGroup(
                Rectangle(width=2, height=1, color=color, fill_opacity=0.2),
                Text(f"User {i+1}", font_size=24),
                Text("Click!", color=WHITE, font_size=20).move_to(DOWN * 0.3)
            ).arrange(DOWN, buff=0.2).shift(LEFT * 4 + UP * (1.5 - i * 1.5))
            for i, color in enumerate(user_colors)
        ])
        
        # Setup CPU + Timeline (Center)
        cpu = Circle(radius=0.8, color=WHITE).shift(RIGHT * 2)
        cpu_label = Text("Time-Sharing CPU", font_size=24).next_to(cpu, UP)
        
        # Timeline dots to show time slices
        timeline = VGroup(*[Dot(radius=0.08) for _ in range(6)]).arrange(RIGHT, buff=0.4).next_to(cpu, DOWN, buff=1)
        timeline_labels = VGroup(*[
            Text(f"T{i+1}", font_size=20).next_to(dot, DOWN)
            for i, dot in enumerate(timeline)
        ])
        
        # Seat Database (Right Side)
        database = VGroup(
            Rectangle(width=3, height=2, color=GREEN),
            Text("RAILWAY DATABASE", font_size=24),
            Text(f"Seats Available: {initial_seats}", font_size=20).shift(DOWN * 0.5)
        ).shift(RIGHT * 4)
        
        # Draw all components
        self.play(
            LaggedStart(
                Create(users),
                Create(cpu), Write(cpu_label),
                Create(timeline), Write(timeline_labels),
                Create(database),
                lag_ratio=0.5
            )
        )
        self.wait(1)
        
        # Animate concurrent requests and time slices
        current_seats = initial_seats
        seat_text = database[2]
        time_slice_highlights = []
        
        for time_slice in range(6):  # 6 time slices
            # Highlight current time slice on timeline
            tl_highlight = timeline[time_slice].copy().set(color=YELLOW, radius=0.12)
            time_slice_highlights.append(tl_highlight)
            self.play(TransformFromCopy(timeline[time_slice], tl_highlight))
            
            # Select user for this slice (round-robin)
            user_idx = time_slice % num_users
            user = users[user_idx]
            user_color = user_colors[user_idx]
            
            # Simulate user request
            request_arrow = Arrow(
                user.get_right(), cpu.get_left(),
                color=user_color, buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            
            # Animate request -> CPU -> Database
            self.play(
                user[2].animate.set_color(user_color),  # Highlight "Click!"
                Create(request_arrow),
                run_time=0.3
            )
            
            # CPU processing animation
            cpu_swirl = VGroup(
                Arc(radius=0.5, start_angle=0, angle=TAU/2, color=user_color),
                Arc(radius=0.5, start_angle=TAU/2, angle=TAU/2, color=user_color)
            ).move_to(cpu)
            self.play(
                Rotate(cpu_swirl, angle=PI, rate_func=linear),
                FadeOut(request_arrow),
                run_time=0.5
            )
            
            # Update database if seats are available
            if current_seats > 0:
                current_seats -= 1
                new_seat_text = Text(f"Seats Available: {current_seats}", font_size=20).move_to(seat_text)
                self.play(
                    seat_text.animate.become(new_seat_text),
                    Indicate(database[0], color=RED),  # Flash the database
                    run_time=0.3
                )
            
            # Reset user "Click!" color
            self.play(user[2].animate.set_color(WHITE))
            self.remove(cpu_swirl)
        
        # Final state
        self.play(
            LaggedStart(*[FadeOut(h) for h in time_slice_highlights]),
            run_time=1
        )
        self.wait(2)