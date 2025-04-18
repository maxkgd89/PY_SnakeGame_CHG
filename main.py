import pygame, sys
from pygame.locals import QUIT
import pygame.key


pygame.init()
# Global vars
Width = 500
Height = 500

# Game States
# 0- Start
# 1- Play
# 2- Dead
game_state = 0



DISPLAYSURF = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Hello World!')



def show_start_screen():
    pygame.display.set_caption('Start Screen')
    #pygame.display.setimage('start_screnn.png')
    DISPLAYSURF.blit(pygame.image.load('start_screnn.png'), (Width/2-150, Height/2-150))
    pass

def start_button_pressed():
    pass

def Update():
    global game_state  # Make sure to modify the global 'game_state' variable
    if game_state == 0:
        if pygame.key.get_pressed()[pygame.K_1]:
            game_state = 1
            print( "game started changed to 1")
    elif game_state == 1:
        if pygame.key.get_pressed()[pygame.K_2]:
            game_state = 2
            print ("game started changed to 2")
    elif game_state == 2:
        if pygame.key.get_pressed()[pygame.K_3]:
            game_state = 0
            print ("game started changed to 0")
           

def Draw(): 
    if game_state == 0:
        show_start_screen()
        print ("Draw State 0")
    if game_state == 1:
        print ("Draw State 1")
    elif game_state == 2:
        print ("Draw State 2")
    pass

while True:
   for event in pygame.event.get():
    Update()
    Draw()
    if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()




