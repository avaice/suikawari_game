# スイカ割りゲーム

## リポジトリをパソコンにCloneする

1. まず、GitHubでSSHできるように設定する。
    1. 参考: https://yu-report.com/entry/githubssh/
3. `git clone git@github.com:avaice/suikawari_game.git`

## ゲームの起動方法

1. pygameをインストールする
2. `python ./`

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

## コードのコミット（アップロード）方法

複数人が同時に同じ箇所を編集した時にソースコードがおかしくならないように、mainリポジトリに直接コミットはできないようになっています。
以下の方法でコードをコミットしてください。

1. 好きな名前でブランチを切る
2. 切ったブランチ -> mainブランチへのPull Requestを出す
3. チームメンバーのApproveを待つ

より具体的な手順: https://chat.openai.com/share/13c1ffbb-8d28-4c8f-b04d-05ed2e698cf1
