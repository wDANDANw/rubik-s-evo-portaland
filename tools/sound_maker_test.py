import pyxel


class App:
    def __init__(self):
        pyxel.init(200, 150, title="Pyxel Adventure Music")

        #Stem 1: Main Theme (Melody)
        # pyxel.sound(1).set("C3E3G3A3E4G3C3E3G3A3E4G3", "T", "6", "V", 15)
        # pyxel.sound(2).set("E3G3B3D4G4B3E3G3B3D4G4B3", "T", "6", "V", 15)
        # pyxel.sound(3).set("G3B3D4F4B4D4G3B3D4F4B4D4", "T", "6", "V", 15)
        # pyxel.sound(4).set("C4E4G4A4E4G4C4E4G4A4E4G4", "T", "6", "V", 15)

        # #Stem 2: Harmony
        # pyxel.sound(5).set("C3E3G3C4E4G4C3E3G3C4E4G4", "S", "5", "F", 15)
        # pyxel.sound(6).set("E3G3B3E4G4B4E3G3B3E4G4B4", "S", "5", "F", 15)
        # pyxel.sound(7).set("G3B3D4G4B4D4G3B3D4G4B4D4", "S", "5", "F", 15)

        # #Stem 3: Percussion
        # pyxel.sound(8).set("R", "N", "0", "N", 15)
        # pyxel.sound(9).set("C2C2C2C2C2C2C2", "P", "4", "N", 15)
        # pyxel.sound(10).set("G2G2G2G2G2G2G2", "P", "4", "N", 15)

        # # 
        # # Setup
        # pyxel.sound(11).set("A2C3E3 A2C3E3 G2B2D3 G2B2D3", "T", "4", "N", 15)

        # # Progression
        # pyxel.sound(12).set("F2A2C3 F2A2C3 E2G2B2 E2G2B2", "T", "5", "N", 20)

        # # Variation
        # pyxel.sound(13).set("D3F3A3 D3F3A3 C3E3G3 C3E3G3", "T", "6", "N", 10)

        # # Climax
        # pyxel.sound(14).set("C4E4G4 C4E4G4 B3D4F4 B3D4F4", "T", "7", "N", 20)

        # # Storytelling
        # pyxel.sound(15).set("A3C4E4 A3C4E4 G3B3D4 G3B3D4", "T", "5", "N", 15)

        # #Adventure Music 2 - "Puzzle Expedition":
        # # Inspired by games like "Super Mario" and "Snake", the music aims to provide a playful and adventurous atmosphere.

        # #Stem 1: Main Theme (Melody)
        # pyxel.sound(16).set("C3E3G3C4E4F3A3C4F4A4", "T", "6", "S", 15)
        # pyxel.sound(17).set("E3G3B3E4G4F3A3C4F4A4", "T", "6", "S", 15)
        # pyxel.sound(18).set("G3B3D4G4B4E4G4B4D4F4", "T", "6", "S", 15)
        # pyxel.sound(19).set("C4E4G4C4E4F4A4C4F4A4", "T", "6", "S", 15)

        # #Stem 2: Harmony
        # pyxel.sound(20).set("C3E3G3C4E4G4C3E3G3C4E4G4", "S", "5", "F", 15)
        # pyxel.sound(21).set("E3G3B3E4G4B4E3G3B3E4G4B4", "S", "5", "F", 15)
        # pyxel.sound(22).set("G3B3D4G4B4D4G3B3D4G4B4D4", "S", "5", "F", 15)

        # #Stem 3: Percussion
        # pyxel.sound(23).set("R", "N", "0", "N", 15)
        # pyxel.sound(24).set("C2C2C2C2C2C2C2", "P", "4", "N", 15)
        # pyxel.sound(25).set("G2G2G2G2G2G2G2", "P", "4", "N", 15)

        # # Setup
        # pyxel.sound(26).set("A2C3E3 A2C3E3 G2B2D3 G2B2D3", "T", "4", "N", 15)

        # # Progression
        # pyxel.sound(27).set("F2A2C3 F2A2C3 E2G2B2 E2G2B2", "T", "5", "N", 20)

        # # Variation
        # pyxel.sound(28).set("D3F3A3 D3F3A3 C3E3G3 C3E3G3", "T", "6", "N", 10)

        # # Climax
        # pyxel.sound(29).set("C4E4G4 C4E4G4 B3D4F4 B3D4F4", "T", "7", "N", 20)

        # # Storytelling
        # pyxel.sound(30).set("A3C4E4 A3C4E4 G3B3D4 G3B3D4", "T", "5", "N", 15)


        # #
        # pyxel.music(0).set(
        #     [11, 0, 12, 1, 13, 2, 14, 15, 9, 10, 11, 2, 13, 1, 14, 0],
        #     [3, 5, 7, 8, 3, 5, 7, 8, 3, 5, 7, 8, 3, 5, 7, 8],
        #     [4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6],
        #     []
        # )

        # pyxel.music(1).set(
        #     [26, 16, 27, 17, 28, 18, 29, 30, 19, 20, 26, 18, 28, 17, 29, 16],
        #     [23, 24, 25, 23, 24, 25, 23, 24, 25, 23, 24, 25, 23, 24, 25, 23],
        #     [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6],
        #     []
        # )

        
        # pyxel.music(0).set(
        #     [9, 0, 10, 1, 11, 2, 12, 13, 0, 1, 9, 2, 10, 11, 1, 12, 2, 13, 0, 1],
        #     [3, 5, 7, 8, 3, 7, 5, 8, 3, 5, 7, 8, 3, 7, 5, 8, 3, 5, 7, 8],
        #     [4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6],
        #     [7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8]
        # )

        # pyxel.music(1).set(
        #     [19, 10, 20, 11, 21, 12, 22, 23, 10, 11, 19, 12, 20, 21, 11, 22, 12, 23, 10, 11],
        #     [3, 5, 7, 8, 3, 7, 5, 8, 3, 5, 7, 8, 3, 7, 5, 8, 3, 5, 7, 8],
        #     [4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6],
        #     [7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8, 7, 8]
        # )

        pyxel.sound(1).set("c3c3b2a2 g2g2f2e2 d2d2c2b1 a1a1g1f2 e2e2d2c2 b1b1a1g1 f1f1e1d1 c1c1g1a1 b1b1c2d2 e2e2f2g2", "T", "6", "n", 25)

        pyxel.sound(2).set("e2rD2rA1rG1rF1rE1rD1rC1rB1rA1rG1rF1rE2rD2rC2rB2rA2rG2rF2rE3rD3rC3rB3rA3rG3rF3", "T", "6", "n", 25)

        # Save sounds and music
        pyxel.save("test.pyxres", image=False, tilemap=False, sound=True, music=True)

        # Run the app
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 50, "Adventure Music", pyxel.frame_count % 16)
        pyxel.text(50, 60, "Press Q to quit", 7)


App()