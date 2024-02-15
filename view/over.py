import pygame
from pygame.locals import *
import status

# ゲームオーバー画面


def render(screen):
    bg = pygame.image.load(
        "./resources/images/over.jpg").convert_alpha()  # スタート画面背景
    font = pygame.font.Font("./resources/uzura.ttf", 60)  # 文字のフォント
    rect_bg = bg.get_rect()
    screen.blit(bg, rect_bg)
    button_s = pygame.Rect(100, 250, 230, 60)  # つづけるボタン(x,y,xの長さ,yの長さ)
    button_e = pygame.Rect(120, 350, 180, 60)  # おわるボタン
    text_title = font.render("ゲームオーバー", True, (255, 0, 0))  # textは描画する文字列
    text_s = font.render("つづける", True, (30, 30, 30))
    text_e = font.render("おわる", True, (30, 30, 30))

    pygame.draw.rect(screen, (255, 60, 60), button_s)
    pygame.draw.rect(screen, (60, 255, 60), button_e)
    screen.blit(text_title, [150, 80])  # 文字列の表示位置[x,y]
    screen.blit(text_s, [100, 250])
    screen.blit(text_e, [120, 350])

    pygame.display.update()    # 画面を更新して表示
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                status.scene = status.Scene.QUIT  # Pygameの終了(画面閉じられる)
                return
            if event.type == MOUSEBUTTONDOWN:  # つづけるボタンに左クリックした場合
                x, y = event.pos  # マウスでクリックされた位置
                if 100 <= x <= 330 and 250 <= y <= 310:
                    status.scene = status.Scene.INGAME  # ゲーム画面に飛ぶ
                    return
                if 120 <= x <= 300 and 350 <= y <= 410:  # おわるボタンをクリックしたら終了
                    status.scene = status.Scene.QUIT  # Pygameの終了(画面閉じられる)
                    return
