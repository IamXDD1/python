import pygame
from random import randrange
import sys
# init = abbr of initialize
pygame.init()
s_w = 500
s_h = 500
screen = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption('GameWindow')
icon_surface = pygame.image.load('images/icon.png')  # 32pixel by 32pixel
screen.fill((255, 0, 0))
screen.blit(icon_surface, (10, 10))
pygame.display.update()
pygame.display.set_icon(icon_surface)
gameRunning = True
keyPressed = False


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = icon_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def update(self):
        self.rect.topleft = (self.x, self.y)


group = pygame.sprite.Group()
Fuck = Player(0, 0)
group.add(Fuck)


while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keyPressed = True
            if event.key == pygame.K_d:
                Fuck.x += 5
            if event.key == pygame.K_a:
                Fuck.x -= 5
            if event.key == pygame.K_w:
                Fuck.y -= 5
            if event.key == pygame.K_s:
                Fuck.y += 5

        if event.type == pygame.KEYUP:
            keyPressed = False
    if keyPressed:
        screen.fill((randrange(0, 255), randrange(0, 255), randrange(0, 255)))

    group.update()
    group.draw(screen)
    pygame.display.update()