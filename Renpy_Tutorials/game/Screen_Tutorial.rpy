
#Screens should be called at the leftomost level of 
#Indentation: outside of labels, init python blocks

#Labels are executed line-by-line to show dialogue and images, but screens are
#Descriptions of UI elements


#Call vs show

#There are two ways to display a screen, call and show

##SHOW SCREEN##
#Show screen is for screens that do not require actions from the player: this is good for
#UI icons, notifications, stat indicators, time trackers, etc. The player can interact
#with the screen, but they should still be able to play the game normally even though
#the screen has appeared

#Showing a screen does not inherently wait for anything to happen, so if you want to wait for a click
#After showing a screen, you need to add a pause
#Sscreens can be hidden with the 'hide screen' command"
#When hiding a screen you don't need to call any parameters, even if you did to show the screen

#An example of showing a screen, waiting for a player to clickl, and then proceeding with the game

label example1():
    window auto hide # Make sure the dialogue window is hidden
    show screen the_game_will_remember_this()
    pause
    hide screen the_game_will_remember_this
    "You've started a new Ren'Py game."



##CALL SCREEN#

#Should be used for screens that require interaction with the player to proceed
#This is good for point and click sections, map screens, or minigames
#Calling a screen causes the whole game to be put on hold unti something happens to
#Return to normal gameplay
#So calling a screen is going to 'wait for an interaction' before proceeding
#typical ways of causing this interaction are by using Return() to go back to the
#line after the screen was called, or 'jump' or 'call' to go to a particular
#label. These actions also automatically cause the screen to hide, unlike show 
#screen

label example2():
    call screen character_creator()
    "Welcome to the game!"


#screen the_game_will_remember_this():


#You can image variables and call them later on in the screen
image intro screen = "mapbutton.png"
image second layer = "me.jpg"
#You can also interpolate things into your 'add call' like so
default example = 'layer'
screen character_creator():
    #Always use 'add' and not 'image' to add images
    add "intro screen"
    add "second [example]"


#What about text screens? That's what we look at next
default score = 0
screen test_screen():
    text "Your score: [score]"


####PROPERTIES#######
####PROPERTIES#######
####PROPERTIES#######

#All screens have size and position properties
#But text images have font and italic properties
#Buttons have action properties
#Input elements have length propreties to dictate
#A maximum input length
#Properties always come in pairs as follows:
#*property name* *value* ie. font "ComicSans.ttf"

screen test_screen():
    text "Your score: [score]" color "#f00"


#When you have lots of properties for your screens, space them out:
screen test_screen():
    text "Your score: [score]":
        color "#fff"
        size 35
        pos (300, 200)
        bold True
        underline True
        anchor (0.5, 0.5)
        italic True
#Or group them on the same line

screen test_screen():
    text "Your score: [score]":
        color "#fff" size 35
        pos (300, 200) anchor (0.5, 0.5)
        bold True underline True italic True


#If I wanted to add propreties to image blocks I could also
#Do it like this

screen character_creator():
    add "intro screen"
    add "second [example]":
        zoom 1.
        

#Organizing properties into blocks lets you adjust the elements
#In the blocks based on conditions

screen test_screen():
    text "Your score: [score]":
        if score < 10:
            color "#f00" # Red
        else:
            color "#0f0" # Green


######BASIC CONTAINERS############
######BASIC CONTAINERS############
######BASIC CONTAINERS############

#Containers are used to organize elements ie images and texts
#Moving a container will also move its elements (aka its children)
#However, the positions of elements are relative to the container, not the screen


#Structure of a container
#container:
#    <container properties>
#    <element1>
#    <element2>
#    <element3>
#Properties of a container are like size, position, and spacing

#Here's an example of a container that is made called fixed,
# it is put within a screen. The first things put in are the 'farthest back'
#layer, so when this is printed, 'world' will appear on top of 'hello'
screen test_screen():
    fixed:
        xysize (300, 400)
        pos (10, 10)
        text "Hello!" color "#f93c3e"
        text "World!" color "#ff8335"

#Fixed is a particular type of container, where the things in it are locked
#To their position relative to the container, and without positioning, things
#Will end up on top of each other since 'fixed' does not organize them

#Next up is vbox, which does organize the things inside it
#Things are automatically organized from top to bottom, whether images or text
#Removing things from a vbox will cause everything else to 'shift' up 
#positions to take their place
screen test_screen():
    vbox:
        pos(200,300)
        text "Top"
        text "Middle"
        text "Bottom"
        text "Rock bottom"


#Next up is the HBox, which organizes elements left-to-right instead of
#Up-to-down. Otherwise it works exactly the same
#If you were to adjust parameters and make these variables overlap, the 'layers'
#Would work the same as before: things at the bottom are on top



#####PROPERTIES##################
#####PROPERTIES##################
#####PROPERTIES##################

#Floats an integers in renpy: floats are treated as a *percentage* of their
#containers, whereas integers are treated as *exact pixel values*

#Starting position: Renpy considers the default for all image properties to be
#(0,0), which corresponds to the top-left of the element positioned

#####Anchors##################

#Position:
#Can either be specified as xpos and ypos or (xpos, ypos)
#Anchor:
#While position moves an element around the screen, anchor basically sets the 
#point of the image relative to that point. By default, if an image is given a position
#The top left of the image appears on that position. If you were to set an anchor
#at .5 .5, then the center of the image will appear on that position
#Usually anchor points at 0.0, .5, or 1.0 as you want to position images relative
#to their center or edges. Recall that floats do this percentage wise, and 
#using integers like 0 or 1 would be very 

#An example of anchoring an image in the middle
screen test_screen():
    add "intro screen":
        pos (200, 300)
        anchor (0.5, 0.5)

'''
anchor (0.0, 0.0) # Top left corner
anchor (0.0, 1.0) # Bottom left corner
anchor (1.0, 0.0) # Top right corner
anchor (1.0, 1.0) # Bottom right corner
anchor (0.5, 0.5) # Exact center

anchor (0.0, 0.5) # Middle of the left edge
anchor (0.5, 0.0) # Middle of the top edge
anchor (1.0, 0.5) # Middle of the right edge
anchor (0.5, 1.0) # Middle of the bottom edge
'''

#####Align##################
#Align combines position and anchors by setting them to both have the 
#Same value. If you use values other than 0.0, 0.5, and 1.0 with align
#You are probably using it wrong. It is not good for positioning things
#That are not already centered or aligned to the edge of their container

#Why isn't my image moving?
#If your image is not moving with align, it is because it has the same 
#dimensions as the screen and you are trying to use align to move it

#Every positional property in RenPy correctly scales, you do not need to use
#Align

#####xycenter##################
#Combines anchor and pos, but sets anchor to .5 and pos to whatever
#value is provided

#####offset##################


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

