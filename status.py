from enum import Enum


class Scene(Enum):  # 画面のシーン
    TOP = "TOP"
    INGAME = "INGAME"
    RESULT = "RESULT"
    QUIT = "QUIT"


# ここから状態定義
scene = Scene.TOP
