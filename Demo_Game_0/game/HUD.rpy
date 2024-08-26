init python:
    style.first_button = Style(style.button)
    style.first_button.background = "#FF0000"  # Red background
    style.first_button.color = "#FFFFFF"  # White text color

    style.second_button = Style(style.button)
    style.second_button.background = "#00FF00"  # Green background
    style.second_button.color = "#000000"  # Black text color

    style.third_button = Style(style.button)
    style.third_button.background = "#0000FF"  # Blue background
    style.third_button.color = "#FFFFFF"  # White text color


# Function to determine which action to take
init python:
    def display_screen(screen_name, method="show"):
        if method == "call":
            renpy.call_screen(screen_name)
        else:
            renpy.show_screen(screen_name)


screen test_screen():
    zorder 1
    frame:
        pos(1080, 900)
        anchor(0.5, 0.5)
        xysize(500, 100)
        has hbox
        spacing 35
        textbutton "Inventory" action Show('Inv_Menu') style "first_button"
        align(.5, .5)
        textbutton "Skills" action Show('Skill_Menu') style "second_button"
        textbutton "Map" action Show("Map_Menu") style "third_button"


screen Inv_Menu():
    zorder 2
    modal True
    frame:
        has hbox
        text "This is the first menu."
        textbutton "Close" action Hide("Inv_Menu")


screen Map_Menu():
    zorder 2
    modal True
    frame:
        has hbox
        text "This is the third menu."
        textbutton "Close" action Hide("Map_Menu")
        textbutton "test room" action Hide("Map_Menu"), Jump('test_room')


screen Skill_Menu():
    modal True
    frame:
        text "This is the second menu."
        textbutton "Close" action Hide("Skill_Menu")

