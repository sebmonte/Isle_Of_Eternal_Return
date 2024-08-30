define narrator = nvl_narrator

""" Don't understand the "variables should be defined before start() thing."
Doesn't that make organization confusing? Perhaps it's best to have a variables  """

#NVD Mode

#VARIABLES
default reputation = 0
default health = 10
#default secret_found = False

#CHARACTERS
define amaris = Character("Amaris", kind = nvl)

image graves = "images/backgrounds/scene1.jpeg"

image plague_doctor = "images/icons/plague_doctor.jpg"

default graveyard_visited = False
default cozyRoom_visited = False

#OBJECTS
init python:
    key_pic = "images/items/item key.png"
    key = Item("Mysterious Key", key_pic, "A very cool key that's definitely not a dog")
    question_pic = "images/items/item question.png"
    question = Item("Question", question_pic, "idk either")

    player_inventory = Inventory() 
    player_inventory.add_item(key)
    player_inventory.add_item(question)

    profile = Profile("Valor", "Paranoia")

transform background_trans:
    xalign 0
    yalign 0

transform character_trans:
    xalign 0.5
    yalign 1.0
    xysize(900, 900)

# NEXT TASK: Make clickable background elements
label start():
    show screen overlay
    jump graveyard_intro

label secret_error():
    "If you're seeing this, something went wrong."