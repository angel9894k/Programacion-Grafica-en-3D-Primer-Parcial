from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

sx = 1.5  # Factor de escala horizontal
sy = 2.5  # Factor de escala vertical

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix() #Guarda estado
    glScalef(sx, sy, 1.0) #Aplica escalacion, El 1.o por que estamos en 2D
    glBegin(GL_TRIANGLES) #Indicamos las coordenadas de los vertices
    glVertex2f(-0.2, -0.2)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.0, 0.2)
    glEnd()

    glPopMatrix() #Restaura

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
glutInitWindowSize(600, 600)  #Se define el tamaño de la ventana
glutCreateWindow(b"Escalacion 2D") #pone titulo a la ventana
glutDisplayFunc(display)
glutMainLoop()