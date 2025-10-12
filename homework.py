import pgzrun 
import random


WIDTH = 450
HEIGHT = 450


turtle = Actor("image")

turtle.x = 255

turtle.y = 255

msg = "catch the turtle"

def draw():
    screen.fill("white")
    turtle.draw()
    screen.draw.text(msg,(100,100),color = ("black"))


def on_mouse_down(pos):
    global msg
    if turtle.collidepoint(pos):
        turtle.x = random.randint(0,500)
        turtle.y = random.randint(0,500)
        msg = "good job"
    else:
        msg = "try again"






pgzrun.go()