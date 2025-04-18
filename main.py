import pygame, sys
from pygame.locals import QUIT
import pygame.key


pygame.init()
# Global vars
Width = 500
Height = 500
Board_Offset_X=10
Board_Offest_Y=40

# Game States
# 0- Start
# 1- Play
# 2- Dead
game_state = 0
score = 10


DISPLAYSURF = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Hello World!')



def show_start_screen():
    pygame.display.set_caption('Start Screen')
    #pygame.display.setimage('start_screnn.png')
    DISPLAYSURF.blit(pygame.image.load('start_screnn.png'), (Width/2-150, Height/2-150))

def start_button_pressed():
    if pygame.key.get_pressed()[pygame.K_1]:
        return True
    else:
        return False

def restart_button_pressed():
    if pygame.key.get_pressed()[pygame.K_3]:
        return True
    else:
        return False

def draw_screen():
    top_left_x = Board_Offset_X - 1
    top_left_y = Board_Offest_Y - 1
    Bwidth = Width - Board_Offset_X - Board_Offset_X+2
    Bheight = Height - Board_Offest_Y - Board_Offest_Y+2
    border_rect = pygame.Rect(top_left_x, top_left_y, Bwidth, Bheight)
    pygame.draw.rect(DISPLAYSURF, (0, 255, 0), border_rect, 2)
    
    font = pygame.font.Font(None, 24) # Assuming you want a default font with 24pt size
    text_surface = font.render("Score:"+str(score), True, (0, 255, 0))
    DISPLAYSURF.blit(text_surface, (Board_Offset_X, Board_Offest_Y/2))


def Update():
    global game_state  # Make sure to modify the global 'game_state' variable
    if game_state == 0:
        if start_button_pressed():
            game_state = 1
            print( "game started changed to 1")
    elif game_state == 1:
        if pygame.key.get_pressed()[pygame.K_2]:
            game_state = 2
            print ("game started changed to 2")
    elif game_state == 2:
        if restart_button_pressed():
            game_state = 0
            print ("game started changed to 0")
           

def Draw(): 
    DISPLAYSURF.fill((0, 0, 0))  # Clear screen with black color
    if game_state == 0:
        show_start_screen()
        print ("Draw State 0")
    if game_state == 1:
        draw_screen()
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




