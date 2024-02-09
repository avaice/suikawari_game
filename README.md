# スイカ割りゲーム

## ディレクトリの構成

<pre>
suikawari_game
│
├── __main__.py (起動時に最初に読み込まれる)
├── settings.py (解像度などのゲーム設定)
├── status.py (Score, Sceneなどの状態を管理する)
└── view (画面)
    ├── top.py (タイトル)
    └── game.py (ゲーム画面)
</pre>

## 画面の切り替え方法

`view/game.py`に実装例があります

```python
import status

def render(screen):

    # ...ゲーム画面の処理...

    # 切り替えたい部分で以下のコードを入れる
    status.scene = status.Scene.遷移先のシーン
    return
```

シーンの一覧は`status.py`の`Scene` class で宣言されています。必要に応じて追加してください
