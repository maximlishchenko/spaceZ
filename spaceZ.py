import pygame
import random

# COMPLETE FILE PROVIDED IN STARTER CODE
from settings import Settings

# PARTIAL FILE PROVIDED IN STARTER CODE
import game_functions as gf

# IMPORT OTHER FILES/CLASSES HERE AS REQUIRED
from ship import Ship
from aliens import Roadster
from bitcoin import Bitcoin, Supercoin


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()

    # Set keys to repeat if held down.
    pygame.key.set_repeat(5,5)

    # Create settings object containing game settings
    ai_settings = Settings()

    # Create the main game screen
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    screen.blit(ai_settings.screen_backgrnd, [0, 0])

    # Create a main window caption
    pygame.display.set_caption("Space Z - Mars Flight")

    clock = pygame.time.Clock()

    while ai_settings.lives > 0:

        # ** CODE TO CREATE SPRITES/GROUPS GOES HERE **
        sprites = pygame.sprite.Group()
        ship = Ship(screen, ai_settings)
        sprites.add(ship)
        for i in range(ai_settings.aliens):
            roadster = Roadster(screen, ai_settings)
            sprites.add(roadster)

        # Refresh the background
        screen.blit(ai_settings.screen_backgrnd, [0, 0])
        sprites.clear(screen, ai_settings.screen_backgrnd)

        # Start the main loop for the game.
        while ship.damage < 100:

            # Watch for keyboard events.
            gf.check_events(screen, ship, sprites)
            # Tell all the sprites to update their status
            sprites.update(ai_settings, sprites)

            # ** ANY OTHER MAIN GAME CODE GOES HERE **
            clock.tick(60)  # adjust FPS
            roadster_hit = pygame.sprite.spritecollide(ship, sprites, False)
            for sprite in roadster_hit:
                # if ship collided with something other than itself
                # or bitcoin then it must be a roadster
                if sprite is not ship and sprite is not ship.bitcoin:
                    sprite.kill()  # remove the roadster from sprites
                    ai_settings.boom_sound.play()
                    roadster = Roadster(screen, ai_settings)  # replace with a new one
                    sprites.add(roadster)
                    ship.damage += 10  # increment damage

            if ship.bitcoin is not None:
                bitcoin_collision = pygame.sprite.spritecollide(ship.bitcoin, sprites, False)
                roadster_hit = []  # list containing the hit roadster
                for sprite in bitcoin_collision:
                    if sprite is not ship and sprite is not ship.bitcoin:
                        roadster_hit.append(sprite)
                        break  # we only want to add the first hit roadster
                if roadster_hit:
                    roadster_hit[0].kill()  # remove the first element from sprites
                    ai_settings.boom_sound.play()
                    # if bitcoin is supercoin, reassign angle
                    if isinstance(ship.bitcoin, Supercoin):
                        ship.bitcoin.angle = random.randint(0, 359)
                    # else destroy the bitcoin
                    else:
                        ship.bitcoin.kill()
                        ship.bitcoin = None
                    roadster = Roadster(screen, ai_settings)
                    sprites.add(roadster)
                    ai_settings.score += 10  # increment score

            sprites.clear(screen, ai_settings.screen_backgrnd)

            # Now update the sprites, etc. on the screen
            gf.update_screen(sprites, ai_settings, screen, ship)
            pygame.display.flip()

            # increment bitcoin mining
            if ship.mining < 100:
                ship.mining += 1

        # Wait for a keypress to continue
        null_event = pygame.event.wait()
        # Remove a life
        ai_settings.lives -= 1

    # GAME ENDS

# Call the main method to start the game
run_game()
