# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ev = Character('Eira Vale', color="#3d813d")
define sk = Character('Headmistress Sable Korrin', color="#4046b7")
define lr = Character('Lucian Reed', color="#b73d3d")
define mv = Character('Mira Vexley', color="#ad3db7")
define nh = Character('Noah Halden', color ="#3db7b7")
define sl = Character('Seraphine Lorne', color ="#b7ad3d")
define us = Character('UNASSIGNED', color="#FFFFFF")

# The game starts here.

label start:
    scene front camp:
        xysize (1920, 1080)

    "Welcome to Arcane Academy."
    return