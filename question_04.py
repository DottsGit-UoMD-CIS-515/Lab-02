import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Function to draw Koch Snowflake recursively
def draw_koch_snowflake(points, depth):
    for i in range(1):
        draw_koch_curve(points[i], points[(i + 1) % 3], depth)

# Recursive function to draw Koch curve between two points
def draw_koch_curve(p1, p2, depth):
    if depth == 0:
        # Draw a line segment between two points
        glBegin(GL_LINES)
        glVertex2f(p1[0], p1[1])
        glVertex2f(p2[0], p2[1])
        glEnd()
    else:
        # Calculate the points that form the Koch curve
        # Split the secment into 3 equal parts
        one_third = [(2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3]
        two_third = [(p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3]

        # Calculate the peak of the equilateral triangle
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        length = math.sqrt(dx ** 2 + dy ** 2) / 3
        angle = math.atan2(dy, dx) + math.pi / 3
        peak = [one_third[0] + length * math.cos(angle), one_third[1] + length * math.sin(angle)]

        # Recursively draw the four segments
        draw_koch_curve(p1, one_third, depth -1)
        draw_koch_curve(one_third, peak, depth -1)
        draw_koch_curve(peak, two_third, depth -1)
        draw_koch_curve(two_third, p2, depth -1)

# Initialize Pygame and OpenGL
def init_window():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(1, 1, 1, 1)  # Set background to white
    gluOrtho2D(-1, 1.5, -1, 1)

# Main loop to render the Koch Snowflake
def main():
    init_window()

    glLineWidth(3.0)
    glEnable(GL_LINE_STIPPLE)
    glLineStipple(1, 0x00FF)

    # Define the vertices of the main equilateral triangle
    radius = 0.8
    vertices = [
        [radius * math.cos(0), radius * math.sin(0)],  # Bottom-left vertex
        [radius * math.cos(2 * math.pi / 3), radius * math.sin(2 * math.pi / 3)], # Top vertex
        [radius * math.cos(4 * math.pi / 3), radius * math.sin(4 * math.pi / 3)]  # Bottom-right vertex
    ]

    vertices[0] = [0, 0]
    vertices[1] = [1, 0]
    
    depth = 4  # Depth of recursion for Koch Snowflake

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

        # Draw the Koch Snowflake
        glColor3f(0, 0, 0)  # Set the color to black
        draw_koch_snowflake(vertices, depth)

        pygame.display.flip()  # Update the display
        pygame.time.wait(10)  # Wait for a short duration

        # Check for quit events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

    glDisable(GL_LINE_STIPPLE)
    pygame.quit()

if __name__ == "__main__":
    main()
