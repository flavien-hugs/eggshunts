# src/main.py

import sys
import pygame
from spritecart import SpriteCart
from spriteeggs import SpriteEggs


def main():
    pygame.init()
    screen_weight = 800
    screen_height = 480
    fpsclock = pygame.time.Clock()

    screen = pygame.display.set_mode((screen_weight, screen_height))
    pygame.display.set_caption("eggs hunts".upper())
    pygame.display.set_icon(pygame.image.load("assets/cart.png"))

    screen_background = pygame.image.load("assets/screen.jpg")
    ground_image = pygame.image.load("assets/ground.png")
    chocolate_bar = pygame.image.load("assets/chocolate.png")
    chocolate_bar = pygame.transform.scale(chocolate_bar, (30, 30))

    # keyboard pressed
    keyboard_pressed = {}

    # color bar chocolate
    color_chocolate_bar = (87, 64, 53)

    # instance sprite cart
    spritecart = SpriteCart(screen_weight, screen_height)

    # instance sprite eggs
    eggs = pygame.sprite.Group()
    eggs.add(SpriteEggs(screen_weight, screen_height, spritecart))
    eggs.add(SpriteEggs(screen_weight, screen_height, spritecart))
    eggs.add(SpriteEggs(screen_weight, screen_height, spritecart))

    while True:
        screen.blit(screen_background, (0, 0))

        # sprite eggs
        eggs.draw(screen)

        # sprite cart
        screen.blit(spritecart.image, spritecart.rect)
        screen.blit(ground_image, (0, 0))

        # create chocolate foregroungbar
        pygame.draw.rect(
            screen, (128, 128, 128),
            [0, screen_height - 30, screen_weight, 8]
        )
        # create chocolate backgroungbar
        chocolate_width = (spritecart.health * 3) - 20
        pygame.draw.rect(
            screen, color_chocolate_bar,
            [0, screen_height - 30, chocolate_width, 8]
        )
        # chocolate bar
        screen.blit(
            chocolate_bar,
            (chocolate_width - chocolate_bar.get_width() / 2, 440)
        )

        # down eggs gravity
        for egg in eggs:
            egg.down_gravity_eggs()

        # get touch pressed
        if keyboard_pressed.get(pygame.K_RIGHT):
            spritecart.move_right()
            print("move to right")
        elif keyboard_pressed.get(pygame.K_LEFT):
            print("move to left")
            spritecart.move_left()

        # update screen
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
                print("exit game")
            elif event.type == pygame.KEYDOWN:
                keyboard_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                keyboard_pressed[event.key] = False

        fpsclock.tick(60)
        pygame.display.update()


if __name__ == '__main__':
    main()
