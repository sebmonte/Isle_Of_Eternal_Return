screen skills_display():
    frame:
        xysize (1200, 100)
        align (0, 0.06)
        hbox:
            align (0.015, 0.015)
            spacing 15
            for skill, key in profile.skills.items():
                frame:
                    background "#33a0ff"
                    text "[skill]: [key]"