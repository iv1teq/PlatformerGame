import pygame

from .app import screen
from .events import quit_game, press_k
from .player import main_player
from .sounds import sound1
from .tilemap import game_map
from .enemies import chicken1
from .settings import heart1, heart2, heart3, heart4, heart5, egg, meat, key
from .fonts import count_font, key_count_text , meat_count_text

pygame.init()

def run():
    running = True

    clock = pygame.time.Clock()
    
    while running:
        screen.fill((0, 0, 0))
        
        # Оновлюємо лічильник яєць
        egg_count_text = count_font.render(f"{main_player.EGGS_COUNT}", True, (255, 255, 255))
        
        screen.blit(egg_count_text, (212, 11))
        screen.blit(key_count_text, (325, 11))
        screen.blit(meat_count_text, (443, 11))
        
        for event in pygame.event.get():
            if quit_game(event):
                running = False
                pygame.quit()
            elif press_k(event):
                print("Натиснуто клавішу К")
                sound1.play()


        move = main_player.move_map()
        game_map.blit_map(screen = screen, move = move)
        
        map_blocks = game_map.create_hitbox_list(layer_name = "Шар колізії блоків")
        map_eggs = game_map.create_hitbox_list(layer_name = "Шар колізії яєць")
        
        
        # game_map.blit_map_hitboxes(screen = screen)
        game_map.blit_decorations(screen = screen)
        
        # main_player.draw_rect(screen = screen)
        main_player.blit_image(screen = screen)
        main_player.gravity(block_list = map_blocks)
        main_player.move_player()

        main_player.can_move_right(hitbox_list = map_blocks, item = "block")
        main_player.can_move_right(hitbox_list = map_eggs, item = "egg")
        main_player.can_move_left(hitbox_list = map_blocks, item = "block")
        main_player.can_move_left(hitbox_list = map_eggs, item = "egg")

        main_player.jump(block_list = map_blocks)
        
        heart1.load_image()
        heart1.blit_image(screen = screen)
        heart2.load_image()
        heart2.blit_image(screen = screen)
        heart3.load_image()
        heart3.blit_image(screen = screen)
        heart4.load_image()
        heart4.blit_image(screen = screen)
        heart5.load_image()
        heart5.blit_image(screen = screen)
        
        
        egg.load_image()
        egg.blit_image(screen = screen)
        meat.load_image()
        meat.blit_image(screen = screen)
        key.load_image()
        key.blit_image(screen = screen)
        
        
        if not chicken1.IS_DELETED:
            chicken1.blit_image(screen = screen)
            # chicken1.draw_rect(screen = screen)
            chicken1.move_chicken()
            main_player.can_move_down(hitbox_list = [chicken1.CHICKEN_RECT], item = "chicken", character = chicken1)
        
        clock.tick(60)
        pygame.display.flip()