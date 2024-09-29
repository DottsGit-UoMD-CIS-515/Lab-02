import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_filled_triangle(vertices, color=(1.0, 1.0, 1.0)):
    glColor3f(*color)
    glBegin(GL_TRIANGLES)
    for vertex in vertices:
        glVertex2f(*vertex)
    glEnd()

def sierpinski(vertices, iteration, color=(1.0, 1.0, 1.0)):
    if iteration == 0:
        draw_filled_triangle(vertices, color)
    else:
        # Find midpoints for drawing other triangles
        mid12 = midpoint(vertices[0], vertices[1])
        mid23 = midpoint(vertices[1], vertices[2])
        mid31 = midpoint(vertices[2], vertices[0])
        
        # Recursively draw smaller triangles
        sierpinski([vertices[0], mid12, mid31], iteration - 1, color)
        sierpinski([mid12, vertices[1], mid23], iteration - 1, color)
        sierpinski([mid31, mid23, vertices[2]], iteration - 1, color)

# Calculate midpoint between two points
def midpoint(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def main():
    pygame.init()
    
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Sierpinski Triangle')
    
    vertices = [
        (0.0, 1.0),      # Top
        (-1.0, -1.0),    # Bottom-left
        (1.0, -1.0)      # Bottom-right
    ]
    
    iteration = 4
    
    color = (1.0, 1.0, 1.0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Draw the Sierpinski Triangle
        sierpinski(vertices, iteration, color)
        
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
