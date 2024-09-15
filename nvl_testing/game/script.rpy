
define l = Character(None, kind=nvl, what_prefix="Sylvie: \"", what_suffix="\"")
#define l = Character('Lezalith', kind=nvl)
define e = Character("Eileen", kind=nvl)


define narrator = nvl_narrator
define menu = nvl_menu
define testVar = 1

image graves = "images/scene1.jpeg"

image plague_doctor = "images/plague_doctor.png"

screen graveyard_screen():
    add "plague_doctor"


label start():
    'You reach the bar. A bartender sits at the counter. There is a shadow figure at the end'
    show screen graveyard_screen
    'Suddenly you notice another thing'

    menu:
        'Talk to the bartender':
            jump bartender
        'Talk to the shadow figure':
            jump figure
        




#nvl clear opens a new page
#If you reach the bottom you can't see choices anymore or more text,
#so need to figure out a way to put all of it in some kind of scrollable box/figure out when to reset text
label bartender():
    e 'Hello there.'
    menu:
        'Hi, Im x':
            e 'Good to meet you'
            jump start
        'What do you have for sale':
            e 'I have ale'
            jump start

label figure():
    'You approach the shadowy figure'
    l 'I dont want to Talk. Lets see what happens when this is realllllly long'
    $ testVar += 1
    jump start
