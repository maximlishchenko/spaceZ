import sys
import pygame
import random

pygame.font.init()

RED = (255, 0, 0)
crash_font = pygame.font.SysFont(None, 60)
instrument_font = pygame.font.SysFont(None, 25)


def check_events(screen, ship, sprites):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move ship right.
                ship.right()
            elif event.key == pygame.K_LEFT:
                # Move ship left.
                ship.left()
            elif event.key == pygame.K_q:
                # Move ship up.
                ship.up()
            elif event.key == pygame.K_a:
                # Move ship down.
                ship.down()
            elif event.key == pygame.K_SPACE:
                # Launch bitcoin
                roll = random.randint(1, 2)
                if roll == 1:
                    ship.launch_bitcoin(screen, sprites)
                else:
                    ship.launch_supercoin(screen, sprites)


def update_screen(sprites, ai_settings, screen, ship):
    """Update sprites & messages on the screen."""

    screen.blit(ai_settings.screen_backgrnd, [0, 0])
    rects = sprites.draw(screen)

    # If damage reaches 100%, display CRASHED message
    if ship.damage >= 100:
        message = crash_font.render('{}'.format('You Have Crashed!'), True, RED)
        message_rect = message.get_rect(center=(ai_settings.screen_width / 2, ai_settings.screen_height / 2))
        screen.blit(message, message_rect)

    # Update the instrument readings
    damage = instrument_font.render('{0:03}'.format(ship.damage), True, RED)
    screen.blit(damage, (100, 14))
    mining = instrument_font.render('{0:03}'.format(ship.mining), True, RED)
    screen.blit(mining, (338, 39))
    lives = instrument_font.render('{0:03}'.format(ai_settings.lives), True, RED)
    screen.blit(lives, (245, 14))
    score = instrument_font.render('{0:03}'.format(ai_settings.score), True, RED)
    screen.blit(score, (100, 42))

    # Update the background region.
    pygame.display.update(rects)
