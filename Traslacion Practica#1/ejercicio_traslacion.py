from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Variables globales para el desplazamiento (traslación)

# Queremos que el triángulo se mueva 0.5 a la derecha y 0.3 hacia arriba
tx = 0.5
ty = 0.3

def display():
    # Limpiamos el buffer de color (borra lo que había antes en la pantalla)
    glClear(GL_COLOR_BUFFER_BIT)
    
    # --- Transformaciones ---
    # Guardamos la matriz actual en la pila para no afectar a otros objetos
    glPushMatrix()
    
    # Aplicamos la traslación usando nuestras variables tx y ty
    glTranslatef(tx, ty, 0.0)

    # Dibujamos el triángulo centrado originalmente en el origen (0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.2, -0.2) # Punto inferior izquierdo
    glVertex2f(0.2, -0.2)  # Punto inferior derecho
    glVertex2f(0.0, 0.2)   # Punta superior
    glEnd()

    # Recuperamos la matriz anterior para "limpiar" la transformación
    glPopMatrix()
    
    # Forzamos la ejecución de los comandos de OpenGL
    glFlush()

def init():
    # Color de fondo (negro sólido)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    # Color del dibujo (blanco)
    glColor3f(1.0, 1.0, 1.0)
    
    # Configuramos la cámara (Proyección)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    
    # Definimos el plano 2D: coordenadas de -1 a 1 en ambos ejes
    gluOrtho2D(-1, 1, -1, 1)

def main():
    # Inicialización estándar de GLUT
    glutInit()
    # Buffer simple y modo de color RGB
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    
    # Tamaño y posición de la ventana en la pantalla
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    
    # Título de la ventana (ojo con la 'b' para el string en Python 3)
    glutCreateWindow(b"Triangulo con Traslacion")
    
    # Llamamos a nuestra configuración inicial
    init()
    
    # El "render loop": le decimos qué función dibuja
    glutDisplayFunc(display)
    
    # Se queda escuchando eventos hasta que cerremos la ventana
    glutMainLoop()

# Ejecutamos el script
main()