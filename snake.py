import pygame

pygame.init()

# Create Surface
gaveDisplay = pygame.display.set_mode((800,600))

pygame.display.set_caption("The Snake") 

pygame.display.update()  #Update surface

gameExit = False
while not gameExit:   
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            gameExit = True

pygame.quit()  # Uninitialize pygame
quit() # Uninitialize python
