import sys, pygame
import time
pygame.init()

width, height = 640, 480
size=(width, height)
speed = [0, 0]
black = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: 
            print("É stato premuto il tasto: ",event.__dict__["unicode"])
            #print(event.__dict__)# --> controlla il dizionario
            if event.__dict__["unicode"] == "a":
                speed[0] -= 5
            if event.__dict__["unicode"] == "w":
                speed[1] -= 5
            if event.__dict__["unicode"] == "s":
                speed[1] += 5
            if event.__dict__["unicode"] == "d":
                speed[0] +=5
    
    if ballrect.left < 0 or ballrect.right > width:
        if speed[0] <= 0:
            speed[0] = 0
    if ballrect.top < 0 or ballrect.bottom > height:
        if speed[1] <= 0:
            speed[1] = 0   
    ballrect = ballrect.move(speed)
    speed[0] = 0
    speed[1] = 0

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(0.0000000001)