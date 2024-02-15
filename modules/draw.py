import pygame
from pygame.locals import *
#プレイヤーの位置を描画する
def mark(screen,p_x,p_y,mark_size):
    pygame.draw.circle(screen, (100, 100, 100),
  (p_x + mark_size, p_y + mark_size), mark_size,mark_size)
    pygame.display.update()  # 画面を更新して表示



