import pygame
from pygame.locals import *
import status


def render(screen):
    background_color = (135, 206, 250)
    screen.fill(background_color)
    font = pygame.font.Font("./resources/uzura.ttf", 60)  # 文字のフォント
    button_e = pygame.Rect(120, 350, 180, 60)  # おわるボタン
    text_title = font.render("ゲーム画面", True, (100, 255, 0))  # textは描画する文字列
    text_e = font.render("おわる", True, (30, 30, 30))

    pygame.draw.rect(screen, (60, 255, 60), button_e)
    screen.blit(text_title, [150, 80])  # 文字列の表示位置[x,y]
    screen.blit(text_e, [120, 350])

    pygame.display.update()    # 画面を更新して表示

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                status.scene = status.Scene.QUIT  # Pygameの終了(画面閉じられる)
                return
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # ボタンに左クリックした場合
                x, y = event.pos  # マウスでクリックされた位置
                if 120 <= x <= 300 and 350 <= y <= 410:  # おわるボタンをクリックしたら終了
                    status.scene = status.Scene.QUIT  # Pygameの終了(画面閉じられる)
                    return
