import pygame

def press_k(event: pygame.event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_k:
            return True