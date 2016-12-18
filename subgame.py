# ============================================================================================
# cardgame.py
# ============================================================================================
# Shell for testing pycards 
# --------------------------------------------------------------------------------------------
# G. Buckbee
# 2016-Oct-31
# Updated 22-Nov-2016
# ============================================================================================
# Imports
# ===============================================================
import os, sys
import time
from random import randint

import pygame
from pygame.locals import *

from Cards import *
from CardTests import *

# ============================================================================================
# Initializations
# ===============================================================
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

background = (80,80,255)

# ---------------------------------------------
# Set up display
# ---------------------------------------------
pygame.mouse.set_visible(True)
screen = pygame.display.set_mode((800,600))
screen.fill(background)
pygame.display.update()

# ---------------------------------------------
# Global variables
# ---------------------------------------------

Graphic_objects = []

# -----------------------------------
# Test Routines.  Comment them out when not in use
# -----------------------------------

if test_all_card_objects(False):
    print("Passed All Tests")

# ---------------------------------------------
# Process Events
# ---------------------------------------------
def process_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if (event.type == MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
#            print (pos)
            new_surf = pygame.Surface((20,20)).convert()
            new_surf.set_alpha(110)
            new_surf.fill((255,0,0))
            Graphic_objects.append((new_surf, pos))
    return

# ---------------------------------------------
# Move Objects
# ---------------------------------------------
def move_objects():
    if len(Graphic_objects) > 0:
        for graphic_item in Graphic_objects:
            obj, pos = graphic_item
            x,y = pos
            x = x + randint(0,10) - 5
            y = y + randint(0,10) - 5
            pos = (x,y)
            loc = Graphic_objects.index(graphic_item)
            Graphic_objects.remove(graphic_item)
            new_item = (obj, pos)
            Graphic_objects.insert(loc, new_item)
#            print (pos)
    return


# ---------------------------------------------
# Draw Objects
# ---------------------------------------------
def draw_objects():
#    print ("number of objects = ", len(Graphic_objects))
    screen.fill(background)
    if len(Graphic_objects) > 0:
        for graphic_item in Graphic_objects:
            obj, pos = graphic_item
#            print(pos)
            screen.blit(obj, pos)
        pygame.display.update()

    return

# ============================================================================================
# Main Loop
# ===============================================================

for i in range(0,200):
    new_surf = pygame.Surface((20,20)).convert()
    new_surf.set_alpha(110)
    new_surf.fill((255,0,0))
    pos = (300,300)
    Graphic_objects.append((new_surf, pos))

for i in range(0,200):
    new_surf = pygame.Surface((20,20))
    new_surf.set_alpha(110)
    new_surf.fill((255,255,0))
    pos = (400,300)
    Graphic_objects.append((new_surf, pos))


while True:

    process_events()

    move_objects()
#    update_objects()
    draw_objects()
          
    time.sleep(0.1)





