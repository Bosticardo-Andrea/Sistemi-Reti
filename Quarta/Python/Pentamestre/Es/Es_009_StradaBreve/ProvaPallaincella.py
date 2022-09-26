import pygame
while(True):
    size = (500,500)
    BLACK,BLU,RED,GREEN = (0, 0, 0),(0, 0, 255),(128,0,0),(0, 255, 0)
    pygame.init()
    screen = pygame.display.set_mode(size)
    screen.fill(BLACK)
    fnt = pygame.font.SysFont("Times New Roman", 12)
    text = fnt.render("ciao", True, BLACK)
    screen.blit(text,(50,50))
    pygame.display.flip()