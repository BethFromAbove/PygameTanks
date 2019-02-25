import pygame, os

# Import helper functions.
#from helpers import top_draggable_sprite_at_point, aspect_scale, draw_rects
#from screen_helpers import quit_game, switch_to_screen, notify

# Import sprites.
from sprites.base_sprites import ImageSprite, ButtonSprite, button_at_point, ThumbnailSprite, TextSprite, ButtonImageSprite

pygame.init()




def end_game(game_state):
    game_state.update({'quit': True})
    game_state.update({'screen_done': True})
    return game_state


# Main group of sprites to display.
general_sprites = pygame.sprite.OrderedUpdates()


def workshop_loop(game_state):
    """The workshop screen loop."""


    #remove all sprites from previous time screen was open

    game_surface = game_state.get('game_surface')
    clock = game_state.get('clock')
    fps = game_state.get('fps')
    size = game_state.get('screen_size')
    screen_width = size[0]
    screen_height = size[1]


    background_image = ImageSprite(0, 0, os.getcwd() + '/images/Mountain.jpg')
    general_sprites.add(background_image)


    general_sprites.add(
        ButtonSprite(screen_width * 0.8, screen_height * 0.05, 'QUIT', quit_game, []),
    )

    # Want to refactor this body into seperate functions.
    while not game_state.get('screen_done'):

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game(game_state)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                b = button_at_point(general_sprites, event.pos)
                if b:
                    click.play()
                    game_state = b.on_click(game_state)

        # Update.
        #toast_stack.update()
                
        # Display.
        game_surface.fill((255, 0, 0))

        general_sprites.draw(game_surface)

        #toast_stack.draw(game_surface)
        
        pygame.display.update()

        clock.tick(fps)

    return game_state
