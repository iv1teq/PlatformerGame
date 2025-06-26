import pygame
from ..sprite import Sprite
from ..tilemap import game_map

class Player(Sprite):
    def __init__(self, ch_x: int, ch_y: int, ch_width: int, ch_height: int, ch_image_name: str, health: int, step: int):
        Sprite.__init__(
            self,
            sprite_ch_x = ch_x, 
            sprite_ch_y = ch_y, 
            sprite_ch_width = ch_width, 
            sprite_ch_height = ch_height, 
            sprite_ch_image_name = ch_image_name
        )
        
        self.HEALTH = health
        self.STEP = step
        
        self.CAN_MOVE_RIGHT = True
        self.CAN_MOVE_LEFT = True

        self.JUMP = False
        self.COUNT_JUMP = 0
        self.CAN_JUMP = False
        
        self.COUNT_MAP_MOVING = 0
        
        self.EGGS_COUNT = 0

    def move_player(self):
        
        pressed_buttons = pygame.key.get_pressed()
        
        if pressed_buttons[pygame.K_LEFT] and self.RECT.x > 0:
            if self.CAN_MOVE_LEFT:
                self.X -= self.STEP
                self.RECT.x -= self.STEP

                self.DIRECTION = "LEFT"
                
                if self.CURRENT_ANIMATION != "run":
                    self.COUNT_ANIMATION = 0 
                    self.CURRENT_ANIMATION = "run"
                
                self.animation(
                    folder_name= "player/run",
                    first_image = 0,
                    last_image = 5,
                    images_count = 6
                )
                
        elif pressed_buttons[pygame.K_RIGHT]:
            if self.CAN_MOVE_RIGHT:
                self.X += self.STEP
                self.RECT.x += self.STEP

                self.DIRECTION = "RIGHT"

                if self.CURRENT_ANIMATION != "run":
                    self.COUNT_ANIMATION = 0 
                    self.CURRENT_ANIMATION = "run"
                
                
                self.animation(
                    folder_name = "player/run",
                    first_image = 0,
                    last_image = 5,
                    images_count = 6
                )
        else:
            if self.JUMP == False and self.ACTIVE_GRAVITY == False:
                
                if self.CURRENT_ANIMATION != "idle":
                    self.COUNT_ANIMATION = 0 
                    self.CURRENT_ANIMATION = "idle"
                    
                self.animation(
                    folder_name = "player/idle",
                    first_image = 0,
                    last_image = 3,
                    images_count = 4
                )
    
    def jump(self, block_list: list):

        pressed_buttons = pygame.key.get_pressed()

        if self.CAN_JUMP:
            if pressed_buttons[pygame.K_UP] and self.COUNT_JUMP < 40:
                self.JUMP = True
                self.COUNT_JUMP += 1

                self.Y -= 12
                self.RECT.y -= 12
                
                self.IMAGE_NAME = 'player/jump/0.png'
                self.direction()
                
                self.can_move_up(block_list = block_list)

                if self.DIRECTION == "LEFT" and self.RECT.x > 0:
                    self.X -= 3
                    self.RECT.x -= 3

                    self.CAN_MOVE_LEFT = False
                if self.DIRECTION == "RIGHT":
                    self.X += 3
                    self.RECT.x += 3

                    self.CAN_MOVE_RIGHT = False

            elif self.COUNT_JUMP >= 40:
                self.JUMP = False
            elif self.COUNT_JUMP > 0 and self.COUNT_JUMP < 40 and not pressed_buttons[pygame.K_UP]:
                self.JUMP = False
                self.CAN_JUMP = False

    def move_map(self) -> int:
        
        pressed_buttons = pygame.key.get_pressed()
        
        player_position = self.RECT.x + self.RECT.width
        
        if player_position >= 640:
            if pressed_buttons[pygame.K_RIGHT] and self.CAN_MOVE_RIGHT:
                
                self.COUNT_MAP_MOVING += 3
                
                self.X -= 3
                self.RECT.x -= 3
        elif player_position <= 640:
            if self.COUNT_MAP_MOVING > 0:
                
                if pressed_buttons[pygame.K_LEFT] and self.CAN_MOVE_LEFT:
                    self.COUNT_MAP_MOVING -= 3

                    self.X += 3
                    self.RECT.x += 3
        
        return self.COUNT_MAP_MOVING

main_player = Player(  
    ch_x = 600,
    ch_y = 650,
    ch_width = 45,
    ch_height = 45,
    ch_image_name = "player/idle/0.png",
    health = 100,
    step = 3
)
