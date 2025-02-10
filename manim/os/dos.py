from manim import *

class DistributedNetflixFinal(Scene):
    def construct(self):
        # Config
        num_servers = 5
        server_colors = [BLUE, YELLOW, GREEN, RED, PURPLE]
        
        # User Device (Bottom Left)
        user = VGroup(
            Rectangle(width=2, height=1.5, color=WHITE, fill_opacity=0.2),
            Text("User Device", font_size=24),
            Text("Watching Netflix", font_size=20, color=BLUE).shift(DOWN * 0.3)
        ).to_edge(DL, buff=1)  # Bottom Left with buffer
        
        # Content Delivery Network (CDN) Servers (Top Center)
        cdn_servers = VGroup(*[
            VGroup(
                Rectangle(width=1.5, height=1, color=color, fill_opacity=0.2),
                Text(f"CDN {i+1}", font_size=20)
            ).shift(UP * 1.5 + RIGHT * (i - 2.5) * 2)  # Adjusted spacing
            for i, color in enumerate(server_colors[:num_servers])
        ])
        
        # Data Centers (Top Right)
        data_centers = VGroup(*[
            VGroup(
                Rectangle(width=2, height=1.5, color=GRAY, fill_opacity=0.2),
                Text(f"Data Center {i+1}", font_size=20)
            ).shift(UP * 1.5 + RIGHT * 5 + DOWN * i * 2)  # Moved further right
            for i in range(2)
        ])
        
        # Draw all components
        self.play(
            LaggedStart(
                Create(user),
                Create(cdn_servers),
                Create(data_centers),
                lag_ratio=0.5
            )
        )
        self.wait(1)
        
        # User requests content
        request_arrow = Arrow(
            user.get_top(), cdn_servers[2].get_bottom(),
            color=BLUE, buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
        self.play(
            Create(request_arrow),
            user[2].animate.set_color(YELLOW),  # Highlight "Watching Netflix"
            run_time=0.5
        )
        
        # CDN Server processes request
        cdn_highlight = cdn_servers[2].copy().set_stroke(color=YELLOW, width=4)
        self.play(
            Create(cdn_highlight),
            FadeOut(request_arrow),
            run_time=0.5
        )
        
        # Check if content is available in CDN
        content_found = False
        if not content_found:
            # Request forwarded to Data Center
            dc_request_arrow = Arrow(
                cdn_servers[2].get_top(), data_centers[0].get_bottom(),
                color=RED, buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            self.play(
                Create(dc_request_arrow),
                cdn_highlight.animate.set_stroke(color=RED),
                run_time=0.5
            )
            
            # Data Center processes request
            dc_highlight = data_centers[0].copy().set_stroke(color=YELLOW, width=4)
            self.play(
                Create(dc_highlight),
                FadeOut(dc_request_arrow),
                run_time=0.5
            )
            
            # Data Center sends content to CDN
            content_arrow = Arrow(
                data_centers[0].get_bottom(), cdn_servers[2].get_top(),
                color=GREEN, buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            self.play(
                Create(content_arrow),
                dc_highlight.animate.set_stroke(color=GREEN),
                run_time=0.5
            )
            
            # CDN caches content and sends to user
            cdn_to_user_arrow = Arrow(
                cdn_servers[2].get_bottom(), user.get_top(),
                color=GREEN, buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            self.play(
                Create(cdn_to_user_arrow),
                cdn_highlight.animate.set_stroke(color=GREEN),
                run_time=0.5
            )
            content_found = True
        
        # User receives content
        self.play(
            FadeOut(cdn_to_user_arrow),
            user[2].animate.set_color(GREEN),  # Highlight "Watching Netflix"
            run_time=0.5
        )
        
        # Load balancing example
        self.play(
            FadeOut(cdn_highlight),
            FadeOut(dc_highlight)
        )
        self.wait(1)
        
        # Simulate load balancing across CDN servers
        for i in range(num_servers):
            request_arrow = Arrow(
                user.get_top(), cdn_servers[i].get_bottom(),
                color=server_colors[i], buff=0.1,
                max_tip_length_to_length_ratio=0.15
            )
            self.play(
                Create(request_arrow),
                user[2].animate.set_color(server_colors[i]),
                run_time=0.3
            )
            self.play(FadeOut(request_arrow))
        
        self.wait(2)