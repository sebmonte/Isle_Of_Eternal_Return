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
        
            //test
            # test

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

'''
Though you could swear you were just climbing down a ladder, you find yourself finishing your ascent.
Darkness plumes around you as if a smoke of nothing rising into nothing.
You clamber onto a stone pathway that feels more stable [gable] than it looks. 
Chained to this twisting path are blank cubes that dangle upwards. Monochromatic [colorful] waterfalls of chalk pour into the sky above, 
reaching past contorted leviathans drifting by, as if resting.
[ALT: Though you could swear you were just taking adderall, you find yourself]
[ finishing your homework. Darkness GLOOMS *around* you as if a smoke of nothing rising into nothing. You clamber the foam /*gable*/ and it's so goddamn wet.]
[ Chained to this twisting path are examples of bad writing.]
**Nihilist** Or maybe they’re just dead.
***History check*** [[Where are we? (success)]] 
    **History** This is the Downside, the true seedy underbelly of the city.
    ***P*** [[But I thought we already were in the seedy underbelly.]]
        **History** We were. This is the seedier, underer-belly. The people here are so ignored, many don’t know they exist.
        **Conceited** I can see why. This place is thoroughly disgusting.
    ***P*** [[Good, I was disappointed by the last one.]]

    ***P*** [[Every step we take, things seem to get worse.]]
[[Where are we? (failure)]]
***Occultism check*** [[Try to understand this place. (success)]] [[Try to understand this place. (failure)]]

<!-- This is unfortunately comment syntax -->

[[Screen Options]] #PERM
'''