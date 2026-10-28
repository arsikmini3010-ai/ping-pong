from random import random, randint
from pygame import *

win_size = (700,500)
FPS = 60

window = display.set_mode(win_size)
display.set_caption('ping-pong')
background = (255,255,255)

clock = time.Clock()
while True:
    window.fill(background)
    display.update()
    clock.tick(40)