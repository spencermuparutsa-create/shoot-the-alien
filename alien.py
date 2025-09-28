import pgzrun
import random

WIDTH = 500
HEIGHT = 500

alien = Actor("alien")

alien.x = 250
alien.y = 250

msg = "catch the alien"

def draw():
    screen.fill("green")
    alien.draw()
    screen.draw.text(msg,(100,100),color = "black")



def on_mouse_down(pos):
    global msg
    if alien.collidepoint(pos):
       alien.x = random.randint(0,500)
       alien.y = random.randint(0,500)
       msg = "well done"
       
    else:
        msg = "you missed"


pgzrun.go()