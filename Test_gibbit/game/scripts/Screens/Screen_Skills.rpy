screen skills_display():
    frame:
        xysize (1600, 150)
        align (0, 0.06)
        
        hbox:
            align (0.015, 0.015)
            spacing 15
            for skill, key in profile.skills.items():
                frame:
                    background "#33a0ff"
                    text "[skill]: [key]"

            button:
                #anchor (0, 0) #anchor is the reference point for aligning. 0, 0 is the default.
                align (0.6, 0.7)
                #xysize (50, 50)

                text "Skill roll":
                    size 36
                    idle_color "#fff"
                    hover_color "#fff"
                    align (0.5, 0.5)
                
                action Function(profile.notify_skill_roll, "P", [profile.get_virtue_vice_mod("Valor")])