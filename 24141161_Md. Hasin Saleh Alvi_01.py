#Task_01
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 500, 500

# Global variables for rain and direction
rain_direction = 0  # 0 = falling straight, positive values bend left, negative values bend right
rain_drops = []
background_color = (0, 0, 0)  # Night-time color (black)

def drawHouse():
    

    # Roof
    glColor3f(1, 1, 0)  # Yellow color for the roof
    glBegin(GL_TRIANGLES)
    glVertex2d(-75, 75)
    glVertex2d(75, 75)
    glVertex2d(0, 125)
    glEnd()
    
    # Walls 
    glColor3f(0, 0, 1)  # Blue color for the walls
    glBegin(GL_QUADS)
    glVertex2d(-75, 75)
    glVertex2d(75, 75)
    glVertex2d(75, -75)
    glVertex2d(-75, -75)
    glEnd()
    
    # Door
    glColor3f(0.5, 0.25, 0)  # Brown color for the door
    glBegin(GL_QUADS)
    glVertex2d(-15, -75)
    glVertex2d(15, -75)
    glVertex2d(15, -20)
    glVertex2d(-15, -20)
    glEnd()
    
    # Left Window
    glColor3f(1, 1, 1)  # White color for windows
    glBegin(GL_QUADS)
    glVertex2d(-60, 10)
    glVertex2d(-30, 10)
    glVertex2d(-30, 40)
    glVertex2d(-60, 40)
    glEnd()
    
    # Right Window
    glBegin(GL_QUADS)
    glVertex2d(30, 10)
    glVertex2d(60, 10)
    glVertex2d(60, 40)
    glVertex2d(30, 40)
    glEnd()



def drawRain():
    
    global rain_direction
    glColor3f(0.0, 0.0, 1.0)  # Blue for raindrops
    for drop in rain_drops:
        x, y, speed = drop
        draw_points(x, y, 3)  #  small point for raindrop
        #  drop's position (falling direction)
        drop[1] -= speed  # Move the raindrop down
        drop[0] += rain_direction  # Apply the rain's horizontal direction change
        if drop[1] < -250:  # Reset if drop goes out of view
            drop[1] = 250
            drop[0] = random.randint(-250, 250)

def draw_points(x, y, s):
    glPointSize(s)  # Set pixel size
    glBegin(GL_POINTS)
    glVertex2f(x, y)  # Draw point at (x, y)
    glEnd()

def drawAxes():
    glLineWidth(1)
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)  # X-axis (red)
    glVertex2f(250, 0)
    glVertex2f(-250, 0)
    glColor3f(0.0, 0.0, 1.0)  # Y-axis (blue)
    glVertex2f(0, 250)
    glVertex2f(0, -250)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(0, 1.0, 0.0)  # Origin (green)
    glVertex2f(0, 0)
    glEnd()

def keyboardListener(key, x, y):
    global rain_direction, background_color
    if key == b'w':
        print("Size Increased")
    if key == b's':
        print("Size Decreased")
    if key == b'r':  # Reset rain direction to straight
        rain_direction = 0
        print("Rain direction reset")
    if key == b'd':  # Switch to daytime (light background)
        background_color = (1, 1, 1)  # White color
        print("Switched to Daytime")
    if key == b'n':  # Switch to night-time (dark background)
        background_color = (0, 0, 0)  # Black color
        print("Switched to Nighttime")
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global rain_direction
    if key == GLUT_KEY_UP:
        rain_direction *= 2  # Increase the bending of the rain
        print("Rain speed increased")
    if key == GLUT_KEY_DOWN:
        rain_direction /= 2  # Decrease the bending of the rain
        print("Rain speed decreased")
    if key == GLUT_KEY_LEFT:
        rain_direction -= 0.01  # Bend rain to left gradually
        print("Rain bent to left")
    if key == GLUT_KEY_RIGHT:
        rain_direction += 0.01  # Bend rain to right gradually
        print("Rain bent to right")
    glutPostRedisplay()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(background_color[0], background_color[1], background_color[2], 0)  # Set background color
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 200, 0, 0, 0, 0, 1, 0)
    
    drawAxes()
    drawHouse()
    drawRain()

    glutSwapBuffers()

def animate():
    glutPostRedisplay()
    global rain_drops
    # Update rain drops position
    for drop in rain_drops:
        drop[1] -= drop[2]  # Move the raindrop down
        if drop[1] < -250:
            drop[1] = 250
            drop[0] = random.randint(-250, 250)

def init():
    glClearColor(0, 0, 0, 0)  # Black background for night-time
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104, 1, 1, 1000.0)

    # Initialize raindrops
    global rain_drops
    for i in range(100):
        x = random.randint(-250, 250)
        y = random.randint(0, 250)
        speed = random.uniform(0.01, 0.05)
        rain_drops.append([x, y, speed])

# Main OpenGL Setup
glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)

wind = glutCreateWindow(b"OpenGL House and Rainfall Simulation")
init()

glutDisplayFunc(display)  # Display callback function
glutIdleFunc(animate)  # Animate during idle time

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)

glutMainLoop()  # The main loop of OpenGL












#Task_02

'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

# Window properties
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Box boundaries
BOUND_LEFT, BOUND_RIGHT = -150, 150
BOUND_BOTTOM, BOUND_TOP = -150, 150

# Color choices
colors = [
    (1, 0, 0),  # Red
    (0, 1, 0),  # Green
    (0, 0, 1),  # Blue
    (1, 1, 0),  # Yellow
    (1, 0, 1),  # Magenta
    (0, 1, 1),  # Cyan
    (1, 0.5, 0),  # Orange
    (0.5, 0, 1),  # Purple
]

# Points: [x, y, dx, dy, r, g, b]
particles = []
move_speed = 1.0
paused = False
flashing = False
last_flash_time = time.time()
flash_toggle = True


def create_particle(x, y):
    #Generates a particle at (x, y) with random movement and color
    dx = random.choice([-1, 1])
    dy = random.choice([-1, 1])
    r, g, b = random.choice(colors)
    particles.append([x, y, dx, dy, r, g, b])


def move_particles():
    #Updates particle positions and handles boundary collisions
    global last_flash_time, flash_toggle
    if paused:
        return

    current_time = time.time()
    if flashing and current_time - last_flash_time >= 0.5:
        flash_toggle = not flash_toggle
        last_flash_time = current_time

    for particle in particles:
        if flashing and not flash_toggle:
            continue

        particle[0] += particle[2] * move_speed
        particle[1] += particle[3] * move_speed

        # Handle bouncing at the box edges
        if particle[0] <= BOUND_LEFT or particle[0] >= BOUND_RIGHT:
            particle[2] *= -1
        if particle[1] <= BOUND_BOTTOM or particle[1] >= BOUND_TOP:
            particle[3] *= -1


def draw_boundary():
    #Draws the inner boundery box
    glColor3f(1, 1, 1)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(BOUND_LEFT, BOUND_BOTTOM)
    glVertex2f(BOUND_RIGHT, BOUND_BOTTOM)
    glVertex2f(BOUND_RIGHT, BOUND_TOP)
    glVertex2f(BOUND_LEFT, BOUND_TOP)
    glEnd()


def render_particles():
    #Renders all particles
    for particle in particles:
        if flashing and not flash_toggle:
            continue

        glColor3f(particle[4], particle[5], particle[6])
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(particle[0], particle[1])
        glEnd()


def render_scene():
    #Main display function
    glClear(GL_COLOR_BUFFER_BIT)
    draw_boundary()
    render_particles()
    glutSwapBuffers()


def update_frame(value):
    #Handles animation updates
    move_particles()
    glutPostRedisplay()
    glutTimerFunc(16, update_frame, 0)


def keyboard_handler(key, x, y):
   #Handles keyboard inputs
    global move_speed, paused, flashing
    if key == b' ':
        paused = not paused
    glutPostRedisplay()


def special_key_handler(key, x, y):
    #Handles  arrow keys
    global move_speed
    if not paused:
        if key == GLUT_KEY_UP:
            move_speed *= 1.2
        elif key == GLUT_KEY_DOWN:
            move_speed *= 0.8
    glutPostRedisplay()


def mouse_handler(button, state, x, y):
    #Handles mouse interactions
    global flashing
    if state == GLUT_DOWN:
        world_x = (x - WIN_WIDTH / 2) * (BOUND_RIGHT / (WIN_WIDTH / 2))
        world_y = ((WIN_HEIGHT - y) - WIN_HEIGHT / 2) * (BOUND_TOP / (WIN_HEIGHT / 2))

        if button == GLUT_RIGHT_BUTTON and not paused:
            create_particle(world_x, world_y)
        elif button == GLUT_LEFT_BUTTON:
            flashing = not flashing
    glutPostRedisplay()


def init_gl():
    
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-250, 250, -250, 250)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIN_WIDTH, WIN_HEIGHT)
glutCreateWindow(b"Particle Simulation")
init_gl()
glutDisplayFunc(render_scene)
glutMouseFunc(mouse_handler)
glutKeyboardFunc(keyboard_handler)
glutSpecialFunc(special_key_handler)
glutTimerFunc(16, update_frame, 0)
glutMainLoop()'''
