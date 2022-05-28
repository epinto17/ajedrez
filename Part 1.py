#interfaz graica
import pygame
pygame.init()

width = 564
height = 564
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("CHESS")

white = (255, 255, 255)
black = (0, 0, 0)

flag = True

background = pygame.image.load("images/chessboard.png").convert()

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    screen.blit(background, [0, 0])
    pygame.display.flip()

pygame.quit()