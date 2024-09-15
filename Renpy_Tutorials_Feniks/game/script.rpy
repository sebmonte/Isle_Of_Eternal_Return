# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image photo = 'images/photo.jpg'

# The game starts here.
screen fenik_screen():
    add "photo":
        pos (200, 300)
        anchor (0.5, 0.5)

label start:
    'test'

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen fenik_screen

    'test2'