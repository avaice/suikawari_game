import pygame
from view import top, game, clear, over
import settings
import status
import sys


# 初期化
pygame.init()  # Pygameの初期化
screen = pygame.display.set_mode(
    (settings.WINDOWSIZE_X, settings.WINDOWSIZE_Y))  # 画面を生成
pygame.display.set_caption("SUIKAWARI_GAME")  # タイトルバーに表示するゲーム名


def main():
    while 1:
        if status.scene == status.Scene.TOP:
            top.render(screen)
        elif status.scene == status.Scene.INGAME:
            game.render(screen)
        elif status.scene == status.Scene.CLEAR:
            clear.render(screen)
        elif status.scene == status.Scene.OVER:
            over.render(screen)
        elif status.scene == status.Scene.QUIT:
            pygame.quit()
            sys.exit()


if __name__ == "__main__":
    main()
