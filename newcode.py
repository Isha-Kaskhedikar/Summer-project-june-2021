from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
   
WINDOW_WIDTH =1000
WINDOW_HEIGHT =1000


# # angle of rotation for the camera direction
angle = 0.0
yAngle = 0.0
# # actual vector representing the camera's direction
lx = 0.0
ly = 0.0 
lz = -1.0
# # XZ position of the camera
x = -5.0
z = 18.0
roll = 0.0
rotAngle=0.0
# #for mouse movements
halfWidth = (float)(WINDOW_WIDTH/2.0)
halfHeight = (float)(WINDOW_HEIGHT/2.0)
mouseX = 0.0
mouseY = 0.0

v_cube = [[0.0, 0.0, 0.0], #0
    [0.0, 0.0, 3.0], #1
    [3.0, 0.0, 3.0], #2
    [3.0, 0.0, 0.0], #3
    [0.0, 3.0, 0.0], #4
    [0.0, 3.0, 3.0], #5
    [3.0, 3.0, 3.0], #6
    [3.0, 3.0, 0.0]  #7
]

quadIndices = [
    [0, 1, 2, 3], #bottom
    [4, 5, 6, 7], #top
    [5, 1, 2, 6], #front
    [0, 4, 7, 3], # back is clockwise
    [2, 3, 7, 6], #right
    [1, 5, 4, 0]  #left is clockwise
]

colors = [
    [0.4, 0.1, 0.0], #bottom
    [0.6, 0.0, 0.7], #top
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 1.0],
    [0.8, 0.0, 0.0],
    [0.3, 0.6, 0.7]
]



def drawCube():

    glBegin(GL_QUADS)
    for i in range(6):    
        glVertex3f(v_cube[quadIndices[i][0]][0],v_cube[quadIndices[i][0]][1],v_cube[quadIndices[i][0]][2])
        glVertex3f(v_cube[quadIndices[i][1]][0],v_cube[quadIndices[i][1]][1],v_cube[quadIndices[i][1]][2])
        glVertex3f(v_cube[quadIndices[i][2]][0],v_cube[quadIndices[i][2]][1],v_cube[quadIndices[i][2]][2])
        glVertex3f(v_cube[quadIndices[i][3]][0],v_cube[quadIndices[i][3]][1],v_cube[quadIndices[i][3]][2])
    
    glEnd()

def sofa1():
    glColor3f(0.67,0.50,1.00)
    glPushMatrix()
    glTranslatef(-4,0,-3)
    glScalef(2, 0.4, 0.8)
    drawCube()
    glPopMatrix()

    glColor3f(0.42,0.30,1.00)
    glPushMatrix()
    glTranslatef(-4,1,-3)
    glScalef(2, 0.4, 0.2)
    drawCube()
    glPopMatrix()

    glColor3f(0.00,0.17,0.50)
    glPushMatrix()
    glTranslatef(-4.3,0,-3)
    glScalef(0.1, 0.6, 0.9)
    drawCube()
    glPopMatrix()

    glColor3f(0.00,0.17,0.50)
    glPushMatrix()
    glTranslatef(1.87,0,-3)
    glScalef(0.1, 0.6, 0.9)
    drawCube()
    glPopMatrix()


def vase():
    glColor3f(0.10,0.00,0.30)
    glPushMatrix()
    glTranslatef(3.4,0,-2)
    glScalef(0.2, 0.4, 0.2)
    drawCube()
    glPopMatrix()  

    glColor3f(0.00,0.90,0.30)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(3.6, 3, -1.5) 
    glVertex3f(3.5, 3.1, -1.5) 
    glVertex3f(3.4, 3, -1.5)  
    glVertex3f(3.8, 2, -1.5)
    glVertex3f(3.7, 2.1, -1.5)
    glVertex3f(3.6, 2, -1.5)
    glEnd()

    glColor3f(1,0.5,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(3.3, 2.4, -1.5)
    glVertex3f(3.2, 2.45, -1.5)
    glVertex3f(3.1, 2.4, -1.5)
    glVertex3f(4, 2.7, -1.5)
    glVertex3f(3.9, 2.8, -1.5)
    glVertex3f(3.8, 2.7, -1.5)
    glEnd()
  
    glColor3f(0.30,0.05,0.00)
    glLineWidth(3.0) 
    glBegin(GL_LINES)
    glVertex3f(3.5, 3, -1.5)
    glVertex3f(3.5, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.9, 2.7, -1.5)
    glVertex3f(3.5, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.2, 2.4, -1.5)
    glVertex3f(3.9, 0, -1.5)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(3.7, 2, -1.5)
    glVertex3f(3.6, 1, -1.5)
    glEnd()


def window():        
        #cupboard
    glColor3f(0.00,0.84,1) #0.3,0.1,0.0
    glPushMatrix()
    glTranslatef(-4,2,-10)
        #glRotatef(22, 0,0,1)
    glScalef(2, 1, 0.03)
    drawCube()
    glPopMatrix()

    #----------------HORIZONTAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 3.5, -9.9)
    glVertex3f(2.0, 3.5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 2, -9.9)
    glVertex3f(2.0, 2, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 5, -9.9)
    glVertex3f(2.0, 5, -9.9)
    glEnd()

    #----------------HVERTICAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4, 2, -9.9)
    glVertex3f(-4, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(2, 2, -9.9)
    glVertex3f(2, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-2.0, 2, -9.9)
    glVertex3f(-2.0, 5, -9.9)
    glEnd()

    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(0, 2, -9.9)
    glVertex3f(0, 5, -9.9)
    glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-6.0, 4, 10.01)
    # glVertex3f(-6.0, 4, 10.01)
    # glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-3.0, 0.0, 10.01)
    # glVertex3f(-3.0, 5.0, 10.01)
    # glEnd()
     


def table():
    #table *****************************************
        
        #table base
        glColor3f(0.10,0.00,0.30)
        glPushMatrix()
        glTranslatef(.6,1.5,4.1)
        glScalef(0.8, 0.08, 0.8)
        drawCube()
        glPopMatrix()
        
        #legs
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(.6,0,4.1)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()
        
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(2.8,0,4.18)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(2.8,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(0.58,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()


def windowbedroom():        
        #cupboard
    glColor3f(0.00,1,1) #0.3,0.1,0.0
    glPushMatrix()
    glTranslatef(-4,2,-10)
        #glRotatef(22, 0,0,1)
    glScalef(2, 1, 0.03)
    drawCube()
    glPopMatrix()

    #----------------HORIZONTAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 3.5, -9.9)
    glVertex3f(2.0, 3.5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 2, -9.9)
    glVertex3f(2.0, 2, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4.0, 5, -9.9)
    glVertex3f(2.0, 5, -9.9)
    glEnd()

    #----------------HORIZONTAL PART---------------
    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-4, 2, -9.9)
    glVertex3f(-4, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(2, 2, -9.9)
    glVertex3f(2, 5, -9.9)
    glEnd()


    glColor3f(0.25,0.28,0.28) #0.3,0.1,0.0
    glLineWidth(7.0)
    glBegin(GL_LINES)
    glVertex3f(-1.0, 2, -9.9)
    glVertex3f(-1.0, 5, -9.9)
    glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-6.0, 4, 10.01)
    # glVertex3f(-6.0, 4, 10.01)
    # glEnd()

    # glBegin(GL_LINES)
    # glVertex3f(-3.0, 0.0, 10.01)
    # glVertex3f(-3.0, 5.0, 10.01)
    # glEnd()
     

def bed():
    #bed headboard
    glColor3f(0.40,0.27,0.00)
    glPushMatrix()
    glScalef(0.1, 0.5, 0.9)
    glTranslatef(-2,-0.5,6)
    drawCube()
    glPopMatrix()
    
    #bed body
    glColor3f(0.824, 0.706, 0.549)
    glPushMatrix()
    glScalef(1, 0.2, 0.9) #1, 0.2, 0.9
    glTranslatef(0,-0.5,6.2)
    drawCube()
    glPopMatrix()
    
    #pillow right far
    glColor3f(0.00,0.50,0.25)
    glPushMatrix()
    glTranslatef(0.5,0.5,6)
    glRotatef(20, 0,0,1)
    glScalef(0.1, 0.15, 0.48)
    drawCube()
    glPopMatrix()
      
    #blanket
    glColor3f(0.67,0.80,0.00)
    glPushMatrix()
    glTranslatef(1.4,0.45,5.5)
    #glRotatef(22, 0,0,1)
    glScalef(0.5, 0.05, 0.95)
    drawCube()
    glPopMatrix()
    
    #blanket side left part
    glColor3f(0.67,0.80,0.00)
    glPushMatrix()
    glTranslatef(1.4,-0.3,8.15)
    #glRotatef(22, 0,0,1)
    glScalef(0.5, 0.25, 0.05)
    drawCube()
    glPopMatrix()

def bedtable():
    #bedtable *****************************************
        #mirror
        glColor3f(0.90,0.90,1.00)
        glPushMatrix()
        glTranslatef(4.6,2,4.7)
        glScalef(0.001, 1, 0.4)
        drawCube()
        glPopMatrix()

        #bedtable base
        glColor3f(0.17,0.20,0.00)
        glPushMatrix()
        glTranslatef(1.6,1.5,4.1)
        glScalef(0.8, 0.08, 0.8)
        drawCube()
        glPopMatrix()
        
        #legs
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(1.6,0,4.1)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()
        
        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(3.8,0,4.18)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(3.8,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()

        glColor3f(0.40,0.27,0.00)
        glPushMatrix()
        glTranslatef(1.58,0,6.25)
        glScalef(0.08, 0.5, 0.08)
        drawCube()
        glPopMatrix()


def cupboard():
    #Cupboard/Almari ************************************************************
        
        #cupboard
        glColor3f(0.40,0.27,0.00) #0.3,0.1,0.0
        glPushMatrix()
        glTranslatef(4,0,4.4)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 1, 0.5)
        drawCube()
        glPopMatrix()
        
        #cupboard's 1st vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's 2nd vertical stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0.5,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's last stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.5, 0.01, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's lst horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5.5,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's right side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.75,1,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 0.67, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's left side horizontal stripline
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4,0,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.01, 1, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle right
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.0001)
        drawCube()
        glPopMatrix()
        
        #cupboard's handle left
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,1.4,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.02, 0.18, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 1st handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.7,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()
        
        #cupboard's drawer's 2nd handle
        glColor3f(0.2,0.1,0.1)
        glPushMatrix()
        glTranslatef(4.5,0.25,5.9)
        #glRotatef(22, 0,0,1)
        glScalef(0.16, 0.02, 0.01)
        drawCube()
        glPopMatrix()



def renderScene():
    # global angle,yAngle,lx,ly,lz,mouseX,mouseY
    # # Clear Color and Depth Buffers
    p=8.9
    q=-20
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # # Reset transformations
    glLoadIdentity()
    # # Set the camera
    gluLookAt(x, 2.5, z, x + lx, 2.5 + ly, z + lz, roll + 0.0, 2.5, 0.0)
    
    glPushMatrix()
    glRotatef(90,0,1,0)
    # # Draw floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-7.0+p, 0.0, -10.0+q)
    glVertex3f(-7.0+p, 0.0, 10.0+q)
    glVertex3f(10.0+p, 0.0, 10.0+q)
    glVertex3f(10.0+p, 0.0, -10.0+q)
    glEnd()
    
    glPushMatrix()
    glTranslatef(0+p,0,-13+q)
    glScalef(1,2,1)
    cupboard()#----------------------------------------------------------------cupboard
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(2+p,0,-13+q)
    glScalef(1,2,1)
    cupboard()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(p,0,q)
    windowbedroom()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(5+p,0,-13+q)
    glScalef(2,2,2)
    glRotatef(-45,0,1,0)
    bed()#----------------------------------------------------------------bed
    glPopMatrix()

    # -----------------------------------------------------------window wall
    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(-7.0+p, 0.0, -10.0+q)
    glVertex3f(-7.0+p, 7.0, -10.0+q)
    glVertex3f(10.0+p, 7.0, -10.0+q)
    glVertex3f(10.0+p, 0.0, -10.0+q)
    glEnd()

    glPushMatrix()
    glTranslatef(5+p,0,-4+q)
    glScalef(1,0.8,1.5)
    bedtable()#----------------------------------------------------------------bedtable
    glPopMatrix()

    # #wall
    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(-7.0+p, 0.0, -10.0+q)
    glVertex3f(-7.0+p, 7.0, -10.0+q)
    glVertex3f(-7.0+p, 7.0, 10.0+q)
    glVertex3f(-7.0+p, 0.0, 10.0+q)
    glEnd()

    # #wall with door
    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(-7.0+p, 0.0, 9.8+q)
    glVertex3f(-7.0+p, 7.0, 9.8+q)
    glVertex3f(-6.0+p, 7.0, 9.8+q)
    glVertex3f(-6.0+p, 0.0, 9.8+q)
    glEnd()

    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(-3.0+p, 0.0, 9.8+q)
    glVertex3f(-3.0+p, 7.0, 9.8+q)
    glVertex3f(10.0+p, 7.0, 9.8+q)
    glVertex3f(10.0+p, 0.0, 9.8+q)
    glEnd()

    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(-6.0+p, 7.0, 9.8+q)
    glVertex3f(-6.0+p, 5.0, 9.8+q)
    glVertex3f(-3.0+p, 5.0, 9.8+q)
    glVertex3f(-3.0+p, 7.0, 9.8+q)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-6.0+p, 5.0, 10.01+q)
    glVertex3f(-3.0+p, 5.0, 10.01+q)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6.0+p, 5.0, 10.01+q)
    glVertex3f(-6.0+p, 0.0, 10.01+q)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.0+p, 0.0, 10.01+q)
    glVertex3f(-3.0+p, 5.0, 10.01+q)
    glEnd()


    #  --------------------------------------wall with door
    glColor3f(0.75,0.93,0.81)
    glBegin(GL_QUADS)
    glVertex3f(10.0+p, 0.0, -10+q)
    glVertex3f(10.0+p, 7.0, -10+q)
    glVertex3f(10.0+p, 7.0, 10+q)
    glVertex3f(10.0+p, 0.0,10+q)
    glEnd()


    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(10.01+p, 5.2, -6+q)
    glVertex3f(10.01+p, 5.2, -3+q)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(9.91+p, 0.0,-6.0+q)
    glVertex3f(9.91+p, 5.0,-6.0+q)
    glVertex3f(9.91+p, 5.0,-3.0+q)
    glVertex3f(9.91+p, 0.0, -3.0+q)
    glEnd()

    glColor3f(1,1,0)
    glPointSize(8)
    glBegin(GL_POINTS)
    glVertex3f(9.87+p, 2.0,-5.5+q)
    glEnd()

    # #ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+p, 7.0, -10.0+q)
    glVertex3f(10.0+p, 7.0, -10.0+q)
    glVertex3f(10.0+p, 7.0, 10.0+q)
    glVertex3f(-10.0+p, 7.0, 10.0+q)
    glEnd()
    glPopMatrix()


def TV():
    glColor3f(0,0,0)
    glPushMatrix()
    glTranslatef(9.3,1.7,4)
    glScalef(0.03, 0.7, 1.2)
    drawCube()
    glPopMatrix()
    # test2.renderScene()


def tvtable():
    glColor3f(0.10,0.00,0.30)
    glPushMatrix()
    glTranslatef(8.2,0.5,2.8)
    glScalef(0.63, 0.2, 1.9)
    drawCube()
    glPopMatrix()    

    glPushMatrix()
    glTranslatef(9.4,4.9,5)
    glScalef(0.2, 0.01, 1)
    drawCube()
    glPopMatrix()    

    glPushMatrix()
    glTranslatef(9.4,4.3,3)
    glScalef(0.2, 0.01, 1)   #---------------------------upper TV shelf
    drawCube()
    glPopMatrix()    
     

def table2():
    # /*--------------Table top------------------*/
    glPushMatrix()
    glColor3f(0.0, 0.61, 0.53)
    glScalef(1.3,0.05,0.65)
    glutSolidCube(1)
    glPopMatrix()
    # /*----------Table legs---------------------*/
    glPushMatrix()
    glTranslatef(0,-0.375,0)
    glPushMatrix()
    glTranslatef(0.6,0,0.275)
    glColor3f(0.151, 0.255, 0.147)
    glScalef(0.05,0.75,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.6,0,-0.275)
    glColor3f(0.151,0.255, 0.147)
    glScalef(0.05,0.75,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-0.6,0,0.275)
    glColor3f(0.151, 0.255, 0.147)
    glScalef(0.05,0.75,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-0.6,0,-0.275)
    glColor3f(0.151, 0.255, 0.147)
    glScalef(0.05,0.75,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

def chair2():
    glPushMatrix()
    glScalef(0.4,1,1)
    table2()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-10,0,0,1)
    glTranslatef(0.2,0.2,0.275)
    glColor3f(0.17,0.23,0.2)
    glScalef(0.05,0.4,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glRotatef(-10,0,0,1)
    glTranslatef(0.2,0.2,-0.275)
    glColor3f(0.17,0.23,0.2)
    glScalef(0.05,0.4,0.05)
    glutSolidCube(1)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0.275,0.4,0)
    glRotatef(80,0,0,1)
    glScalef(0.2,1.1,1)
    glColor3f(0, 20, 155)
    glScalef(1.3,0.05,0.65)
    glutSolidCube(1)
    glPopMatrix()


def fridge():

    glPushMatrix()
    glScalef(1,1,1)
        # /*-----------Fridge------------*/
    glPushMatrix()
    glScalef(5,2.72,5)
    glTranslatef(0,0.5,0)
    glPushMatrix()
    glColor3f(0.1,0.1,0.1)
    glTranslatef(1.75,0,-1.5)
    glScalef(0.5,1.2,0.5)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()

        # /*-----------Freezer------------*/
    glPushMatrix()
    glTranslatef(0.0,1.35,0.0)
    glScalef(5,2,5)
    glPushMatrix()
    glColor3f(0.5,0.5,0.5)
    glTranslatef(1.75,1.17,-1.5)
    glScalef(0.5,0.7,0.5)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()
        # /*-----------Freezer handle------------*/
    glPushMatrix()
    glScalef(1,1,1)
    glPushMatrix()
    glColor3f(0.0, 0.0, 0.0)
    glTranslatef(10.0,3.75,-6.55)
    glScalef(0.1,0.5,-0.25)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

        # /*-----------Fridge handle------------*/
    glPushMatrix()
    glScalef(1,1,1)
    glPushMatrix()
    glColor3f(0.5, 0.5, 0.5)
    glTranslatef(10.0,2.3025,-6.55)
    glScalef(0.1,1.2,-0.25)
    glutSolidCube(1)
    glPopMatrix()
    glPopMatrix()

def fan():
    global rotAngle
    glPushMatrix()

    glRotatef(rotAngle, 0.0, 1.0, 0.0)
    glPushMatrix()
    glScalef(0.5,0.05,0.5)
    glColor3f(0.0,0.0,0.0)
    glutSolidSphere(1,32,32)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,1.3)
    glScalef(0.5,0.05,3)
    glColor3f(0.0,0.0,0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.3,0,1.7)
    glColor3f(0.0,0.0,0.0)
    glRotatef(40,0,1,0)
    glScalef(0.5,0.05,3)
    glTranslatef(0,0,-1.3)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1.3,0,1.7)
    glColor3f(0.0,0.0,0.0)
    glRotatef(-40,0,1,0)
    glScalef(0.5,0.05,3)
    glTranslatef(0,0,-1.3)
    glutSolidCube(1)
    glPopMatrix()

    glPopMatrix()



def kitchenCeilingCabinet():
        # /*----------------Cabinet part1 ------------------------*/
    glPushMatrix()
    # glColor3f(0.0,0.4,0.5)
    glTranslatef(0,-0.3,0)
    glScalef(0.8,0.3,0.8)
    glutSolidCube(1)
    glPopMatrix()

            # /*----------------Cabinet part2 ------------------------*/
    glPushMatrix()
    # glColor3f(0.0,0.4,0.5)
    glTranslatef(0,-0.6,0)
    glScalef(0.8,0.3,0.8)
    glutSolidCube(1)
    glPopMatrix()
    # /*----------------Cabinet part3 ------------------------*/
    glPushMatrix()
    # glColor3f(0.0,0.4,0.5)
    glTranslatef(0,-0.6,0)
    glScalef(0.8,0.3,0.8)
    glutSolidCube(1)
    glPopMatrix()
    # /*----------------Cabinet handle1 ------------------------*/
    glPushMatrix()
    glColor3f(0.0,0.0,0.0)
    glTranslatef(0,-0.65,.5)
    glScalef(0.2,0.025,0.05)
    glutSolidCube(1)
    glPopMatrix()

def kitchOven():
    glPushMatrix()
    glScalef(0.6,1,0.6)
    # glPushMatrix()
    glTranslatef(0,0.25,0)
    glPopMatrix()
    # /*----------------Cabinet part1 ------------------------*/
    glPushMatrix()
    glColor3f(0.2,0.8,0.0)
    glTranslatef(0,-0.3,0)
    glScalef(0.8,0.3,0.8)
    glutSolidCube(1)
    glPopMatrix()

    # /*----------------Cabinet part2 ------------------------*/
    glPushMatrix()
    glColor3f(0.2,0.8,0.0)
    glTranslatef(0,-0.6,0)
    glScalef(0.8,0.3,0.8)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()#Black
    glColor3f(0, 0, 0)
    glTranslatef(0,-0.4,0.175)
    glScalef(0.6,0.25,0.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glColor3f(60, 60, 60)
    glTranslatef(0,-0.4,0.2)
    glScalef(0.5,0.2,0.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glColor3f(200, 200, 200)
    glTranslatef(0,-0.2,0.3)
    glScalef(0.5,0.025,0.5)
    glutSolidCube(1)
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(0, 0, 0)
    glTranslatef(0,-0.6,0.16)
    glScalef(0.8,0.01,0.5)
    glutSolidCube(1)
    glPopMatrix()

def renderkitchen():
    global angle,yAngle,lx,ly,lz,mouseX,mouseY
    # # # Clear Color and Depth Buffers

    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    i=20
    a=4
    # # Reset transformations
    glLoadIdentity()
    # # Set the camera
    gluLookAt(x, 2.5, z,
        x + lx, 2.5 + ly, z + lz,
        roll + 0.0, 2.5, 0.0)

    # # Draw floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 0.0, -10.0)
    glVertex3f(-10.0+i, 0.0, 8.0)
    glVertex3f(7.0+i, 0.0, 8.0)
    glVertex3f(7.0+i, 0.0, -10.0)
    glEnd()
    

    # -----------------------------------------------------------cabinet wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 0.0, -10.0)
    glVertex3f(-10.0+i, 7.0, -10.0)
    glVertex3f(7.0+i, 7.0, -10.0)
    glVertex3f(7.0+i, 0.0, -10.0)
    glEnd()

    glPushMatrix()
    glTranslatef(5.2+i,9.2,-9.7)
    glScalef(4.6,5.5,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.6+i,2.8,-9.7)
    glScalef(4.6,1.4,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()    #---------------------down right
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1.6+i,1.9,-9.7)
    glScalef(4.6,1.4,3.4)
    glColor3f(0.75,1.00,0.70)
    kitchenCeilingCabinet()    #---------------------down right
    glPopMatrix()
    glPushMatrix()
    glTranslatef(1.6+i,1.1,-9.7)
    glScalef(4.6,1.4,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()    #---------------------down right
    glPopMatrix()
    # glPushMatrix()
    # glTranslatef(5.14+i,1.1,-9.7)
    # glScalef(4.02,1.8,3.4)
    # glColor3f(0.0,0.4,0.5)
    # kitchenCeilingCabinet()    #---------------------down right single
    # glPopMatrix()
   
    glPushMatrix()
    glTranslatef(1.5+i,9.2,-9.7)
    glScalef(4.6,5.5,3.4)
    glColor3f(0.75,1.00,0.70)
    kitchenCeilingCabinet()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-4.5+i,9.2,-9.7)
    glScalef(4.6,5.5,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-8.1+i,9.2,-9.7)
    glScalef(4.6,5.5,3.4)
    glColor3f(0.75,1.00,0.70)
    kitchenCeilingCabinet()
    glPopMatrix()


    glPushMatrix()
    glTranslatef(-4.6+i,2.8,-9.7) #---------------------down left
    glScalef(4.6,1.4,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-4.6+i,1.9,-9.7) #---------------------down left
    glScalef(4.6,1.4,3.4)
    glColor3f(0.75,1.00,0.70)
    kitchenCeilingCabinet()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(-4.6+i,1.1,-9.7) #---------------------down left
    glScalef(4.6,1.4,3.4)
    glColor3f(0.0,0.4,0.5)
    kitchenCeilingCabinet()
    glPopMatrix()

    
    glPushMatrix()
    glScalef(8.0,8.0,5.0)
    
    glPushMatrix()
    glTranslatef(-17.69+i,0.32,-1.76)
    glScalef(0.39,0.4,0.5)
    kitchOven()
    glPopMatrix()

    glPushMatrix()  #--------------------------------------------Stove
    glTranslatef(-17.69+i,0.285,-1.76)
    glScalef(0.31,0.05,0.4)
    glColor3f(0.0,0.0,0.0)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()  #--------------------------------------------Stove grey part
    glTranslatef(-17.69+i,0.315,-1.76)
    glScalef(0.31,0.01,0.4)
    glColor3f(0.5,0.5,0.5)
    glutSolidCube(1)
    glPopMatrix()
    
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-17.4+i,0.0,9.0)
    fridge()
    glPopMatrix()

    # ---------------------------------------------left wall
    # glColor3f(1.00,0.90,0.70)
    # glBegin(GL_QUADS)
    # glVertex3f(-10.0, 0.0, -10.0)
    # glVertex3f(-10.0, 7.0, -10.0)
    # glVertex3f(-10.0, 7.0, 10.0)
    # glVertex3f(-10.0, 0.0, 10.0)
    # glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 0.0,-10.0)
    glVertex3f(-10.0+i, 7.0,-10.0)
    glVertex3f(-10.0+i, 7.0, -6.0)
    glVertex3f(-10.0+i, 0.0, -6.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 7.0,-6.0)
    glVertex3f(-10.0+i, 5.0,-6.0)
    glVertex3f(-10.0+i, 5.0,-3.0)
    glVertex3f(-10.0+i, 7.0, -3.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 0.0, -3.0)
    glVertex3f(-10.0+i, 7.0, -3.0)
    glVertex3f(-10.0+i, 7.0, 10.0)
    glVertex3f(-10.0+i, 0.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-10.01+i, 5.0, -6)
    glVertex3f(-10.01+i, 5.0, -3)
    glEnd()

    # --------------------------------------------------------entrance wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 0.0,8.0)
    glVertex3f(-10.0+i, 7.0, 8.0)
    glVertex3f(7.0+i, 7.0,8.0)
    glVertex3f(7.0+i, 0.0, 8.0)
    glEnd()
    # -----------------------------------------------------------right wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(7.0+i, 0.0,-10.0)
    glVertex3f(7.0+i, 7.0,-10.0)
    glVertex3f(7.0+i, 7.0, 8.0)
    glVertex3f(7.0+i, 0.0,8.0)
    glEnd()

    glPushMatrix()   #--------------------------- window
    glTranslatef(17.01,0,0)
    glRotatef(270,0,1,0)
    window() 
    glPopMatrix()

        
    glPushMatrix()
    glScalef(4.0,4.0,4.0)
    glTranslatef(5.0,0.2,0.2)
    glPushMatrix()#------------------------------------------dining table
    # glTranslatef(0.6,0.2,0.5)
    glRotatef(90,0,1,0)
    glScalef(1.5,0.5,0.5)
    # glTranslatef(0,0.2,0)
    chair2()
    glPopMatrix()
    glPushMatrix()#------------------------------------------dining table
    # glTranslatef(0.6,0.2,0.5)
    # glRotatef(90,0,0,1)
    glScalef(1.5,0.5,0.5)
    # glTranslatef(0,0.2,0)
    chair2()
    glPopMatrix()
    glPushMatrix()#------------------------------------------dining table
    # glTranslatef(0.6,0.2,0.5)
    glRotatef(180,0,1,0)
    glScalef(1.5,0.5,0.5)
    # glTranslatef(0+i,0.2,0)
    chair2()
    glPopMatrix()
    glPushMatrix()#------------------------------------------dining table
    # glTranslatef(0.6+10,0.2,0.5)
    glRotatef(-90,0,1,0)
    glScalef(1.5,0.5,0.5)
    # glTranslatef(0,0.2,0)
    chair2()
    glPopMatrix()
    glPopMatrix()


    # --------------------------------------------------------------ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0+i, 7.0, -10.0)
    glVertex3f(7.0+i, 7.0, -10.0)
    glVertex3f(7.0+i, 7.0, 8.0)
    glVertex3f(-10.0+i, 7.0, 8.0)
    glEnd()
	
    if(abs(mouseX) > 0.3):
        angle -= (0.004 * mouseX)
        lx = math.math.sin(angle)
        lz = -math.math.cos(angle)

    if(abs(mouseY) > 0.3):
        if(abs(yAngle) < (math.pi/2)):
            yAngle += (0.002 * mouseY)
        ly = math.math.sin(yAngle)


def renderScene1():
    global angle,yAngle,lx,ly,lz,mouseX,mouseY,rotAngle
    # # Clear Color and Depth Buffers

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # # Reset transformations
    glLoadIdentity()
    # # Set the camera
    gluLookAt(x, 2.5, z,
        x + lx, 2.5 + ly, z + lz,
        roll + 0.0, 2.5, 0.0)

    # # Draw floor
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()
    
    sofa1()

    glPushMatrix()
    glTranslatef(-6,0,2.9)
    glRotatef(90,0,1,0)
    sofa1()#----------------------------------------------------------------sofa
    glPopMatrix()
    # sofa2()
    TV()#----------------------------------------------------------------TV
    glPushMatrix()
    glTranslatef(-0.2,0,0)
    tvtable()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-6,0,-5)
    glScalef(1.8,0.5,1.4)  
    table()#----------------------------------------------------------------main table
    glPopMatrix()


    glPushMatrix()
    glTranslatef(2,0,0)
    glScalef(2,1,1)  
    window()#----------------------------------------------------------------window
    glPopMatrix()

    # -----------------------------------------------------------window wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()

    vase()

    # ---------------------------------------------left wall
    # glColor3f(1.00,0.90,0.70)
    # glBegin(GL_QUADS)
    # glVertex3f(-10.0, 0.0, -10.0)
    # glVertex3f(-10.0, 7.0, -10.0)
    # glVertex3f(-10.0, 7.0, 10.0)
    # glVertex3f(-10.0, 0.0, 10.0)
    # glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0,-10.0)
    glVertex3f(-10.0, 7.0,-10.0)
    glVertex3f(-10.0, 7.0, -6.0)
    glVertex3f(-10.0, 0.0, -6.0)
    glEnd()
    
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0,-6.0)
    glVertex3f(-10.0, 5.0,-6.0)
    glVertex3f(-10.0, 5.0,-3.0)
    glVertex3f(-10.0, 7.0, -3.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -3.0)
    glVertex3f(-10.0, 7.0, -3.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-10.01, 5.0, -6)
    glVertex3f(-10.01, 5.0, -3)
    glEnd()

    # --------------------------------------------------------entrance wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-3.0, 0.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(-6.0, 7.0, 10.0)
    glVertex3f(-6.0, 5.0, 10.0)
    glVertex3f(-3.0, 5.0, 10.0)
    glVertex3f(-3.0, 7.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-6.0, 5.0, 10.01)
    glVertex3f(-6.0, 0.0, 10.01)
    glEnd()

    glBegin(GL_LINES)
    glVertex3f(-3.0, 0.0, 10.01)
    glVertex3f(-3.0, 5.0, 10.01)
    glEnd()


    # -----------------------------------------------------------right wall
    glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0,-10.0)
    glVertex3f(10.0, 7.0,-10.0)
    glVertex3f(10.0, 7.0, -6.0)
    glVertex3f(10.0, 0.0, -6.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 7.0,-6.0)
    glVertex3f(10.0, 5.0,-6.0)
    glVertex3f(10.0, 5.0,-3.0)
    glVertex3f(10.0, 7.0, -3.0)
    glEnd()

    # glColor3f(1.00,0.90,0.70)
    glBegin(GL_QUADS)
    glVertex3f(10.0, 0.0, -3.0)
    glVertex3f(10.0, 7.0, -3.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glEnd()

    glColor3f(0.4, 0.2, 0.0)
    glLineWidth(30.0)
    glBegin(GL_LINES)
    glVertex3f(10.01, 5.0, -6)
    glVertex3f(10.01, 5.0, -3)
    glEnd()

    # --------------------------------------------------------------ceiling
    glColor3f(0.95, 0.95, 0.95)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, -10.0)
    glVertex3f(10.0, 7.0, 10.0)
    glVertex3f(-10.0, 7.0, 10.0)
    glEnd()
    glPushMatrix()
    glTranslatef(-1.5,7,0)
    fan()
    glPopMatrix()

    glPushMatrix()
    renderScene() # --------------------------------------------------------------bedroom
    glPopMatrix()

    glPushMatrix()
    renderkitchen()
    glPopMatrix()
	
    if(abs(mouseX) > 0.3):
        angle -= (0.004 * mouseX)
        lx = math.math.sin(angle)
        lz = -math.math.cos(angle)

    if(abs(mouseY) > 0.3):
        if(abs(yAngle) < (math.pi/2)):
            yAngle += (0.002 * mouseY)
        ly = math.math.sin(yAngle)


    glutSwapBuffers()


# # @param key : key pressed
# # @param xx : x coordinate of mouse position
# # @param yy : y coordinate of mouse position
def processSpecialKeys(key,xx,yy):
    global x,z,angle,lx,lz

    fraction = 0.1

    if GLUT_KEY_LEFT:
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    if GLUT_KEY_RIGHT:
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    if GLUT_KEY_UP:
        x += lx * fraction
        z += lz * fraction
    if GLUT_KEY_DOWN:
        x -= lx * fraction
        z -= lz * fraction
		



# # Handles the events triggered when any key on the keyboard is pressed.
# #Specifically, handles w,a,s,d and Esc.
# # moves the camera frward, backward and sideways.
# # @param key : key pressed
# # @param xx : x coordinate of mouse position
# # @param yy : y coordinate of mouse position
def processNormalKeys(key,xx,yy):
    global x,z,roll,lx,ly,lz,angle
    fraction = 0.1
    if key == b'w' or key ==b'g':
        x += lx * fraction
        z += lz * fraction
    elif(key == b'a'):
        x += math.sin(angle - math.pi/2.0) * fraction
        z += -math.cos(angle - math.pi/2.0) * fraction
    elif(key == b's'):
        x -= lx * fraction
        z -= lz * fraction
    elif(key == b'd'):
        x += math.sin(math.pi/2.0 + angle) * fraction
        z += -math.cos(math.pi/2.0 + angle) * fraction
    elif (key == b'x'): 
        roll += 0.5
    elif (key == b'z'):
        roll -= 0.5

    if (key == 27):
        exit(0)

#   Handles the events triggered when the mouse is moved in the window area. 
#  Handles yaw and pitch of the camera.
#  @param xx : x coordinate of mouse position
#  @param yy : y coordinate of mouse position
def processMouseMovement(xx,yy):

    global angle,yAngle,lx,lz,ly 
    mouseX = (float)(halfWidth - xx)/halfWidth
    mouseY = (float)(halfHeight - yy)/halfHeight
    angle -= (0.005 * mouseX)
    lx = math.sin(angle)
    lz = -math.cos(angle)

    if(abs(yAngle) < (math.pi/2)):
        yAngle += (0.005 * mouseY)
    ly = math.sin(yAngle)


def animate():
    global rotAngle
    if  z<=14.75:
        rotAngle+=1.5
    glutPostRedisplay()

#   Adjusts the viewport sie when the window size is changed and sets the projection.
#   @param w : new width of window
#   @param h : new height of window
def changeSize(w, h) :

	# # Prevent a divide by zero, when window is too short
	# # (you cant make a window of zero width).
	if (h == 0):
		h = 1
	ratio = w * 1.0 / h

	# # Use the Projection Matrix
	glMatrixMode(GL_PROJECTION)

	# # Reset Matrix
	glLoadIdentity()

	# # Set the viewport to be the entire window
	glViewport(0, 0, w, h)
	halfWidth = (float)(w/2.0)
	halfHeight = (float)(h/2.0)

	# # Set the correct perspective.
	gluPerspective(45.0, ratio, 0.1, 100.0)

	# # Get Back to the Modelview
	glMatrixMode(GL_MODELVIEW)





# init GLUT and create window
glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowPosition(0, 0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow("HOUSE")

# register callbacks

glutDisplayFunc(renderScene1)
glutReshapeFunc(changeSize)
glutDisplayFunc(animate)
glutKeyboardFunc(processNormalKeys)
glutSpecialFunc(processSpecialKeys)
glutIdleFunc(renderScene1)
glutPassiveMotionFunc(processMouseMovement)

# # OpenGL init
glEnable(GL_DEPTH_TEST)

# # enter GLUT event procesmath.sing cycle
glutMainLoop()

