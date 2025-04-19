import sys

import pygame
import pygame.key
from pygame.locals import QUIT

pygame.init()
# Global vars
time = 5
Board_Offset_X=10
Board_Offest_Y=40
Board_Grid_Size = 14
Board_max_x = 35
Board_max_y = 35
Width = (Board_Offset_X*2)+(Board_Grid_Size*(Board_max_x+1))
Height = (Board_Offest_Y*2)+(Board_Grid_Size*(Board_max_y+1))
Snake_Min_Speed = 10

# Game States
# 0- Start
# 1- Play
# 2- Dead
game_state = 0
score = 0
size = 1
speed =1

DISPLAYSURF = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Hello World!')

# Class definition

class Position:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Snake:
    def __init__(self):
        self.body_position = Position(2,2)
        self.direction = 1
        self.move_delay = Snake_Min_Speed
        self.move_delay_counter = self.move_delay
    def render(self):
        body_screen_pos = get_screen_coords(self.body_position)
        body_rect = pygame.Rect(
            body_screen_pos.x, 
            body_screen_pos.y, 
            Board_Grid_Size, 
            Board_Grid_Size)
        pygame.draw.rect(DISPLAYSURF, (0, 200, 0), body_rect, 3)
    def move(self):
        #print("move")
        # 0 = up
        # 1 = right
        # 2 = down
        # 3 = left
        if self.direction == 0: #UP
            self.body_position.y -= 1
        elif self.direction == 1: #RIGHT
            self.body_position.x = self.body_position.x +1
            print(self.body_position.x)
        elif self.direction == 2: #DOWN
            self.body_position.y += 1
        elif self.direction == 3: #LEFT
            self.body_position.x -= 1
            
    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        if abs(new_direction - self.direction) != 2:
            self.direction = new_direction

# Create snake instance outside the game loop
snake = Snake()

# Function Defenintion

def show_start_screen():
    pygame.display.set_caption('Start Screen')
    #pygame.display.setimage('start_screnn.png')
    DISPLAYSURF.blit(pygame.image.load('start_screnn.png'), (Width/2-150, Height/2-150))

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

    font = pygame.font.Font(None, 24) # Assuming you want a default font with 24pt size
    text_surface = font.render("Size:"+str(size), True, (0, 255, 0))
    DISPLAYSURF.blit(text_surface, (Board_Offset_X+200, Board_Offest_Y/2))
    
    font = pygame.font.Font(None, 24) # Assuming you want a default font with 24pt size
    text_surface = font.render("Speed:"+str(speed), True, (0, 255, 0))
    DISPLAYSURF.blit(text_surface, (Board_Offset_X+100, Board_Offest_Y/2))

def get_screen_coords(position):
    x = Board_Offset_X + (position.x*Board_Grid_Size)
    y = Board_Offest_Y + (position.y*Board_Grid_Size)
    return Position(x,y)

def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game_state == 0 and event.key == pygame.K_SPACE: 
                return 1  # Signal to start the game
            elif game_state == 1:
                if event.key == pygame.K_UP:
                    snake.change_direction(0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(2)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(3)
                elif event.key == pygame.K_SPACE:
                    return 2 # Finish game
            elif game_state == 2 and event.key == pygame.K_SPACE:
                return 3 # Restart game
                
            # Signal to change to game over state
    return None

def Update():
    global game_state  # Make sure to modify the global 'game_state' variable
    input_result = handle_input()
    if game_state == 0:
        if input_result == 1:
            game_state = 1
            print( "game started changed to 1")
    elif game_state == 1: #playing
        if input_result == 2:
            game_state = 2
            print ("game started changed to 2")
        else:
            snake.move()
    elif game_state == 2:
        if input_result == 3:
            game_state = 0
            print ("game started changed to 0")
           

def Draw(): 
    DISPLAYSURF.fill((0, 0, 0)) # Clear screen with black color
    if game_state == 0:
        show_start_screen()
        print ("Draw State 0")
    if game_state == 1:
        draw_screen()
        snake.render()
        print ("Draw State 1")
    elif game_state == 2:
        DISPLAYSURF.fill((0, 0, 0))
        print ("Draw State 2")

clock = pygame.time.Clock()

while True:
    Update()
    Draw()
    pygame.display.update()
    clock.tick(time)

