from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(1, 1, 1, 0)
    glColor3f(0.0, 0.0, 1.0)
    glutWireCube(1.0)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
glutMainLoop()