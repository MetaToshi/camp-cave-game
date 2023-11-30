#GAMING!!!!
#this is a fade for the timer bar!
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

#THIS IS WHERE I HAVE ADDED THE CLICKABLE OBJECTS!!!!
screen startButton():
    imagebutton:
        xalign 0.5
        yalign 0.8
        auto "start_%s.png" action [ToggleScreen("startButton"), Jump('Heart')]

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

                    
define u = Character("...", what_italic=True)
define mc = Character("Player")
define rey = Character("Rey")
define notrey = Character("Rey")

image Rey_N_Default = "Rey_N_Default.png"
image Rey_N_Guilt = "Rey_N_Guilt.png"
image Rey_N_Nervous = "Rey_N_Nervous.png"
image Rey_N_Question = "Rey_N_Question.png"
image Rey_N_Smile = "Rey_N_Smile.png"
image Rey_N_Speechless = "Rey_N_Speechless.png"
image Rey_M_Default = "Rey_M_Default.png"
image Rey_M_Guilt = "Rey_M_Guilt.png"
image Rey_M_Nervous = "Rey_M_Nervous.png"
image Rey_M_Question = "Rey_M_Question.png"
image Rey_M_Smile = "Rey_M_Smile.png"
image Rey_M_Speechless = "Rey_M_Speechless.png"
image Robbie_N_Awkward = "Robbie_N_Awkward.png"
image Robbie_N_Cheeky = "Robbie_N_Cheeky.png"
image Robbie_N_Default = "Robbie_N_Default.png"
image Robbie_N_Guilt = "Robbie_N_Guilt.png"
image Robbie_N_Question = "Robbie_N_Question.png"
image Robbie_N_Speechless = "Robbie_N_Speechless.png"
image titlepageone = "titlepageone.png"

###----------------THE GAME STARTS HERE----------------###
label start:
    scene bg titlepageone
    call screen startButton

#Intro Screen
label Heart:
    scene bg cave

    u "You finally feel the passage begin to widen in front of you, and you draw a breath, inching your way forward."
    u "Just keep moving forward."
    u "Slowly, the walls loosen their grip on you and begin to give way."
    u "You find yourself in  a small cavern; it isn't the most spacious thing in the world, but compared to what you had just been through, it feels like a penthouse suite"

    u "The passage spits you out low to the floor, and you push yourself up on your knees."
    play sound "Footsteps-Normal.ogg" loop
    u "Your brain pulses against the sides of your skull, feeling the rhythm align with the sound of your heartbeat in your ears."
    u "Blood pulsing through your body becomes apparent to you as you feel its pressure in your fingers and toes. The rhythmic beating of your blood, no, your heart, feel external. It’s all around you, emanating from the walls. "
    u "You see it out of the corner of your eye, the rocks organically begin to pulse alongside the rhythm of your exhausted body. "
    u "You turn to take a closer look, but are reassured that is not the case, as you glance at the static wall. "
    stop sound fadeout 0.5

    menu:
        "God, you need to calm down.":
            pass
        "Jesus Christ, the walls really did look like they were palpitating. What the fuck?":
            pass

label HeartA:
    scene bg cave
    u "You take a deep breath and put a hand on a nearby rock to steady yourself. But immediately spring back from the contact–you expected a rough surface underneath your palm, but instead were greeted with thin protruding lines."
    u "They’re almost like spiderwebs sticking out from the rocks, but within that brief moment of contact you could’ve sworn you felt…a pulse? They almost look like…"
    menu:
        "...veins?":
            jump HeartA1
        "...just a weird rock formation.":
            jump HeartA2
label HeartA1:
    scene bg cave
    u "You glance down at your own inner arm, the weak light of your flashlight illuminating your skin. The pattern on the rocks match the spindly contours of your veins. You shiver."
    jump StandUp
label StandUp:
    u "Nothing to see here"
    jump Trash
label HeartA2:
    scene bg cave
    u "You shake your head, dismissing whatever bizarre connection your brain was about to make."
    jump Trash
label HeartB:
    scene bg cave
    u "You squint, convinced your eyes were playing tricks on you. This place had to be playing tricks on you, right? Rocks didn’t move like that."
    jump Trash


label Trash:
    scene bg cave
    u "You have no interest in staying in this room any longer–it creeps you the fuck out. It was probably time to meet up with the others, anyway. You should get back to the rendezvous point."
    menu:
        "Look around the room":
            jump TrashA
        "Shimmy backward in the passage and head back to the rendezvous point.":
            jump RendezvousPoint
label TrashA:
    scene bg cave
    u "You notice a piece of trash on the floor; a crumpled soda can."
    menu:
        "Pick it up.":
            jump TrashA1
        "Leave it.":
            jump TrashA2
label TrashA1:
    scene bg cave
    u "You pick up the can; even in a place as unpleasant as this, there shouldn’t be trash laying around. Pollution sucked no matter where it was."
    jump RendezvousPoint
label TrashA2:
    scene bg cave
    u "You shake your head. You don’t want to carry around a piece of gross trash; this place was already unpleasant enough. You shimmy back in the tunnel and start to head back to the rendezvous point."
    jump RendezvousPoint


label RendezvousPoint:
    $time = 5
    $timer_range = 5
    $timer_jump = 'RendezvousPoint'
    scene bg cave
    play sound "Footsteps-Reverbed.ogg"
    u "You finally make it back to the rendezvous point. An empty, silent cavern greets you."
    stop sound fadeout 0.5
    u "Where were the others? You cast your flashlight beam around the space, but see nothing except stone walls and stalagmites."
    u "Shifting uneasily, you bite your lip. This whole thing just isn’t sitting right with you. This cave felt off, in more ways than one. Maybe it was time to get the hell out of this place."
    show screen countdown
    menu:
        "Leave the cave":
            jump RendezvousPointA
        "Go looking for your friends.":
            jump RendezvousPointB
label RendezvousPointA:
    scene bg cave
    play sound ["Footsteps-Reverbed.ogg", "Foosteps-Normal.ogg"]
    u "You can’t take this place anymore. You turn to make your way back through the passages and rooms, ignoring the jab of guilt at leaving your friends behind in the cave."
    u " They should be fine–they were probably all together somewhere down there. Sooner or later they would reach the same conclusion you did and leave."
    u "..."
    u "You climb until you see the faint rays of daylight from the mouth of the cave."
label RendezvousPointB:
    scene bg cave
    u "You can’t leave your friends behind. But sitting alone in the cavern is sending shivers down your spine."
    u "Your gaze locks on the far end of the cavern, where two gaping openings mark distinct paths."
    u "The one on the right has a narrow entrance; you’d have to turn sideways to slide through. The one on the left has a wider opening."
    menu:
        "You choose the path on the right.":
            jump RendezvousPointB1
        "You choose the path on the left.":
            jump RendezvousPointB2
#THESE TWO NEED ROCK SOUNDS_______________________________________________________
label RendezvousPointB1:
    scene bg cave
    u "You take the path on the right. You flip sideways and move into the passage with your arms flat at your sides. You feel the abrasive rock rub at your skin."
    jump Womb
label RendezvousPointB2:
    scene bg cave
    u "You veer toward the right opening. Though the entrance to the passage is wide, about fifteen paces in it slant sharply downward."
    u "You crouch, and then eventually go to your hands and knees.You crouch, and then eventually go to your hands and knees."
    u "The walls seem to constrict around you until you're flat on your stomach, army crawling forward. You regret choosing this path as you feel the back of your head knock against the low ceiling, the distance between it and the floor barely a foot in height."
    u "But there wasn’t any space to turn around, so you continue ahead."
    jump Stomach


label Womb:
    u "It may have been your imagination, but you swore you felt the skitter of spider legs crawl over one of your hands."
    u "You yelp a bit, but your flashlight is in your other hand, and the space is far too narrow to turn your head to look down at where you felt the movement. You shudder."
    u "The opening to leave the passage was smaller than the tunnel itself, and you have to bend awkwardly at the waist to get low enough to duck through."
    u "Once on the other side, you look up and nearly jump straight out of your skin."
    u "Rey is standing in the center of the room, watching you quietly."

    show Rey_M_Default
    mc "Rey? What-what  are you doing here?"
    u "She stares right through you, only looking up and meeting your eyes when you walk closer."
    mc "Rey? What are you-"
    notrey "Oh, hello."
    u "Her voice sounds somber, almost tired, like she had just finished crying."
    mc "Uh, hi? C’mon Rey, stop acting weird, why are you down here?"
    u "As you ask her again, she offers what seems like a forced smile and continues."
    notrey "I was looking for you, and the rest of our group. Not sure how I got here…"
    mc "Ah, yeah me too…"
    mc "I wonder if Chance and Robbie are lost too, or if they’re looking for us."
    u "Rey stares at you, blankly."

label Stomach:
    pass



