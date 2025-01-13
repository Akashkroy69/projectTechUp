package applet;
import java.applet.Applet;
import java.awt.Graphics;

public class HelloApplet {
     // Initialize the applet
     public void init() {
        System.out.println("Applet initialized.");
    }

    // Start the applet
    public void start() {
        System.out.println("Applet started.");
    }

    // Stop the applet
    public void stop() {
        System.out.println("Applet stopped.");
    }

    // Destroy the applet
    public void destroy() {
        System.out.println("Applet destroyed.");
    }

    // Draw on the applet
    public void paint(Graphics g) {
        g.drawString("Hello, Applet!", 50, 50);
    }
}
