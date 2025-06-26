import pygame 

def quit_game(event: pygame.event):
    if event.type == pygame.QUIT:
        return True