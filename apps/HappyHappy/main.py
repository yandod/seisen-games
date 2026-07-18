import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.x >= pyxel.width:
            self.x = -8
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.x += 1
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.x -= 1

    def draw(self):
        pyxel.cls(3)
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
        pyxel.blt(self.x, 90, 0, 0, 0, 16, 16, 2)
        pyxel.text(48, 53, "Happy Happy Happy", pyxel.rndi(1, 15))

App()