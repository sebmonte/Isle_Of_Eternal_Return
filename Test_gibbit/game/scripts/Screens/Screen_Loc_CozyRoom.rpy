screen cozyRoom_screen():
    button:
        text "black goo"
        xysize (200, 50)
        align (0.1, 0.9)
        background "#000"  
        action Call("cozyRoom_goo")

    button:
        xysize (130, 130)
        align (0.295, 0.58999)
        hovered Notify("IT WATCHES")
        action Call("cozyRoom_eye")