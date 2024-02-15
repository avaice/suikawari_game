import pygame
from pygame.locals import *
import random
import math
import serial

# 他ファイルのインポート
from modules import update, draw
import status


WINDOWSIZE_X = 450  # 盤面のサイズ
WINDOWSIZE_Y = 450

# ゲーム画面


def render(screen):
    # 盤面は9*9とする
    size = 50
    player_x = random.randrange(0, 9) * size
    player_y = random.randrange(0, 9) * size
    suika_x = random.randrange(0, 9) * size
    suika_y = random.randrange(0, 9) * size
    dis = calc_distance((player_x / size, player_y / size),
                        (suika_x / size, suika_y / size))
    mark_size = 25  # プレイヤーの位置表示の大きさ(半径)
    count = 0  # 経過ターン格納変数
    p_x = player_x/size  # プレイヤーの初期位置の座標
    p_y = player_y/size

    bg = pygame.image.load("./resources/images/beach.jpg").convert_alpha()
    font = pygame.font.Font("./resources/uzura.ttf", 60)  # 文字のフォント
    rect_bg = bg.get_rect()
    screen.blit(bg, rect_bg)
    turn_dis = pygame.Rect(500, 0, 300, 100)  # ターン表示枠
    pygame.draw.rect(screen, (60, 255, 60), turn_dis)  # 右上にターン表示枠
    text_t = font.render("0ターン", True, (30, 30, 30))  # 経過ターン
    screen.blit(text_t, [540, 20])  # 経過ターン表示位置
    dis_sc = pygame.Rect(500, 100, 300, 400)  # スイカとの距離表示枠
    pygame.draw.rect(screen, (255, 0, 0), dis_sc)  # 右下に距離表示枠
    text_head = font.render("スイカまで", True, (30, 30, 30))
    text_d = font.render(str(dis), True, (30, 30, 30))
    screen.blit(text_head, [505, 120])  # 「スイカまで」表示位置
    screen.blit(text_d, [500, 200])  # 距離表示位置
    text_p = font.render("プレイヤー", True, (30, 30, 30))
    screen.blit(text_p, [505, 300])  # テキスト「プレイヤー」表示位置
    text_l = font.render("["+str(p_x)+","+str(p_y)+"]", True, (30, 30, 30))
    screen.blit(text_l, [500, 380])  # 現在地表示位置
    # 初期位置表示↓
    draw.mark(screen, player_x, player_y, mark_size)

    pygame.display.update()  # 画面を更新して表示
    data = 0  # マイコンからのデータを受けとる変数
    ser = serial.Serial('COM5', 9600, timeout=1)  # マイコンとシリアル通信する

    while count < 15:  # 15ターンで終了とする

        # マイコンのイベント
        line = ser.readline()  # マイコンからのデータを受け取る
        if len(line) != 0:  # データを受け取ったらintに変換
            str_data = str(line, 'ascii').strip()
            data = int(str_data)
            # 移動方向は1は上　2は右上　3は右　4は右下　
            # 5は下　6は左下　7は左　8は左上
            if data == 3:
                if player_x + size <= WINDOWSIZE_X:
                    player_x += size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")  # プロンプトに通知、画面には表示しないので注意
            elif data == 7:
                if player_x - size >= 0:
                    player_x -= size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 1:
                if player_y - size >= 0:
                    player_y -= size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 5:
                if player_y + size <= WINDOWSIZE_Y:
                    player_y += size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 2:
                if player_x + size <= WINDOWSIZE_X and player_y - size >= 0:
                    player_x += size
                    player_y -= size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 4:
                if player_x + size <= WINDOWSIZE_X and player_y + size <= WINDOWSIZE_Y:
                    player_x += size
                    player_y += size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 6:
                if player_x - size >= 0 and player_y + size <= WINDOWSIZE_Y:
                    player_x -= size
                    player_y += size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
            elif data == 8:
                if player_x - size >= 0 and player_y - size >= 0:
                    player_x -= size
                    player_y -= size
                    draw.mark(screen, player_x, player_y, mark_size)
                    count += 1
                else:
                    print("範囲外")
                    # スイカまでの距離を計算し逐次画面表示する
            dis = calc_distance(
                (player_x / size, player_y / size), (suika_x / size, suika_y / size))
            update.sc_up(screen, count, dis, player_x/size, player_y/size)
            if suika_x == player_x and suika_y == player_y:  # プレイヤーとスイカの座標が同じだとクリア
                status.scene = status.Scene.CLEAR
                return
        else:
            # キーボードのイベント
            # 注意：マイコンのデータ受信を優先したためキーイベントは処理が遅い
            # wは上　aは左　sは下　dは右
            # eは右上　cは右下　zは左下　qは左上
            for event in pygame.event.get():
                if event.type == QUIT:  # 閉じるボタンが押されたら終了
                    status.scene = status.Scene.QUIT  # Pygameの終了(画面閉じられる)
                    return
                if event.type == KEYDOWN:  # 何かキーが押されたら
                    if event.key == K_d:  # dキーが押された
                        if player_x + size <= WINDOWSIZE_X:
                            player_x += size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1

                        else:
                            print("範囲外")
                    if event.key == K_a:
                        if player_x - size >= 0:
                            player_x -= size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_w:
                        if player_y - size >= 0:
                            player_y -= size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_s:
                        if player_y + size <= WINDOWSIZE_Y:
                            player_y += size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_e:
                        if player_x + size <= WINDOWSIZE_X and player_y - size >= 0:
                            player_x += size
                            player_y -= size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_c:
                        if player_x + size <= WINDOWSIZE_X and player_y + size <= WINDOWSIZE_Y:
                            player_x += size
                            player_y += size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_z:
                        if player_x - size >= 0 and player_y + size <= WINDOWSIZE_Y:
                            player_x -= size
                            player_y += size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")
                    if event.key == K_q:
                        if player_x - size >= 0 and player_y - size >= 0:
                            player_x -= size
                            player_y -= size
                            draw.mark(screen, player_x, player_y, mark_size)
                            count += 1
                        else:
                            print("範囲外")

                dis = calc_distance(
                    (player_x / size, player_y / size), (suika_x / size, suika_y / size))
                update.sc_up(screen, count, dis, player_x /
                             size, player_y / size)
                if suika_x == player_x and suika_y == player_y:  # プレイヤーとスイカの座標が同じだとクリア
                    status.scene = status.Scene.CLEAR
                    return
    ser.close()  # マイコンのデータ受信を終了する

    status.scene = status.Scene.OVER  # 15ターン経過でゲームオーバー
    return


def calc_distance(pos1, pos2):
    # ２点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)
