import pygame
from ..sprite import Sprite
from ..tilemap import game_map


class Player(Sprite):
    def __init__(self, ch_x: int, ch_y: int, ch_width: int, ch_height: int, ch_image_name: str, health: int, step: int ):
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
        self.CAN_MOVE_DOWN = True

        self.JUMP = False
        self.COUNT_JUMP = 0
        self.CAN_JUMP = False
        
        self.COUNT_MAP_MOVING = 0
        
        self.EGGS_COUNT = 0
        self.FLY = False

    def move_player(self):
        pressed_buttons = pygame.key.get_pressed()
        
        if pressed_buttons[pygame.K_a] and self.RECT.x > 0:
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
                
        elif pressed_buttons[pygame.K_d]:
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
        elif pressed_buttons[pygame.K_s]: #go down
            if self.CAN_MOVE_DOWN == True:
                self.Y += self.STEP
                self.RECT.y += self.STEP

                self.DIRECTION = "DOWN"

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
    def gravity(self, block_list: list):

        self.can_move_down(hitbox_list = block_list, item = "block")

        self.CAN_MOVE_DOWN == True

        if not main_player.FLY:

            if self.DIRECTION == "LEFT" and not self.JUMP and self.RECT.x > 0:
                self.X -= 3
                self.RECT.x -= 3

                self.CAN_MOVE_LEFT = False
            if self.DIRECTION == "RIGHT" and not self.JUMP:
                self.X += 3
                self.RECT.x += 3

                self.CAN_MOVE_RIGHT = False
            
            if self.ACTIVE_GRAVITY:
                self.Y += self.GRAVITY
                self.RECT.y += self.GRAVITY
                
                self.IMAGE_NAME = "player/gravity/0.png"
                self.direction()

    def jump(self, block_list: list):

        pressed_buttons = pygame.key.get_pressed()

        self.CAN_MOVE_DOWN == True
        
        if self.CAN_JUMP:
            if pressed_buttons[pygame.K_SPACE] and self.COUNT_JUMP < 40:
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
            
    def fly (self):
        pressed_buttons = pygame.key.get_pressed()
        
        if pressed_buttons[pygame.K_f] :
            self.GRAVITY = 0
            self.FLY = True
        if pressed_buttons[pygame.K_g] :
            self.GRAVITY = 6
            self.FLY = False
            
            

    def move_map(self) -> int:
        
        pressed_buttons = pygame.key.get_pressed()
        
        player_position = self.RECT.x + self.RECT.width
        
        if player_position >= 640:
            if pressed_buttons[pygame.K_d] and self.CAN_MOVE_RIGHT:
                
                self.COUNT_MAP_MOVING += 3
                
                self.X -= 3
                self.RECT.x -= 3
        elif player_position <= 640:
            if self.COUNT_MAP_MOVING > 0:
                
                if pressed_buttons[pygame.K_a] and self.CAN_MOVE_LEFT:
                    self.COUNT_MAP_MOVING -= 3

                    self.X += 3
                    self.RECT.x += 3
        
        return self.COUNT_MAP_MOVING

main_player = Player(  
    ch_x = 100,
    ch_y = 500,
    ch_width = 50,
    ch_height = 50,
    ch_image_name = "player/idle/0.png",
    health = 100,
    step = 3
)
