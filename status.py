from enum import Enum


class Scene(Enum):  # 画面のシーン
    TOP = "TOP"
    INGAME = "INGAME"
    CLEAR = "CLEAR"
    OVER = "OVER"
    QUIT = "QUIT"


# ここから状態定義
scene = Scene.TOP
