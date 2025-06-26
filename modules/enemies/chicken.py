from ..sprite import Sprite

class Chicken(Sprite):
    def __init__(self, ch_x: int, ch_y: int, ch_width: int, ch_height: int, ch_image_name: str):
        Sprite.__init__(
            self,
            sprite_ch_x = ch_x, 
            sprite_ch_y = ch_y, 
            sprite_ch_width = ch_width, 
            sprite_ch_height = ch_height, 
            sprite_ch_image_name = ch_image_name,
        )

        self.IS_DELETED = False
        self.CHICKEN_MOVE_COUNT = 0
    
    def move_chicken(self):
        
        self.animation(
            folder_name = "chicken/walk",
            first_image = 0,
            last_image = 3,
            images_count = 4
        )
        
        if self.CHICKEN_MOVE_COUNT < 250:
            self.DIRECTION = "RIGHT"
            self.direction()

            self.X += 1
            self.RECT.x += 1

        elif self.CHICKEN_MOVE_COUNT == 500:
            self.CHICKEN_MOVE_COUNT = 0

        elif self.CHICKEN_MOVE_COUNT > 250:
            self.DIRECTION = "LEFT"
            self.direction()

            self.X -= 1
            self.RECT.x -= 1
        
        self.CHICKEN_MOVE_COUNT += 1

chicken1 = Chicken(
    ch_x = 550,
    ch_y = 650,
    ch_width = 50,
    ch_height = 50,
    ch_image_name = "chicken/idle/0.png"
)
