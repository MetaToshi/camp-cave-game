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

default Mimic = 0
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

                    
define u = Character("", what_italic=True)
define mc = Character("Player")
define rey = Character("Rey")
define notrey = Character("Rey")
define robbie = Character("Robbie")
define stranger = Character("Stranger")

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
    scene bg blacksquare

    u "You finally feel the passage begin to widen in front of you, and you draw a breath, inching your way forward."
    u "Just keep moving forward."
    u "Slowly, the walls loosen their grip on you and begin to give way."
    scene bg cave with dissolve
    play sound "Footsteps-Normal.ogg" fadein 1.0 volume 0.6
    u "You find yourself in  a small cavern; it isn't the most spacious thing in the world, but compared to what you had just been through, it feels like a penthouse suite"
    stop sound fadeout 1.5
    u "The passage spits you out low to the floor, and you push yourself up on your knees."
    play sound "Medium-Heartbeat.ogg" fadein 1.0 loop
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
    u "You finally make it back to the rendezvous point.{nw}" 
    stop sound fadeout 0.5
    u "You finally make it back to the rendezvous point.{fast} An empty, silent cavern greets you."
    u "Where were the others? You cast your flashlight beam around the space, but see nothing except stone walls and stalagmites."
    u "Shifting uneasily, you bite your lip. This whole thing just isn’t sitting right with you. This cave felt off, in more ways than one. Maybe it was time to get the hell out of this place."
    show screen countdown
    menu:
        "Leave the cave":
            hide screen countdown
            jump RendezvousPointA
        "Go looking for your friends.":
            hide screen countdown
            jump RendezvousPointB
label RendezvousPointA:
    scene bg cave
    play sound ["Footsteps-Reverbed.ogg", "Footsteps-Normal.ogg"]
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
    $Mimic = 1
    jump Womb
label RendezvousPointB2:
    scene bg cave
    u "You veer toward the right opening. Though the entrance to the passage is wide, about fifteen paces in it slant sharply downward."
    u "You crouch, and then eventually go to your hands and knees.You crouch, and then eventually go to your hands and knees."
    u "The walls seem to constrict around you until you're flat on your stomach, army crawling forward. You regret choosing this path as you feel the back of your head knock against the low ceiling, the distance between it and the floor barely a foot in height."
    u "But there wasn’t any space to turn around, so you continue ahead."
    jump Stomach


label Womb:
    scene bg cave
    $time = 5
    $timer_range = 5
    $timer_jump = 'SafeZone'
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
    hide Rey_M_Default
    show Rey_M_Smile
    u "As you ask her again, she offers what seems like a forced smile and continues."
    notrey "I was looking for you, and the rest of our group. Not sure how I got here…"
    mc "Ah, yeah me too…"
    mc "I wonder if Chance and Robbie are lost too, or if they’re looking for us."
    hide Rey_M_Smile
    show Rey_M_Default
    u "Rey stares at you, blankly."
    mc "Um… so, do you want to try to find a way out? Maybe if we-"
    notrey "Mm, follow me."
    mc "Oh do you know a way ou{nw}"
    hide Rey_M_Default with fade
    mc "Oh do you know a way ou{fast}–hey! Rey"
    u "She runs off, making no attempt to check on you before doing so."
    mc "Hey, slow down! Rey!"
    u "If she hears you, she does not respond."
    u "The two of you go deeper into the cave, passing by a few different tunnels and narrow rooms, all of which she avoids."
    mc "Hey uh, are you sure this is the right way?"
    notrey "…"
    play sound "Footsteps-Squishy.ogg"
    u "The walls feel like they’re closing in, and each step you take progressively sounds more and more squishy. You watch as Rey pushes past a curtain of some thin, fleshy-looking substance, red liquid staining her hands, making them look bloody."
    u "She turns around and looks at you as a thick droplet of it lands on her face, but instead of freaking out, she stays completely silent and motionless."
    mc "Rey, can you at least tell me where we’re going?"
    notrey "We’re heading out."
    u "She steps close to a passage that’s lower to the ground, looks back at you, and walks into it."
    show screen countdown
    menu:
        "Follow Rey.":
            hide screen countdown
            jump WombA
        "Hesitate.":
            hide screen countdown
            jump WombB
label WombA:
    scene bg fleshhole
    u "You follow after Rey, a strange feeling in your stomach. She must have been moving fast, because you don’t catch sight of her ahead of you."
    u "Fifteen paces in, the ceiling starts to slant sharply downward. You crouch, and then eventually go to your hands and knees."
    u "The walls seem to constrict around you until you're flat on your stomach, army crawling forward. You regret choosing this path as you feel the back of your head knock against the low ceiling, the distance between it and the floor barely a foot in height. But there wasn’t any space to turn around, so you continue ahead."
    mc "Rey? Are you there? Slow down, I don't want to lose you."
    jump Stomach
label WombB:
    scene bg fleshhole
    u "You watch Rey crawl through the low passage, but your feet don’t move. For some reason, the whole interaction didn’t sit quite right with you."
    u "Trusting your gut, you hurry forward and slip into a tunnel off to the side, before you had a chance to second guess yourself."
    u "You hear voices up ahead, and tense for a moment."
    u "“Is someone there?”"
    jump SafeZone
#SAFEZONE IS AT THE BOTTOM RN (PLAYTEST)


label Stomach:
    scene bg fleshhole
    u "You squirm through the final twist, your hips at an uncomfortable angle that makes a pain throb up your spine. The air begins to feel warm and damp, and a strange smell stings your nostrils; almost acidic, with the metallic undertones of rotting flesh."
    u "You swallow down  the urge to gag, and wiggle out onto the flat floor. You bend your knees to pull your legs free, swinging them around to–"
    u "You jolt, adrenaline flooding through every part of your body as your legs dangle into open air. A scream is pushed down as you realize the thing you thought was floor was actually a narrow ledge, barely foot wide before it drops off into gaping nothingness."
    scene bg cave
    u "You’d reached a pit, yawning in front of you like a horrid black void."
    if Mimic == 1:
        u "Rey was nowhere to be seen."
    menu:
        "You need to get away from the edge.":
            jump StomachA
        "You need to look for a way forward.":
            jump StomachB
label StomachA:
    scene bg cave
    u "You precariously shuffle away from the edge, but there isn’t anywhere to go, short of backtracking through the tight passage you just came through."
    menu:
        "You decide to go back.":
            jump Backtrack
        "You don't want to go back through that awful passage. Looks like you're working with what you got.":
            jump StomachB
label StomachB:
    scene bg cave
    u "You idle on the edge, looking around. Apart from the ledge you’re sitting on, there’s nothing else protruding from the curved walls, and no other opening that you can see."
    u "The smell of rancid meat is almost overpowering, and you cover your mouth with one hand, eyes water."
    u "The movement causes a wayward rock to skitter off the ledge and into the pit, and you hold your breath to see if you can hear when it lands."
    u "..."
    u "Seconds pass. You don’t hear the rock land, but you do hear something else. It sounds like…voices?"
    if Mimic == 1: 
        u "Had Rey fallen down there? Was she hurt?"
    menu:
        "You decide to go back.":
            jump Backtrack
        "You stay for a moment longer":
            jump StomachB2
label StomachB2:
    scene bg cave
    u "You lean in closer. Yes, voices. They weren’t saying words, but muted groans and stuttering gasps."
    if Mimic == 1: 
        u "It didn't sound like Rey, but..."
    if Mimic == 0:
        menu:
            "You decide to go back.":
                pass
            "You call out. 'Hello? Is someone down there?'":
                jump StomachB22
    if Mimic == True:
        menu:
            "You decide to go back.":
                pass
            "You call out. 'Hello? Is someone down there?' 'Rey? Are you down there?'":
                jump StomachB22
label StomachB22:
    scene bg cave
    u "Your words are swallowed up in the heavy moist air. You’re beginning to sweat due to the smothering warmth of the chamber. Your hands are slick as they grip the ledge beneath you and you lean forward more. “Hello–is anyone down th–"
    u "Your hands slip on the stone ledge, and your balance is lost. A scream tears loose from your throat as you fall into the pit, your phone flashlight sliding from your hand." with sshake
    u "..."
    scene bg blacksquare with fade
    jump StomachB22B
label StomachB22B:
    scene bg blacksquare
    u "You aren’t sure how long you’ve been falling, but you expect to be dead when you hit the ground, anticipating hard stones or stalagmites that will spear you through."
    play sound  "Bones and flesh.ogg"
    u "Instead, you land on something that squelches loudly when your body makes contact with it."
    u "Your phone flashlight has gone out, lost somewhere out of reach."
    u "In the dark, you hear the sound of something bubbling, and realize you’re sitting in warm standing liquid. Your whole body is tingling."
    u "Your breathing escalates."
    u "A noie comes from your left and you jump. it's a voice, weak and gasping."
    stranger "H-help me…"
    if Mimic == 1:
        u "This definitely wasn't Rey. Where had she gone?"
    u "You tentatively reach out, and feel the rough fabric of a backpack and what seems like metal carabiners and a length of rope. A cave diver?"
    mc "Hello? Who are you? How long have you been down here?"
    stranger "Help…help…please…"
    mc "Are you hurt?"
    u "The tingling on your skin is getting worse. You continue to fumble in the dark, and the next thing you touch is something smooth and long, its base covered in spongy material."
    u "The cave diver groans. It almost feels like a chicken drumstick in its shape, and you laugh at the incredulity of it. "
    mc "What's this?"
    stranger "...t-the liquid ...my leg..."
    mc "Your {i}leg?{/i}" 
    u "You feel over the smooth part again. It’s too hard to be flesh. Feeling more reveals that it curves slightly, almost like–"
    u "-like a bone.{fast}"
    u "Despite the warm liquid around you, your blood runs cold. Your hand touches the spongy part again, feeling loose flaps of–"
    u "The smell of rotting meat is stronger down here."
    u "You suck in a breath. No. No. No."
    u "Your hand smells metallic."
    stranger "The liquid…"
    u "The diver groans again."
    u "The tingling is beginning to burn against your skin. No. No. No."
    u "You jump to your feet, the liquid sloshing around you." with sshake
    u "It comes up to just below your knees, {nw}"
    play sound "Footsteps-Squishy-V2.ogg"
    u "It comes up to just below your knees, {fast}and you awkwardly run until your hands smack up against a wall that feels springy and wet."
    u "You feel for a handhold, a dip, anything you could grab to climb up."
    u "There’s nothing."
    u "No. No. No."
    u "The burning is getting worse.  How did you get into this position? You should’ve turned back while you could. You should’ve never come to this cave in the first place. You begin to cry."
    return 

label Backtrack:
    scene bg cave
    u "You backtrack through the passage, keeping your breathing as steady as you can. But you must’ve taken a wrong turn somewhere because the cavern you suddenly find at the end of the tunnel isn’t the same one you came in through."
    u "You hear a rustle and tense."
    mc "Is someone there?"
    jump SafeZone


label SafeZone:
    scene bg cave
    mc "Hello? Where-"
    show Rey_N_Nervous at right
    show Robbie_N_Default at left
    rey "Claire!!! Oh my god you made it! Where were you?! We were all waiting here and I was worried sick and we didn’t know if you got lost or-"
    hide Rey_N_Nervous
    show Rey_N_Default at right
    mc "Hey, hey I’m okay! Is everyone here?"
    robbie "It’s just me and Rey right now, Chance is still out exploring."
    if Mimic == 1:
        mc "Wait… Rey? I thought you were…"
        rey "Hm? Thought I was what?"
        mc "You were ahead of me- and you were acting all weird and stuff and-"
        hide Rey_N_Default
        show Rey_N_Nervous at right
        u "Rey looks confused, and shakes her head at you while looking concerned."
        rey "Claire I’ve been here for a while, Robbie can attest to that."
        u "You mention everything you saw with Rey in the other room, and at the mention of the bloodied hands, Rey raises hers. Clean, other than a few scrapes."
        rey "Look, I’m all good."
        mc "Who...or what, did I follow then, I–"
        u "Your friends stand around awkwardly, a bit of tension in the air as all of you try to understand what happened, before moving on."
    mc "How did you guys get here? This cave is so weird, I was worried I wouldn’t be able to find you all."
    hide Rey_N_Nervous 
    show Rey_N_Smile at right 
    rey "Mm, I definitely got lost for a while… and I was hearing all these weird noises, but eventually I ran into Robbie! Definitely a sight for sore eyes!"
    mc "How about you, Robbie? How was your solo adventure?"
    hide Robbie_N_Default
    show Robbie_N_Awkward at left 
    u "Robbie's face goes white."
    robbie "Oh uh- hah I-"
    mc "...are you okay?"
    robbie "So funny story… I uh, thought I had {i}already{/i} ran into you guys. I ran into Claire- or someone I thought was Claire, but you–I mean, {i}she{/i}, was acting REALLY weird. She never laughed? Or breathed, I think?"
    hide Rey_N_Smile
    show Rey_N_Nervous at right 
    mc "Robbie…this is the first time I’ve seen you since we separated to explore."
    robbie "Then who the hell was {i}that{/i}?? She looked almost identical to you! I heard the rest of you guys nearby, talking and laughing and–and I thought I was safe, I thought we were all okay, but she just kept {i}looking{/i} at me and-"
    mc "You’re okay, alright? We’re all here and we’re all ourselves. Normal."
    robbie "Ok, yeah. Yeah! We’re all good, sorry about that."
    rey "We’re all okay, calm down. I think this cave is just–messing with us."
    mc "Yeah, we need to get out of here, and soon. This place isn’t safe to be in, and I don’t wanna think about what could happen if we stay any longer. Something weird is going on."
    robbie "What makes you think that? The flesh walls? The fake voices? The fake {i}people{/i} or–or {i}whatever{/i} they are?"
    mc "All of the above. This place is some horror movie shit."
    mc "We can question what the hell is happening later, but for now, let’s just find Chance and figure out how to get out of here."
    $Mimic = 0
    u "[[To be continued...]]"
    return



