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

default Mimic = 0
default trashcounter = 0
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

                    
define thought = Character("", what_italic=True)
define claire = Character("Claire", color="#005BFF")
define rey = Character("Rey", color="#FFEC24")
define notrey = Character("Rey", color="#FFEC24")
define robbie = Character("Robbie", color="#EA9807")
define stranger = Character("Stranger")
define chance = Character("Chance", color="#EA2F07")

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
image Chance_N_Default = "Chance_N_Default.png"
image Chance_N_Scared = "Chance_N_Scared.png"
image Chance_N_Question = "Chance_N_Question.png"
image Chance_N_Happy = "Chance_N_Happy.png"
image Chance_N_Guilt = "Chance_N_Guilt.png"
image Chance_M_Default = "Chance_M_Default.png"
image Chance_M_Happy = "Chance_M_Happy.png"
image Chance_M_Scared = "Chance_M_Scared.png"
image bg splashscreen = "splashscreen.png"
image cavemap = "hellmouthmap.png"

###----------------THE GAME STARTS HERE----------------###
label start:
    jump Welcome

#Intro Screen
label Welcome:
    thought "Welcome to Hellmouth Caves."
    thought "This game is designed to emulate the HellHole caves on the UCSC campus–with a little bit of a twist. You’ll be playing as {i}Claire{/i}, a college student that has dared to enter the cave with her group of friends."
    thought "If at any point you feel lost, confused, or unsure about how to proceed, the best advice is (just as in real cave exploration); take a moment and observe your surroundings, or in this case, what the story is trying to tell you."
    thought "Best of luck in your exploration."
    thought "You’ll need it."
    jump ContentWarning

label ContentWarning:
    thought "Content Warning: This game features graphic depictions of body horror and claustrophobia that may not be agreeable for some viewers. Proceed Appropriately."
    jump Mouth

label Mouth:
    scene bg blacksquare
    play sound "echofootsteps.ogg" volume 0.4
    play music "footstepsreverb.ogg" loop volume 0.8
    claire "Hey, who brought the flashlight?"
    robbie "Oooh, is someone scared of the dark?"
    claire "I just can’t see anything."
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
    scene bg cave
    show Rey_N_Default at r
    show Robbie_N_Default at l
    show Chance_N_Default at m
    thought "Someone turns on a flashlight, revealing the space around you. The cavern is tight, but the four of you have managed to squeeze inside." 
    thought "Below your feet is a small tunnel, about the width of a manhole, leading into the depths of the cave."
    hide Robbie_N_Default
    show Robbie_N_Cheeky at l
    robbie "Welcome! To Hellmouth Caves."
    rey "..."
    claire "..."
    chance "..."
    hide Robbie_N_Cheeky 
    show Robbie_N_Default at l 
    robbie "Okay, I was expecting a bigger reaction to that. Come on guys, it’s an adventure! One last hurrah before graduation with the ol’ gang!"
    hide Rey_N_Default
    show Rey_N_Question at r
    rey "You’re so dramatic."
    hide Rey_N_Question
    show Rey_N_Smile at r
    claire "You thought cave spelunking would be a good bonding experience??"
    robbie "C’mon Bro, back me up!"
    chance "Hey, I’m for it. I like a little challenge."
    robbie "That’s the spirit! Come on Claire, get on board! And Rey, don’t look so nervous. Here, I brought a map and everything."
    show cavemap at t with dissolve
    robbie "It’s decently accurate."
    hide Rey_N_Smile
    show Rey_N_Nervous at r
    rey "Decently?"
    robbie "Well come on, would that guy downtown really sell me a defective map? Like, who even does that?"
    thought "Robbie looks down at the map he’s holding and squints, before turning it on its side and staring at it."
    robbie "…It’s probably fine."
    claire "Oh god, what sort of shitshow did we sign up for?"
    hide Rey_N_Nervous
    show Rey_N_Default at r
    hide map
    chance "We should be fine guys, and anyway, we probably won’t even need a map! You guys have got me, and I’ve tackled more difficult caves in my sleep!"
    robbie "Uh huh. Yeah I’m still using the map."
    rey "Well, I hope at least one of you knows their way around, cuz Claire and I don’t have a clue…"
    claire "You can say that again, I don’t know how easy it’ll be to navigate in those tight tunnels. I really wouldn’t be doing this if it wasn’t for you guys."
    rey "Hey… if you want we could head back? Maybe try for another time-"
    robbie "No way!! This is the one day we have the time to do this,, c’mon I promise it’ll be fun!"
    hide Rey_N_Default
    show Rey_N_Speechless at r
    rey "Robbie! If Claire's not up to it we shouldn't ofrce her to do this"
    hide Robbie_N_Default
    show Robbie_N_Awkward at l
    robbie "Right, right, sorry my bad."
    claire "Thanks Rey, but I should be fine. I’ve got you and the boys here, it’ll be fun, I promise!"
    hide Robbie_N_Awkward
    show Robbie_N_Default at l
    chance "Yeah! As long as you all stick by me, everything will be perfect."
    thought "As Chance says this, he looks over at Rey and, very obviously, winks at her. She turns to look away, a small blush spreading across her cheeks."
    robbie "C’mon! I can’t keep waiting like this, I wanna see what all’s in there!"
    thought "Robbie folds up the map, and starts climbing down the tunnel at your feet. Even as his head dips below the tunnel entrance, you can hear him laughing and shouting up at the group."
    rey "Ah- Robbie! Wait for us! You have the map you idiot!"
    claire "Rey, make sure he doesn’t fall down into a bottomless pit, would you?"
    thought "Rey smiles and nods, before climbing down after him, leaving you and Chance lagging behind."
    jump Trash

label Trash:
    thought "As you prepare to descend into the hole, Something glints in the light of your phone flashlight. You squint, and in the corner of the tight space, right by Chance’s foot, is a glass beer bottle."
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
    chance "Pff, {i}really{/i}? Wow Claire, I didn’t know you’re suddenly an eco warrior now."
    claire "Come on, it’s not weird to treat nature with respect and stuff."
    chance "Ok, whatever you say Captain Planet."
    chance "Just hurry up alright?"
    jump Throat

label Throat:
    play music "caveroomtone1.ogg" loop if_changed volume 0.2
    if trashcounter < 1:
        scene bg blacksquare
        thought "You tear your gaze away from the litter, and drop down into the manhole after Rey."
    thought "The tunnel extends into a deep downward slope, which doesn’t make it easy to progress through."
    scene bg tightsqueeze
    thought "Above you, Chance is holding his flashlight with his mouth, and the unsteady light illuminates the tight crevice."
    thought "You’re able to shove your toe  into a ledge for a bit of leverage as you descend. Chance begins to descend too, and steps on your hand more than once."
    thought "Below you, Rey is in a similar position, arms and legs spread like a starfish to stay wedged in place. And below her is Robbie, casually leading the way."
    thought "His reassured voice echoes throughout the cavern, giving words of advice as his body naturally navigates through the squeeze. "
    scene bg cavealt with dissolve
    show Robbie_N_Default at r 
    show Rey_N_Default at m
    show Chance_N_Default at l
    thought "Eventually, you begin to see your friends turn and pull their way out of the climb. As you step out, you see Robbie staring at the map."
    claire "Everyone good? Why are we all just standing around?"
    rey "We’re at a fork in the road. Or, cave, I guess."
    hide Robbie_N_Default
    show Robbie_N_Cheeky at r
    robbie "Also a fork is normally when it splits into two, and this one has three paths."
    hide Rey_N_Default 
    show Rey_N_Speechless at m
    hide Robbie_N_Cheeky at r 
    show Robbie_N_Default at r
    rey "...dude shut up."
    hide Chance_N_Default
    show Chance_N_Question at l
    chance "What does the map say, Rob?"
    hide Rey_N_Speechless
    show Rey_N_Default at m
    hide Robbie_N_Default
    show Robbie_N_Question at r
    robbie "Let me look..."
    thought "As he checks the map, you take a moment to sneak a glance for yourself."
    show  cavemap at t 
    thought "None of the paths seem particularly different from each other, but when the room falls silent you’re able to pick up on a few faint details."
    hide cavemap
    hide Robbie_N_Question
    show Robbie_N_Default at r
    hide Chance_N_Question
    show Chance_N_Default at l
    rey "The way forward looks pretty normal? Let’s take that."
    hide Chance_N_Default
    show Chance_N_Happy at l
    chance "Really? It looks so boring, the left and right paths seem more mysterious!"
    hide Robbie_N_Default
    show Robbie_N_Question at r 
    robbie "Mm, they seem cool, but the middle one has tons of graffiti and junk on it. It could be like a secret party room or something!"
    claire "Hmm… Anything on the map, Robbie?"
    hide Chance_N_Happy
    show Chance_N_Default at l
    hide Robbie_N_Question
    show Robbie_N_Default at r
    robbie "Nah, no matter which path we take, they all go on for a while. I don’t know if we’d be able to explore all of these together…"
    chance "What if we split up? We could check each one ourselves, and that way it would be more of a challenge!"
    hide Rey_N_Default
    show Rey_N_Speechless at m
    rey "You need {i}more{/i} of a challenge? Really?"
    hide Chance_N_Default
    show Chance_N_Happy at l
    chance "C'mon, it would be fun!"
    hide Robbie_N_Default
    show Robbie_N_Cheeky at r
    robbie "It would be fun..."
    rey "No! What if we get lost or something?"
    hide Robbie_N_Cheeky
    show Robbie_N_Default at r
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
    jump Paths:
label Paths:
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
label StayTogetherLeft:
    claire "I wonder where all that wind is coming from."
    hide Rey_N_Default
    show Rey_N_Smile at m
    rey "Me too! I definitely don't mind cooling off a bit, hehe."
    jump Lungs
label StayTogetherRight:
    play sound "mediumheartbeat.ogg" volume 0.25 loop
    claire "What's with the vibrations from over there?"
    hide Chance_N_Default
    show Chance_N_Happy at l
    chance "I don't know! Let's check it out."
    jump Heart
label StayTogetherMid:
    claire "How about just going straight ahead?"
    hide Robbie_N_Default
    show Robbie_N_Awkward at r
    robbie "Not having to squeeze into one of the others sounds good, yeah."
    jump PartyRoom

label Lungs:
    scene bg tightsqueezeflip
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
            jump GoBackExplore
        "Leave it be.":
            jump GoBackExplore

label PartyRoom:
    hide Rey_N_Smile
    hide Robbie_N_Awkward
    hide Chance_N_Default
    scene bg blacksquare
    play sound "clothingshufflev3.ogg" volume 0.2
    play voice "rockscrapingv1.ogg" volume 0.5
    thought "You turn sideways to shuffle through the narrow passageway, feeling the rock cling to your back."
    stop sound
    stop voice
    play sound "rocksfallingv2.ogg"
    play voice "footstepsreverb.ogg"
    thought "The sound of your friend’s footsteps fills up the space alongside the falling pebbles that come off the walls as your bodies inch through the passageway."
    scene bg partyroom with AlphaDissolve
    show Robbie_N_Default at m
    show Rey_N_Default at l
    show Chance_N_Default at r
    thought "The space widens as you enter this new room with a ceiling high enough to stand upright."
    thought "Thank God–you aren’t necessarily claustrophobic, but that narrow passage you came through questioned how much of a squeeze you can truly handle."
    thought "From the light of your phone, you see graffiti spray painted on the stone walls."
    thought "Some are tags from people who have been here, messily scribbled on with Sharpie markers. Others are larger, spray-painted phrases such as “Do not enter” and “Funky”."
    thought "Upon looking down, you see a small handwritten note “Do not continue. It’s alive.”"
    hide Robbie_N_Default
    show Robbie_N_Cheeky at m
    robbie "Oh hell yeah! Finally some signs of life in here!"
    hide Rey_N_Default
    show Rey_N_Guilt at l
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
    show Rey_N_Default at l
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
            $trash += 1
            jump Flashlight
        "Leave it be.":
            jump Flashlight
label Flashlight:
    thought "You walk back over to where Rey, Robbie, and Chance are clustered."
    chance "Find anything interesting?"
    claire "Not really, no."
    hide Rey_N_Default
    show Rey_N_Nervous at l
    rey "I still don’t really know what’s up with this place. Is the graffiti just from pranksters, or…"
    hide Robbie_N_Default
    show Robbie_N_Cheeky at m
    robbie "It’s probably from dead hikers, doomed to forever haunt these caverns! OooOooOohh!"
    hide Rey_N_Nervous
    show Rey_N_Speechless at l
    rey "Shut up!!!"
    hide Chance_N_Default
    show Chance_N_Nervous at r
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
    show Chance_N_Default
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
    play sound "celinescream.ogg"
    rey "AAAAAAAAA!!!"
    thought "You and Robbie both laugh, as Rey yells at you two, and Chance stays quiet. After a pause, Robbie turns on the flashlight, the light illuminating on everyone except an absent Chance."
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
    thought "You open your mouth to suggest-"
    play sound "guyscream.ogg"
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
    scene bg blacksquare with AlphaDissolve
    scene bg partyroomempty with AlphaDissolve
    thought "The rendezvous point isn’t  far from the room you are in. A short walk later, and you’re back at the check-in spot. Still no Chance. The three of you wait in silence for a few minutes."
    thought "Every distant echo in the cave makes you hold your breath. But Chance never appears."
    claire "Wherever he is, I don't think he's around here."
    rey "God, do we need to go get help? Maybe we should levae and come back?"
    robbie "No no, I don't think it's that serious! He's probably fine, just adventuring away deeper in the cave."
    rey "Claire, what do you think?"
    menu:
        "Leave the cave and go seek help.":
            jump PlayAlongA
        "Stay in the cave and look for Chance.":
            jump PlayAlongB
label PlayAlongA:
    claire "We clearly don't know this cave that well. If he really is missing, we need professional help."
    hide Rey_N_Nervous
    show Rey_N_Default at r
    rey "No I agree. Chance was the most experienced out of all of us, and if he’s lost? Then I don’t know about our odds."
    robbie "We don't even know if he's lost..."
    hide Robbie_N_Question
    show Robbie_N_Guilt at l
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
    show Reu_N_Default at l
    show Robbie_N_Default at r
    scene bg cave
    thought "Your chest loosens a bit when you see daylight pierce down into the darkness, and the breeze glides on your face."
    thought "You boost Rey up first, and as she crawls through the entrance, you cast one last look back into the depths of the cave."
    thought "You see Robbie doing the same, and the two of you share a look before he nudges you with his elbow."
    robbie "Come on. Let's get moving. You said we should go get help, right?"
    thought "You nod, not only to reassure him, but to reassure yourself=. You hope Chance is okay, wherever he is."



    