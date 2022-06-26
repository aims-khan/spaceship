import pygame
win = pygame.display.set_mode((900,500))

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.Quit:
                run =False
    pygame.quit()
    
if __name__ =="__main__":
    main()    
                