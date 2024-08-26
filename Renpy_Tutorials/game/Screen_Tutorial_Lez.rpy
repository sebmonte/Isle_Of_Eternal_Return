#This is a script for the screen tutorial from lezcave


#################################################################
#TUTORIAL 1: DEFINING SCREENS, SCREEN SYNTAX, and NULL STATEMENTS
#################################################################

#Screens are define by screen followed by parentheses for arguments and a colon for a screen block

#Making a simple screen
screen ourScreen():

    add "gui/window_icon.png"

#The add statement adds an iamge or displayable, which are different

# The game starts here.

label startOne:

    call screen ourScreen

    return


#Now we use align and size to change the image, these are transform properties
#The align property positions the image, 25% of the way across the screen and 50% vertically

screen ourScreen():

    add "gui/window_icon.png":

        align (0.25, 0.5)
        size (400, 400)

# The game starts here.

label startTwo:

    call screen ourScreen

    return

#################################################################
#TUTORIAL 2: TEXT, HBOX, AND VBOX STATEMENTS
#################################################################

#Adding text characters to a screen
screen ourScreen():

    text "Hello everyone!":

        align (0.5, 0.5)

# The game starts here.

label startThree:

    call screen ourScreen

    return

#Screen statements use different style properties, they all take positional properties but also other
#Here are some properties the text statement can take


screen ourScreen():

    text "Hello everyone!":

        # Positional properties
        align (0.5, 0.5)

        # Text properties 
        bold True
        underline True
        color "ff00ff"

# The game starts here.

label startFour:

    call screen ourScreen

    return

#Hbox and vbox
#Displays things in rows or columns

screen ourScreen():

    vbox:

        align (0.5, 0.5)

        text "I am the first text."
        text "Me be second."
        text "Yarr, I be the third!"

# The game starts here.

label startFive:

    call screen ourScreen

    return


#Hbox and Vbox use box style properties (look at page link)
#One example is spacing, which defines pixels between elements

screen ourScreen():

    vbox:

        align (0.5, 0.5)
        spacing 20

        text "I am the first text."
        text "Me be second."
        text "Yarr, I be the third!"

# The game starts here.

label startSix:

    call screen ourScreen

    return

#Null creates an empty area on the screen, which can be used to space things or fill a screen

#Example with lots of different text elements to see what things look like

screen ourScreen():

    # vbox in the top part
    vbox:

        align (0.5, 0.25)

        # first and second text
        text "First red text.":
            bold True
            color "ff0000"
        text "Second red text.":
            bold True
            color "ff0000"

        # null for the empty space
        null:
            height 45

        # third and fourth text
        text "Third red text.":
            bold True
            color "ff0000"
        text "Fourth red text.":
            bold True
            color "ff0000"

    # hbox in the bottom part
    hbox:

        align (0.5, 0.75)
        spacing 50

        # first vbox (moved to the left), with blue texts
        vbox:

            spacing 20

            # two blue texts
            text "First blue text.":
                color "0000ff"
            text "Second blue text.":
                color "0000ff"

        # second vbox (moved to the right) with green texts
        vbox:

            spacing 75

            # two green texts
            text "First green text.":
                color "00ff00"
            text "Second green text.":
                color "00ff00"

# The game starts here.

label startSeven:

    call screen ourScreen

    return

#################################################################
#TUTORIAL 2: FRAME AND FIXED STATEMENTS, DISPLAYABLES
#################################################################

#Next up we look at the frame statement
#Frame creates a rectangular area that has a background and a few pixels of padding
#xysize is used for this, since 'size' is used for text peroperties
#Everything that we now add will be positioned relative to the top-left corner of that frame rather than the screen as usual


screen ourScreen():

    frame:

        xysize (500, 500)
        align (0.25, 0.25)
        text 'Text inside the frame'

# The game starts here.

label startEight:

    call screen ourScreen

    return


#For instance, here we put a vbox in the center of the frame with text: and it the text becomes relative
#to that vbox


screen ourScreen():

    frame:

        xysize (500, 500)
        align (0.25, 0.25)

        vbox:

            align (0.5, 0.5)
            spacing 40  

            text "First text inside the frame."
            text "Second text inside the frame."
            text "Third text inside the frame."

#Next up is the fixed statement: it works the same as frame, but it functions only as an area,
#With no default background or padding. So if we used the same thing we'd see no background

screen ourScreen():

    fixed:

        xysize (500, 500)
        align (0.25, 0.25)

        vbox:

            align (0.5, 0.5)
            spacing 40  

            text "First text inside the frame."
            text "Second text inside the frame."
            text "Third text inside the frame."

#Next up we will talk about displayables
#Displayables are things that can be shown to the player
#They can be defined either through 'define' or 'image'
#Solid creates an area of single color with the hex code

define whiteDefined = Solid("fff")
image whiteImaged = Solid("fff")

screen ourScreen():

    add whiteDefined
    # add "whiteImaged"

    frame:

        xysize (500, 500)
        align (0.25, 0.25)

        vbox:

            align (0.5, 0.5)
            spacing 40  

            text "First text inside the frame."
            text "Second text inside the frame."
            text "Third text inside the frame."

label startNine:
    call screen ourScreen


#when you use define, you can simply use the name of the displayble
#Images need the name in quotes
#Two more displayables are show below, frame and composite:


#Frame displayables take images, keep the borders the same and resize
#the middle to fit an area
#Composites require multiuple arguments: they combine multiple
#images or displayables. The first argument is the size of the
#whole composite. Then, every odd argument is a tuple giving a position
#relative to the top left corner of the area, where the displayable is
#placed. Every even argument is the displayable


define whiteDefined = Solid("fff")


define SolidExample = Solid("f80", xysize = (100, 100))

define FrameExample = Frame("gui/frame.png", xysize = (200, 200))

define CompositeExample = Composite((200, 200), 
    (0, 0), FrameExample, 
    (35, 35), SolidExample,
    (35, 35), Text("Hey everyone!", size = 22, color = "00f" )
    )


screen ourScreen():

    add whiteDefined

    add SolidExample align (0.25, 0.5)
    add FrameExample align (0.5, 0.5)
    add CompositeExample align (0.75, 0.5)

    
label startTen:
    call screen ourScreen


#ConditionSwitch displayables
#These change based on a variable


#################################################################
#TUTORIAL 4: BUTTONS AND SCREEN ACTIONS
#################################################################

#statements to create a  button: button, textbutton, and imagebutton


#Buttons can only be interacted with if they have the action property
#The action property defines what happens when the button is clicked
#Its value has to be a screen action
#Screen actions are used by statements that players can interact with, to determine what 
#Happens when they do. They are not functions despite the parentheses at the end
#Nullaction makes it so the button does nothing unless it's hovered
screen ourScreen():

    textbutton "Click me, I do stuff!":

        align (0.5, 0.5)

        action NullAction()

#Here is an example of a screen action called 'notify'. This make the notify screen appear,
#with a given action, before fading away

screen ourScreen():

    textbutton "Click me, I do stuff!":

        align (0.5, 0.5)

        action Notify("See? I told you I do stuff.")


label startEleven:
    call screen ourScreen


#Textbutton is a combination of button and text. We can look at that more closely
#by recreating the above code using just the button statement 

define white = Solid("fff")

screen ourScreen():

    button:

        background white 
        xysize (450, 300)
        align (0.5, 0.5)

        action Notify("See? I told you I do stuff.")

        text "Click me, I do stuff!":

            size 36
            idle_color "08a"
            hover_color "01a"
            align (0.5, 0.5)

#Button is similar to frame: it has a background and padding by default
#Inside we put text with the same message as the previous button. Here we add
#Size and color and allign it in the middle of the button

#The thing about teh button statement is that you can put multiple statemetnts under it
#Multiple texts, frames, and it will sstill be a button

#If we wanted to recreate the textbutton in the same style as above, we could do as follows:

#Text properties are preceded by text_

define white = Solid("fff")

screen ourScreen():

    textbutton "Click me, I do stuff!":

        background white 
        xysize (450, 300)
        align (0.5, 0.5)

        text_size 36
        text_color "08a"
        text_align (1.0, 0.5)

        action Notify("See? I told you I do stuff.")


#Lastly we look at the imagebutton s
#Imagebutton shows displayables or images
#To understand idle and hover, we need to understand buttonstates. There are five button states:
#Insensitive, idle, hover, selected_idle, and selected_hover
#Insensitive is when the button can't be interacted with
#Idle is the state when the button is not hovered, hover is when it is hovered
#The Selected_ states are the same, but they apply to when the button is selected


define darker = Solid("72619c")
define brighter = Solid("c6bfd7")

screen ourScreen():

    imagebutton:

        xysize (300, 300)
        align (0.5, 0.5)

        idle darker
        hover brighter

        action Notify("Taste the power of an imagebutton!")


#You can use all button states as prefixes for its properties, too
#For instance, you could have properties like idle_background to have its background
#Change depending on its state
#This can be used by non-button statements inside buttons, like hover_cover for a text
#Or selected_idle_spacking for a vbox


#The 'selected' state:
#You can define a variable that makes a button selected as follows: 
#selected(valor_selected) as a child of the button statement
#This makes it so when that variable is true, the button will use the properties assigned to
#selected_ instead of the normal ones

screen ourScreen():

    button:

        idle_background white 
        hover_background darker
        xysize (450, 300)
        align (0.5, 0.5)

        action Notify("See? I told you I do stuff.")

        text "Click me, I do stuff!":

            size 36
            idle_color "08a"
            hover_color "01a"
            align (0.5, 0.5)

        vbox:
            align(0.0, .5)

            text 'p' color "08a"


#################################################################
#TUTORIAL 5: SCREEN ACTIONS
#################################################################



#The screen action on the action property activates when the button is clicked
#Hovered activates when the button is hovered, and unhovered activates when its idle

define darker = Solid("72619c")
define brighter = Solid("c6bfd7")

screen ourScreen():

    imagebutton:

        xysize (300, 300)
        align (0.5, 0.5)

        idle darker
        hover brighter

        action NullAction()
        hovered Notify("Stop touching me!")
        unhovered Notify("Ah, much better.")


#An alternative to button if you only wanted to do something like the above
#Is the mosearea statement. Unlike buttons, it does not take an action property
#But it can still take actions with hovered and unhovered: so if you just want to do these two things
#It's more efficient than a button

screen ourScreen():

    mousearea:

        xysize (300, 300)
        align (0.5, 0.5)

        hovered Notify("Stop touching me!")
        unhovered Notify("Ah, much better.")


#More about screen actions, specifically the four most common ones

#TO display screens you can use the 'use statement', the show screen action
#Or a renpy function

define darker = Solid("72619c")
define brighter = Solid("c6bfd7")

screen ourScreen():

    imagebutton:

        xysize (300, 300)
        align (0.5, 0.5)

        idle darker
        hover brighter

        action Show("alsoOurScreen")

screen alsoOurScreen():

    textbutton "Can you click me? I'm a little shy.":

        xalign 0.5

        text_size 42

        action Hide("alsoOurScreen")

#The call screen action

#We use this to call a provided label, exit the screen, and enter it

define darker = Solid("72619c")
define brighter = Solid("c6bfd7")

screen ourScreen():

    imagebutton:

        xysize (300, 300)
        align (0.5, 0.5)

        idle darker
        hover brighter

        action Call("ourLabel1")

label ourLabel1():

    "Lezalith" "This is the only message you're going to get."

    return

#Last action to look at: SetVariable. This shows us that one button can use multiple screen actions


#In this example, it's important that the variable is set before calling the screen
#As screen actions are executed in the order that is provided
default whatDidYouClick = "You clicked nothing."

screen ourScreen():

    hbox:

        align (0.5, 0.5)
        spacing 150

        textbutton "The Left Button!":
            action SetVariable("whatDidYouClick", "You clicked The Left Button!"), Call("ourLabel")

        textbutton "The Right Button!":
            action SetVariable("whatDidYouClick", "You clicked The Right Button!"), Call("ourLabel")


label ourLabel():

    "Lezalith" "[whatDidYouClick]"

    return


#################################################################
#TUTORIAL 6: HOW TO CHANGE AND/OR RE-USE SCREENS WITH ARGUMENTS, THE USE
#AND TRANSCLUDE STATEMENTS
#################################################################

#Up until now we've coded screens that are always the same. But what about screens
#That should change? We could change them using variables, but what if it's something insignificant?
#Here we look at arguments. But we start by creating a simple screen with a frame and text

screen frameScreen():

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        text "I am inside the frame!":
            align (0.5, 0.5)

label startTwelve():

    call screen frameScreen

#Arguments are temporary variables, that are given a value each time the screen is shown

screen frameScreen(textToShow):

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        text textToShow:
            align (0.5, 0.5)

label startThirteen():
#How to call a screen while passing an argument
    call screen frameScreen(textToShow = "I am inside the frame!")



#The arguments that are named in parentheses don't have a default value. So you couldn't 
#call a screen without giving it an argument. You could, however, give it a default value
#by writing it inside the screen statement as follows

screen frameScreen(textToShow = "I am inside the frame!"):

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        text textToShow:
            align (0.5, 0.5)

label startFourteen():

    call screen frameScreen


#And you can of course give screens multiple arguments

screen frameScreen(firstText, secondText):

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        text firstText:
            xalign 0.5

        text secondText:
            yalign 0.5

label startFifteen():

    call screen frameScreen(firstText = "I am centered horizontally!",
    secondText = "I am centered too, but vertically.")


#The use statement
#This is something that we use to insert one screen into another screen
#For instance, we can create a textScreen here and use the use statement to put it into the frame

screen frameScreen():

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        use textScreen

screen textScreen():

    text "I am inside the frame!":
        align (0.5, 0.5)

label startSixteen():

    call screen frameScreen


#The use statement can utilize arguments too, like so:

screen frameScreen():

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        use textScreen(textToShow = "I am inside the frame!")

screen textScreen(textToShow):

    text textToShow:
        align (0.5, 0.5)

label startSeventeen():

    call screen frameScreen


#The use statement combined with arguments allows use to resue a screen multiple times

screen frameScreen():

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        use textScreen(textToShow = "I am inside the frame!")
        use textScreen(textToShow = "I will make this confusing.")

screen textScreen(textToShow):

    text textToShow:
        align (0.5, 0.5)

label startEighteen():

    call screen frameScreen


#The last statement to cover is transclude. You can include it in a screen that you intend
#to use at somepoint with the use statement, and you can then add things to the use statement with a colon
#And they will be inserted where transclude is
#For instance:
#In this example, screenwithtexts is called, and it uses framescreen and the text after the use statement
#is inserted for transclude, making it relative to the frame inside framescreen

screen frameScreen():

    frame:
        align (0.5, 0.5)
        xysize (400, 200)

        transclude

screen screenWithTexts():

    use frameScreen:

        text "I am inside the frame!":
            xalign 0.5

        text "I no longer make things confusing.":
            yalign 0.5

label startNineteen():

    call screen screenWithTexts

#Transclude means we can prepare a background, for instance, and place whatever we want on top if it, anywhere


#Final block that combines everything we've learned today

# All sorts of colors for backgrounds.
define red = Solid("#800a0a")
define orange = Solid("#ff7605")
define yellow = Solid("#f3ff17")

screen frameScreen( framePosition ):

    # The bottom, red frame.
    frame:
        background red
        
        # At a given position.
        pos framePosition
        xysize (400, 220)

        # The smaller, orange frame.
        frame:
            background orange

            # Centered in the red frame.
            align (0.5, 0.5)
            xysize (370, 190)

            transclude

        # The yellow frame, just a decoration.
        frame:
            background yellow

            # Slightly off the right side.
            align (1.0, 0.5)
            xoffset -20
            xysize (40, 200)

screen mainScreen():

    # First frame, top left.
    use frameScreen( framePosition = (100, 100) ):

        text "I am inside the frame!":
            yalign 0.5
            color "#4a1c00"

    # Second frame, bottom middle.
    use frameScreen( framePosition = (400, 400) ):

        vbox:
            spacing 5

            yalign 0.5
            xoffset 30

            text "One"
            text "Two"
            text "Three"
            text "Four"
            text "What's behind"
            text "        the fridge door"

    # Third frame, top right.
    use frameScreen( framePosition = (700, 100) ):

        add "gui/window_icon.png":
            align (0.2, 0.5)


label start():

    call screen mainScreen