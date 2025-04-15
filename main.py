import pygame, sys
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
pygame.draw.line(DISPLAYSURF,"white", (0,0),(400,400),5)
pygame.draw.lines(DISPLAYSURF,"Yellow",False,[(50,100),(150,100),(150,150)],3)
#small change 01

while True:
   for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
   pygame.display.update()