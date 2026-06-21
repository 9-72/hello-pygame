

import pygame
import color
import ball


def check_run():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    
    return True


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('pygame')

    running = True

    while running:
        running = check_run()
        ball.move()

        screen.fill(color.BLACK)

        ball.draw(screen)

        pygame.display.flip()

    pygame.quit()


main()
