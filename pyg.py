import pygame

pygame.init()
black = (0,0,0)
white = (255,255,255)

# Create Surface
gameDisplay = pygame.display.set_mode((800,600))

#pygame.diplay.flip() ---> Updates the entire surface at once

pygame.display.set_caption("The Snake")  # Window Title

gameExit = False
while not gameExit:     # Main loop
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(black)
    pygame.display.update()

pygame.quit()  # Uninitialize pygame
quit() # Uninitialize python
