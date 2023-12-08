#GAMING!!!!
#this is a fade for the timer bar!
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0

transform m:
    xpos 0.3
    ypos 0.2

transform l:
    xpos 0
    ypos 0.2

transform r:
    xpos 0.66
    ypos 0.2

transform t:
    xpos 0.2
    ypos 0.03
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
default HeartTrashed = 0
default facestrash = 0
default chanceroom = 0
default Mimic = 0
default trashcounter = 0
default QuestionChance = 0
default chosen_menu_choices = []
default goleft = 0
default goright = 0
default gomid = 0
default SepLungsVar = 0
default SepHeartVar = 0
default SepPartyRoomVar = 0
default callout = 0
default SepStayVar = 0
default bottle = 0
default corkscrewstom = 0
default notreyvar = 0


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

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

define thought = Character("", what_italic=True)
define thoughtnoi = Character("")
define claire = Character("Claire", color="#005BFF")
define rey = Character("Rey", color="#FFEC24")
define notrey = Character("Rey?", color="#FFEC24")
define robbie = Character("Robbie", color="#EA9807")
define notrobbie = Character("Robbie?", color="#EA9807")
define stranger = Character("Stranger")
define chance = Character("Chance", color="#EA2F07")
define notchance = Character("Chance?", color="#EA2F07")

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
image Robbie_M_Default = "Robbie_M_Default.png"
image Robbie_M_Smile = "Robbie_M_Happy.png"
image Chance_N_Default = "Chance_N_Default.png"
image Chance_N_Scared = "Chance_N_Scared.png"
image Chance_N_Question = "Chance_N_Question.png"
image Chance_N_Happy = "Chance_N_Happy.png"
image Chance_N_Guilt = "Chance_N_Guilt.png"
image Chance_N_Nervous = "Chance_N_Nervous.png"
image Chance_M_Default = "Chance_M_Default.png"
image Chance_M_Happy = "Chance_M_Happy.png"
image Chance_M_Scared = "Chance_M_Scared.png"
image bg splashscreen = "splashscreen.png"
image cave = "bg cave.png"
image cavemap = "hellmouthmap.png"
image reydied = "reyDied.png"
image chancedied = "chanceDied.png"
image robbiedied = "robbieDied.png"
image everybodydied = "everybodyDied.png"
image nobodydied = "nobodyDied.png"
image reyandchance = "reyAndChance.png"
image reyandrobbie = "reyAndRobbie.png"
image robbieandchance = "robbieAndChance.png"

###----------------THE GAME STARTS HERE----------------###
label start:
    jump Welcome

#Intro Screen
label Welcome:
    scene bg blacksquare with fade
    thought "Welcome to Hellmouth Caves."
    thought "This game is designed to emulate the HellHole caves on the UCSC campus–with a little bit of a twist."
    thought "You’ll be playing as {i}Claire{/i}, a college student that has dared to enter the cave with her group of friends."
    thought "If at any point you feel lost, confused, or unsure about how to proceed, the best advice is (just as in real cave exploration); take a moment and observe your surroundings, or in this case, what the story is trying to tell you."
    thought "Best of luck in your exploration."
    thought "You’ll need it."
    jump ContentWarning

label ContentWarning:
    thought "Content Warning: This game features graphic depictions of body horror and claustrophobia that may not be agreeable for some viewers. Proceed Appropriately."
    jump Mouth

label Mouth:
    scene bg blacksquare with fade
    play sound "echofootsteps.ogg" volume 0.4
    play music "footstepsreverb.ogg" loop volume 0.8
    claire "Hey, who brought the flashlight?"
    robbie "Oooh, is someone scared of the dark?"
    claire "I just can’t see anything."
    window show
    play sound "echofootsteps.ogg" volume 0.4
    rey "Yeah–can someone please turn the light on? I’m getting the creeps from this place already."
    robbie "Chicken."
    stop sound
    rey "Stop screwing around, Robbie. Claire and I have never done anything like this, remember?"
    robbie "Well neither have I! I just heard about this place from friends, it’s not like I'm some cave expert like Chance!"
    claire "Stop arguing, guys. We’re barely into the cave!"
    stop music
    chance "Bro, just turn on the lights for them. This is supposed to be fun."
    robbie "Okay okay, here."
    scene bg cave with Dissolve(3.0)
    play music "caveroomtone1.ogg" volume (0.8)
    show Rey_N_Default at r with dissolve
    show Robbie_N_Default at l with dissolve
    show Chance_N_Default at m with dissolve
    thought "Someone  turns on a flashlight, revealing the space around you. The cavern is tight, but the four of you have managed to squeeze inside."
    thought "Below your feet is a small tunnel, about the width of a manhole, leading into the depths of the cave."
    hide Robbie_N_Default
    show Robbie_N_Cheeky at l, bounce
    robbie "Welcome! To Hellmouth Caves."
    show Rey_N_Default at r, bounce
    rey "..."
    claire "..."
    show Chance_N_Default at m, bounce
    chance "..."
    hide Robbie_N_Cheeky
    show Robbie_N_Default at l, bounce
    robbie "Okay, I was expecting a bigger reaction to that. Come on guys, it’s an adventure! One last hurrah before graduation with the ol’ gang!"
    hide Rey_N_Default
    show Rey_N_Question at r, bounce
    rey "You’re so dramatic."
    hide Rey_N_Question
    show Rey_N_Smile at r
    claire "You thought cave spelunking would be a good bonding experience??"
    show Robbie_N_Default at l, bounce
    robbie "C’mon Bro, back me up!"
    show Chance_N_Default at m, bounce
    chance "Hey, I’m for it. I like a little challenge."
    show Robbie_N_Default at l, bounce
    robbie "That’s the spirit! Come on Claire, get on board! And Rey, don’t look so nervous. Here, I brought a map and everything."
    show cavemap at t with dissolve
    robbie "It’s decently accurate."
    hide Rey_N_Smile
    show Rey_N_Nervous at r, bounce
    rey "Decently?"
    show Robbie_N_Default at l, bounce
    robbie "Well come on, would that guy downtown really sell me a defective map? Like, who even does that?"
    thought "Robbie looks down at the map he’s holding and squints, before turning it on its side and staring at it."
    show Robbie_N_Default at l, bounce
    robbie "…It’s probably fine."
    claire "Oh god, what sort of shitshow did we sign up for?"
    hide Rey_N_Nervous
    show Rey_N_Default at r
    hide cavemap with dissolve
    show Chance_N_Default at m, bounce
    chance "We should be fine guys, and anyway, we probably won’t even need a map! You guys have got me, and I’ve tackled more difficult caves in my sleep!"
    show Robbie_N_Default at l, bounce
    robbie "Uh huh. Yeah I’m still using the map."
    show Rey_N_Default at r, bounce
    rey "Well, I hope at least one of you knows their way around, cuz Claire and I don’t have a clue…"
    claire "You can say that again, I don’t know how easy it’ll be to navigate in those tight tunnels. I really wouldn’t be doing this if it wasn’t for you guys."
    show Rey_N_Default at r, bounce
    rey "Hey… if you want we could head back? Maybe try for another time-"
    show Robbie_N_Default at l, bounce
    robbie "No way!! This is the one day we have the time to do this,, c’mon I promise it’ll be fun!"
    hide Rey_N_Default
    show Rey_N_Speechless at r, bounce
    rey "Robbie! If Claire's not up to it we shouldn't force her to do this"
    hide Robbie_N_Default
    show Robbie_N_Awkward at l, bounce
    robbie "Right, right, sorry my bad."
    claire "Thanks Rey, but I should be fine. I’ve got you and the boys here, it’ll be fun, I promise!"
    hide Robbie_N_Awkward
    show Robbie_N_Default at l
    show Chance_N_Default at m, bounce
    chance "Yeah! As long as you all stick by me, everything will be perfect."
    thought "As Chance says this, he looks over at Rey and, very obviously, winks at her. She turns to look away, a small blush spreading across her cheeks."
    hide Robbie_N_Default at l
    show Robbie_N_Cheeky at l, bounce
    robbie "C’mon! I can’t keep waiting like this, I wanna see what all’s in there!"
    hide Robbie_N_Cheeky with dissolve
    thought "Robbie folds up the map, and starts climbing down the tunnel at your feet. Even as his head dips below the tunnel entrance, you can hear him laughing and shouting up at the group."
    rey "Ah- Robbie! Wait for us! You have the map you idiot!"
    claire "Rey, make sure he doesn’t fall down into a bottomless pit, would you?"
    hide Rey_N_Speechless with dissolve
    thought "Rey smiles and nods, before climbing down after him, leaving you and Chance lagging behind."
    jump Trash

label Trash:
    thought "As you prepare to descend into the hole, Something glints in the light of your phone flashlight. You squint, and in the corner of the tight space, right by Chance’s foot, is a glass beer bottle."
    show Chance_N_Default at m, bounce
    chance "Okay, Rey and Robbie are up ahead, just waiting on you now Claire."
    thought "The sight of trash here makes you cringe a bit. Is it such a hassle for people to pick up after themselves?"
    menu:
        "Pick up the trash":
            play sound "pickupsoundv2.ogg"
            $trashcounter += 1
            jump TrashA
        "Leave it be":
            jump Throat
label TrashA:
    #SHOW CHANCE TEASING
    show Chance_N_Default at m, bounce
    chance "Pff, {i}really{/i}? Wow Claire, I didn’t know you’re suddenly an eco warrior now."
    claire "Come on, it’s not weird to treat nature with respect and stuff."
    show Chance_N_Default at m, bounce
    chance "Ok, whatever you say Captain Planet."
    show Chance_N_Default at m, bounce
    chance "Just hurry up alright?"
    scene bg blacksquare with fade
    jump Throat

label Throat:
    play music "caveroomtone1.ogg" loop if_changed volume 0.2
    if trashcounter < 1:
        scene bg blacksquare with fade
        thought "You tear your gaze away from the litter, and drop down into the manhole after Rey."
    thought "The tunnel extends into a deep downward slope, which doesn’t make it easy to progress through."
    scene bg tightsqueeze with fade
    thought "Above you, Chance is holding his flashlight with his mouth, and the unsteady light illuminates the tight crevice."
    thought "You’re able to shove your toe  into a ledge for a bit of leverage as you descend. Chance begins to descend too, and steps on your hand more than once."
    thought "Below you, Rey is in a similar position, arms and legs spread like a starfish to stay wedged in place. And below her is Robbie, casually leading the way."
    thought "His reassured voice echoes throughout the cavern, giving words of advice as his body naturally navigates through the squeeze. "
    scene bg cavealt with dissolve
    show Robbie_N_Default at r with dissolve
    show Rey_N_Default at m with dissolve
    show Chance_N_Default at l with dissolve
    thought "Eventually, you begin to see your friends turn and pull their way out of the climb. As you step out, you see Robbie staring at the map."
    show Rey_N_Default at m
    claire "Everyone good? Why are we all just standing around?"
    show Rey_N_Default at m, bounce
    rey "We’re at a fork in the road. Or, cave, I guess."
    hide Robbie_N_Default
    show Robbie_N_Cheeky at r, bounce
    robbie "Also a fork is normally when it splits into two, and this one has three paths."
    hide Rey_N_Default
    show Rey_N_Speechless at m, bounce
    hide Robbie_N_Cheeky at r
    show Robbie_N_Default at r
    rey "...dude shut up."
    hide Chance_N_Default
    show Chance_N_Question at l, bounce
    chance "What does the map say, Rob?"
    hide Rey_N_Speechless
    show Rey_N_Default at m
    hide Robbie_N_Default
    show Robbie_N_Question at r, bounce
    robbie "Let me look..."
    thought "As he checks the map, you take a moment to sneak a glance for yourself."
    show cavemap at t with dissolve
    thought "None of the paths seem particularly different from each other, but when the room falls silent you’re able to pick up on a few faint details."
    hide cavemap with dissolve
    hide Robbie_N_Question
    show Robbie_N_Default at r
    hide Chance_N_Question
    show Chance_N_Default at l
    show Rey_N_Default at m, bounce
    rey "The way forward looks pretty normal? Let’s take that."
    hide Chance_N_Default
    show Chance_N_Happy at l, bounce
    chance "Really? It looks so boring, the left and right paths seem more mysterious!"
    hide Robbie_N_Default
    show Robbie_N_Question at r, bounce
    robbie "Mm, they seem cool, but the middle one has tons of graffiti and junk on it. It could be like a secret party room or something!"
    claire "Hmm… Anything on the map, Robbie?"
    hide Chance_N_Happy
    show Chance_N_Default at l
    hide Robbie_N_Question
    show Robbie_N_Default at r, bounce
    robbie "Nah, no matter which path we take, they all go on for a while. I don’t know if we’d be able to explore all of these together…"
    show Chance_N_Default at l, bounce
    chance "What if we split up? We could check each one ourselves, and that way it would be more of a challenge!"
    hide Rey_N_Default
    show Rey_N_Speechless at m, bounce
    rey "You need {i}more{/i} of a challenge? Really?"
    hide Chance_N_Default
    show Chance_N_Happy at l, bounce
    chance "C'mon, it would be fun!"
    hide Robbie_N_Default
    show Robbie_N_Cheeky at r, bounce
    robbie "It would be fun..."
    show Rey_N_Speechless at m, bounce
    rey "No! What if we get lost or something?"
    hide Robbie_N_Cheeky
    show Robbie_N_Default at r, bounce
    robbie "If these two just go back and forth I think we'll stay here forever. Claire, what do you think?"
    hide Chance_N_Happy
    show Chance_N_Default at l
    menu:
        "Choose to stay together.":
            jump StayTogether
        "Choose to separate.":
            jump Separate

label StayTogether:
    hide Rey_N_Speechless
    show Rey_N_Default at m
    claire "I think it's best if we stay together."
    chance "Fine, but which way should we go?"
    jump Paths

label GoBackExplore:
    hide Rey_N_Speechless
    hide Robbie_N_Awkward
    hide Chance_N_Nervous
    scene bg cavealt with dissolve
    thought "You find yourself back at the crossroads from before."
    thought "You look down the three branching tunnels, wondering where to go next."
    jump Paths

label Paths:
    if goleft == 0:
        if goright == 0:
            if gomid == 0:
                    thought "To the left, a faint wind sends a chill down your spine. You know some caverns have wind tunnels in them. It could be worth exploring."
                    thought "To the right, you feel a strange sort of hum vibrate the bottom of your feet. It reverberates off the walls with a subtle noise. How curious–what could that be?"
                    thought "Straight ahead is the largest opening, an entrance wide enough to walk into without a necessity to squeeze."
                    menu:
                        "Left, toward the sound.":
                            jump StayTogetherLeft
                        "Right, toward the vibration.":
                            jump StayTogetherRight
                        "Straight ahead, toward the large tunnel entrance.":
                            jump StayTogetherMid
    if goleft == 1:
        if goright == 0:
            if gomid == 0:
                    thought "To the right, you feel a strange sort of hum vibrate the bottom of your feet. It reverberates off the walls with a subtle noise. How curious–what could that be?"
                    thought "Straight ahead is the largest opening, an entrance wide enough to walk into without a necessity to squeeze."
                    menu:
                        "Right, toward the vibration.":
                            jump StayTogetherRight
                        "Straight ahead, toward the large tunnel entrance.":
                            jump StayTogetherMid
    if goleft == 1:
        if goright == 0:
            if gomid == 1:
                    thought "To the right, you feel a strange sort of hum vibrate the bottom of your feet. It reverberates off the walls with a subtle noise. How curious–what could that be?"
                    menu:
                        "Right, toward the vibration.":
                            jump StayTogetherRight
    if goleft == 1:
        if goright == 1:
            if gomid == 0:
                    thought "Straight ahead is the largest opening, an entrance wide enough to walk into without a necessity to squeeze."
                    menu:
                        "Straight ahead, toward the large tunnel entrance.":
                            jump StayTogetherMid
    if goleft == 0:
        if goright == 1:
            if gomid == 0:
                    thought "To the left, a faint wind sends a chill down your spine. You know some caverns have wind tunnels in them. It could be worth exploring."
                    thought "Straight ahead is the largest opening, an entrance wide enough to walk into without a necessity to squeeze."
                    menu:
                        "Left, toward the sound.":
                            jump StayTogetherLeft
                        "Straight ahead, toward the large tunnel entrance.":
                            jump StayTogetherMid
    if goleft == 0:
        if goright == 1:
            if gomid == 1:
                    thought "To the left, a faint wind sends a chill down your spine. You know some caverns have wind tunnels in them. It could be worth exploring."
                    menu:
                        "Left, toward the sound.":
                            jump StayTogetherLeft
    if goleft == 0:
        if goright == 0:
            if gomid == 1:
                    thought "To the left, a faint wind sends a chill down your spine. You know some caverns have wind tunnels in them. It could be worth exploring."
                    thought "To the right, you feel a strange sort of hum vibrate the bottom of your feet. It reverberates off the walls with a subtle noise. How curious–what could that be?"
                    menu:
                        "Left, toward the sound.":
                            jump StayTogetherLeft
                        "Right, toward the vibration.":
                            jump StayTogetherRight
    if goleft == 1:
        if goright == 1:
            if gomid == 1:
                thought "The unsettling feeling of this isolation begins to settle in, and you realize it’s probably time to meet up with the others, anyway."
                menu:
                    "You turn and start to make your way back to the rendezvous point.":
                        jump RendezvousPoint
label StayTogetherLeft:
    $goleft += 1
    claire "I wonder where all that wind is coming from."
    hide Rey_N_Default
    show Rey_N_Smile at m
    rey "Me too! I definitely don't mind cooling off a bit, hehe."
    scene bg blacksquare with fade
    jump Lungs
label StayTogetherRight:
    $goright += 1
    play sound "mediumheartbeat.ogg" volume 0.25 loop
    claire "What's with the vibrations from over there?"
    hide Chance_N_Default
    show Chance_N_Happy at l
    chance "I don't know! Let's check it out."
    scene bg blacksquare with fade
    jump Heart
label StayTogetherMid:
    $gomid += 1
    claire "How about just going straight ahead?"
    hide Robbie_N_Default
    show Robbie_N_Awkward at r
    robbie "Not having to squeeze into one of the others sounds good, yeah."
    scene bg blacksquare with fade
    jump PartyRoom

label RendezvousPoint:
    thought "You finally make it back to the rendezvous point."
    thought "An empty, silent cavern greets you. Where were the others?"
    thought "You cast your flashlight beam around the space, but see nothing except stone walls and stalagmites."
    thought "Shifting uneasily, you bite your lip. This whole thing just isn’t sitting right with you."
    thought "Something about this cave leaves you feeling unsettled , in more ways than one."
    thought "Maybe it was time to get the hell out of this place."

    menu:
        "Leave the Cave":
            jump LeaveCave

label LeaveCave:
    thought "You can’t take this place anymore."
    thought "You turn to make your way back through the passages and rooms, ignoring the jab of guilt at leaving your friends behind in the cave."
    thought "They should be fine–they were probably all together somewhere down there."
    thought "Sooner or later they would reach the same conclusion you did and leave."
    thought "You climb until you see the faint rays of daylight from the mouth of the cave."
    jump ENDING4

label ENDING4:
    # Ending Screen: Show outside cave entrance, no sprites.
    scene bg cavetitlescreen
    thought "Claire is separated from Robbie, Rey and Chance within Hellmouth caves. Spooked by the strange atmosphere of the caves, Claire leaves by herself."
    thought "What happens to Robbie, Rey and Chance is unknown."
    return


label Lungs:
    scene bg tightsqueezeflip with fade
    stop music
    play sound "deepwindv2.ogg" volume 0.3 fadein 1.0 fadeout 0.5
    thought "You turn sideways to shuffle through the narrow passageway. The wind from the other side is cold, leaving goosebumps wherever it can find bare skin."
    thought "It lightly pushes against you and your friends but gets stronger as you get closer ."
    thought "Occasionally it eases up, but is replaced by a gust of wind from behind."
    thought "You don’t remember there being wind from the previous room, though maybe you just weren’t paying enough attention to realize it was there."
    queue sound "deepwindv2.ogg" fadein 0.5 loop
    thought "Upon entering the vast space, you try to call out to your friends and ensure everyone is accounted for. You find yourself yelling through the deafening wind."
    scene bg cavealt with fade
    show Rey_N_Nervous at l
    show Robbie_N_Awkward at m
    show Chance_N_Nervous at r
    rey "OKAY…THIS IS REALLY, REALLY WINDY! WHAT’S UP WITH THIS?"
    chance "I DON’T KNOW, IT’S PROBABLY CONNECTED TO THE SURFACE, OR SOMETHING!"
    claire "REALLY?? THIS FAR DOWN?"
    stop sound fadeout 1.0
    thought "For a brief moment, the wind slows down, and the sound is replaced by the air current rapidly traversing through the passageway your group once came through."
    play sound "deepwindv1.ogg" volume 0.6
    thought "You take a breath to say something within this moment of clarity, but it is short-lived as the rapid winds start up again."
    menu:
        "Look around the room.":
            jump LungsTrash
        "Go back and explore.":
            jump GoBackExplore
label LungsTrash:
    play sound "deepwindv2.ogg" volume 1.0 loop
    thought "You look around the room, trying to ignore the deafening winds."
    stop sound
    thought "As you continue to look, it once again stops."
    play sound "deepwindv2.ogg" volume 1.0 loop
    thought "Then starts."
    stop sound
    thought "Then stops."
    play sound "deepwindv2.ogg" volume 1.0 loop
    thought "Then starts."
    stop sound
    thought "It’s almost rhythmic how the wind moves in and out of the space, perfectly timed."
    thought "..."
    thought "A cigarette butt is wedged nearby in a rock"
    menu:
        "Pick up the trash.":
            $trashcounter += 1
            play sound "pickupsoundv2.ogg"
            thought "You pick it up. Yuck"
            menu:
                "Go back and explore.":
                    jump GoBackExplore
        "Leave it be.":
            thought "You leave it."
            menu:
                "Go back and explore.":
                    jump GoBackExplore

label PartyRoom:
    hide Rey_N_Smile
    hide Robbie_N_Awkward
    hide Chance_N_Default
    scene bg blacksquare with fade
    play sound "clothingshufflev3.ogg" volume 0.2
    play voice "rockscrapingv1.ogg" volume 0.5
    thought "You turn sideways to shuffle through the narrow passageway, feeling the rock cling to your back."
    stop sound
    stop voice
    play sound "rocksfallingv2.ogg"
    play voice "footstepsreverb.ogg"
    thought "The sound of your friend’s footsteps fills up the space alongside the falling pebbles that come off the walls as your bodies inch through the passageway."
    scene bg partyroom with dissolve
    thought "The space widens as you enter this new room with a ceiling high enough to stand upright."
    thought "Thank God–you aren’t necessarily claustrophobic, but that narrow passage you came through questioned how much of a squeeze you can truly handle."
    thought "From the light of your phone, you see graffiti spray painted on the stone walls."
    thought "Some are tags from people who have been here, messily scribbled on with Sharpie markers. Others are larger, spray-painted phrases such as “Do not enter” and “Funky”."
    thought "Upon looking down, you see a small handwritten note “Do not continue. It’s alive.”"
    show Rey_N_Default at l with dissolve
    show Chance_N_Default at r with dissolve
    show Robbie_N_Cheeky at m with dissolve
    show Robbie_N_Cheeky at m, bounce
    robbie "Oh hell yeah! Finally some signs of life in here!"
    hide Rey_N_Default
    show Rey_N_Guilt at l, bounce
    rey "Ooh, have other students been down here?"
    chance "Hmm, it looks like it yeah."
    robbie "Man, I’ve seen some weird messages, but I think these take the cake. Like, “OOoOoOoh, the cAvE is aLiVe ooOoOh!!”, come on!"
    hide Chance_N_Default
    show Chance_N_Happy at r
    chance "I know, like what idiot would believe that? If they’re trying to scare us, do something about a serial killer or something!"
    hide Rey_N_Guilt
    show Rey_N_Question at l
    thought "Rey clearly looks nervous and skittish, but the jokes from the boys seem to make her laugh, at least a little."
    hide Robbie_N_Cheeky
    show Robbie_N_Default at m
    rey "Uh... yeah, haha.."
    claire "Hmm, I might look around, maybe the people before us left something behind."
    hide Rey_N_Question
    hide Chance_N_Happy
    show Chance_N_Default at r
    show Rey_N_Default at l, bounce
    rey "Mhm! Don't go too far!"
    menu:
        "Look around the room.":
            jump PartyRoomTrash
        "Go Back.":
            jump Flashlight
label PartyRoomTrash:
    scene bg partyroom
    thought "You spy a flattened ramen cup, muddied on the ground."
    menu:
        "Pick up the trash.":
            $trashcounter += 1
            jump Flashlight
        "Leave it be.":
            jump Flashlight
label Flashlight:
    thought "You walk back over to where Rey, Robbie, and Chance are clustered."
    chance "Find anything interesting?"
    claire "Not really, no."
    hide Rey_N_Default
    show Rey_N_Nervous at l, bounce
    rey "I still don’t really know what’s up with this place. Is the graffiti just from pranksters, or…"
    hide Robbie_N_Default
    show Robbie_N_Cheeky at m, bounce
    robbie "It’s probably from dead hikers, doomed to forever haunt these caverns! OooOooOohh!"
    hide Rey_N_Nervous
    show Rey_N_Speechless at l, bounce
    rey "Shut up!!!"
    hide Chance_N_Default
    show Chance_N_Nervous at r, bounce
    chance "Come on, don't pull this bro."
    robbie "Oh no! What's happening? I-i think the lights aren't working!"
    thought "Robbie turns off his flashlight, plunging the room into darkness. Immediately, Rey screams, and he starts laughing to the point of tears."
    scene bg blacksquare
    hide Rey_N_Speechless
    hide Chance_N_Nervous
    hide Robbie_N_Cheeky
    rey "Robbie! Turn the lights on right now! You fucking {i}idiot!{/i}"
    robbie "Ok but you have to admit it's funny! Right? Chance? Claire?"
    menu:
        "Insist the flashlight is turned back on.":
            jump TurnItOn
        "Play along with the joke.":
            jump PlayAlong
label TurnItOn:
    claire "Come on, dude. Don't make this scarier then it needs to be."
    rey "Ugh fine, fine. Didn't realize I was with a bunch of buzzkills."
    show Rey_N_Guilt at l with dissolve
    show Robbie_N_Guilt at m with dissolve
    show Chance_N_Question at r with dissolve
    scene bg partyroom with dissolve
    thought "The light comes back on, and all your friends' faces are illuminated in the pale glow."
    hide Rey_N_Guilt
    show Rey_N_Speechless at l
    rey "Enough with the games, guys."
    hide Robbie_N_Guilt
    show Robbie_N_Cheeky at m
    robbie "What was that? Bwak.... bwak bwak bwaaaakk?"
    claire "Are those supposed to be chicken noises?"
    hide Rey_N_Speechless
    show Rey_N_Nervous at l
    rey "Look, I’m fine with exploring, but no one said we have to do it in the dark."
    hide Chance_N_Question
    show Chance_N_Default at r
    chance "Aw come on Rey, it was just a little joke."
    rey "..."
    claire "....okay, come on. Let's keep exploring."
    jump GoBack2
label GoBack2:
    scene bg cavealt with dissolve
    show Rey_N_Default at m
    show Chance_N_Default at r
    show Robbie_N_Default at l
    thought "You find yourself back at the crossroads from before."
    robbie "So, where to next?"
    jump Paths
label PlayAlong:
    scene bg blacksquare
    claire "Oh noOoOo! I can’t see anything! I think our flashlights died!"
    rey "Not you too Claire! Guys, come on, please?"
    robbie "It’s so dark… something could be lurking here, and we wouldn’t even know! Something… like… a… GHOST!"
    thought "You and Robbie both laugh, as Rey yells at you two, and Chance stays quiet."
    thought "After a pause, Robbie turns on the flashlight, the light illuminating on everyone except an absent Chance."
    scene bg partyroom
    show Robbie_N_Cheeky at l
    show Rey_N_Speechless at r
    rey "Ugh, you guys suck! I expected that from Robbie, but I can’t believe you went with that Claire!"
    claire "Uh..."
    rey " And to do shit like this in a cave, where you already know I’m scared, it’s so frustrating!"
    hide Robbie_N_Cheeky
    show Robbie_N_Question at l
    robbie "Hey, where's Chance?"
    hide Rey_N_Speechless
    show Rey_N_Nervous at r
    rey "And I- oh. Wait what?"
    robbie "I don't see him here. Maybe he's hiding?"
    thought "You frown. Chance did like to join Robbie’s pranks; maybe he ran off as a joke? But you didn’t hear any footsteps or anything."
label PlayAlong2:
    thought "You open your mouth to sug{nw}"
    play sound "guyscream.ogg"
    thought "You open your mouth to sug{fast}gest-"
    hide Robbie_N_Question
    show Robbie_N_Awkward at l
    thought "All of you freeze."
    rey "That-that sounded like....Chance."
    hide Robbie_N_Awkward
    show Robbie_N_Question at l
    robbie "Relax, relax. I'm sure he just wants to spook us."
    claire "Chance? Are you there?"
    claire "Chance this isn't funny!"
    robbie "He's- he's fine, he's probably just back at the start, waiting for us!"
    rey "Yeah! Yeah that's probably it!"
    scene bg blacksquare with dissolve
    scene bg partyroomempty with dissolve
    show Robbie_N_Awkward at l with dissolve
    show Rey_N_Nervous at r with dissolve
    thought "The rendezvous point isn’t  far from the room you are in. A short walk later, and you’re back at the check-in spot."
    thought "Still no Chance. The three of you wait in silence for a few minutes."
    thought "Every distant echo in the cave makes you hold your breath. But Chance never appears."
    claire "Wherever he is, I don't think he's around here."
    rey "God, do we need to go get help? Maybe we should leave and come back?"
    robbie "No no, I don't think it's that serious! He's probably fine, just adventuring away deeper in the cave."
    rey "Claire, what do you think?"
    menu:
        "Leave the cave and go seek help.":
            jump PlayAlongA
        "Stay in the cave and look for Chance.":
            hide Rey_N_Nervous
            hide Robbie_N_Awkward
            jump PlayAlongB
label PlayAlongA:
    claire "We clearly don't know this cave that well. If he really is missing, we need professional help."
    hide Rey_N_Nervous
    show Rey_N_Nervous at r
    show Robbie_N_Question at l
    rey "No I agree. Chance was the most experienced out of all of us, and if he’s lost? Then I don’t know about our odds."
    robbie "We don't even know if he's lost..."
    hide Robbie_N_Question
    show Robbie_N_Speechless at l
    thought "Robbie clearly looks conflicted. Maybe you can convince him to come with you?"
    menu:
        "Try to reason with him.":
            jump Ending1
        "Plead with him to leave.":
            jump Ending2
label Ending1:
    claire "Robbie, I know Chance can handle himself. If we all go down there to find him and just end up getting hurt as a result, then we aren’t making it any easier for him."
    rey "Yeah, we can't hhelp him if we end up needing him to save us."
    thought "The indecision on Robbie’s face causes concern to rise, and you hold your breath for a moment. Then he hesitantly nods."
    hide Robbie_N_Guilt
    show Robbie_N_Question at l
    robbie "Okay, okay. Let’s-uh, let’s go get some help. But if this just turns out to be you guys overreacting, you’ll never live this one down."
    scene bg blacksquare with dissolve
    hide Robbie_N_Question
    hide Rey_N_Default
    thought "Together, you, Rey, and Robbie make your way back to the mouth of the cave."
    scene bg cave
    show Rey_N_Default at l
    show Robbie_N_Default at r
    thought "Your chest loosens a bit when you see daylight pierce down into the darkness, and the breeze glides on your face."
    thought "You boost Rey up first, and as she crawls through the entrance, you cast one last look back into the depths of the cave."
    thought "You see Robbie doing the same, and the two of you share a look before he nudges you with his elbow."
    robbie "Come on. Let's get moving. You said we should go get help, right?"
    thought "You nod, not only to reassure him, but to reassure yourself. You hope Chance is okay, wherever he is."
    jump ending1end
label ending1end:
    show chancedied
    window hide
    pause
    thought "Ending 1 - Chance was lost in the depths of Hellmouth caves. Claire made it out with Rey and Robbie to go seek help."
    return
label Ending2:
    show Robbie_N_Speechless at l
    show Rey_N_Nervous at r
    claire "Robbie, we can’t do this on our own, we need to go and get help!"
    rey "This cave is clearly too much for us, come on, we gotta go! Please, Robbie!"
    hide Robbie_N_Speechless
    show Robbie_N_Question at l
    thought "Robbie raises a brow, looking at both of you. Then he shakes his head."
    hide Robbie_N_Question
    show Robbie_N_Guilt at l
    robbie "Whatever. If you want to be lame and dip, do it. I’m going to keep exploring, and probably find Chance hiding behind a rock or something. Bye."
    thought "Before you could protest,{nw}"
    hide Robbie_N_Guilt
    thought "Before you could protest,{fast} Robbie’s gone, walking further into the cave. You start to follow and try to bring him back, but Rey catches your arm."
    hide Rey_N_Nervous
    show Rey_N_Guilt at r
    rey "Don’t. He’s just being stubborn–chasing after him won’t do anything. Come on, let’s go get help, yeah?"
    thought "You don’t want to leave Robbie behind, but Rey’s right. You should go get help. Worst case scenario, you were overreacting, but better safe than sorry, right?"
    scene bg blacksquare with dissolve
    thought "Together, you and Rey make your way back to the mouth of the cave."
    scene bg cave with dissolve
    show Rey_N_Nervous at r
    thought "Your chest loosens a bit when you see daylight pierce down into the darkness, and you feel the breeze on your face."
    thought "You boost Rey up first, and as she crawls through the entrance, you cast one last look back into the depths of the cave."
    hide Rey_N_Nervous
    thought "You hope Robbie and Chance are okay, wherever they are."
    jump Ending2End
label Ending2End:
    show robbieandchance
    window hide
    pause
    thought "Chance was lost in the depths of Hellmouth caves. Robbie went to go find him. Claire made it out with Rey to go seek help."
    return

label PlayAlongB:
    claire "We can't just leave him down there, let's go find him."
    hide Robbie_N_Question
    show Robbie_N_Default at l with dissolve
    show Rey_N_Question at r with dissolve
    robbie "Yeah, and he’s probably not far anyway! We’ll find him in no time!"
    rey "Okay…I don’t like going further into this, whatever {i}this{/i} is, but let’s go."
    claire "We got this, just stay close, and keep your flashlights on, okay?"
    hide Robbie_N_Default
    hide Rey_N_Question
    jump LookForChance

label Heart:
    scene bg tightsqueeze
    hide Chance_N_Happy
    hide Rey_N_Default
    hide Robbie_N_Default
    thought "You squeeze into the narrow passageway alongside your friends. The walls scratch against whatever bare skin it can find."
    play sound "rockscrapingv2.ogg"
    thought "Breathing in is taxing, as you feel your expanded stomach push against the front wall."
    claire "God, why did this have to be so damn tight!"
    rey "I know…it’s so restrictive…I think I’m already covered in scratches!"
    robbie "You ever…done anything like this…bro?"
    chance "Mm, once or twice… but this is a lot…"
    robbie "I think…there’s an opening up ahead… if the map was right"
    play sound "clothingshufflev2.ogg"
    play voice "clothingshufflev3.ogg"
    queue sound "clothingshufflev3.ogg"
    queue voice "clothingshufflev2.ogg"
    thought "The passage finally begins to widen in front of you, and you draw a breath, inching your way forward. Just keep moving forward."
    thought "Slowly, the walls loosen their grip on you and begin to give way."
    thought "The passage spits you out low to the floor, and you push yourself up on your knees."
    scene bg cave with dissolve
    thought "It’s a small cavern, not the most spacious thing in the world; but compared to what you had just been through, it feels like a penthouse suite."
    play sound "mediumheartbeatv2.ogg" loop
    thought "Your brain pulses against the sides of your skull, feeling the rhythm align with the sound of your heartbeat in your ears."
    stop sound
    play sound "fastheartbeat.ogg" fadein 1.0 loop
    thought "Blood pulsing through your body becomes apparent to you as you feel its pressure in your fingers and toes. The rhythmic beating of your blood, no, your heart, feels external."
    thought "It’s all around you, emanating from the walls. You see it out of the corner of your eye, the rocks organically begin to pulse alongside the rhythm of your exhausted body."
    thought "You turn to take a closer look, but are reassured that is not the case, as you glance at the static wall."
    menu:
        "Calm yourself down.":
            jump HeartA
        "Look closer.":
            jump HeartB
label HeartA:
    thought "You take a deep breath and put a hand on a nearby rock to steady yourself. Immediately you spring back from the contact."
    thought "Instead of touching a rough surface underneath your palm, you are instead greeted with thin protruding lines."
    thought "They’re almost like spiderwebs sticking out from the rocks, but within that brief moment of contact, you could’ve sworn you felt…a pulse? They almost look like… "
    menu:
        "veins.":
            jump HeartA1
        "a weird rock formation.":
            jump HeartA2
label HeartA1:
    thought "You glance down at your own inner arm, the weak light of your flashlight illuminating your skin. The pattern on the rocks match the spindly contours of your veins. You shiver."
    show Robbie_N_Cheeky at l
    show Chance_N_Default at m
    show Rey_N_Default at r
    robbie "Yo, earth to Claire? What's up?"
    claire "N-nothing. Just getting grossed out by this place."
    jump StayOrContinue
label HeartA2:
    thought "You shake your head, dismissing whatever bizarre connection your brain was about to make."
    jump StayOrContinue
label HeartB:
    thought "You squint, convinced your eyes were playing tricks on you. This place had to be playing tricks on you, right?"
    thought "Rocks didn’t move like that. Rocks actually don’t tend to move on their own at all."
    show Robbie_N_Default at l
    show Chance_N_Default at m
    show Rey_N_Question at r
    rey "Hey Claire? Are you alright?"
    claire "Y-yeah. Just getting grossed out by this place."
    jump StayOrContinue

label StayOrContinue:
    if HeartTrashed == 0:
        menu:
            "Stay.":
                jump HeartTrash
            "Continue.":
                thought "There’s a path at the end of the cavern; the opening is small, barely shoulder width. You continue towards it."
                jump UpperIntestines
    else:
        menu:
            "Continue.":
                thought "There’s a path at the end of the cavern; the opening is small, barely shoulder width. You continue towards it."
                jump UpperIntestines

label HeartTrash:
    $HeartTrashed += 1
    thought "You notice a crumpled soda can."
    menu:
        "Pick it up.":
            play sound "pickupsoundv1.ogg"
            thought "You pick up the can; even in a place as unpleasant as this, there shouldn’t be trash laying around. Pollution sucks no matter where it is."
            jump StayOrContinue
        "Leave it.":
            thought "You don’t want to carry around a piece of gross trash; this place was already unpleasant enough."
            jump StayOrContinue

label UpperIntestines:
    scene bg tightsqueezeflip
    thought "You kneel before the small opening and peer inside, seeing that there will be hardly any room to move. Taking a deep breath, you crawl into the tunnel, feeling the walls lock you into the passageway."
    play sound "clothingshufflev2.ogg"
    play music "clothingshufflev3.ogg" loop
    play voice "rocksfallingv2.ogg"
    scene bg blacksquare with dissolve
    thought "Your knees have no room to bend, so you drag your feet across the floor and inch your way across."
    thought "For a moment, you stop to breathe, but feeling the heat of your breath reflecting off the frontal wall only causes panic to rise."
    stop music
    thought "Breathe. You must breathe."
    play sound "heavybreathing.ogg" fadein 1.0 fadeout 2.0
    thought "Being reminded to breathe makes your mind aware of your lung’s inability to work on their own now. You must focus."
    chance "Hey! Guys!"
    claire "What’s up?"
    chance "I think…I can’t fit."
    rey "What?"
    chance "I can’t fit through this part of the tunnel. All those days bulking up have finally paid off, just not in the way I wanted, haha."
    robbie "What should we do?"
    chance "I think I’ll stay here, if y’all want to keep going ahead?"
    rey "..."
    rey "Are you sure?"
    chance "Mhm, and when you’re done, just come back this way and find me, alright?"
    robbie "Bro…"
    claire "Yeah! Got it, Chance. I’ll lead them, and make sure we find you on the way back."
    chance "Thanks, you guys got this!"
    thought "You head forward, without Chance, and try to stay calm in this ever tighter part of the cave."
    thought "Your breath is kept at a steady pace to fight against the panic in your racing heart. You want to turn back. You should turn back."
    thought "Upon trying to shuffle backwards you find that your body has subconsciously leaned your torso forward. Trying to move back feels contradictory to the way you’ve been positioned."
    thought "As you continue to shuffle through the crevice, you feel the slight breeze of an opening. Your anxieties lessen for a moment, allowing you to retain your composure."
    thought "You continue to shuffle forward, finally latching your hand to the corner of the exit."
    jump HallOfFaces

label HallOfFaces:
    scene bg blacksquare
    thought "Grabbing to the exterior wall, you begin to pull yourself closer to the exit. Your other arm reaches out the thin passageway, allowing the leverage to pull your head out."
    thought "Then your torso. Finally, your knees bend and push their way out, until you fall to the floor. "
    thought "You take a deep breath in, slightly proud that you made it through in one piece."
    thought "There should be no one in here yet."
    thought "But…"
    scene bg halloffacesilluminated with dissolve
    thought "In the corner of your eyes, you see a face."
    thought "A slight gasp escapes as you jump back. You raise your phone flashlight to illuminate the room."
    thought "You lock eyes with the sculpture of a head, no, a face carved out of the wall. Upon looking around, you see faces that line the walls."
    thought "Though no two are looking in the same direction, you can’t help but feel disturbed by their presence."
    show Rey_N_Question at l
    show Robbie_N_Awkward at r
    rey "Okay I think this cave is officially haunted. What the hell is this place?! "
    robbie "Well I- okay yeah I can’t even argue. That’s creepy as hell."
    claire "Maybe it’s some art student’s thesis project?"
    hide Rey_N_Question
    hide Robbie_N_Question
    show Rey_N_Default at l
    show Robbie_N_Question at r
    thought "Rey and Robbie both look at you, quizzically."
    claire "Okay yeah I’ve got nothing, this place sucks."
    robbie "Is there something similar about the faces? Like, what if they’re all a family or something?"
    hide Rey_N_Default
    show Rey_N_Question at l
    rey "I think trying to understand this is dumb. Maybe Claire was onto something, what if it is some weird art installation?"
    robbie "Like that thing we saw downtown, with jars of people’s teeth? "
    rey "Yeah like that!"
    claire "I don’t think it’s like that, but we could pause here for a bit and look around? "
    hide Rey_N_Question
    show Rey_N_Smile at l
    rey "Sure, I never mind a break."
    claire "Okay, I’ll be over here for a bit."
    menu:
        "Look Around.":
            jump LookAround
        "Rejoin your friends.":
            jump Friends
label LookAround:
    thought "Looking around the room, you begin to feel a sense of unease rise."
    thought "Something’s wrong here. Even though most faces are not turned to look at you, you can’t help but feel the presence of eyes glaring at you."
    thought "No, that’s not quite right."
    thoughtnoi "{i}You feel the presence of{/i} things {i}looking at you.{/i}"
    if facestrash == 0:
        menu:
                "Look at floor.":
                    thought "You look down and see a bright blue medical mask."
                    menu:
                        "Pick up the trash.":
                            play sound "pickupsoundv2.ogg"
                            $trashcounter += 1
                            $facestrash += 1
                            thought "You scoop it up and stuff it in your pocket."
                            jump LookAround
                        "Leave it":
                            jump LookAround
                "Look at faces":
                    thought "Upon closer inspection you begin to realize a commonality between the faces. Despite being made of rock, the craftsmanship is incredible. It’s almost as though you can see the pores of their skin."
                    jump LookAround
                "Touch the faces on the wall.":
                    thought "You reach out and gently touch the cheek of one of the faces. For a moment, you thought that there was a bit of elasticity in the rock."
                    thought "No, that’s not right. As you push harder, you realize that it’s still solid, just as it’s supposed to be."
                    jump LookAround
                "Rejoin your Friends":
                    jump Friends
    else:
        menu:
            "Look at faces":
                thought "Upon closer inspection you begin to realize a commonality between the faces. Despite being made of rock, the craftsmanship is incredible. It’s almost as though you can see the pores of their skin."
                jump LookAround
            "Touch the faces on the wall.":
                thought "You reach out and gently touch the cheek of one of the faces. For a moment, you thought that there was a bit of elasticity in the rock."
                thought "No, that’s not right. As you push harder, you realize that it’s still solid, just as it’s supposed to be."
                jump LookAround
            "Rejoin your Friends":
                jump Friends

label Friends:
    thought "You walk over to rejoin your friends. They’re muttering to one another, shining their flashlights around the room."
    thought "You glance back the way you came–your stomach seems to be in knots. You think about Chance, all alone back in the previous room. Maybe you shouldn’t have separated after all…"
    thought "You clear your throat."
    claire "Guys, I’m worried about Chance. I think we should head back for him."
    hide Rey_N_Smile
    show Rey_N_Default at l
    robbie "What? He’s probably fine. He’s Chance, remember? The star athlete from high school?"
    hide Rey_N_Default
    show Rey_N_Smile at l
    rey "Yeah! He knows what he’s doing."
    claire "I know, I just… I have this gut feeling that something’s up."
    robbie "I know I joked that it’s haunted, but really this place hasn’t been that bad. A little dark and creepy but like, what cave isn’t?"
    rey "Yeah, and I think this room is growing on me a little! It’s more spacious than the previous place."
    claire "I know he’s probably fine, I’m just…worried about him."
    menu:
        "Leave to check on Chance.":
            jump Chance
        "Stay with the rest of your friends.":
            jump Others

label Others:
    hide Rey_N_Smile
    show Rey_N_Default at l
    rey "Claire…I know you’re worried about him, but let’s stay here for a bit. Then after we’re prepared, we can head back for him together! Does that work?"
    claire "Yeah…yeah! That should be good."
    thought "The three of you walk closer to the faces on the wall, inspecting them."
    claire "Okay, really, what do you think this place is?"
    hide Robbie_N_Question
    show Robbie_N_Awkward at r
    robbie "Hmm…"
    hide Rey_N_Default
    show Rey_N_Question at l
    rey "I think I am going with the art installation idea. They’re all just- so realistic."
    robbie "Maybe some party goers put their faces in molds and like–put them up here as a memory?"
    claire "Hmm… what if, and this is a little morbid, but it’s a memorial of people that got lost?"
    hide Rey_N_Question
    show Rey_N_Nervous at l
    hide Robbie_N_Awkward
    show Robbie_N_Guilt at l
    robbie "Oh god, I don’t wanna think about that."
    rey "Yeah that’s a bit sad…"
    thought "You try not to think about Chance being lost, but the idea of Chance’s face being added to the wall appears in your head for a second, before vanishing."
    claire "Maybe…we should go check on Chance now? I don’t like staring at all these faces, it’s giving me the chills."
    robbie "Same. Let’s go!"
    hide Robbie_N_Guilt
    hide Rey_N_Nervous
    thought "Together, you turn back toward the entrance you came through, preparing for the tight twists and turns of the tunnel."
    scene bg tightsqueeze with dissolve
    thought "You navigate them a bit better on the backswing than you did the first time, and soon you’re back in the previous  room. Behind you, you hear Robbie and Rey crawl through."
    scene bg blacksquare
    thought "You brush off your clothes from all the dust and grime. At some point, your phone flashlight turns off as you fumble to turn it back on, shouts echo throughout the room."
    claire "Chance? You good buddy?"
    claire "Chance?"
    thought "No response."
    robbie "Hey dude? You there?"
    rey "Chance?"
    thought "No response."
    claire "We wanted to come back and make sure you’re okay. Did you get back okay?"
    claire "Chance?"
    show Robbie_N_Speechless at l
    show Rey_N_Nervous at r
    scene bg cave
    thought "You find the button on your phone, and light floods the room. Chance is nowhere in sight."
    claire "Fuck."
    rey "Oh god, where did he go, is he lost? Is he-"
    robbie "Guys, calm down everything is fine, he’s just- he’s hiding somewhere or something."
    claire "But…would he just run off? He said he would be here."
    rey "Where would he have even gone?"
    thought "You frown. Chance did like to join Robbie’s pranks; maybe he ran off as a joke? But you didn’t hear any footsteps or anything."
    jump PlayAlong2

label Chance:
    $chanceroom += 1
    claire "I think I’ll head back to check on Chance. I’m worried about him…"
    hide Robbie_N_Question
    hide Rey_N_Smile
    show Robbie_N_Default
    show Rey_N_Default
    robbie "Claire, he’s probably fine-"
    rey "No, it’s okay. Go check on him, and I’ll stay here with Robbie."
    claire "Okay, I’ll see you guys soon, I promise."
    hide Rey_N_Default
    hide Robbie_N_Default
    thought "You turn back towards the passage you came through, preparing for the tight twists and turns. Navigation is a bit better this time, and soon you’re back in the other room."
    scene bg blacksquare
    thought "You brush off your clothes from all the dust and grime. At some point, your phone flashlight turned off. As you fumble to turn it back on, shouts echo throughout the room. "
    claire "Chance? You good buddy?"
    claire "Chance?"
    thought "No response"
    claire "I wanted to come back and make sure you’re okay."
    claire "Chance?"
    scene bg cave
    thought "You find the button on your phone, and light floods the room. Chance is nowhere in sight."
    claire "Chance! Are you here?"
    claire "Respond you jerk! Where are you?"
    thought "No response."
    thought "Where did he go? Didn’t he say that he was planning to wait for you to come back?"
    thought "You turn back toward the twisty passageway and yell into it."
    claire "Guys! Chance isn’t here! "
    claire "I don’t know where he went, he said he would be right there!"
    thought "..."
    claire "Robbie? Rey? Are you guys there?"
    thought "They should be able to hear you."
    thought "Didn’t Robbie say something about a rendezvous point? Maybe Chance ended up back there?"
    scene bg blacksquare with fade
    thought "Worth a check. You quickly travel quickly back."
    jump RendezvousPoint

label LookForChance:
    thought "You venture in the direction you heard the scream, followed by Rey and then Robbie."
    play sound "footstepsreverb.ogg"
    thought "As you traverse into the depths, echoes coming from your shoes and nearby water droplets become louder."
    thought "You feel the air grow thick with the dust kicking up, filling your lungs with the unventilated air."
    rey "Chance! You dummy, where are you?"
    robbie " Dude, this isn’t as funny anymore, just come out already! "
    hide Rey_N_Question
    rey "“Ah!”"
    thought "You spin around, startled."
    show Rey_N_Speechless at l
    show Robbie_N_Awkward at r
    thought "Rey is on her knees in an awkward position. Robbie stoops to help her, and she winces as she gets up."
    robbie "Oh shit, you okay?"
    rey "My ankle…"
    thought "Robbie props her up against a rock, and stands back."
    claire "Do you need a moment to rest?"
    hide Rey_N_Speechless
    show Rey_N_Default at l
    rey "Maybe…yeah…maybe a few minutes."
    hide Robbie_N_Awkward
    show Robbie_N_Default at r
    robbie "We shouldn’t pause for long…Chance is still out there."
    hide Rey_N_Default
    show Rey_N_Speechless at l
    rey "I thought you were the one being all ‘it’s a joke, don’t worry?"
    robbie "I know my brother; he wouldn’t be able to hold a joke this long. He would’ve given it up by now."
    claire "Rey, can you walk?"
    rey "I think I need a bit longer, sorry."
    hide Robbie_N_Default
    show Robbie_N_Awkward at r
    thought "Robbie shifts, eyes darting around."
    robbie "Look, if something really is wrong with Chance, we need to find him asap. Rey, if you need to rest, that’s fine, but I’m going to scope out the area ahead."
    robbie "Claire, do you want to stay with Rey, or come with me?"
    rey "Hey, I don’t want to be alone!"
    robbie "It’ll only be for a few minutes, and we’ll come right back."
    if chanceroom == 1:
        rey "We only left Chance for a few minutes! I don’t want to end up like him!"
        claire "Rey, calm down, we don’t know what happened to him. That’s what we’re trying to figure out."
    hide Rey_N_Speechless
    show Rey_N_Nervous at l
    rey "..."
    menu:
        "Stay with Rey.":
            claire "Robbie, you go on ahead, I think I’ll stay here with Rey for a bit."
            hide Rey_N_Nervous
            show Rey_N_Guilt at l
            rey "Sorry guys…"
            hide Robbie_N_Awkward
            show Robbie_N_Default at r
            robbie "No, it’s okay! Get some rest, and I’ll go ahead to look for Chance."
            hide Robbie_N_Default
            jump StayWithRey
        "Go with Robbie.":
            claire "Rey, if it’s alright I think I’ll go ahead with Robbie."
            rey "That’s…alright. I’ll stay here, I promise. "
            hide Robbie_N_Awkward
            show Robbie_N_Default at r
            robbie "We’ll be back in no time!"
            claire "Get some rest! We’ll go ahead."
            jump GoWithRobbie
label StayWithRey:
    hide Rey_N_Guilt
    show Rey_N_Default at l
    rey "I’m worried about them. What if they don’t come back?"
    claire "Hey, it’ll be okay. They know what they’re doing."
    rey "I know it’s just, this whole cave thing is so creepy. I know that’s just because I’m scared but losing Chance certainly hasn’t helped it."
    claire "I know. This place is-"
    #ROBBIE MIMIC SPRITE
    show Robbie_M_Default at r
    thought "Robbie walks back into the cave, barely after he left. His movements look slow, like he’s tired, but he’s not breathing too hard. As you get up, Robbie looks over at you and opens his mouth."
    claire "Robbie! You’re back already?"
    robbie "Yes."
    rey "Oh! Did you find Chance?"
    hide Robbie_M_Default
    show Robbie_M_Smile at r
    pause
    robbie "Yes! He’s just down there. "
    claire "Oh, shit!"
    robbie "I need your help. I can’t get him alone. "
    claire "Ah, we can wait for a bit, until Rey feels better maybe?"
    rey "Yeah, my ankle’s doing a bit better, I could walk on it in a few minutes, maybe-"
    hide Robbie_M_Smile
    show Robbie_M_Default at l
    robbie "There’s no time! We- Claire and I should go. "
    claire "O-oh, you sure?"
    robbie "He’s…stuck! Down there, and he wants you to come to him!"
    claire "Really? Rey, are you alright if I go down to get Chance? I don’t know if-"
    rey "No no, it’s okay! Go get him. I’ll be okay. "
    robbie "It won’t take long."
    thought "Something’s up with Robbie, like he’s really nervous. Maybe he’s just antsy and worried about his brother?"
    claire "Okay, let’s go."
    thought "You squeeze Rey’s shoulder one last time before following Robbie down the tunnel. He looks over his shoulder multiple times to check that you’re still following."
    hide Rey_N_Default
    thought "You walk for a few minutes before clearing your throat."
    claire "Are we uh, close? To Chance?"
    robbie "Nearly, yes. Almost. Almost."
    claire "....did you say he was hurt?"
    robbie "I said he wanted you to come to him."
    claire "Robbie, what’s–"
    scene bg blacksquare
    thought "Suddenly, Robbie’s flashlight flickers out. For a brief moment, your heart skips a beat, but then the light comes back on, and—"
    scene bg cave
    show Chance_M_Default at m
    claire "Chance! You’re here!"
    thought "Chance is standing in the middle of the tunnel, slightly awkwardly. He looks okay, if a little bit…expressionless"
    thought "Like being lost hundreds of feet underground was the least interesting thing that had happened to him that day."
    chance "Claire! You’re here. That’s good."
    robbie "I brought her!"
    claire "Oh my god Chance I was so worried about you! Are you alright?"
    chance "Yes! I am fine."
    claire "Oh- uh. Are you sure? You’ve been down here for a while. I thought something had happened to you…"
    thought "At this comment, his expression changes from boredom to concern, and begins checking his body for any signs of injury."
    chance "No! Nothing bad, just got a little lost."
    hide Robbie_M_Default
    show Robbie_M_Smile at l
    robbie "Yeah. I found him down here walking around, but he wasn’t hurt."
    claire "That’s good… um. We should probably go back for Rey, then! She’s probably worried sick about you guys-"
    show Rey_M_Default at r
    thought "You turn around to walk back to Rey, but find her standing right in front of you, smiling."
    rey "Hi Claire!"
    claire "Oh- hi, Rey? What are you doing? I thought you were resting."
    rey "Oh, you took too long. So I came to find all of you."
    claire "Oh- are you sure that’s not too much on your ankle? You doing alright?"
    hide Rey_M_Default
    show Rey_M_Smile at r
    rey "Yes! I am fine."
    hide Chance_M_Default
    show Chance_M_Happy at m
    chance "Should we head out? We have everyone right here."
    claire "Oh uh-"
    thought "Something isn’t right. But…you have all your friends back."
    thought "Right?"
    robbie "Yes! Why don’t we head back. This whole adventure has been tiring."
    rey "Back at home, let’s rest and play some games!"
    hide Chance_M_Happy
    hide Rey_M_Smile
    hide Robbie_M_Smile
    show Robbie_M_Default at l
    show Rey_M_Default at r
    show Chance_M_Default at m
    claire "Sure! Uh, well if everyone is ready, let’s head back!"
    chance "Lead the way, Claire!"
    hide Robbie_M_Default
    hide Rey_M_Default
    hide Chance_M_Default
    thought "You lead the way back through the cave, squirming through the narrow, twisty passageways."
    thought "Your friends are deadly quiet behind you, but when you turn to look, they’re there, following you with smiles on their faces."
    thought "As you finally see rays of daylight streaming through the mouth of the cave, you have a funny, pressurized sort of feeling in your chest."
    play sound "mediumheartbeatv2.ogg" loop
    thought "You found all your friends. Didn’t you?"
    thought "You all got out together. Didn’t you?"
    thought "….Then why did this feel so…."
    thought "…wrong?"
    stop sound
    jump Ending8
label Ending8:
    show everybodydied
    window hide
    pause
    thought "Claire was able to find her “friends” in the depths of Hellmouth. She leaves with “Robbie”, “Rey” and “Chance”."
    return

label GoWithRobbie:
    scene bg cave with dissolve
    show Robbie_N_Default at r
    thought "You try to keep up with Robbie as he moves down the tunnel."
    hide Robbie_N_Default with dissolve
    thought " For a brief moment, you glance in the direction of Rey, and when you swivel back to face Robbie…"
    thought "He’s gone."
    claire "Uh, Robbie? Where did you go?"
    robbie "Claire…"
    thought "The response comes from a passage to your left. You slip down it, and almost run straight into Robbie."
    show Robbie_M_Default at r, bounce
    claire "GOD! Robbie, I almost ran straight into you dude!"
    robbie "Sorry."
    claire "No, it’s fine I just didn’t see you for a second. What’s up?"
    robbie "I’m just looking for Chance, I don’t know where he is."
    claire "Yeah duh, we were looking for him together."
    hide Robbie_M_Default
    show Robbie_M_Smile at r
    thought "Robbie seems a bit surprised by this, and then gives you a tiny smile."
    robbie "Oh, right. Sorry!"
    claire "No need to apologize, dude. You doing alright?"
    hide Robbie_M_Smile
    show Robbie_M_Default at r
    robbie "Mhm, just a bit tired, but we need to be fast, we-"
    play sound "footstepsnormal.ogg"
    thought "Robbie freezes, and at the same time you hear Rey stumbling down the tunnel after you, shouting."
    rey "Claire! Robbie! Where are you guys?"
    hide Robbie_M_Default
    thought "You turn towards the voice, and shout back"
    claire "Rey! We’re over here! But you shouldn’t be chasing after us, rest your ankle! "
    show Rey_N_Nervous at m
    thought "Rey appears in front of you, limping, and nearly throws herself at you."
    rey "Sorry, I couldn’t wait. I was so creeped out by being left alone that I needed to find you two."
    claire "Well, me and Robbie are here, and everything’s good so-"
    hide Rey_N_Nervous
    show Rey_N_Question at m
    rey "What? No he isn’t"
    thought "You turn around and, sure enough, Robbie is no longer standing beside you. Or, for that matter, no longer anywhere in this room."
    claire "What? But- he was-"
    show Robbie_N_Default at r
    robbie "Hey! Claire! Rey! I found y’all! Oh my god I was so worried!"
    claire "Wait, no- but you were just here!"
    hide Robbie_N_Default
    show Robbie_N_Question at r
    robbie "What? No, I was running down the tunnel, and when I looked back I didn’t see you. I heard Rey’s voice and ran towards that. "
    claire "What- "
    robbie " I haven’t seen either of you since I left. Claire, I thought you were right behind me."
    hide Rey_N_Question
    show Rey_N_Default at m
    rey "Claire, are you okay?"
    play sound "fastheartbeat.ogg" fadein 1.5
    thought "Your mind races with what just happened, trying to make sense of each event in succession. Was that- not Robbie? Is there another person down here?"
    thought "What’s going on?"
    claire "I’m- I’m fine. I think."
    hide Robbie_N_Question
    show Robbie_N_Default at r
    robbie "Okay, but we gotta keep moving, Chance could be down here!"
    claire "Okay, yeah! Rey, are you good to-"
    hide Rey_N_Default
    show Rey_N_Nervous at m
    rey "Yeah yeah, I’ll be coming with. Being alone like that creeped me out"
    claire "Okay, then let’s move."
    scene bg blacksquare with fade
    thought "Progress is a bit slow with Rey trying to keep her weight off her bad ankle, but the three of you managed to move through the cave’s tunnels and twists."
    scene bg partyroomempty with dissolve
    show Rey_N_Default at l
    show Robbie_N_Default at r
    thought "Eventually, the tunnel branches ahead of you."
    robbie "Oh come on, another branching path?"
    rey "This cave loves them, I think."
    robbie "Alright, you lead the way, Claire. We’ll stick right behind you."
    menu:
        "Go into the small passage.":
            thought "You lead the way into the smaller passage."
            jump NotReyAlt
        "Go into the larger passage.":
            thought "You step into the larger passage."
            jump Ending3
label Ending3:
    robbie "Good call, Chance’s massive shoulders probably wouldn’t have fit into that tight squeeze, anyway."
    claire "Ha, yeah I–AH JESUS!"
    show Chance_N_Default at m
    chance "BOO!" with sshake
    hide Rey_N_Default
    show Rey_N_Speechless at l
    rey "Chance!"
    hide Robbie_N_Default
    show Robbie_N_Guilt at r
    robbie "Dude!"
    claire "You scared the shit out of me!"
    hide Chance_N_Default
    show Chance_N_Happy at m
    chance "Haha, sorry, sorry. Couldn’t help myself"
    rey "We’ve been looking all over for you, numbskull! We were worried."
    claire "We heard you scream."
    hide Chance_N_Happy
    show Chance_N_Question at m
    chance "Huh?"
    robbie "It’s true, man. We heard it earlier, right after you disappeared."
    chance "I was just trying to prank you guys! I mean… I did get a little lost after I ran off to hide, haha."
    chance "That’s what took me so long to find you. But I never screamed or anything like that."
    hide Rey_N_Speechless
    show Rey_N_Nervous at l
    hide Robbie_N_Guilt
    show Robbie_N_Awkward at r
    rey "…"
    robbie "…."
    claire "Then what…"
    rey "It doesn’t matter. Let’s get out of here. Please? We’re all together now, can we just–this place is—"
    claire "Yeah, I know. You’re right. Let’s get out of here, asap."
    scene bg blacksquare with dissolve
    thought "The four of you, reunited, begin to make your way back through the cave’s labyrinth of tunnels and branching passageways."
    thought "Robbie and Chance switch out supporting Rey as she limps along. You’ll have to make sure she gets that ankle looked out when you get out."
    thought "When you near the exit and catch sight of the first rays of sunlight you’ve seen in hours, you breathe a sigh of relief. You all got out, save for some scrapes."
    thought "As Robbie and Chance help boost Rey up through the cave entrance, you take one last moment to turn back and look into the dark depths you just resurfaced from."
    thought "Something told you there was more to this cave than what meets the eye…"
    thought "…but perhaps some things are better left alone."
    thought ""
    show nobodydied
    window hide
    pause
    thought "Claire was able to find Chance, and left Hellmouth caves with him, as well as Robbie and Rey."
    return

label NotReyAlt:
    hide Robbie_N_Default
    hide Rey_N_Default
    scene bg tightsqueezeflip
    play sound "mediumheartbeatv2.ogg" loop
    thought "You begin to walk through the small passage. It’s not tight enough where you have to contort your body to fit within, but your shoulders occasionally clip along the walls. "
    thought "Your heart pounds into your chest as you traverse deeper into the cave. A part of you wants to believe that this is a prank, and that you’ll find your dumb friend laughing by himself on the other side."
    thought "Another part of you wonders what if it’s not? The more you think about your friend screaming for help, isolated in this cavern, the more you wonder what could be happening to him."
    scene bg cavealt
    thought "Maybe a bat flew by? Scared him just enough to cause a scream?"
    stop sound fadeout 3.0
    thought "Or maybe he thought he saw something."
    thought "Maybe he did see something."
    thought "Maybe there is something there, waiting for others to come to it."
    thought "No, that’s just fear talking."
    thought "Or is it logic?"
    thought "Keep yourself together."
    thought "As you reach the opening, you shine your light around the room, calling out in hopes of hearing a response."
    claire "Chance! You there?"
    thought "Your friends join in too."
    show Rey_N_Question at r
    show Robbie_N_Default at l
    rey "Chance!"
    robbie "Chance!! Where are you?"
    rey "This isn’t funny!! Ok, you got us, ha ha!! You can come out now!!"
    play sound "fastheartbeat.ogg"
    thought "As you continue to shine your flashlight, {nw}"
    thought "As you continue to shine your flashlight, {fast}you could’ve sworn you saw the glimpse of a person. But upon turning back, it seems like there’s no one there."
    stop sound
    play sound "footstepsnormal.ogg"
    thought "Out of the corner of your eye, you once again see a figure. Chance, perhaps? You quickly turn around, and hear the skittering of footsteps."
    thought "Though you know no one is there, the dust cloud left behind argues otherwise."
    hide Rey_N_Question
    hide Robbie_N_Default
    show Rey_N_Speechless at r
    show Robbie_N_Question at l
    rey "C’mon Chance! It’s just go- AH!"
    thought "The sound of a person falling makes you quickly turn around and lock eyes with… Chance."
    show Chance_M_Happy at m
    thought "He stands on the other side of the room, still as a statue with a grin on his face. Robbie rushes over to Rey, helping her off the ground as she looks at Chance with an angry glare."
    rey "You scared the shit out of me!"
    hide Chance_M_Happy
    show Chance_M_Default at m
    chance "I’m sorry Rey. "
    hide Robbie_N_Question
    show Robbie_N_Speechless at l
    robbie "You scared the shit out of us! We thought something happened to you."
    chance "I’m sorry Robbie."
    claire "God, that’s not funny dude! But…I am glad you’re okay."
    hide Rey_N_Speechless
    show Rey_N_Default at r
    rey "Yeah, even if that is a bit of a dick move, we missed you."
    hide Chance_M_Default
    show Chance_M_Scared at m
    thought "At Rey’s comments, Chance looks confused for a few seconds, before smiling and giving the three of you a giant hug."
    hide Chance_M_Scared
    show Chance_M_Happy at m
    rey "Oh- I-"
    hide Chance_M_Happy
    show Chance_M_Default at m
    chance "Thank you."
    rey "I- yeah I can’t be mad at you. Sorry for yelling."
    thought "While their exchange is heartwarming, the thing you immediately notice as Chance hugs you is his arms."
    thought "The skin on his forearms feels bumpy, like if it was caked in mud and left out to dry. As well, when he’s this close, you notice that he smells…off."
    claire "Dude, not that close, you stink!"
    hide Robbie_N_Speechless
    show Robbie_N_Cheeky at l
    robbie "Oh that’s probably just his sweat, I don’t think I’ve seen him put on deodorant in months."
    thought "You and Rey immediately push off him, making fake gagging noises."
    chance "Sorry."
    rey "Blegh, gross. I take back what I said."
    hide Robbie_N_Cheeky
    show Robbie_N_Question at l
    robbie "How did you end up down here dude? We’ve been searching for ages for you!"
    chance "I got a bit lost."
    hide Rey_N_Default
    show Rey_N_Guilt at r
    rey "A bit? A bit lost is losing your friend in the supermarket aisle, not going down a mile into the earth!"
    claire "Well- regardless, it’s good to see you. "
    hide Chance_M_Default
    show Chance_M_Happy at m
    chance "Mhm! How about we head out."
    robbie "Oh- uh, you sure? Did you want to explore more?"
    hide Chance_M_Happy
    show Chance_M_Default at m
    chance "No. Let’s leave. "
    jump QuestioningChance
label QuestioningChance:
    if QuestionChance == 0:
        menu:
                "Question Chance's behavior.":
                    $QuestionChance += 1
                    thought "Chance seems very eager to leave. And for most people, you would understand that, but the Chance you know wouldn’t want to flee unless the worst had happened."
                    thought "The fact that he hasn’t cracked some joke yet or made light of the situation felt…strange."
                    thought "Something's not right."
                    claire "Not so fast. Something’s up."
                    hide Rey_N_Guilt
                    show Rey_N_Nervous at r
                    rey "Huh?"
                    robbie "Claire, what are you talking about?"
                    chance "Yeah. What’s up?"
                    claire "It's Chance. Something's...off."
                    chance "I'm fine"
                    rey "Claire, are you sure?"
                    claire "Something's just - off."
                    thought "Something's not right."
                    chance "We should go."
                    jump QuestioningChance
                "Leave the cave with the group.":
                    jump Ending5
    if QuestionChance == 1:
        menu:
                "Question Chance's behavior.":
                    $QuestionChance += 1
                    thought "Chance seems very eager to leave. And for most people, you would understand that, but the Chance you know wouldn’t want to flee unless the worst had happened."
                    thought "The fact that he hasn’t cracked some joke yet or made light of the situation felt…strange."
                    thought "Something's not right."
                    claire "Not so fast. Something’s up."
                    hide Rey_N_Guilt
                    show Rey_N_Nervous at r
                    rey "Huh?"
                    robbie "Claire, what are you talking about?"
                    chance "Stop that."
                    claire "It's Chance. Something's...off."
                    chance "I don't know what you're talking about. I'm fine."
                    rey "Are you sure Claire?"
                    claire "Something's just - off."
                    thought "Something's not right."
                    chance "We need to go right now. Leave."
                    jump QuestioningChance
                "Leave the cave with the group.":
                    jump Ending5
    if QuestionChance == 2:
        menu:
                "Question Chance's behavior.":
                    $QuestionChance += 1
                    thought "Chance seems very eager to leave. And for most people, you would understand that, but the Chance you know wouldn’t want to flee unless the worst had happened."
                    thought "The fact that he hasn’t cracked some joke yet or made light of the situation felt…strange."
                    thought "Something's not right."
                    claire "Not so fast. Something’s up."
                    hide Rey_N_Guilt
                    show Rey_N_Nervous at r
                    rey "Huh?"
                    robbie "Claire, what are you talking about?"
                    chance "STOP IT."
                    claire "It's Chance. Something's...off."
                    hide Chance_M_Default
                    show Chance_M_Scared at m
                    chance "I SAID IM FINE!"
                    rey "..."
                    claire "Something's just - off."
                    thought "Something's not right."
                    chance "WE NEED TO LEAVE WE NEED TO LEAVE WE NEED TO LEAVE."
                    jump MimicMayhem
                "Leave the cave with the group.":
                    jump Ending5

label Ending5:
    scene bg cavealt
    show rey n nervous r
    show chance m default m
    show robbie n question l
    claire "Mhm. Let’s leave, I think we’ve been down here too long."
    hide Chance_M_Default
    show Chance_M_Happy at m
    chance "Yes! Let’s go, now."
    robbie "Well- true. I hope everyone had fun though."
    rey "Are you kidding me? I can't wait to get out. Chance are you-"
    hide Chance_M_Happy
    thought "Rey turns to look at Chance, but he’s already walking back towards the direction you came from."
    rey "Hey! You oaf, slow down!"
    thought  "You make your way back through the cave’s twisty passages and sharp turns. Ahead of you, you can hear Chance muttering."
    menu:
        "Check on Chance":
            thought "As you meet his gaze, he stares at you with a deer in the headlights look in his eyes. Upon listening closer you begin to make out his muttering. "
            chance "Light on flesh. Light on rock. Light on the ones that rot. Rot in the grotto that invites those who are flesh."
            chance "The flesh that impersonates that of rock  The rock that impersonates that of flesh. Flesh that impersonates that of flesh. Light on flesh…"
            thought "He continues to repeat these phrases. Something is terribly wrong with him. You’re not sure what, but hopefully someone outside can help."
            scene bg blacksquare with dissolve
            thought "You all leave the cave."
            jump Ending5End
        "Exit the cave":
            scene bg cavetitlescreen
            thought "You and your friends exit the cave. Rey begins to take a long stretch, enjoying the spacious area of the outdoors. Robbie sits down, taking a deep breath of relief in the fresh misty forest air"
            thought "You turn to Chance. He doesn’t turn to you."
            thought "No, instead his eyes are locked straight onto the sky."
            thought "You look to see what he is looking towards, only to feel your eyes burn after looking straight into the sun."
            thought "Turning back to him, you get closer to see his current condition."
            thought "In the bright light of the day, you begin to notice the unusual texture of his skin."
            thought "The rugged textures of his eyeballs."
            thought "No, that can’t be right. You’re not seeing a crack on the corner of his eye. The lack of moisture on them raises your concerns even higher."
            thought "He smiles. Despite the jagged texture that his skin looks like, it organically moves and pinches into dimples you don’t remember Chance having."
            show Chance_M_Happy at r
            chance "Light that is not mechanical ways. Warmth of a body made of the flesh that impersonates rock. Flesh that impersonates flesh. What a beautiful day it is."
label Ending5End:
    show chancedied
    window hide
    pause
    thought "Claire was able to find “Chance” within the twists and turns of Hellmouth caves. She leaves with him, in addition to Robbie and Rey."
    return

label MimicMayhem:
    scene bg blacksquare
    thought "Suddenly, all of the flashlights go out, in a single click of darkness."
    claire "Turn the lights on, Chance, right now!"
    rey "What’s going on?!"
    robbie "What’s happening??"
    scene bg cavealt
    thought "Then, just as suddenly as it goes out, the light returns…"
    show Chance_N_Default at l
    show Chance_M_Default at r
    thought "... and before you, stand two identical Chances."
    thought "Rey screams, while Robbie is standing there, speechless."
    hide Chance_N_Default
    show Chance_N_Nervous at l
    chance "Guys! What- what’s going on?"
    hide Chance_M_Default
    show Chance_M_Scared at r
    notchance "Who is this? Why are there two versions of me?"
    claire "Fuck. Really?"
    show Robbie_N_Awkward at m
    robbie "What- what the {i}hell{/i}?"
    hide Chance_N_Nervous
    show Chance_N_Happy at l
    chance "Finally, I found you! Why- why is there-"
    notchance "Found you? No, you’ve been here the whole time, I found them just now!"
    hide Chance_N_Happy
    show Chance_N_Nervous at l
    chance "What the hell are you talking about I-"
    claire "STOP IT!"
    hide Chance_N_Nervous
    hide Chance_M_Scared
    hide Robbie_N_Awkward
    show Chance_N_Default at l
    show Chance_M_Default at r
    show Robbie_N_Default at m
    thought "With that, everyone in the room turns and looks at you, including both of the Chances."
    claire "I know what to do."
    hide Robbie_N_Default
    show Rey_N_Nervous at m
    rey "Claire…what are you-"
    claire "One of these two is a fake. I don’t know how, but they’re looking like our friend."
    claire "And we need to find out who is who."
    hide Rey_N_Nervous
    show Robbie_N_Question at m
    robbie "How would we figure it out?"
    hide Chance_N_Default
    hide Chance_M_Default
    show Chance_N_Nervous at l
    show Chance_M_Scared at r
    thought "You look over, trying to inspect each Chance. The one on the left is nervous, shaking a little bit, and the one on the right is still, but looks concerned."
    thought "From your point of view, both of their features, their eyes, their hair, everything, are nearly identical."
    chance "I don’t- I’m confused, can’t you tell I’m {i}me{/i}?"
    notchance "No, I’m me! That other…thing, is clearly the fake! We should-"
    claire "Quiet! Stop this."
    hide Chance_M_Scared
    show Chance_M_Default at r
    hide Chance_N_Nervous
    show Chance_N_Guilt at l
    thought "Surprisingly, both Chances stop talking and stare at you. You’d never been able to pull rank before, especially on Chance."
    thought "Inspecting them, you look and point at the Chance on the left. "
    claire "How did you get here?"
    chance "I- heard y’all’s voices, and I followed the direction it was coming from before stumbling in here. It was dark, and when the lights came on, there was another me."
    hide Chance_M_Default
    show Chance_M_Scared at r
    notchance "No! That’s not what happened, please you-"
    claire "Shut up! Now, Chance on the right, how did you get here?"
    hide Chance_M_Scared
    show Chance_M_Default at r
    notchance "I walked in and saw someone that looked like me talking with you. And then the lights went out. "
    thought "Both of the stories seem plausible… and they’re both acting like Chance, at least, right now. But whichever one of them was here before was acting strangely…"
    thought "Right here, right now, you aren’t sure if you could tell them apart."
    claire "I…"
    hide Chance_M_Default
    show Chance_M_Scared at r
    hide Chance_N_Guilt
    show Chance_N_Question at l
    thought "They both look at you, nervous."
    claire "I think… the real one is…"
    thought "Left? Or right? Which one?"
    claire "The real one is-"
    play sound "footstepsreverb.ogg"
    play audio "heavybreathing.ogg"
    hide Chance_M_Scared
    thought "Suddenly, one of the Chance’s looks at you, fear in his eyes, and runs."
    thought "Something tugs at you–what if that was the real Chance? Before you know what you’re doing, you’re sprinting after him."
    play sound "footstepsreverb.ogg" loop
    play audio "heavybreathing.ogg" loop
    claire "Rey, Robbie! Watch that Chance, make sure he doesn’t leave!"
    hide Robbie_N_Question
    thought "Through the twists and turns of the cavern, you’re not able to keep him within your sights. The sound of your friends footsteps are just within earshot, so you keep following them."
    stop sound
    thought "Eventually, they turn the corner, and rapidly stop."
    thought "You begin to slow down too, catching your breath after the chase. As you turn the corner you feel your heart sink."
    stop audio
    thought "A couple feet away from you is Chance…"
    thought "And a body."
    thought "Something is wrong. Though you are shining your bright flashlight at him, he seems to not notice you."
    thought "  notice you."
    play sound "pestopastav2.ogg"
    thought "The creature’s fingers begin to grow, pulling at the imitation flesh but not tearing. They grow into jagged points."
    thought "You watch as the thing pretending to be your friend kneels down beside the body, and grasps the man's face."
    thought "It’s claws piece skin, and begin to curl its fingers until it can get a firm grip of the pocket between teeth and cheek."
    thought "The thing grabs onto its own arm, and with it’s whole body begins to yank at the face."
    thought "Only then you realize what it's trying to do. Stricken with nausea, you look away. The ungodly sounds ring throughout the room as the thing rips…"
    thought "and digs…"
    thought "and tears…"
    thought "and pulls…"
    play sound "celinescream.ogg"
    thought "A deafening screech echoes around the room. The thing mimicking your friend screams, and then you hear a man's voice speak out."
    stranger "H-h-h-h-he-hello? Hello?? Can someone hear me?"
    thought "then a woman's voice… "
    stranger "Please, oh please can someone help me? I'm stuck, I need help!"
    thought "then a cry that you swear came from a child…"
    stranger "Mommy!!"
    thought "As it continues to adjust, you hear Robbie's voice…"
    stranger "H-hey guys this isn't funny! Where are you? Chance?"
    thought "then Rey's voice…"
    stranger "Where are you guys? Can you hear me? Claire? Chance? Robbie?"
    thought "..then Chance…"
    stranger "Okay where the hell did they go off to? Rey? Claire? If you can hear me, come here!"
    thought "and then…"
    thought "..the thing speaks in your voice."
    stranger "Who are you?"
    play sound "footstepssquishynormaltrans.ogg"
    thought "You run."
    play audio "heavybreathing.ogg" loop
    play music "fastheartbeat.ogg" loop
    thought "Your feet fly beneath you, stumbling over rocks and uneven ground. You can hear whatever that THING is pursuing you, its footsteps, heavy thumps, rapid thumps."
    thought "Your mind racing, you reach a fork in the tunnel and quickly dart down a direction, not bothering to stall and debate which way to go."
    thought "You don’t have time."
    thought "You need to get away."
    thought "You need to get away, or else–"
    stop audio
    stop music
    play sound "rocksfallingv1.ogg"
    play audio "footstepsreverb.ogg" loop
    thought "A gasp escapes you as you slam face first into a stone wall."
    thought "No. No. Nonononono–"
    thought "A dead end."
    thought "A FUCKING dead end."
    stop audio
    thought "You hear the thumping footsteps draw close, and then slow to a stop."
    thought "Feeling your heart pound out of your chest, you slowly turn around."
    thought "The creature stares at you with rugged textured eyes behind the skin it wears."
    thought "The edges of the stolen face sink into the jagged imitation of human flesh. Its hands remained locked open, waiting for your next move."
    if bottle > 0:
        menu:
            "Scream for help.":
                thought "You scream for help, pleading for someone, anyone to come save you."
                jump Scream
            "Fight":
                jump Fight
label Fight:
    thought "You slowly reach into your bag, allowing no sudden movements to alarm it as it tracks your movement. There has to be something here to help."
    thought "Half empty plastic water bottle… receipts… gum… useless."
    thought "Your hand then glides across the neck of a bottle you picked up earlier."
    stranger "“What…”  it says in Chance’s voice"
    stranger "“Are…” it says in Rey’s voice"
    stranger "“You…” it says in Robbie’s voice"
    stranger "“Doing…?” it says in your voice"
    thought "You wrap your hand around it, holding it so tightly to the point that it feels as though your knuckles are about to rip apart."
    thought "As you begin to pull it out, the creature lunges at you."
    thought "In a sudden impulse move, you yank the bottle out of your bag and swing at the creature. The glass shatters as its head concaves to the blunt force."
    thought "The skin that once melded into its mockery flesh hangs loose in the indentation. "
    thought "It staggers backwards with a gut wrenching scream ringing throughout the tight room."
    thought "It glares at you one final time, putting together the remains of whatever voice it has left, it asks… "
    stranger "Light…not…mechanical ways. Warmth?"
    thought "The creature collapses, its body sinking into the ground below."
    jump Ending10

    if bottle == 0:
        menu:
            "Scream for help.":
                thought "You scream for help, pleading for someone, anyone to come save you."
                jump Scream
            "Fight":
                jump FightFake
label FightFake:
    thought "You slowly reach into your bag, allowing no sudden movements to alarm it as it tracks your movement. There has to be something here to help."
    thought "Half empty plastic water bottle…receipts… gum…useless."
    stranger "“What…”  it says in Chance’s voice"
    stranger "“Are…” it says in Rey’s voice"
    stranger "“You…” it says in Robbie’s voice"
    stranger "“Doing…?” it says in your voice"
    thought "You beg for something to be in here to come to help you. The bag begins to rapidly ruffle as you desperately try to find something!! Anything!!"
    jump Scream

label Scream:
    thought "You hear the gutteral sound of blades digging into organs. It is only when your stomach runs cold that you realize what happened."
    thought "You can’t look down though. No, your eyes are locked into the ones behind the stolen flesh. It yanks the claws out of your intestines, allowing you to stagger backwards to the wall."
    thought "It closes the gap once again, shoving it’s talons in the same gouge in your stomach with more force."
    thought "You feel it piece not only through your organs, but your spine slides between its fingers  as they make an exit out your back."
    thought "You hear the wall behind you crack as it penetrates the rock with the remaining force."
    thought "It slightly curves its fingers before yanking its hand out, hollowing out more of the crevice in your torso."
    thought "You fall to the ground and watch as the creature stabs and rips into your still conscious body."
    thought "The feeling of your flesh being rendered to shreds or the feeling of your torso going cold from your blood splattering across the floor is nowhere near as horrifying as watching the creature reach for its own face."
    thought "In the last moments of your consciousness, you watch as it begins to dig into its own flesh and peel off the previously stolen face. It looks at you, and begins to reach for yours."
    jump Ending7
label Ending10:
    scene bg cavetitlescreen
    show Rey_N_Smile at l
    show Robbie_N_Cheeky at m
    show Chance_N_Happy at r
    window hide
    pause
    thought "Claire is able to find Chance and “Chance” within the depths of the Hellmouth caves."
    thought "In trying to decipher who the real Chance is, she discovers a strange, unidentifiable creature that seems to have the ability to MIMIC people’s voices and appearance."
    thought "Claire is able to defend herself against the mimic and escape the caves with Robbie, Rey and Chance"
    return

label Ending7:
    scene nobodydied
    window hide
    pause
    thought "Claire is able to find Chance and “Chance” within the depths of the Hellmouth caves."
    thought "In trying to decipher who the real Chance is, she discovers a strange, unidentifiable creature that seems to have the ability to MIMIC people’s voices and appearance."
    thought "Claire fails to fend off the mimic, and dies in Hellmouth caves. What happens to Chance, Rey and Robbie is unknown."
    return

label Separate:
    scene bg cavealt
    show Chance_N_Default at l
    show Robbie_N_Default at r
    show Rey_N_Speechless at m
    claire " I think it makes more sense to split up for a bit."
    hide Rey_N_Speechless
    show Rey_N_Nervous at m
    rey "…Ok. If you’re sure, but I'm tagging along with one of the boys."
    hide Chance_N_Default
    show Chance_N_Happy at l
    chance "We’ll be fine! We’ve got our flashlights, and this cave doesn’t even seem that deep! This way, we’ll be out of here in no time!"
    robbie "Okay, if we’re doing this, let’s set up a rendezvous point alright?"
    claire "Mhm, if any of you hit a dead end, or need to come back, this is our spot. Let’s all meet back here once we’re done, alright?"
    chance "Sounds perfect! See you then"
    jump SepPaths

label SepGoBackExplore:
    scene bg partyroomempty
    thought "You find yourself back at the crossroads from before."
    jump SepPaths

label SepPaths:
    scene bg partyroomempty
    thought "To the left, a faint wind sends a chill down your spine. You know some caverns have wind tunnels in them. It could be worth exploring."
    thought "To the right, you feel a strange sort of hum vibrate the bottom of your feet. It reverberates off the walls with a subtle noise. How curious–what could that be?"
    thought "Straight ahead is the largest opening, an entrance wide enough to walk into without a necessity to squeeze."
    if SepLungsVar == 0:
        if SepHeartVar == 0:
            if SepPartyRoomVar == 0:
                menu:
                    "Left, toward the sound.":
                        jump SepLungs
                    "Right, toward the vibration.":
                        jump SepHeart
                    "Straight ahead, toward the large tunnel entrance.":
                        jump SepPartyRoom
    if SepLungsVar == 1:
        if SepHeartVar == 0:
            if SepPartyRoomVar == 1:
                menu:
                    "Right, toward the vibration.":
                        jump SepHeart
    if SepLungsVar == 1:
        if SepHeartVar == 0:
            if SepPartyRoomVar == 0:
                menu:
                    "Right, toward the vibration.":
                        jump SepHeart
                    "Straight ahead, toward the large tunnel entrance.":
                        jump SepPartyRoom
    if SepLungsVar == 1:
        if SepHeartVar == 1:
            if SepPartyRoomVar == 0:
                menu:
                    "Straight ahead, toward the large tunnel entrance.":
                        jump SepPartyRoom
    if SepLungsVar == 1:
        if SepHeartVar == 1:
            if SepPartyRoomVar == 1:
                thought "The unsettling feeling of this isolation begins to settle in,  and you realize it’s probably time to meet up with the others, anyway. You turn and start to make your way back to the rendezvous point."
                jump SepRendezvousPoint
    if SepLungsVar == 0:
        if SepHeartVar == 1:
            if SepPartyRoomVar == 0:
                menu:
                    "Left, toward the sound.":
                        jump SepLungs
                    "Straight ahead, toward the large tunnel entrance.":
                        jump SepPartyRoom
    if SepLungsVar == 0:
        if SepHeartVar == 1:
            if SepPartyRoomVar == 1:
                menu:
                    "Left, toward the sound.":
                        jump SepLungs
    if SepLungsVar == 0:
        if SepHeartVar == 0:
            if SepPartyRoomVar == 1:
                menu:
                    "Left, toward the sound.":
                        jump SepLungs
                    "Right, toward the vibration.":
                        jump SepHeart
    else:
        if SepLungsVar == 0:
            if SepHeartVar == 0:
                if SepPartyRoomVar == 0:
                    menu:
                        "Left, toward the sound.":
                            jump SepLungs
                        "Right, toward the vibration.":
                            jump SepHeart
                        "Straight ahead, toward the large tunnel entrance.":
                            jump SepPartyRoom


label SepLungs:
    $SepLungsVar += 1
    scene bg tightsqueeze
    thought "You turn sideways to shuffle through the narrow passageway. The wind from the other side is cold, leaving goosebumps wherever it can find bare skin."
    thought "It lightly pushes against you and your friends but gets stronger the closer you get."
    thought "Occasionally it will ease up but be replaced by a gust of wind from behind."
    thought "You don’t remember there being wind from the previous room, though maybe you just weren’t paying enough attention to realize it was there."
    thought "Upon entering the vast space, the winds are deafening. It’s almost to the point where it’s hard to breathe."
    thought "For a brief moment, the wind slows down, and the sound is replaced by the air current rapidly traversing through the passageway your group once came through."
    thought "You take a breath to enjoy this moment of clarity, but it is short-lived as the rapid wind starts up again."
    menu:
        "Stay a moment longer, looking around the room.":
            thought "A cigarette butt is lying nearby on a rock."
            menu:
                "Pick up the trash.":
                    $trashcounter += 1
                    "You pick it up. Yuck."
                    jump SepGoBackExplore
                "Leave it be.":
                    "You leave it."
                    jump SepGoBackExplore
        "Go back.":
            jump SepGoBackExplore
label SepPartyRoom:
    $SepPartyRoomVar += 1
    scene bg tightsqueezeflip
    thought "You turn sideways to shuffle through the narrow passageway, feeling the rock cling to your back."
    play sound "rocksfallingv2.ogg"
    thought "The sound of your own footsteps fills up the space alongside the falling pebbles that come off the walls as your body inches through the passageway."
    scene bg partyroom with dissolve
    thought "The space widens as you enter this new room with a ceiling high enough to stand upright."
    thought "Thank God–you aren’t necessarily claustrophobic, but that narrow passage you came through questioned how much of a squeeze you can truly handle."
    thought "From the light of your phone, you see graffiti spray painted on the stone walls."
    thought "Some are tags of the people who have been here, messily scribbled on with Sharpie markers. Others are larger spray-painted phrases such as “Do not enter” and “Funky”."
    thought "Upon looking down, you see a small handwritten note “Do not continue. It’s alive.”"
    menu:
        "Stay a moment longer, looking around the room.":
            thought "You spy a flattened ramen cup, muddied on the ground."
            menu:
                "Pick up the trash.":
                    play sound "pickupsoundv2.ogg"
                    $trashcounter += 1
                    thought "You pick it up. You guess you should take this with you."
                    jump SepGoBackExplore
                "Leave it be.":
                    thought "You turn away."
                    jump SepGoBackExplore
label SepHeart:
    $SepHeartVar += 1
    scene bg tightsqueeze
    thought "You squeeze into the narrow passageway, the walls scratching against whatever bare skin it can find. Breathing in is taxing, as you feel your expanded stomach push against the front wall."
    play sound "mediumheartbeatv2.ogg" loop
    thought "The passage finally begins to widen in front of you, and you draw a breath, inching your way  forward. Just keep moving forward."
    thought "Slowly, the walls loosen their grip on you and begin to give way."
    scene bg cave
    thought "You find yourself in a small cavern; it wasn’t the most spacious thing in the world, but compared to what you had just been through, it felt like a penthouse suite."
    thought "Your brain pulses against the sides of your skull, feeling the rhythm align with the sound of your heartbeat in your ears."
    thought "Blood pulsing through your body becomes apparent to you as you feel its pressure in your fingers and toes."
    thought "The rhythmic beating of your blood, no, your heart, feel external. It’s all around you, emanating from the walls."
    thought "You see it out of the corner of your eye, the rocks organically begin to pulse alongside the rhythm of your exhausted body."
    menu:
        "Calm yourself down.":
            thought "You take a deep breath and put a hand on a nearby rock to steady yourself.  Immediately you spring back from the contact."
            thought "Instead of touching a rough surface underneath your palm, you are instead greeted with thin protruding lines."
            thought "They’re almost like spiderwebs sticking out from the rocks, but within that brief moment of contact, you could’ve sworn you felt…a pulse? They almost look like…"
            menu:
                "veins":
                    thought "You glance down at your own inner arm, the weak light of your flashlight illuminating your skin. The pattern on the rocks match the spindly contours of your veins. You shiver."
                    jump SepStayOrContinue
                "a weird rock formation":
                    thought "You shake your head, dismissing whatever bizarre connection your brain was about to make."
                    jump SepStayOrContinue
        "Take a closer look.":
            thought "You squint, convinced your eyes were playing tricks on you. This place had to be playing tricks on you, right? Rocks didn’t move like that. Actually, rocks just don’t move on their own in general"
            jump SepStayOrContinue
label SepStayOrContinue:
    if SepStayVar == 0:
        $SepStayVar += 1
        menu:
            "Stay a moment longer, looking around the room.":
                thought "You notice a piece of trash on the floor; a crumpled soda can."
                menu:
                    "Pick it up.":
                        thought "You pick up the can; even in a place as unpleasant as this, there shouldn’t be trash laying around. Pollution sucked no matter where it was."
                        jump SepStayOrContinue
                    "Leave it.":
                        thought "You shake your head. You don’t want to carry around a piece of gross trash; this place was already unpleasant enough."
                        jump SepStayOrContinue
            "There’s a path at the end of the cavern; the opening is small, barely shoulder width. You start toward it.":
                jump SepUpperIntestines
    if SepStayVar == 1:
        menu:
            "There’s a path at the end of the cavern; the opening is small, barely shoulder width. You start toward it.":
                jump SepUpperIntestines
label SepUpperIntestines:
    scene bg tightsqueeze
    thought "You kneel before the small opening and peer inside, seeing that there will be hardly any room to move."
    play sound "mediumheartbeat.ogg" loop
    play audio "rockscrapingv2.ogg" loop
    thought "Taking a deep breath, you crawl into the tunnel, feeling the walls lock you into the passageway. Your knees have no room to bend, so you drag your feet across the floor and inch your way across."
    stop audio
    thought "For a moment, you stop to breathe, but feeling the heat of your breath reflecting off the frontal wall only causes panic to rise."
    play music "heavybreathing.ogg" loop
    thought "Breathe. You must breathe."
    thought "Being reminded to breathe makes your mind aware of your lung’s inability to work on their own now. You must focus."
    thought "Your breath is kept at a steady pace to fight against the panic in your racing heart. You want to turn back. You should turn back."
    play audio "rockscrapingv2.ogg" loop
    thought "Upon trying to shuffle backwards you find that your body has subconsciously leaned your torso forward. Trying to move back feels contradictory to the way you’ve been positioned."
    thought "As you continue to shuffle through the crevice, you feel the slight breeze of an opening. Your anxieties lessen for a moment, allowing you to retain your composure."
    thought "You continue to shuffle forward, finally latching your hand to the corner of the exit."
    stop audio
    stop sound
    stop music
    jump SepHallOfFaces
label SepHallOfFaces:
    scene bg blacksquare
    thought "Grabbing to the exterior wall, you begin to pull yourself closer to the exit. Your other arm reaches out the thin passageway, allowing the leverage to pull your head out."
    thought "Then your torso. Finally, your knees bend and push their way out, until you fall to the floor."
    thought "You take a deep breath in, slightly proud that you made it through in one piece."
    thought "In the corner of your eye, you see a face."
    thought "There should be no one here."
    thought "A slight gasp escapes as you jump back. You raise your phone flashlight to illuminate the room."
    thought "You lock eyes with the sculpture of a head, no, a face carved out of the wall. Upon looking around, you see the faces that line the walls."
    thought "Though no two are looking in the same direction, you can’t help but feel disturbed by their presence."
    menu:
        "Look around more.":
            thought "You notice an empty plastic water bottle that someone has wedged into a crack in the wall."
            menu:
                "Pick up the trash.":
                    $trashcounter += 1
                    thought "You reach up and pry the trash free. Who had left this down here?"
                    jump smally
                "Leave it be.":
                    thought "You dismiss it, and turn back the way you came."
                    jump smally
label smally:
    scene bg partyroomempty
    "You find yourself back at the crossroads from before. You look down the three branching tunnels, wondering where to go next."
    jump SepPaths

label SepRendezvousPoint:
    play sound "echofootsteps.ogg"
    scene bg partyroomempty with dissolve
    thought "You finally make it back to the rendezvous point. An empty, silent cavern greets you."
    thought "Where were the others? You cast your flashlight beam around the space, but see nothing except stone walls and stalagmites."
    thought "Shifting uneasily, you bite your lip. This whole thing just isn’t sitting right with you."
    thought "Something about this cave leaves you feeling unsettled , in more ways than one. Maybe it was time to get the hell out of this place."
    menu:
        "Leave the cave.":
            play sound "echofootsteps.ogg" fadeout 0.5
            thought "You can’t take this place anymore. You turn to make your way back through the passages and rooms, ignoring the jab of guilt at leaving your friends behind in the cave."
            play sound "footstepsnormal.ogg" fadein 0.5
            thought "They should be fine–they were probably all together somewhere down there. Sooner or later they would reach the same conclusion you did and leave."
            thought "You climb until you see the faint rays of daylight from the mouth of the cave."
            jump Ending4
        "Go looking for your friends":
            thought "You can’t leave your friends behind. But sitting alone in the cavern is sending shivers down your spine."
            thought "But where were they?"
            thought "Suddenly, you hear something. Was that….your name? You listen."
            thought "You could’ve sworn you heard something, and as you shine your light through the branching paths, you notice something you didn’t before; another passage."
            thought "This one has a narrow mouth, barely bigger than a bowling ball. You have  a thin build; chances are you could probably fit."
            thought "You could see from the entrance a bit, and you notice the tunnel sharply twists less than a few feet inside–almost like a corkscrew. You swallow."
            claire "Hello??? Is anyone else there?"
            claire "Chance? Robbie? Rey? Anyone?"
            rey "Hey! I’m"
            chance "Over here, come"
            robbie "This way!"
            jump Corkscrew
label Ending4:
    scene bg cavetitlescreen
    thought "Claire is separated from Robbie, Rey and Chance within Hellmouth caves. Spooked by the strange atmosphere of the caves, Claire leaves by herself."
    thought "What happens to Robbie, Rey and Chance is unknown."

label Corkscrew:
    scene bg tightsqueeze
    thought "Sucking in your stomach, you squeeze yourself into the corkscrew, inching down with staggered movements."
    thought "The jagged edges of the rock pull at your shirt until all you can see is the stone in front of you and the glaring light of your phone."
    thought "As you proceed down, the rock walls on your back and stomach tighten until breathing no longer feels like second nature, but you must remain calm."
    thought "Is the passage getting looser? No, the wall pressing against your back is as close as before, though there is some elasticity in the material."
    thought "Instead of the sharp rocks grabbing hold of your body, you feel it begin to organically mold to your shape."
    thought "You take a deep breath, allowing your stomach to expand in the tight space, but the wall in front begins to move with you as well. "
    jump Corkscrew2
label Corkscrew2:
    if callout == 0:
        menu:
            "Call out for help":
                thought "The air sucked in by a deep breath is all released at once as you cry out for help, but your heart sinks at the sound of your voice echoing back at you. "
                thought "There’s not enough agency in the space in order to move your head up, but staining your eyes far enough allows you to see that the entryway has been closed off."
                thought "Not by rock, however, but rather by a convulsing substance that tries to deceive your vision into believing that it is a rock formation."
                # callout += 1
                jump Corkscrew2
            "Continue climbing":
                thought "You reach for the next available area to grab ahold of, but your hand retracts with a moist substance."
    if callout == 1:
        menu:
            "Continue climbing":
                thought "You reach for the next available area to grab ahold of, but your hand retracts with a moist substance."
                thought "The convulsing nature of the walls around you allows the ability to conclude what your mind can't seem to comprehend."
    thought "This is blood."
    thought "Stay calm. Stay calm. Stay calm."
    thought "You go to take another reassuring breath in to find that not only does the organic wall not move, but rather it begins to press in on you. You need to…"
    menu:
        "Scream for help":
            $corkscrewstom += 1
            thought "With whatever air your lungs gather, a cry that can be considered a scream{nw}"
            play sound "celinescream.ogg"
            thought "With whatever air your lungs gather, a cry that can be considered a scream{fast} pours out of your mouth."
            thought "The walls begin to tremble, closing in tighter. Your hands lose their grip on the ledges, and your legs hang in freefall as this being squeezes you in its grasp."
            thought "The pressure relieves a small crack in your sternum as it locks you in place."
            thought "You feel your heart sink as the flesh-like walls begin to convulse around your body, pushing you down through its system."
            thought "Centimeter by centimeter…"
            thought "Then inch by inch…"
            thought "Then feet by feet…"
            thought "this place begins to swallow you."
            jump Stomach
        "Climb":
            thought "You continue to climb down, allowing your breathing to become a rhythmic pattern to keep your sanity afloat."
            thought "Breathe in. Breathe out."
            thought "Your lungs feel heavy in your chest as you feel them expand and contract mechanically to avoid hyperventilation. "
            thought "You reach for another ledge but find your hand wrapped around a mass of the organic substance. The liquid oozes between your fingers, and the walls tremble, closing in tighter. "
            thought "Your legs hang in freefall as this being squeezes you in its grasp, but you do not lose your grip."
            thought "The pressure relieves a small crack in your sternum as it locks you in place."
            thought "However, you do not lose grip of the mass. With a pull, the organic walls begin to shift, allowing you passage down its system."
    menu:
        "Scream for help":
            $corkscrewstom += 1
            thought "With whatever air your lungs gather, a cry that can be considered a scream pours out of your mouth."
            thought "The walls begin to tremble, closing in tighter. Your hands lose their grip on the mass as this being squeezes you in its grasp."
            thought "You feel your heart sink as the flesh-like walls begin to convulse around your body, pushing you down through its system."
            thought "Centimeter by centimeter…"
            thought "then inch by inch…"
            thought "then feet by feet…"
            thought "This place begins to swallow you."
            jump Stomach
        "Climb":
            thought "Breathe."
            thought "Even if the walls press against your torso in a way that restricts the inflation of your chest, you must keep these shallow breaths consistent."
            thought "Grabbing another mass, you curl your fingers and dig into it."
            thought "The liquid has now not only soaked your hand but drips down your sleeve as the rest of the walls begin to soak your clothes in the same warm substance."
            thought "In one strong tug, you continue to pull yourself through this being’s body. In the corner of your eye, you see an opening."
            thought "The desperation to get out encompasses you, pleading for you to panic."
            thought "But you won’t."
            thought "Breathe. Breathe. Breathe."
            thought "You grab a hold of a mass and, in one last dug, get closer to the opening."
            thought "Your arm reaches through it, feeling the open space on the other side."
            jump Womb

label Womb:
    notreyvar += 1
    scene bg fleshhole
    thought "You shudder, and with one last burst of strength, you lurch your body forward and tumble from the tunnel, landing in a heap on the ground."
    thought "You look up and nearly jump straight out of your skin."
    show Rey_M_Default at m
    thought "Rey is standing in the center of the room, watching you quietly."
    claire "Rey? What-what are you doing here?"
    thought "She stares right through you, only looking up and meeting your eyes when you walk closer."
    claire "Rey? What are you-"
    notrey "Oh, hello."
    thought "Her voice sounds somber, almost tired, like she had just finished crying."
    claire "Hi? C’mon Rey, stop acting weird, why are you down here?"
    hide Rey_M_Default
    show Rey_M_Smile at m
    thought "As you ask her again, she offers what seems like a forced smile and continues. "
    hide Rey_M_Smile
    show Rey_M_Default at m
    notrey "I was looking for you, and the rest of our group. Not sure how I got here…"
    claire "Ah, yeah me too…"
    claire "I wonder if Chance and Robbie are lost too, or if they’re looking for us."
    thought "Rey stares at you, blankly."
    claire "Um… so, do you want to try to find a way out? Maybe if we-"
    notrey "Mm, follow me."
    claire "Oh do you know a way ou–hey! Rey?"
    hide Rey_M_Default
    play sound "footstepssquishy.ogg"
    thought "She runs off, making no attempt to check on you before doing so."
    claire "Hey, slow down! Rey!"
    thought "If she hears you, she does not respond."
    scene bg fleshcavealt2
    thought "The two of you go deeper into the cave, passing by a few different tunnels and narrow rooms, all of which she avoids."
    claire "Hey uh, are you sure this is the right way?"
    notrey "…"
    thought "The walls feel like they’re closing in, and each step you take progressively sounds moister than the last."
    thought "You watch as Rey pushes past a curtain of some thin, flesh-looking substance, red liquid staining her hands."
    thought "She turns around and looks at you as a thick droplet of it lands on her face, but instead of freaking out, she stays completely silent and motionless."
    claire "Rey, can you at least tell me where we’re going?"
    notrey "We’re heading out."
    thought "She steps close to a passage that’s lower to the ground, looks back at you, and walks into it."
    menu:
        "Follow Rey":
            thought "You follow after Rey, a strange feeling in your stomach. She must have been moving fast, because you don’t catch sight of her ahead of you."
            thought "Fifteen paces in, the ceiling starts to slant sharply downward. You crouch, and then eventually go to your hands and knees."
            thought "The walls seem to constrict around you until you're flat on your stomach, army crawling forward."
            thought " You regret choosing this path as you feel the back of your head knock against the low ceiling, the distance between it and the floor barely a foot in height."
            thought "But there wasn’t any space to turn around, so you continue ahead."
            claire "Rey? Are you there? Slow down, I don’t want to lose you."
            jump Stomach
        "Hesitate":
            thought "You watch Rey crawl through the low passage, but your feet don’t move. For some reason, something doesn’t sit quite right with you."
            thought "Before you have a chance to second guess yourself, you trust your gut and hurry forward  to slip into a tunnel off to the side."
            thought "You hear voices up ahead, and tense for a moment."
            claire "Is someone there?"
            jump SafeZone

label SafeZone:
    scene bg cave
    claire"AH"
    show Rey_N_Nervous at r
    show Robbie_N_Default at l
    claire "Oh my god! There you are, we were worried about you!"
    hide Rey_N_Nervous
    show Rey_N_Default at r
    rey "Claire!!! Oh my god you made it! Where were you?! We were all waiting here and I was worried sick and we didn’t know if you got lost or-"
    robbie "It’s just me and Rey right now, Chance is still out exploring."
    if notreyvar == 1:
        claire"Wait… Rey? I thought you were…"
        rey "Hm? Thought I was what?"
        claire"You were ahead of me- and you were acting all weird and stuff and-"
        hide Rey_N_Default at r
        show Rey_N_Nervous at r
        thought "Rey looks confused, and shakes her head at you while looking concerned."
        rey "Claire I’ve been here for a while, Robbie can attest to that."
        thought "You mention everything you saw with Rey in the other room, and at the mention of the bloodied hands, Rey raises hers. Clean, other than a few scrapes."
        rey "Look, I’m all good."
        claire"Who...or what, did I follow then, I–"
        thought "Your friends stand around awkwardly, a bit of tension in the air as all of you try to understand what happened, before moving on."
    claire"How did you guys get here? This cave is so weird, I was worried I wouldn’t be able to find you all."
    hide Rey_N_Nervous 
    show Rey_N_Smile
    rey "Mm, I definitely got lost for a while… and I was hearing all these weird noises, but eventually I ran into Robbie! Definitely a sight for sore eyes!"
    claire"How about you, Robbie? How was your solo adventure?"
    hide Robbie_N_Default
    show Robbie_N_Awkward
    thought "Robbie's face goes white."
    robbie "Oh uh- hah I-"
    claire"...are you okay?"
    robbie "So funny story… I uh, thought I had {i}already{/i} ran into you guys. I ran into Claire- or someone I thought was Claire, but you–I mean, {i}she{/i}, was acting REALLY weird. She never laughed? Or breathed, I think?"
    hide Rey_N_Smile
    show Rey_N_Nervous
    claire"Robbie…this is the first time I’ve seen you since we separated to explore."
    robbie "Then who the hell was {i}that{/i}?? She looked almost identical to you! I heard the rest of you guys nearby, talking and laughing and–and I thought I was safe, I thought we were all okay, but she just kept {i}looking{/i} at me and-"
    claire"You’re okay, alright? We’re all here and we’re all ourselves. Normal."
    robbie "Ok, yeah. Yeah! We’re all good, sorry about that."
    rey "We’re all okay, calm down. I think this cave is just–messing with us."
    claire"Yeah, we need to get out of here, and soon. This place isn’t safe to be in, and I don’t wanna think about what could happen if we stay any longer. Something weird is going on."
    robbie "What makes you think that? The flesh walls? The fake voices? The fake {i}people{/i} or–or {i}whatever{/i} they are?"
    claire"All of the above. This place is some horror movie shit."
    claire"We can question what the hell is happening later, but for now, let’s just find Chance and figure out how to get out of here."
    chance"Ah- about that."
    rey "Hmm?"
    chance "When I was exploring, I thought the path would loop back around, like some other caves I’ve been in."
    chance "But…when I got to what I thought was the path back, it was covered in rubble and rocks. So that couldn’t have been it."
    robbie "No… uh. I think that is, or, was, the entrance."
    claire "What? What do you mean?"
    robbie " I went that way too, earlier. I saw the way we came from, and I watched as something fell or like- shifted? And then the entrance was covered in rocks."
    rey "Are we stuck here?"
    chance "Fuck, that’s. Uh. "
    rey "ARE WE STUCK HERE?"
    robbie "I-I don’t know. We could go check? Maybe I was wrong? "
    chance "There has to be some way out. There has to be. "
    rey "What should we do?"
    menu:
        "Flee":
            claire "Let's get out."
            chance "And if the route is blocked off?"
            claire "…Let’s just hope it isn’t."
            jump Flee
        "Reason":
            jump Reason

label Flee:
    thought "Together, you swiftly make your way back to the mouth of the cave system. Or…what you remembered to be the mouth."
    thought "Chance was right."
    thought "All that is in front of you now was a large rock, jammed into the space that would’ve been the entrance. And your only exit."
    claire "What the fuck."
    robbie "Did we go the right way? This has to be it, right?"
    chance "It is, I made sure."
    rey "There’s no way a cave-in could’ve happened, right? We would’ve heard it!"
    claire "Uh, no we- there’s some way out."
    robbie "This fucking cave…"
    rey "We should’ve never come here!"
    chance "God- are we…stuck?"
    rey "Oh god. We’re stuck here."
    claire "Everyone, stay calm, there’s. Something. Something we can do."
    thought "There’s no way we’re just trapped here."
    thought "Right?"
    jump Ending12:

label Ending12:
    show everybodydied
    window hide
    pause
    thought "Claire is reunited with Chance, Rey and Robbie within Hellmouth caves."
    thought "Upon trying to flee the caves, they discover the only known exit is unexplainably blocked. All four friends remain trapped inside the cave."

label Reason:
    thought "still finishing..."

label Stomach:
    scene bg fleshcavealt1
    if corkscrewstom == 0:
        thought "You squirm through the final twist, your hips at an uncomfortable angle that makes a pain throb up your spine."
        thought "The air begins to feel warm and damp, and a strange smell stings your nostrils; almost acidic, with the metallic undertones of rotting flesh."
        thought "You swallow down  the urge to gag, and wiggle out onto the flat floor. You bend your knees to pull your legs free, swinging them around to–"
        thought "You jolt, adrenaline flooding through every part of your body as your legs dangle into open air."
        thought "A scream is pushed down as you realize the thing you thought was floor was actually a narrow ledge, barely foot wide before it drops off into gaping nothingness."
        claire "Rey? Rey?!"
        thought "You quickly turn around, hoping to spot your friend. In a split second, you see the grin of your friend begin to meld into a nearby wall until it disappears altogether."
    if corkscrewstom == 1:
        thought "Tears stream down your face. You want to continue screaming, but the convulsing walls leave no forgiveness for you."
        thought "You’re only able to suck in small gasps of air that tremble out in the whimpers of your cries."
        thought "You feel the walls begin to loosen, slipping you down the passageway. "
        thought "In one sudden convulsion, the walls open, dropping you for what feels like hours, but in reality is probably no more than a couple seconds."
        thought "The air begins to feel warm and damp, and a strange smell stings your nostrils; almost acidic, with the metallic undertones of rotting flesh."
        thought "You swallow down  the urge to gag, and stand onto the flat floor. Everything in you screams to run. Run as fast as you can."
        thought "You briefly try to run, adrenaline flooding through every part of your body, but rapidly stop yourself as you find there is no more space in front of you."
        thought "A scream is pushed down as you realize the thing you thought was floor was actually a narrow ledge, barely foot wide before it drops off into gaping nothingness."
    thought "You’d reached a pit, yawning in front of you like a horrid black void."
    if corkscrewstom == 0:
        menu:
            "Go back":
                jump Backtrack
# if corkscrewstom == 1:
label Backtrack:
    scene bg cave
    thought "You backtrack through the passage, keeping your breathing as steady as you can. But you must’ve taken a wrong turn somewhere because the cavern you suddenly find at the end of the tunnel isn’t the same one you came in through."
    thought "You hear a rustle and tense."
    claire "Is someone there?"
    jump SafeZone
label StomachA:
    scene bg fleshcavealt1
    thought "You precariously shuffle away from the edge, but there isn’t anywhere to go, short of backtracking through the tight passage you just came through."
    menu:
        "You decide to go back.":
            jump Backtrack
        "You don't want to go back through that awful passage. Looks like you're working with what you got.":
            jump StomachB
label StomachB:
    scene bg fleshcavealt1
    thought "You idle on the edge, looking around. Apart from the ledge you’re sitting on, there’s nothing else protruding from the curved walls, and no other opening that you can see."
    thought "The smell of rancid meat is almost overpowering, and you cover your mouth with one hand, eyes water."
    thought "The movement causes a wayward rock to skitter off the ledge and into the pit, and you hold your breath to see if you can hear when it lands."
    thought "..."
    thought "Seconds pass. You don’t hear the rock land, but you do hear something else. It sounds like…voices?"
    if corkscrewstom == 0:
        thought "Had Rey fallen down there? Was she hurt?"
    menu:
        "You decide to go back.":
            jump Backtrack
        "You stay for a moment longer":
            jump StomachB2
label StomachB2:
    scene bg fleshcavealt1
    thought "You lean in closer. Yes, voices. They weren’t saying words, but muted groans and stuttering gasps."
    if corkscrewstom == 0:
        thought "It didn't sound like Rey, but..."
    if corkscrewstom == 1:
        menu:
            "You decide to go back.":
                jump Backtrack
            "Call out for help":
                claire "Hello! Is someone there?"
                jump StomachB22
    if corkscrewstom == 0:
        menu:
            "You decide to go back.":
                jump Backtrack
            "Call out for help":
                claire "Hello! Is someone there?"
                jump StomachB22
label StomachB22:
    scene bg fleshcavealt1
    thought "Your words are swallowed up in the heavy moist air. You’re beginning to sweat due to the smothering warmth of the chamber. Your hands are slick as they grip the ledge beneath you and you lean forward more. “Hello–is anyone down th–"
    thought "Your hands slip on the stone ledge, and your balance is lost. A scream tears loose from your throat as you fall into the pit, your phone flashlight sliding from your hand." with sshake
    thought "..."
    scene bg blacksquare with fade
    jump StomachB22B
label StomachB22B:
    scene bg blacksquare
    thought "You aren’t sure how long you fall, but you expect to be dead when you hit the ground, anticipating hard stones or stalagmites that will spear you through."
    play sound  "bonesandflesh.ogg"
    thought "Instead, you land on something that squelches loudly when your body makes contact with it."
    thought "Your phone flashlight has gone out, lost somewhere out of reach."
    play sound "bubbles 2.ogg" loop volume 0.2
    thought "In the dark, you hear the sound of something bubbling, and realize you’re sitting in warm standing liquid. Your whole body is tingling."
    thought "Your breathing escalates."
    thought "A noie comes from your left and you jump. it's a voice, weak and gasping."
    stranger "H-help me…"
    stop sound fadeout 2.0
    if corkscrewstom == 0:
        thought "This definitely wasn't Rey. Where had she gone?"
    thought "You tentatively reach out, and feel the rough fabric of a backpack and what seems like metal carabiners and a length of rope. A cave diver?"
    claire "Hello? Who are you? How long have you been down here?"
    diver "Help…help…please…"
    claire "Are you hurt?"
    thought "The tingling on your skin is getting worse. You continue to fumble in the dark, and the next thing you touch is something smooth and long, its base covered in spongy material."
    thought "The cave diver groans. It almost feels like a chicken drumstick in its shape, and you laugh at the incredulity of it. "
    claire "What's this?"
    diver "...t-the liquid ...my leg..."
    claire "Your {i}leg?{/i}"
    thought "You feel over the smooth part again. It’s too hard to be flesh. Feeling more reveals that it curves slightly, almost like–"
    thought "-like a bone.{fast}"
    thought "Despite the warm liquid around you, your blood runs cold. Your hand touches the spongy part again, feeling loose flaps of–"
    thought "The smell of rotting meat is stronger down here."
    thought "You suck in a breath. No. No. No."
    thought "Your hand smells metallic."
    diver "The liquid…"
    thought "The diver groans again."
    thought "The tingling is beginning to burn against your skin. No. No. No."
    thought "You jump to your feet, the liquid sloshing around you." with sshake
    thought "It comes up to just below your knees, {nw}"
    play sound "footstepssquishyv2.ogg"
    thought "It comes up to just below your knees, {fast}and you awkwardly run until your hands smack up against a wall that feels springy and wet."
    thought "You feel for a handhold, a dip, anything you could grab to climb up."
    thought "There’s nothing."
    thought "No. No. No."
    thought "The burning is getting worse.  How did you get into this position? You should’ve turned back while you could. You should’ve never come to this cave in the first place. You begin to cry."
    jump Ending11

label Ending11:
    scene bg blacksquare
    show nobodyDied
    window hide
    pause
    thought "Claire falls into an inescapable pit within Hellmouth caves. She is consumed by some strange liquid. The fate of Robbie, Rey and Chance is unknown."
    return
