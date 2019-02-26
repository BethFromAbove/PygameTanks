import pygame, os


# Import sprite options
from sprites.base_sprites import ImageSprite, ButtonSprite, button_at_point, ThumbnailSprite, TextSprite, ButtonImageSprite

pygame.init()


def quit_game(game_state):
    game_state.update({'quit': True})
    game_state.update({'screen_done': True})
    return game_state

# Main group of sprites to display.
general_sprites = pygame.sprite.OrderedUpdates()
tank_sprites = pygame.sprite.OrderedUpdates()


def arena_loop(game_state):
    """The arena screen loop."""

    game_surface = game_state.get('game_surface')
    clock = game_state.get('clock')
    fps = game_state.get('fps')
    size = game_state.get('screen_size')
    screen_width = size[0]
    screen_height = size[1]


    background_image = ImageSprite(0, 0, os.getcwd() + '/images/Background.png')
    general_sprites.add(background_image)


    general_sprites.add(
        ButtonSprite(screen_width * 0.8, screen_height * 0.05, 'QUIT', quit_game, []),
    )


    tank1 = ImageSprite(0,0, os.getcwd() + '/images/Tank.png')
    tank2 = ImageSprite(300,0, os.getcwd() + '/images/Tank.png')
    tank_sprites.add(tank1,tank2)


    while not game_state.get('screen_done'):

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game(game_state)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                
                b = button_at_point(general_sprites, event.pos)
                if b:
                    game_state = b.on_click(game_state)

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    tank1.move((10,0))
                elif keys[pygame.K_LEFT]:
                    tank1.move((-10,0))
                elif keys[pygame.K_UP]:
                    tank1.move((0,-10))
                elif keys[pygame.K_DOWN]:
                    tank1.move((0,10))
                elif keys[pygame.K_d]:
                    tank2.move((10,0))
                elif keys[pygame.K_a]:
                    tank2.move((-10,0))
                elif keys[pygame.K_w]:
                    tank2.move((0,-10))
                elif keys[pygame.K_s]:
                    tank2.move((0,10))


    
        # Display.
        game_surface.fill((255, 0, 0))

        general_sprites.draw(game_surface)
        tank_sprites.draw(game_surface)
        
        pygame.display.update()

        clock.tick(fps)

    return game_state
