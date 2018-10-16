import pyxel
import time

class App:
    def __init__(self):
        # 160x120の画面領域を確保
        pyxel.init(160, 120, caption="Sample Cat App")

        # 画像バンクの0版に画像を読み込む
        pyxel.image(0).load(0, 0, "assets/cat_16x16.png")

        # 画面番号
        self.screen = 0

        # catの描画情報
        self.cat_x = 50
        self.cat_y = 70
        self.cat_direction_left = True

        # 関連メソッドを読み込んでアプリケーションを実行
        pyxel.run(self.update, self.draw)

    def update(self): # フレーム更新
        # ゲームの終了コマンド
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # ルーティング
        if self.screen == 0:
            self.update_title()
        elif self.screen == 1:
            self.update_cat()

    def update_title(self): # タイトルメニュー
        if pyxel.btn(pyxel.KEY_ENTER):
            self.screen = 1

    def update_cat(self): # 猫の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.cat_x = self.cat_x - 2
            self.cat_direction_left = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.cat_x = self.cat_x + 2
            self.cat_direction_left = False

    def draw(self): # 描画
        # ルーティング
        if self.screen == 0:
            self.draw_title()
        elif self.screen == 1:
            self.draw_game()

    def draw_game(self): # メインのゲーム描画
        self.screen = 1
        pyxel.cls(0)
        pyxel.rect(0, 80, 160, 120, 3)

        xy = "CAT:  [X: {}][Y: {}][DIR: {}]".format(self.cat_x, self.cat_y, "LEFT" if self.cat_direction_left else "RIGHT")
        pyxel.text(5, 110, xy, 10)
        mouse = "MOUSE:[X: {}][Y: {}]".format(pyxel.mouse_x, pyxel.mouse_y)
        pyxel.text(5, 100, mouse, 10)
        pyxel.blt(
            self.cat_x,
            self.cat_y,
            0,
            0,
            0,
            16 if self.cat_direction_left else -16,
            16,
            5,
        )

    def draw_title(self): # タイトル画面描画
        self.screen = 0
        pyxel.rect(0, 0, 160, 120, 0)
        pyxel.text(50, 40, "Sample Cat App", 7)
        pyxel.text(30, 80, "PRESS ENTER TO GAME START", 10)
        pyxel.text(5, 110, "PRESS Q TO EXIT", 7)

App()
