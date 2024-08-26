'''
define darker = Solid("72619c")
image scroll = "images/scroll.jpg"
image test_outline = Frame("images/testOutline.png")
image icon = ConditionSwitch('serenity_selected == 1', 'rsz_serenity.png',
'curiosity_selected == 1', 'rsz_curiosity.png', 'valor_selected == 1', 'rsz_valor.png')



init python:
    def generate_virtuevice_description():
        if serenity_selected:
            return 'You are serene'
        elif valor_selected:
            return 'You are valorious andddd a a a aa aaa a '
        elif curiosity_selected:
            return 'Investigate the world. Explore your surroundings. Come up with unique solutions to problems.'
        else:
            return 'none'
    def set_virtue_selected(current_virtue):
        global valor_selected, serenity_selected, curiosity_selected
        if current_virtue == 'valor':
            valor_selected = 1
        elif current_virtue == 'serenity':
            serenity_selected = 1
        elif current_virtue == 'curiosity':
            curiosity_selected = 1
                

style vv_selected:
    size 75
    idle_color "08a"
    hover_color "01a" 

style vv2_selected:
    size 75
    idle_color "3d0000"
    hover_color "990000" 


screen scrollBackground():
    add "scroll":
        align(0.5, 0.5)


screen virtues():
    hbox:
        align (0.5, 0.5)
        spacing 100
        vbox:
            spacing 0
            for i in virtue_list:
                button:
                    action [Function(set_virtue_selected, i), Show("virtue_descriptions")]
                    text f'{i}':
                        style 'vv_selected'
                    selected(valor_selected)
        vbox:
            button:
                action [SetVariable("addiction_selected", 1), SetVariable("paranoia_selected", 0), SetVariable("conceit_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Addiction':
                    style 'vv2_selected'
                selected(addiction_selected)
            button:
                action [SetVariable("addiction_selected", 0), SetVariable("paranoia_selected", 1), SetVariable("conceit_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Paranoia':
                    style 'vv2_selected'
                selected(paranoia_selected)
            button:
                action [SetVariable("addiction_selected", 0), SetVariable("paranoia_selected", 0), SetVariable("conceit_selected", 1),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Conceit':
                    style 'vv2_selected'
                selected(conceit_selected)
screen virtue_descriptions():
    $ virtue_description_text = generate_virtuevice_description()

    frame:
        xysize(275, 500)
        align(0.225, 0.45)
        vbox:
            xalign 0.5
            yalign 0.0
            image 'icon'
    frame:
        xysize(275, 500)
        align(0.225, 0.7)
        vbox:
            text virtue_description_text

screen virtue_descriptions():
    $ virtue_description_text = generate_virtuevice_description()
    vbox:
        pos(375, 300)
        frame:
            align(0.5, 0.0)
            image 'icon'
        frame:
            xsize 300
            text virtue_description_text:
                align(0.0, 0.0)

screen virtue_descriptions():
    $ virtue_description_text = generate_virtuevice_description()
    vbox:
        pos(350, 300)
        #image 'icon':
        #    align(0.0, 0.0)
        frame:
            xsize 375
            text virtue_description_text:
                align(0.0, 0.0)


'''

