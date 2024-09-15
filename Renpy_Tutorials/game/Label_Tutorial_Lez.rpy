




#####TUTORIAL 2: DEFINING CHARACTERS AND CREATINGE EFFECTS ON TEXT USING TEXT TAGS###

#By predefining characters, I can then reference them using their assigned variable

define l = Character("Lezalith")
#Character instantiates a character object, which takes one mandatory input: its name
#It also bundles in the image of the character, how their name and dialogue look, etc


#Here is an example of what you can do with the character object
#Here we define the color of the character's name and their dialogue color
define l = Character("Lezalith", who_color = "00FF00", what_color = "FF0000")

##We can add more examples of properties
#Yoffset changes the position of an element after itis calculated from other properties
#I could have also used position to adjust this thing's location
define l = Character("Lezalith",
    who_color = "00FF00", 
    who_yoffset = -200,

    what_color = "FF0000",
    what_size = 72,
    what_font = "DejaVuSans-Bold.ttf",
    what_yoffset = -200)

#Next up let's look at text tags, which let you format particular text
#While keeping the defined style ie. add bold or italics. Here are examples:

label tagExample():

    l "This is how I can {b}shout out loud!{/b}"

    l "This is... I don't {i}actually know{/i} what this is."

    l "Maybe it's {font=DejaVuSans.ttf}just a dream.{/font}"

    return


######TUTORIAL 3: SHOWING AND HIDING BACKGROUND AND CHARACTER IMAGES#########



#Image statements are similar to define statements, you just pass them an image
#You can define an image simply by putting it into the game/ directory
#So if it's in that folder, you can simply write 'scene main_menu' to pull it up 
#without needing to specify its path


image ourBackground = "gui/main_menu.png"
image icon = "gui/window_icon.png"


#Adding a scene statement causes a change to happen in between the statements

#What about the show statement? A scene can only show one image at a time
#Show can bring up images even if others are present. Therefore, scene is good as the background
#Image, whereas show is good for things like character sprites

#Finally, the hide statement takes away the image.

label start0():

    l "This line takes place without a background."

    scene ourBackground

    l "This line has a background."

    show icon

    l "This line has a background and a sprite."

    hide ourBackground

    l "Background got hidden."

    hide icon

    l "Sprite got hidden."

    return


#the 'scene expression' statement
#If you add 'expression' after scene like so:
# scene expression Solid("c0c0c0") you are telling renpy that what is coming next is not an image
#but something in python code ie. a function/variable


######TUTORIAL 4: Transforms 1: the basics of ATL#########

#Today we are going to learn how to move the image around, rotate it, change its size, make it transparent, etc.
#This is all done through ATL, the animation and transformation language

#xalign centers the image horizontally, yalign centers it vertically
#A link to all of the transform properties:
#https://www.renpy.org/doc/html/atl.html#list-of-transform-properties

label start1():

    l "Let's show an icon!"

    show icon:
        xalign 0.5
        yalign 0.5

    l "Isn't it spectacular?"

    return

#Using rotate to rotate the object, and alpha to make it transparent


label start2():

    l "Let's show an icon!"

    show icon:
        xalign 0.5
        yalign 0.5
        rotate 90.0
        alpha 0.6

    l "Isn't it spectacular?"

    return

#We can use these same properties not only as part of the show statement, but also in scene statements,
#image statements, and transform statements 
#for instance, we could do it this way:

image icon:
    "gui/window_icon.png"
    xalign 0.5
    yalign 0.5
    rotate 90.0
    alpha 0.6

label start3():

    l "Let's show an icon!"

    show icon

    l "Isn't it spectacular?"

    return



#The transform statement lets us define a set of attributes for an image, and then we can use that
#Set of attributes multiple times on different images

image icon = "gui/window_icon.png"
image slot = "gui/button/slot_hover_background.png"

transform ourTransform:
    xalign 0.5
    yalign 0.5
    rotate 90.0
    alpha 0.6

label start4():

    l "Let's show two images instead of one!"

    show icon at ourTransform
    show slot at ourTransform

    l "Isn't it spectacular? Twice as spectacular now."

    return


######TUTORIAL5: Branching a story with menus#########

#The menu button allows you to define choices for the user
#Note about NVL mode: you can also make it so that menu options appear in NVL mode as well

'''
define l = Character("Lezalith",
    who_color = "E34D0C", kind=nvl)
define e = Character("Eileen", kind=nvl)
define narrator = nvl_narrator
default traveled = False
define menu = nvl_menu
'''
define l = Character("Lezalith",
    who_color = "E34D0C")

define e = Character("Eileen",
    who_color = "E6E600")

label start5():

    # Silver background
    scene expression Solid("c0c0c0")
    
    "What should we ask Eileen?"

    menu:

        "Are you enjoying the spring?":

            e "I am! Hopefully the readers are too."
            e "Or other seasons, if they're reading this later."

        "What did you have for lunch today?":

            e "I've had chicken tikka masala. It was delicious!"

    l "I'm glad to hear that!"

    return