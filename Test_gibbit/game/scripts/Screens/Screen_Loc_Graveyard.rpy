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

        action Jump("cozyRoom_intro")

    #test
    button:
        #anchor (0, 0) #anchor is the reference point for aligning. 0, 0 is the default.
        align (0.08, 0.25)
        #xysize (50, 50)

        idle_background "#000"  
        hover_background "#fff"
        text "Test":
            size 36
            idle_color "#fff"
            hover_color "#000"
            align (0.5, 0.5)

        action Call("test")