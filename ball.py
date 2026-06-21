
import pygame
import color

r = 100
posX, posY = 400, 300

def draw(screen):
    pygame.draw.circle(screen, color.RED, (posX, posY), r)


# def move():
#     keys = pygame.key.get_pressed()

#     global posX
#     global posY

#     if keys[pygame.K_DOWN]:
#         posY += 1
    
#     if keys[pygame.K_UP]:
#         posY -= 1
    
#     if keys[pygame.K_LEFT]:
#         posX -= 1

#     if keys[pygame.K_RIGHT]:
#         posX += 1

def move():
    global posX
    global posY
    posX, posY = pygame.mouse.get_pos()
