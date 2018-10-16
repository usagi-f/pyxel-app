import pyxel

class App:
    def __init__(self):
        # 160x120の画面領域を確保
        pyxel.init(160, 120, caption="Sample Cat App")

        # 画像バンクの0版に画像を読み込む
        pyxel.image(0).load(0, 0, "assets/cat_16x16.png")

        # catの描画情報
        self.cat_x = 50
        self.cat_y = 70
        self.cat_direction_left = True

        # 関連メソッドを読み込んでアプリケーションを実行
        pyxel.run(self.update, self.draw)

    def update(self): # フレーム更新
        self.update_cat()

    def update_cat(self): # 猫の移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.cat_x = self.cat_x - 2
            self.cat_direction_left = True

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.cat_x = self.cat_x + 2
            self.cat_direction_left = False

    def draw(self): # 描画
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

App()
