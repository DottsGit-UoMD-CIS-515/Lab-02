import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def main():
    pygame.init()
    display = (680, 480)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Simple PyGame Window")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClearColor(0.0, 0.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
