from pico2d import *
import math

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

click_positions = []
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
t = 0
def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    pass

def mouse_events():
    global running
    global click_positions

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_positions.append((event.x, TUK_HEIGHT - event.y))

running = True
frame = 0

while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)

    for pos in click_positions:
        hand_arrow_x, hand_arrow_y = pos
        hand_arrow.draw(hand_arrow_x, hand_arrow_y)

    if len(click_positions) > 0:
        hand_arrow_x, hand_arrow_y = click_positions[0]

        if t < 1:
            character_x = (1 - t) * character_x + t * hand_arrow_x
            character_y = (1 - t) * character_y + t * hand_arrow_y
            t += 0.02
        else:
            t = 0
            click_positions.pop(0)

    update_canvas()
    mouse_events()
    handle_events()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()