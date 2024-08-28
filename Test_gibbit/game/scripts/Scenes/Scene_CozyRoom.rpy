label cozyRoom_intro():
    $ cozyRoom_visited = True
    #Clears screen and adds new background
    scene bg judgement at background_trans:
        zoom 0.3

    "intro text"
    
    call screen cozyRoom_screen

    return

label cozyRoom_goo():
    "A pit of endless, viscous dark suffocates the ground before you. The slightest sensation of calming warmth eminates from it."
    if profile.skillcheck("Presence") >= 1:
        "I shouldn't have to be the one to tell you this, but please don't stick your hand in there."
    
    menu:
        "Stick your hand in there anyway" if profile.skillcheck("Pre") >= 1:
            jump cozyRoom_goo_plunge
        "Stick your hand in there" if profile.skillcheck("Pres") < 1:
            jump cozyRoom_goo_plunge
        "Leave it alone":
            return

    return

label cozyRoom_goo_plunge():
    "You plunge your hand deep into the roiling goo. For a moment, the heat bathes your skin with calm pressure..."
    "Then the heat rises and begins to claw at your flesh. You attempt to rip your hand back out."
    "But it is too late. Only its right half remains."

    $ profile.set_skill("P", 0)

    "sucks"
    
    if profile.skillcheck("P") >= 1:
        "You really should listen to me more often" 
    else:
        "duhh duhhh stoopid"

    return

label cozyRoom_eye():
    "boo spooky"

    return


