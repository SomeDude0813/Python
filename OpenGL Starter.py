import glfw
import sys

from OpenGL import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():
    display()

# Keep objects on screen
def iterate():
    glViewport (0, 0, 500,500)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    glOrtho (0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

# Initialize the screen

def showScreen():
    sqR,sqG,sqB = 1.0, 1.0, 1.0
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT ) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity() # Reset all graphic/shape's position
    iterate()
    glColor3f(sqR, sqG, sqB) # Set the color
    square()
    glutSwapBuffers()
    
    
 # Display the screen
def display():
    width, height = 500,500
    posY, posX = 500,0
    
    glutInit()  # Initialize a glut instance which will allow us to customize our window
    
    glutInitDisplayMode(GLUT_RGBA)  # Set the display mode to be colored
    
    glutInitWindowSize(width,height)    # Set the width and height of your window
    
    glutInitWindowPosition(posX,posY)   # Set the position at which this window should appear
    
    wind = glutCreateWindow("Project")     # Give your window a title
    
    glutDisplayFunc(showScreen)     # Tell OpenGL to call the showScreen method continiuously
    
    glutIdleFunc(showScreen)    # Draw any graphics or shapes in the showScreen function at all times
    
    glutMainLoop()  # Keeps the window created above displaying/running in a loop
    #end

# Draw square
def square():
    glBegin(GL_QUADS) # Begin the sketch
    glVertex2f(100,100) # bottom left point coords
    glVertex2f(200,100) # bottom right point
    glVertex2f(300,200) # top right point coords
    glVertex2f(100,200) # top left point coords
    glEnd() # Mark the end of drawing
    
main()