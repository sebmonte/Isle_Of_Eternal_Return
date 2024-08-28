screen graveyard_screen():
    #character Plague Doctor
    imagebutton:
        #anchor (0, 0) #anchor is the reference point for aligning. 0, 0 is the default.
        align (0.6, 0.7)
        #xysize (50, 50)

        idle "icons/plague_doctor.png"
        hover "icons/plague_doctor.png"
        at Transform(zoom = 1.6)
        
        action Call("graveyard_pd")

    #portal door
    imagebutton:
        #anchor (0, 0) #anchor is the reference point for aligning. 0, 0 is the default.
        align (0.05, 0.8)
        #xysize (50, 50)

        idle "icons/door.PNG"
        hover "icons/door.PNG"
        at Transform(zoom = 1.6)

        action Call("cozyRoom_intro")