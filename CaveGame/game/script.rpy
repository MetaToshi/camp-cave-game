# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Camera")
define p = Character("Croissant")
define rey = Character("Rey")
define chance = Character("Chance")
define robby = Character("Robby")
define mc = Character("")

image p1s1 = "p1s1.png"
image rey1 = "rey1.png"
image rey2 = "rey2.png"
image reyblegh = "reyblegh.png"
image chance = "chance.png"
image robby = "robby.png"
image bottle = "bottle.png"
image bottle2 = "bottle2.png"
image reycry = "reycry.png"
image reyyell = "reyyell.png"
image reyyell2 = "reyyell2.png"
image titlepageone = "titlepageone.png"
#this is a fade for the timer bar!
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

#THIS IS WHERE I HAVE ADDED THE CLICKABLE OBJECTS!!!!
screen bottleButton():
    imagebutton:
        xalign 0.5
        yalign 0.5
        auto "bottle_%s.png" action [ToggleScreen("bottleButton"), Jump("scene2")]

screen startButton():
    imagebutton:
        xalign 0.5
        yalign 0.8
        auto "start_%s.png" action [ToggleScreen("startButton"), Jump('scene1')]


#THIS IS THE SHAKE FUNCTION 
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,time,
                        child,
                        add_sizes=True,
                        **properties)

        Shake = renpy.curry(_Shake)
        
    #
#If you want to use the shake function during dialogue: example = c "ahhhhhh!" with sshake
init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

#THIS IS THE FUNCTION FOR THE TIMER!!!
init:
    $timer_range = 0
    $timer_jump = 0
    $time = 0
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.6 xmaximum 300 at alpha_dissolve

<<<<<<< Updated upstream
#THIS IS THE INVENTORY
#IN ORDER TO ADD ITEMS PLEASE USE inventoryitems.append("itemname_%s.png")
#Please keep in mind these are imagebuttons and do need separate images for action, hover, and idle.
#These images can be duplicates tho
default item_descriptions = {}
default inventoryitems = []
default item_description = ""

screen inventory:
    zorder 90
    frame:
        background "#7e2811"
        xalign 0.935
        yalign 0.9

        textbutton "Inventory":
            action ToggleScreen("itemdescriptions")
style inventorybutton is frame:
    xsize 200
    ysize 200

style inventorybuttontext:
    xalign 0.5
    yalign 0.5

init:
    transform customzoom:
        zoom 0.5

screen itemdescriptions:
    window:
        background "#ABB8"
        xsize 420
        ysize 750
        xalign 1.0
        yalign 0.5
    window:
        background "#ffffff"
        xsize 400
        ysize 720
        xalign 1.0
        yalign 0.5
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inventory"
            for i in inventoryitems:
                imagebutton:
                    auto i
                    at customzoom
                    #xsize 100
                    #ysize 300

                    

###----------------THE GAME STARTS HERE----------------###
label start:
=======
# The game starts here !!!!! 
label start:


    mc "You finally feel the passage begin to widen in front of you, and you draw a breath, inching your way  forward. Just keep moving forward. Slowly, the walls loosen their grip on you and begin to give way."
     
    mc "You find yourself in a small cavern; it isn’t the most spacious thing in the world, but compared to what you had just been through, it feels like a penthouse suite. "

    # show bg picture 
    scene bg cave
    mc "The passage spits you out low to the floor, and you push yourself up on your knees. "

    mc "Your brain pulses against the sides of your skull, feeling the rhythm align with the sound of your heartbeat in your ears. "

    mc "Blood pulsing through your body becomes apparent to you as you feel its pressure in your fingers and toes. The rhythmic beating of your blood, no, your heart, feel external. It’s all around you, emanating from the walls."

    mc "You see it out of the corner of your eye, the rocks organically begin to pulse alongside the rhythm of your exhausted body. You turn to take a closer look, but are reassured that is not the case, as you glance at the static wall."

    menu: 
        "God, you needed to calm down":
            jump StartA
        "Jesus Christ, the walls really did look like they were palpitating. What the fuck?":
            jump StartB

label StartA:
    
    mc "You take a deep breath and put a hand on a nearby rock to steady yourself. But immediately spring back from the contact–you expected a rough surface underneath your palm, but instead were greeted with thin protruding lines."

    mc " They’re almost like spiderwebs sticking out from the rocks, but within that brief moment of contact you could’ve sworn you felt…a pulse? They almost look like… "



label StartB:
    
    mc "You squint, convinced your eyes were playing tricks on you. This place had to be playing tricks on you, right? Rocks didn’t move like that."

    # pick up trash im assuming
    menu:
        "Pick up Trash":
            jump Trash

label Trash:
    mc "You have no interest in staying in this room any longer–it creeps you the fuck out. It was probably time to meet up with the others, anyway. You should get back to the rendezvous point."

label croissantstart:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

>>>>>>> Stashed changes
    scene bg m1s1

    c "Ahhhhhhhhh!" with sshake

    show p1s1

    p "aaaaaaaaaa"

    p "Stop! I coulda dropped my croissant..."

    # This ends the game.

    jump introscreen

label introscreen:
    scene bg titlepageone
    call screen startButton

#Intro Screen
label scene1:
    scene bg cave

    show p1s1 at left

    p "oh my gooooooodness!"

    show rey1 at right

    rey "woah we are in a cave!"

    show rey2 at right

    rey "it's pretty nice in here :)"
   
    hide p1s1
    show chance at left
    
    chance "Psh, yeah whatever dude"
    hide rey2
    show rey1 at right

    show robby

    robby "Heh yeah whatever this cave is like super boring guys right lol yeah..."
   
    show robby at topleft
    show robby behind chance

    call screen bottleButton

label scene2:
    $time = 5
    $timer_range = 5
    $timer_jump = 'decide'
    scene bg cave

    show robby at right
    show screen inventory
    $inventoryitems.append("bottle_%s.png") 
    $inventoryitems.append("start_%s.png")
    robby "woah what did that bottle do?"

    show chance at left

    chance "don't know, but"
    chance "let's smash it!!!"
#THIS MENU FEATURE IS HOW U MAKE CHOICES
    show screen countdown
    menu:
        "SMASH IT!":
            hide screen countdown
            jump Smashed
        "Leave it.":
            hide screen countdown
            jump left
label decide:
    $time = 5
    $timer_range = 5
    $timer_jump = 'decide'
    scene bg cave
    show robby at right
    show chance at left

    chance "Well, what should we do?"

    show screen countdown
    menu:
        "SMASH IT!":
            hide countdown
            jump Smashed
        "Leave it.":
            hide countdown
            jump left
label Smashed:
    scene bg cave

    show reycry
    rey "OW!" with sshake

    hide reycry
    show chance at right
    show reyyell2 at left 

    chance "What even happened"

    hide reyyell2 
    show reyyell at left

    rey "The glass sliced my arm dude!"

    chance "oh sorry, it must've bounced off the cave wall or something..."
    
    return

label left:
    scene bg cave
    
    show rey1
    rey "Good, let's treat the cave nicely."
    
    return

