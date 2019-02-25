import pygame, os, random, string

# Import helper functions.
#from helpers import top_draggable_sprite_at_point, aspect_scale, draw_rects
#from screen_helpers import quit_game, switch_to_screen, notify

# Import sprites.
from sprites.base_sprites import ImageSprite, ButtonSprite, InputBox, button_at_point, TextSprite

def quit_game(game_state):
    game_state.update({'quit': True})
    game_state.update({'screen_done': True})
    return game_state

def start_game(game_state):
    game_state.update({'active_screen': 'workshop_screen'})
    game_state.update({'screen_done': True})
    return game_state


def main_menu_loop(game_state):
    """The main menu screen loop.
    """

    game_surface = game_state.get('game_surface')
    clock = game_state.get('clock')
    fps = game_state.get('fps')
    screen_size = game_state.get('screen_size')
    screen_width = screen_size[0]
    screen_height = screen_size[1]
    framecount = 1

    #toast_stack = game_state.get('toast_stack')
    logo_sprites = pygame.sprite.OrderedUpdates()
    logo = ImageSprite(
            screen_width*0.315,
            screen_height*0.15,
            os.getcwd() +"/images/pixel-rubber-duck.png"
            )
    logo.rect.centerx = (screen_width/2)
    logo_sprites.add(logo)

    # company_name = game_state.get('company_name')
    # input_font = pygame.font.Font("ARCADECLASSIC.TTF", 40)
    # input_width, input_height = 0.1* screen_width, 0.0625*screen_height

    # company_name_input = InputBox(
    #     (0.5*screen_width) - (0.5*input_width),
    #     0.68*screen_height,
    #     input_width + 10,
    #     input_height + 10,
    #     input_font,
    #     (0, 0, 255),
    #     (255, 255, 0),
    #     center_x=0.5*screen_width,
    #     text=company_name,
    #     max_width=500
    # )
    # company_name_input.active = True

    # Main group of sprites to display.
    all_sprites = pygame.sprite.OrderedUpdates()
    all_sprites.add(
        ButtonSprite(
            (screen_width * 0.455),
            (screen_height * 0.8),
            'Play!',
            start_game,
            []),
        ButtonSprite(
            (screen_width * 0.455),
            (screen_height * 0.9),
            'Quit',
            quit_game,
            [],
        ),
    )

    # prompt = TextSprite((0.43*screen_width) , 0.62 *screen_height, 400, 30, "Enter Company Name", text_color=(255,255,255), arcade_font=True)
    # prompt.rect.centerx = (screen_width/2)
    # name_prompt = pygame.sprite.Group()
    # name_prompt.add(prompt)

    # Want to refactor this body into seperate functions.
    while not game_state.get('screen_done'):

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game(game_state)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                b = button_at_point(all_sprites, event.pos)
                if b:
                    game_state = b.on_click(game_state)

            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_RETURN:
            #         game_state.update({'company_name': company_name_input.text})
            #         start_game(game_state)
            #     else:
            #         company_name_input.event_handle(event) #Input Box Class has inbuilt event handling function for key down events.

        # Update.
        all_sprites.update()
        #toast_stack.update()

        # Display.
        game_surface.fill((0, 0, 0))
        all_sprites.draw(game_surface)
        logo_sprites.draw(game_surface)

        pygame.display.update()

        clock.tick(fps)

    return game_state
