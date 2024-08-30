init python:
    overlay_screens = ["inventory_display", "skills_display", "map_display"]

    #Hides strings from given list (screen_list)
    # except the screen listed in keep_screen if there is one
    def hide_screens(screen_names, keep_screen = None):
        for name in screen_names:
            if name != keep_screen:
                renpy.hide_screen(name)

screen overlay():
    #Inventory
    button:
        idle_background "#fff"  
        hover_background "#000"  
        align (0.0, 0.0)
        text "Inventory":
            size 36
            idle_color "#000"
            hover_color "#fff"
            align (0.5, 0.5)
        action ToggleScreen("inventory_display"), Function(hide_screens, overlay_screens, "inventory_display")
    
    #Skills
    button:
        idle_background "#fff"  
        hover_background "#000"  
        align (0.12, 0.0)
        text "Skills":
            size 36
            idle_color "#000"
            hover_color "#fff"
            align (0.5, 0.5)
        action ToggleScreen("skills_display"), Function(hide_screens, overlay_screens, "skills_display")
    
    #Map
    button:
        idle_background "#fff"  
        hover_background "#000"  
        align (0.2, 0.0)
        text "Map":
            size 36
            idle_color "#000"
            hover_color "#fff"
            align (0.5, 0.5)
        action ToggleScreen("map_display"), Function(hide_screens, overlay_screens, "map_display")