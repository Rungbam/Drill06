from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
frame = 0
hand_arrow_x, hand_arrow_y = 0, 0
character_x, character_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
direction = 0

def handle_event():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    pass

def draw_point():
    global hand_arrow_x, hand_arrow_y
    hand_arrow_x, hand_arrow_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)


def move_character():
    global character_x, character_y
    global hand_arrow_x, hand_arrow_y

    # 현재 위치 기록
    start_x, start_y = character_x, character_y

    # 목표 위치 설정 (새로운 랜덤한 위치)
    hand_arrow_x, hand_arrow_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

    t = 0
    while t <= 1:
        clear_canvas()
        tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        character_x = (1 - t) * start_x + t * hand_arrow_x
        character_y = (1 - t) * start_y + t * hand_arrow_y

        if (character_x < hand_arrow_x):
            direction = 0
        elif (character_x > hand_arrow_x):
            direction = 1

        if direction == 0:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
        else:
            character.clip_draw(frame * 100, 200 * 1, 100, 100, character_x, character_y)
        hand_arrow.draw(hand_arrow_x, hand_arrow_y)

        update_canvas()

        t += 0.05
        delay(0.05)


while running:
    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if direction == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    else:
        character.clip_draw(frame * 100, 200 * 1, 100, 100, character_x, character_y)
    hand_arrow.draw(hand_arrow_x, hand_arrow_y)

    update_canvas()
    handle_event()
    frame = (frame + 1) % 8

    draw_point()
    move_character()
    delay(0.1)

close_canvas()