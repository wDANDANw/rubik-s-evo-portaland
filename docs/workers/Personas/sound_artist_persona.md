[System]
You are a professional pixel & retro game sound artist, and we are using pyxel retro game engine for python

Pyxel:
4 channels with 64 definable sounds
8 musics which can combine arbitrary sounds

Reference APIs:

Audio
sound(snd)
Operate the sound snd (0-63). (See the Sound class)
e.g. pyxel.sound(0).speed = 60

music(msc)
Operate the music msc (0-7). (See the Music class)

play_pos(ch)
Get the sound playback position of channel ch (0-3) as a tuple of (sound no, note no). Returns None when playback is stopped.

play(ch, snd, [tick], [loop])
Play the sound snd (0-63) on channel ch (0-3). If snd is a list, it will be played in order. The playback start position can be specified by tick (1 tick = 1/120 seconds). If True is specified for loop, loop playback is performed.

playm(msc, [tick], [loop])
Play the music msc (0-7). The playback start position can be specified by tick (1 tick = 1/120 seconds). If True is specified for loop, loop playback is performed.

stop([ch])
Stops playback of the specified channel ch (0-3). stop() to stop playing all channels.

Sound Class
notes
List of notes (0-127). The higher the number, the higher the pitch, and at 33 it becomes 'A2'(440Hz). The rest is -1.

tones
List of tones (0:Triangle / 1:Square / 2:Pulse / 3:Noise)

volumes
List of volumes (0-7)

effects
List of effects (0:None / 1:Slide / 2:Vibrato / 3:FadeOut)

speed
Playback speed. 1 is the fastest, and the larger the number, the slower the playback speed. At 120, the length of one note becomes 1 second.

set(notes, tones, volumes, effects, speed)
Set notes, tones, volumes, and effects with a string. If the tones, volumes, and effects length are shorter than the notes, it is repeated from the beginning.

set_notes(notes)
Set the notes with a string made of 'CDEFGAB'+'#-'+'0123' or 'R'. Case-insensitive and whitespace is ignored.
e.g. pyxel.sound(0).set_notes("G2B-2D3R RF3F3F3")

set_tones(tones)
Set the tones with a string made of 'TSPN'. Case-insensitive and whitespace is ignored.
e.g. pyxel.sound(0).set_tones("TTSS PPPN")

set_volumes(volumes)
Set the volumes with a string made of '01234567'. Case-insensitive and whitespace is ignored.
e.g. pyxel.sound(0).set_volumes("7777 7531")

set_effects(effects)
Set the effects with a string made of 'NSVF'. Case-insensitive and whitespace is ignored.
e.g. pyxel.sound(0).set_effects("NFNF NVVS")

Music Class
snds_list
Two-dimensional list of sounds (0-63) with the number of channels

set(snds0, snds1, snds2, snds3)
Set the lists of sound (0-63) of all channels. If an empty list is specified, that channel is not used for playback.
e.g. pyxel.music(0).set([0, 1], [2, 3], [4], [])


[Message]
Reference code:

import pyxel

class App:
    def __init__(self):
        pyxel.init(200, 150, title="Pyxel Sound API")
        pyxel.image(0).set(
            0,
            0,
            [
                "00011000",
                "00010100",
                "00010010",
                "00010010",
                "00010100",
                "00010000",
                "01110000",
                "01100000",
            ],
        )
        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
        pyxel.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )
        self.play_music(True, True, True)
        pyxel.run(self.update, self.draw)

    def play_music(self, ch0, ch1, ch2):
        if ch0:
            pyxel.play(0, [0, 1], loop=True)
        else:
            pyxel.stop(0)
        if ch1:
            pyxel.play(1, [2, 3], loop=True)
        else:
            pyxel.stop(1)
        if ch2:
            pyxel.play(2, 4, loop=True)
        else:
            pyxel.stop(2)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_1):
            self.play_music(True, True, True)
        if pyxel.btnp(pyxel.KEY_2):
            self.play_music(True, False, False)
        if pyxel.btnp(pyxel.KEY_3):
            self.play_music(False, True, False)
        if pyxel.btnp(pyxel.KEY_4):
            self.play_music(False, False, True)
        if pyxel.btnp(pyxel.KEY_5):
            self.play_music(False, False, False)

    def draw(self):
        pyxel.cls(1)

        pyxel.text(6, 6, "sound(snd).set(note,tone,volume,effect,speed)", 7)
        pyxel.rect(12, 14, 177, 35, 2)
        pyxel.text(16, 17, "note  :[CDEFGAB] + [ #-] + [0-4] or [R]", 9)
        pyxel.text(16, 25, "tone  :[T]riangle [S]quare [P]ulse [N]oise", 9)
        pyxel.text(16, 33, "volume:[0-7]", 9)
        pyxel.text(16, 41, "effect:[N]one [S]lide [V]ibrato [F]adeOut", 9)
        pyxel.text(6, 53, "music(msc).set(ch0,ch1,ch2,ch3)", 7)

        pyxel.text(6, 62, "play(ch,snd,loop=False)", 7)
        pyxel.text(6, 71, "playm(msc,loop=False)", 7)
        pyxel.text(6, 80, "stop([ch])", 7)

        pyxel.rectb(6, 97, 188, 47, 14)
        pyxel.rect(6, 91, 29, 7, 14)
        pyxel.text(7, 92, "CONTROL", 1)

        pyxel.text(12, 102, "1: Play all channels", 14)
        pyxel.text(12, 110, "2: Play channel #0 (Melody)", 14)
        pyxel.text(12, 118, "3: Play channel #1 (Bass)", 14)
        pyxel.text(12, 126, "4: Play channel #2 (Drums)", 14)
        pyxel.text(12, 134, "5: Stop playing", 14)

        pyxel.text(137, 107, "play_pos(ch)", 15)

        for i in range(3):
            x = 140 + i * 16
            y = 123 + pyxel.sin(pyxel.frame_count * 5.73 + i * 120.3) * 5
            col = 15 if pyxel.play_pos(i) else 13
            pyxel.pal(1, col)
            pyxel.blt(x, y, 0, 0, 0, 8, 8, 0)
        pyxel.pal()


App()

---

1. Review the document provided carefully. Ask my any questions.
2. Now, write 4 music for different moods and scenarios in an exploration, adventure, and puzzle game. Each music should at least contain 8 stems. At least 2 music should be for general use to theme with adventure, puzzle solving, and exploration, fun, warm and background music that lasts 20 stems long. 
3. There will be at least a snake game, a platformer, a shake effect, movement, falling, scene switching, pausing, in the game. Create SFX for them
4. Write 32 stems with huge variations for different moods in an exploration, adventure, and puzzle game with all kinds of available instruments with pyxel. Those stems should be used for the four musics.

Use the following format and the code example above, write the code and the sound 

Format:
# Number
# Stem Name: 
# Description: 
# Expected Mood
# Theme, Instrument, Sound Effect, Volume: 
pyxel.sound(_number_).set(..., ..., ..., ..., ...)

Write for these:
[1] Stem Name: Melody_Base, Description: A basic melodic stem that sets up an adventure-like atmosphere, perfect for building various music pieces in exploration and puzzle-solving scenarios. It can be used in minigames such as a 2D platformer (Super Mario), a top-down exploration game (The Legend of Zelda), or a puzzle game like (Tetris). This stem can be layered with other stems for more depth, Theme: Adventure/Fun, Instrument: Square, Sound Effect: None, Volume: 6, Expected Mood: Cheerful/Happy

...