import pygame

from .images import create_path
from .tilemap import game_map


class Settings:
    def __init__(self, x: int, y: int, width: int, height: int, image_name: str):
        self.X = x
        self.Y = y
        self.WIDTH = width
        self.HEIGHT = height
        self.IMAGE_NAME = image_name
        self.RECT = pygame.Rect(self.X + 7.5, self.Y + 10, self.WIDTH - 15, self.HEIGHT - 10)
        
        self.GRAVITY = 6
        
        self.ACTIVE_GRAVITY = True
        
        if self.IMAGE_NAME:
            self.load_image()
    
    def load_image(self, can_direction = False):
        self.IMAGE = pygame.image.load(create_path(path = f"assets/{self.IMAGE_NAME}"))
        self.IMAGE = pygame.transform.scale(
            surface = self.IMAGE,
            size = (self.WIDTH, self.HEIGHT)
            
        )
        self.IMAGE = pygame.transform.flip(
            surface = self.IMAGE,
            flip_x = can_direction,
            flip_y = False
        )
    
    def blit_image(self, screen: pygame.Surface):
        if "chicken" in self.IMAGE_NAME:
            self.CHICKEN_RECT = self.RECT.copy()
            self.CHICKEN_RECT.x -= game_map.MOVE

            screen.blit(self.IMAGE, (self.X - game_map.MOVE, self.Y))
        else:
            screen.blit(self.IMAGE, (self.X, self.Y))
    
    def draw_rect(self, screen: pygame.Surface):
        if "chicken" in self.IMAGE_NAME:
            pygame.draw.rect(screen, (255, 0, 0), self.CHICKEN_RECT)
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.RECT)
    
# 😊😊😊

heart1 = Settings(
    x = 21,
    y = 15,
    height = 24,
    width = 24,
    image_name = "items/heart.png"
)

heart2 = Settings(
    x = 45,
    y = 15,
    width = 24,
    height = 24,
    image_name = "items/heart.png"
)

heart3 = Settings(
    x = 69,
    y = 15,
    width = 24,
    height = 24,
    image_name = "items/heart.png"
)

heart4 = Settings(
    x = 93, 
    y = 15, 
    height = 24,
    width = 24,
    image_name = "items/heart.png"
)

heart5 = Settings(
    x = 117, 
    y = 15, 
    height = 24,
    width = 24,
    image_name = "items/heart.png"
)

meat = Settings(
    height = 21,
    width = 44,
    x = 387,
    y = 13,
    image_name = "items/meat.png"
)

key = Settings(
    height = 21,
    width = 39,
    x = 277,
    y = 13,
    image_name = "items/key.png"
)

egg = Settings(
    height = 31,
    width = 25,
    x = 183,
    y = 8,
    image_name = "items/egg.png"
)