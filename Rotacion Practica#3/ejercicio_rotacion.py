from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Ángulo de rotación inicial
angulo = -60

def display():
    # Limpia la pantalla (borra el frame anterior)
    glClear(GL_COLOR_BUFFER_BIT)

    # Guarda la matriz de transformación actual
    glPushMatrix()
    
    # Aplica la rotación (ángulo, eje x, eje y, eje z)
    glRotatef(angulo, 0.0, 0.0, 1.0)

    # Dibuja un cuadrado (4 vértices)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.2)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.2, 0.2)
    glVertex2f(-0.2, 0.2)
    glEnd()

    # Restaura la matriz original (evita que las transformaciones se acumulen)
    glPopMatrix()
    
    # Fuerza el dibujado de las operaciones
    glFlush()

# --- Configuración del entorno ---
glutInit()
# Modo de color y buffer simple
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
# Tamaño de la ventana
glutInitWindowSize(600, 600)
# Crea la ventana con un título
glutCreateWindow(b"Rotacion 2D")
# Color de fondo (negro)
glClearColor(0.0, 0.0, 0.0, 1.0)
# Define la función que dibujará el contenido
glutDisplayFunc(display)
# Inicia el ciclo infinito de la aplicación
glutMainLoop()