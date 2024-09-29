import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def init_window():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    pg.display.set_caption('Koch Snowflake')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def koch_curve(p1, p2, iteration):
    if iteration == 0:
        return [p1, p2]
    else:
        # Points dividing the segment into thirds
        pA = [(2*p1[0] + p2[0])/3, (2*p1[1]+p2[1])/3]
        pB = [(p1[0] + 2 * p2[0])/3, (p1[1] + 2 * p2[1])/3]

        dx = (p2[0] - p1[0])
        dy = (p2[1] - p1[1])

        # Compute the peak of the equilateral triangle
        length = math.sqrt(dx**2 + dy**2)/3
        angle = math.atan2(dy, dx) + math.pi/3

        pPeak = (pA[0] + length * math.cos(angle), pA[1] + length * math.sin(angle))

        # Recursively compute the points
        points = []
        points += koch_curve(p1, pA, iteration -1)[:-1]
        points += koch_curve(pA, pPeak, iteration -1)[:-1]
        points += koch_curve(pPeak, pB, iteration -1)[:-1]
        points += koch_curve(pB, p2, iteration -1)

        return points

def generate_koch_snowflake(iteration, width_units, height_units, fill_percent=0.8):
    # Compute size based on fill_percent
    size_width_limit = width_units * fill_percent
    size_height_limit = (height_units * fill_percent) * (2 / math.sqrt(3))
    size = min(size_width_limit, size_height_limit)

    # Compute height
    height = size * math.sqrt(3) / 2

    # Center the snowflake in the window
    center_x = 0
    center_y = 0

    # Define the initial triangle
    p1 = (center_x - size / 2, center_y - height / 3)
    p2 = (center_x + size / 2, center_y - height / 3)
    p3 = (center_x, center_y + 2 * height / 3)

    # Per-side, compute the Koch curve
    side1 = koch_curve(p1, p2, iteration)
    side2 = koch_curve(p2, p3, iteration)
    side3 = koch_curve(p3, p1, iteration)

    # Concatenate sides
    points = side1[:-1] + side2[:-1] + side3

    return points

def main():
    init_window()

    # Set up orthographic projection to properly fit the window around the object
    left, right = -400, 400
    bottom, top = -200, 300
    gluOrtho2D(left, right, bottom, top)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    width_units = right - left
    height_units = top - bottom

    # BG color
    glClearColor(1.0, 1.0, 1.0, 1.0)

    iteration = 4

    while True:
        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        # Clear and set line color
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.0, 0.0, 0.0)

        # Get points and draw lines
        points = generate_koch_snowflake(iteration, width_units, height_units, fill_percent=0.8)
        glBegin(GL_LINE_STRIP)
        for p in points:
            glVertex2f(p[0], p[1])
        glEnd()

        pg.display.flip()

if __name__ == "__main__":
    main()
