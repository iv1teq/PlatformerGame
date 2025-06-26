import pygame

from .settings import Settings
from .tilemap import game_map

class Sprite(Settings):
    def __init__(self, sprite_ch_x, sprite_ch_y, sprite_ch_width, sprite_ch_height, sprite_ch_image_name):
        Settings.__init__(
            self,
            x = sprite_ch_x, 
            y = sprite_ch_y, 
            width = sprite_ch_width, 
            height = sprite_ch_height, 
            image_name = sprite_ch_image_name,
        )

        self.DIRECTION = ""
        
        self.COUNT_ANIMATION = 0
        self.SPEED_ANIMATION = 0
        self.CURRENT_ANIMATION = ""
    
    def can_move_right(self, hitbox_list: list, item: str):
        for hitbox in hitbox_list:
            if self.RECT.y + self.RECT.height - 10 < hitbox.y + hitbox.height and self.RECT.y + self.RECT.height - 10 > hitbox.y:
                if self.RECT.x + self.RECT.width > hitbox.x and self.RECT.x < hitbox.x:
                    if item == "block":
                        self.CAN_MOVE_RIGHT = False
                        
                        self.X -= 4
                        self.RECT.x -= 4
                    
                    elif item == "egg":
                        game_map.delete_tile(
                            x = hitbox.x,
                            y = hitbox.y,
                            layer_name = "Шар яєць"
                        )
                        game_map.REMOVED_EGGS_HITBOXES.append((hitbox.x + game_map.MOVE, hitbox.y))
                        self.EGGS_COUNT += 1
                else:
                    self.CAN_MOVE_RIGHT = True
            else:
                self.CAN_MOVE_RIGHT = True

    def can_move_left(self, hitbox_list: list, item: str):
        for hitbox in hitbox_list:
            if self.RECT.y + self.RECT.height - 10 < hitbox.y + hitbox.height and self.RECT.y + self.RECT.height - 10 > hitbox.y:
                if self.RECT.x < hitbox.x + hitbox.width and self.RECT.x + self.RECT.width > hitbox.x + hitbox.width:
                    if item == "block":
                        self.CAN_MOVE_LEFT = False
                        
                        self.X += 4
                        self.RECT.x += 4
                        
                    elif item == "egg":
                        game_map.delete_tile(
                            x = hitbox.x,
                            y = hitbox.y,
                            layer_name= "Шар яєць"
                        )
                        game_map.REMOVED_EGGS_HITBOXES.append((hitbox.x + game_map.MOVE, hitbox.y))
                        self.EGGS_COUNT += 1
                else:
                    self.CAN_MOVE_LEFT = True
            else:
                self.CAN_MOVE_LEFT = True
    
    def can_move_down(self, hitbox_list: list, item, character = None):
        for element in hitbox_list:
            hitbox = pygame.Rect(element.x, element.y, element.width, 1)

            if self.RECT.colliderect(hitbox):
                if item == "block":
                    self.ACTIVE_GRAVITY = False

                    self.COUNT_JUMP = 0
                    self.DIRECTION = "IDLE"
                    self.CAN_JUMP = True

                    break
                elif item == "egg":
                    game_map.delete_tile(
                        x = hitbox.x,
                        y = hitbox.y,
                        layer_name = "Шар яєць"
                    )
                    
                    game_map.REMOVED_EGGS_HITBOXES.append((hitbox.x + game_map.MOVE, hitbox.y))
                    self.EGGS_COUNT += 1
                elif item == "chicken":
                    character.IS_DELETED = True
            else:
                self.ACTIVE_GRAVITY = True
    
    def can_move_up(self, block_list: list):
        for block in block_list:
            block_hitbox = pygame.Rect(block.x, block.y + block.height, block.width, 1)
            
            if self.RECT.colliderect(block_hitbox):
                self.CAN_JUMP = False
                self.JUMP = False
    
    def animation(self, folder_name: str, first_image: int, last_image: int, images_count: int):
        
        self.SPEED_ANIMATION += 0.5
        
        if self.SPEED_ANIMATION % images_count == 0:
            if last_image == self.COUNT_ANIMATION:
                self.COUNT_ANIMATION = first_image
            
            self.IMAGE_NAME = f"{folder_name}/{self.COUNT_ANIMATION}.png"
            self.direction()
            self.COUNT_ANIMATION += 1
    
    def gravity(self, block_list: list):
        
        self.can_move_down(hitbox_list = block_list, item = "block")

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
    
    def direction(self):
        if self.DIRECTION == 'RIGHT' or self.DIRECTION == 'IDLE':
            self.load_image()
        elif self.DIRECTION == 'LEFT':
            self.load_image(can_direction = True)