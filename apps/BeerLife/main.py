import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load("my_resource.pyxres")
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.GAMEPAD1_BUTTON_SELECT) and pyxel.btn(pyxel.GAMEPAD1_BUTTON_START):
            pyxel.quit()
        
        self.x += 0.5
        if self.x >= pyxel.width:
            self.x = -8

    def draw(self):
        pyxel.cls(3)
        pyxel.bltm(0, 0, 0, 0, 0, 160, 120)
        pyxel.blt(self.x, 70, 0, 0, 0, 8, 8, 1)
        pyxel.blt(self.x, 100, 0, 16, 8, 8, 8, 1)
        pyxel.blt(self.x, 30, 0, 24, 8, 8, 8, 1)
        pyxel.blt(self.x, 10, 0, 24, 0, 8, 8, 1)
        pyxel.text(48, 53, "No Beer, No Life", pyxel.rndi(1, 15))
    
    


App()
