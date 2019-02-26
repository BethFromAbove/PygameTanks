import pygame, os

from arena_screen import arena_loop
from main_menu_screen import main_menu_loop


#from sprites.base_sprites import ToastStack

# Initialise pygame stuff.
pygame.init()

clock = pygame.time.Clock()
general_sprites = pygame.sprite.OrderedUpdates()
display_width = 1200
display_height = 675
game_surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')
#icon = pygame.image.load(os.getcwd() + '/data/imgbase/sporktop.png')
#pygame.display.set_icon(icon)
pygame.display.update()

game_state = {
    'clock': clock,
    'fps': 60,
    'game_surface': game_surface,
    'screen_done': False,
    'quit': False,
    'screen_size': (display_width, display_height),
    'active_screen': 'main_menu_screen',
}

done = False

while not done:
    active_screen = game_state.get('active_screen')

    if game_state.get('quit'):
        done = True

    elif active_screen == 'main_menu_screen':
        game_state.update({'screen_done': False})
        game_state = main_menu_loop(game_state)

    elif active_screen == 'arena_screen':
        game_state.update({'screen_done': False})
        game_state = arena_loop(game_state)


    elif active_screen == 'game_end_screen':
        game_state.update({'screen_done': False})
        game_state = game_end_loop(game_state)

pygame.quit()
