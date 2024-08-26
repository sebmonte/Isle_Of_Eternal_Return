# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Lezalith",
    who_color = "E34D0C", kind=nvl)

define narrator = nvl_narrator
define menu = nvl_menu
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you ca
    show screen scrollBackground
    call screen virtues

    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    hide screen scrollBackground
    e "You've created a new Ren'Py game."
    menu:
        'option 1':
            jump one

        'option 2':
            jump two

    
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


label one:
    return

label two:
    return
