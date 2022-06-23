import pygame
import os
width, height = 900 , 500

WIN = pygame.display.set_mode((width , height))
pygame.display.set_caption("spacesgip evening")
WHITE = (255,255,255)
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("assets","spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),90)

RED_SPACEHIP_IMAGE = pygame.image.load(os.path.join("assets","spaceship_red.png"))
RED_SPACEHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACEHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)

def draw_window():
        WIN.fill(WHITE)
        WIN.blit(YELLOW_SPACESHIP,(300, 100))
        WIN.blit(RED_SPACEHIP,(700, 100))
        pygame.display.update()
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.QUIT()
    
if __name__=="__main__":
    main()