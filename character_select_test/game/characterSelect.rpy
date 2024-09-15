
define darker = Solid("72619c")
image scroll = "images/scroll.jpg"
image icon = ConditionSwitch('serenity_selected == 1', 'rsz_serenity.png',
'curiosity_selected == 1', 'rsz_curiosity.png', 'valor_selected == 1', 'rsz_valor.png')




init python:
    #Function that determines the desriptor for a given virtue based on what button is currently pressed and returns it to display
    def generate_virtuevice_description():
        if serenity_selected:
            return 'You are serene'
        elif valor_selected:
            return 'You are valorious andddd a a a aa aaa a '
        elif curiosity_selected:
            return 'Investigate the world. Explore your surroundings. Come up with unique solutions to problems.'
        else:
            return 'none'
                

#Blue colors for virtues, red colors for vices
style virtue_buttons:
    size 75
    idle_color "08a"
    hover_color "01a" 
style vice_buttons:
    size 75
    idle_color "3d0000"
    hover_color "990000" 


#Background with a centered image of scroll
screen scrollBackground():
    add "scroll":
        align(0.5, 0.5)



#Show virtue and vice buttons
screen virtues():
    #hbox organizes the two columns horizontally
    hbox:
        align (0.5, 0.5)
        spacing 100
        #First vbox for virtues
        vbox:
            spacing 0
            #Each button sets the variables such that the virtue that was selected is 1 and the others are 0
            #Also shows a screen that describes each virtue and pulls up an icon associated with it
            button:
                action [SetVariable("valor_selected", 1), SetVariable("serenity_selected", 0), SetVariable("curiosity_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Valor':
                    style 'virtue_buttons'
                #selected() makes it so when the button is in the selected state (has been pressed) any property
                #starting with selected is true. In this case, selected_background will be true and so darker will be added
                #until the button is deselected
                selected(valor_selected)
            button: 
                action [SetVariable("valor_selected", 0), SetVariable("serenity_selected", 1), SetVariable("curiosity_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Serenity':
                    style 'virtue_buttons'
                selected(serenity_selected)
            button:
                action [SetVariable("valor_selected", 0), SetVariable("serenity_selected", 0), SetVariable("curiosity_selected", 1),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Curiosity':
                    style 'virtue_buttons'
                selected(curiosity_selected)
        #Second column for the vices
        vbox:
            button:
                action [SetVariable("addiction_selected", 1), SetVariable("paranoia_selected", 0), SetVariable("conceit_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Addiction':
                    style 'vice_buttons'
                selected(addiction_selected)
            button:
                action [SetVariable("addiction_selected", 0), SetVariable("paranoia_selected", 1), SetVariable("conceit_selected", 0),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Paranoia':
                    style 'vice_buttons'
                selected(paranoia_selected)
            button:
                action [SetVariable("addiction_selected", 0), SetVariable("paranoia_selected", 0), SetVariable("conceit_selected", 1),
                Show("virtue_descriptions")]
                selected_background darker
                text 'Conceit':
                    style 'vice_buttons'
                selected(conceit_selected)
            button:
                action [Hide("virtues"), Hide('virtue_descriptions'), Return()]
                text 'meow'

#Pulls up the description of each virtue
screen virtue_descriptions():
    vbox:
        pos(350, 300)
        add 'icon':
            align(0.5, 0.0)
        fixed:
            xsize 375
            text generate_virtuevice_description():
                align(0.0, 0.0)


            

