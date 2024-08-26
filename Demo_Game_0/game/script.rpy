# The script of the game goes in this file.

define l = Character("Eileen", kind=nvl)
define narrator = nvl_narrator
default traveled = False


label start():
    'You are at the square of the city'
    menu:
        'start the game':
            call start4
        'Dont start the game':
            'ok'
    'After the game'





#Label
label start4():
    show screen test_screen()
    l "Hi again!"

    l "How are you doing today?"

    jump start2


label start2():
    if traveled:
        'smuck'
    else:
        l "This is how I can {b}shout out loud!{/b}"

        l "This is... I don't {i}actually know{/i} what this is."

        l "Maybe it's {font=DejaVuSans.ttf}just a dream.{/font}"

    $ traveled = True
    return
    jump start3



label start3():
    "Another location"
    "This is start3"

    jump start2



label test_room():
    "The mysterious test room"
    if John.reputation > 1:
        "hello"

    jump start2


