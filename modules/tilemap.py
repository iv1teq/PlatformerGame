import pygame
import pytmx
from .images import create_path

class Map:
    def __init__(self, filename: str):
        self.PATH = create_path(path = f"assets/tilemaps/{filename}")
        self.TILEMAP = pytmx.load_pygame(self.PATH)
        self.WIDTH =  self.TILEMAP.tilewidth
        self.HEIGHT = self.TILEMAP.tileheight
        
        self.MOVE = 0
        
        self.REMOVED_EGGS_HITBOXES = []
    
    def blit_map(self, screen: pygame.Surface, move: int):
        self.TILE_LAYERS = self.TILEMAP.visible_tile_layers

        for layer_id in self.TILE_LAYERS:
            layer = self.TILEMAP.layers[layer_id]
            
            for x, y, cell in layer:
                if cell:
                    image = self.TILEMAP.get_tile_image_by_gid(cell)
                    
                    self.MOVE = move
                    
                    screen.blit(image, (x * self.WIDTH - move, y * self.HEIGHT))
    
    def blit_map_hitboxes(self, screen: pygame.Surface):
        self.COLLISION_LAYER = self.TILEMAP.get_layer_by_name("Шар колізії блоків")
        
        for collision_object in self.COLLISION_LAYER:
            
            block_hitbox = pygame.Rect(
                collision_object.x - self.MOVE, 
                collision_object.y, 
                collision_object.width, 
                collision_object.height
            )
            
            pygame.draw.rect(
                surface = screen, 
                color = (255, 0, 0), 
                rect = block_hitbox,
                width = 2
            )
    
    def create_hitbox_list(self, layer_name):
        self.COLLISION_LAYER = self.TILEMAP.get_layer_by_name(layer_name)
        
        map_hitboxes = []
        
        for collision_object in self.COLLISION_LAYER:
            if (collision_object.x, collision_object.y) in self.REMOVED_EGGS_HITBOXES:
                continue 
            
            hitbox = pygame.Rect(
                collision_object.x - self.MOVE, 
                collision_object.y, 
                collision_object.width, 
                collision_object.height
            )
            
            map_hitboxes.append(hitbox)
            
        return map_hitboxes 
    def blit_decorations(self, screen: pygame.Surface):
        self.DECORATION_LAYER = self.TILEMAP.get_layer_by_name("Шар декорацій")
        
        for decoration_object in self.DECORATION_LAYER:
            screen.blit(decoration_object.image, (decoration_object.x - self.MOVE, decoration_object.y))

    def delete_tile(self, x: int, y: int, layer_name: str):
        self.LAYER = self.TILEMAP.get_layer_by_name(layer_name)
        
        x += self.MOVE
        
        column =  x // 50
        row = y // 50
        
        self.LAYER.data[row][column] = 0
    
game_map = Map(filename = "First.project/map.tmx")
