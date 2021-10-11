import pygame
from random import randrange
import sys

# init = initialize
pygame.init()


s_w = 500
s_h = 500
# Display Surface              (width, height)
screen = pygame.display.set_mode((s_w, s_h))


# screen title / icon
pygame.display.set_caption('GameWindow')

# load image from external -> 相對位置 ex:所在位置中的images folder 裡面的 icon.png
# 圖片顯示分為兩種：Display Surface (what user can see on the screen)/ (Regular) Surface

icon_surface = pygame.image.load('images/icon.png')  # 載入圖片 (ex: 32pixel by 32pixel)
pygame.display.set_icon(icon_surface) # 圖標
screen.blit(icon_surface, (10, 10)) # 將圖片放入畫面中 (Regular -> Display)(不限畫質)
screen.fill((255, 0, 0)) # 填滿顏色 (R,G,B)

pygame.display.update() # 每次都要更新(會覆蓋過去)


gameRunning = True # 遊戲執行
keyPressed = False # 設置按住按鍵可以連按

# 設置移動的物件
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
player = Player(0, 0)
group.add(player)

while gameRunning:
    # contents of the game

    # def event.get(): return EventObjectList = ['QUIT', 'KEYDOWN', 'MOUSEDOWN' , ......]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() # 按X才能關閉

        if event.type == pygame.KEYDOWN:
            keyPressed = True # 偵測有沒有按鍵被按下
            if event.key == pygame.K_d: # 若按下的是D 則向右移動
                player.x += 5
            if event.key == pygame.K_a: # 若按下的是A 則向左移動
                player.x -= 5
            if event.key == pygame.K_w: # 若按下的是W 則向上移動
                player.y -= 5
            if event.key == pygame.K_s: # 若按下的是S 則向下移動
                player.y += 5

        if event.type == pygame.KEYUP:
            keyPressed = False # 偵測有沒有按鍵被放開

    if keyPressed:
        screen.fill( (randrange(0, 255), randrange(0, 255), randrange(0, 255)) )

    # 更新角色移動
    group.update()
    group.draw(screen)

    pygame.display.update()