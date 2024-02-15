import pygame
from pygame.locals import *
# ターンやプレイヤーの位置を逐次更新し画面に表示する


def sc_up(screen, count, dis, p_x, p_y):  # 画面を更新する
    font = pygame.font.Font("./resources/uzura.ttf", 60)  # 文字のフォント
    turn_dis = pygame.Rect(500, 0, 300, 100)  # ターン表示枠
    pygame.draw.rect(screen, (60, 255, 60), turn_dis)  # 右上にターン表示枠
    text_t = font.render(str(count)+"ターン", True, (30, 30, 30))  # 経過ターン
    screen.blit(text_t, [540, 20])  # 経過ターン表示位置
    dis_sc = pygame.Rect(500, 100, 300, 400)
    pygame.draw.rect(screen, (255, 0, 0), dis_sc)  # 右下に距離表示枠
    text_head = font.render("スイカまで", True, (30, 30, 30))
    screen.blit(text_head, [505, 120])  # 「スイカまで」表示位置
    text_d = font.render(str(dis), True, (30, 30, 30))
    screen.blit(text_d, [500, 200])  # 距離表示位置
    text_p = font.render("プレイヤー", True, (30, 30, 30))
    screen.blit(text_p, [505, 300])  # 「プレイヤー」表示位置
    text_l = font.render("["+str(p_x)+","+str(p_y)+"]", True, (30, 30, 30))
    screen.blit(text_l, [500, 380])  # 現在地表示位置
    pygame.display.update()  # 画面を更新して表示
