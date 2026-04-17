#MCs
define ev = Character('Eira Vale', color="#3d813d") # Main character, the player will be playing as Eira Vale, a 16 year old girl 
define sk = Character('Headmistress Sable Korrin', color="#4046b7") # The headmistress of Eidolon Academy, she is a strict and mysterious woman
define lr = Character('Lucian Reed', color="#b73d3d") # Careful observer (1) calm, slightly distant, always noticing things others don’t
define mv = Character('Mira Vexley', color="#ad3db7") # Disruptor (2) chaotic, unpredictable, sharp.. always stirring the pot. (LOL THATS SUCH A WEIRD WAY TO PUT IT)
define nh = Character('Noah Halden', color ="#3db7b7") #"Echo" // emotional mirror (3) soft-spoken, emotionally reflective, empathetic, always there to listen and support others
define sl = Character('Seraphine Lorne', color ="#b7ad3d") # "Anchor" (4) calm stability in chaos (reassuring, grounded, tries to keep peace between students, follows rules… but questions them privately)
define us = Character('UNASSIGNED', color="#FFFFFF") # NULL (??) inconsistent existence.. Err0r, $ome7hin6 1$ Wr*n666
define u = Character('Unknown', color = "#FFFFFF") #Only used when a character hasn't been revealed yet!

#Eira's family
define evm = Character('Mom', color="#3d813d")
define evd = Character('Dad', color="#3d813d")

#Stats
define hunger = 10
# if hunger drops below 5 you will become hungy, if it is at 1 or 2 during a check, you will be starving, if it is 0, you will die.
define group = 0
#Group 1 = Careful Observer, Group 2 = Disruptor, Group 3 = Emotional Mirror, Group 4 = Anchor, Group 5 = Null
define mood = 0
#0 = null, 1 = happy, 2 = annoyed, 3 = upset, 4 = tired, 5 = hungry, 6 = nervous, 7 = angry, 8 = scared
define tiredness = 0
#If tiredness drops below 5, you will become tired. If tiredness ever hits zero, you will be forced to rest.
define health = 100
define proc = False


label start:
    scene home-desk:
        xysize (1920, 1080)
    #"Your health is at" + health + "This may decrease throughout the game and you will be alerted in between scenes of your current health. Please be careful, there may be consequences if you run out of it."
    "The letter arrived without a return address."
    "No seal, no signature.. It only had your name hand written perfectly in the center of the envelope."
    "You open it, and find a single sheet of paper inside. It reads: "
    " 'You Have been accepted into Eidolon Academy!' "
    " 'Congratulations! This is no easy feat Eira, and I hope to see you in the fall.' "
    " 'Your tuition is fully covered, and you will be receiving a stipend to cover your living expenses on campus as well.' "
    " 'Please report to the admissions office on the first day of classes, and be sure to bring this letter with you.' "
    "You don't remember applying, and decide to look the academy up online,"
    "Eidolon Academy is a prestigious school for the most acedemically gifted students in the world, and you have no idea how you got in."
    "As you keep reading.. You notice that there is no application process, and that the academy hand picks their students based on their potential."
    "And.. teacher reccomendations? You don't remember any of your teachers recommending you for anything, and you don't even remember most of your teachers."
    "Of course, there were over fourty students in every single one of your middle school classes."
    "You decide to call your parents, but they don't answer. You leave a voicemail, and they never call back."
    "You decide to go to bed, and hope that they will call you in the morning."

    scene home-bed:
        xysize (1920, 1080)
    "The next morning, you wake up to the sound of your phone ringing. It's your parents."
    show eira-mom
    evm "Eira? Are you home right now?"
    hide eira-mom
    show eira
    ev "Yeah, I'm home. Why?"
    hide eira
    show eira-mom
    evm "We.. we need to talk. Can you come downstairs?"
    hide eira-mom
    show eira
    ev "Sure, I'll be down in a minute."
    hide eira
    "You decide to go downstairs, to see whatever it is your parents want."
    
    scene home-lr:
        xysize (1920, 1080)
    show eira-mom
    evm "Eira, we need to talk about the letter you got yesterday."
    hide eira-mom
    show eira
    ev "You know about the letter?"
    hide eira
    show eira-dad
    evd "Of course we do. We got the same letter as you did."
    hide eira-dad
    show eira
    ev "Wait, what? You got the same letter?"
    hide eira
    show eira-mom
    evm "Yes, we got the same letter. Did you apply to this school?"
    hide eira-mom
    show eira
    ev "No, I didn't apply. I don't even know how I got in."
    hide eira
    show eira-dad
    evd "Well, we don't know how you got in either. But we do know that this school is very prestigious, and we want you to go there."
    hide eira-dad
    show eira
    ev "I don't know if I want to go there. Why do I not get to make that choice? I know nothing about the school."
    hide eira
    show eira-mom
    evm "Eira, we want you to go there. We think it's a great opportunity for you, and we want you to succeed."
    hide eira-mom
    show eira
    ev "I know you want me to go there, but I want to make that choice for myself. I want to know more about the school before I decide if I want to go there or not."
    hide eira
    show eira-dad
    evd "Eira, respectfully you're going to that school. We don't want to have this conversation anymore. We want you to go there, and that's final."
    hide eira-dad
    show eira
    ev "Fine, I'll go there. But I want to know more about the school before I go there."
    hide eira
    scene home-bed:
        xysize(1920, 1280)

    "It's been a few weeks."
    "'Today's supposed to be your first day.'"
    "'Wake up Eira.'"
    "'You need to get ready.'"
    "You cut off your alarm and get up."
    "It's 4:40AM."
    "Your bus will be there in about an hour."
    "You get out of bed and go to your bathroom."
    
    scene h-bathroom:
        xysize(1920, 1280)
    "You take a quick shower, then brush your teeth and wash your face,"
    "You hear someone call your name from downstairs."
    "'Eira!'"
    "'Are you almost ready? We need to go take you to the bus station, you're going to be late!'"
    "You hurry to finish getting ready and am downstairs by 5am."

    scene home-lr:
        xysize(1920,1280)
    "When you walk downstairs with your things, you see your mother sitting at the table drinking coffee."
    show eira-mom
    evm "Goodmorning Eira."
    hide eira-mom
    show eira
    ev "Goodmorning, mom."
    hide eira
    show eira-mom
    evm "Excited for your new school?"
    hide eira-mom
    show eira
    menu:
        "Absolutely not.":
            ev "Absolutely not, mom."
            hide eira
            show eira-mom
            evm "Well you better start to get excited. You're going weather you like it or not."
            hide eira-mom
            show eira
            ev "Trust me, I won't like it."
            $ mood = 2
        "I guess..":
            $ mood = 6
            ev "I guess I am.. I'm just a bit nervous."
            ev "I feel like there's so much that can go wrong today."
            hide eira
            show eira-mom
            evm "Maybe that's true, but you need to stay strong."
            evm "Besides, you'll always ave the opportunity to talk to me if you need!"
            hide eira-mom
            show eira
            ev "and what if i can't talk to you?"
            hide eira
            show eira-mom
            evm "Why would that even be something you're worried about? You have a phone for a reason."
            evm "And we'll call you later tonight anyway."
            hide eira-mom
        "Yeah!":
            ev "Yeah mom! This is a really good opportunity, so I'm going to make the most of it."
            hide eira
            show eira-mom
            evm "Who are you and what have you done to my daughter?"
            evm "You're being highly optomistic, which is the last thing I expected from you."
            hide eira-mom
            show eira
            ev "Why did you ask if I was excited then?"
            hide eira
            show eira-mom
            evm "It was supposed to be a rhetorical question, you were supposed to roll your eyes or something."
            hide eira-mom
            show eira
            ev "Oh.. Okay well I guess that makes sense-"
            ev "Anyway, yeah! I'm excited!"
            hide eira

    scene bus-station:
        xysize(1920, 1280)
    "You get to the bus station and wait for the bus to arrive."
    "You see a few other students waiting there, but you don't recognize any of them."
    "The bus arrives and you get on, finding a seat near the back."
    "The bus is pretty empty, and you have the whole row to yourself."
    "You decide to go on your phone to pass the time, but you don't have any service."
    show noah
    nh "Hey, do you know if this bus is going to Eidolon Academy?"
    hide noah
    show eira
    ev "Yeah, it is."
    hide eira
    show noah
    nh "Oh, cool. I-I'm Noah, by the way."
    nh "A-are you the new girl? I haven't seen you around before."
    hide noah
    show eira
    ev "Yeah, I am. I'm Eira."
    hide eira
    show noah
    nh "Nice to meet you, Eira."
    nh "What are you?"
    hide noah
    show eira
    ev "What do you mean?"
    hide eira
    show noah
    nh "Oh. You haven't picked yet.. I thought everyone had to pick before they came here."
    hide noah
    show eira
    ev "Pick? What do you mean?"
    hide eira
    show noah
    nh "you'll see.. just.. choose wisely."
    hide noah
    show eira
    ev "Okay.. is there anything else I should know?"
    hide eira
    show noah
    nh "Yeah.. ru-"
    hide noah
    "The boy infront of you seems to stop talking."
    "As if his throat closed up mid sentence."
    "He looks at you with wide eyes, and you can see the fear in them."
    "He looks like he's about to say something, but he just can't get the words out."
    "You can see tears in his eyes, and you ask if he's okay."
    "He smiles weakly and says he's fine, but you can tell he's not."
    
    scene black
    "And suddenly everything goes black."
    "Your head begins to hurt."
    "you smell something.. foul.. in the air."
    "Everything around you has gone eerily silent."
    "No screams, talking, movement.. just silence.."
    "You realize that you and Noah were the only two people still on the bus before the blackout.."
    "Were they going somewhere else..? Or did they know something you didn't."
    "You begin to panic, ready to run, kick, punch, scream."
    "Anything to get out.."
    "When you feel something."
    "Hard."
    "Hit the back of your head."
    "You fall forward.."
    "And hit the ground."
    "The.. ground..?"
    "There were seats infront of you though.."
    "Atleast.. you think there were."
    u "Eira?"
    "You try to speak but can't."
    u "Oh.. I'm going to get so fired.."
    "It's a girl's voice. Soft spoken.. likely a teenager or young adult.."
    u "Eira please.. wake up.."
    "Whoever it is on the bus with you, picks you up and carries you on their back."
    "You try to open your eyes.. but they burn.."
    "So, you decide to keep then closed."
    u "I'm just taking you to the headmistress, she'll help fix your eyes and get you registered."
    u "Today's just a move-in day for you. You'll have your own room."
    "You can feel yourself slowly drifting to sleep.."

    scene hm-office:
        xysize(1920,1280)
    "When you wake back up, you're in an office."
    "There's a woman looking intently at you."
    show headmaster
    sk "Goodmorning, Eira."
    sk "I want to apologize on behalf of my coworker, she forgot you were not registered."
    sk "I'm sure you have many questions."
    sk "Before I begin with you registration, I'd like to give you some time to ask these."
    sk "But, there is much to discover during your time here."
    sk "For that reason, I'll only be allowing you to ask one question today."
    sk "Don't worry! You'll be allowed to as more later!"
    hide headmaster
    menu:
        "Where am I?":
            show eira
            ev "Where am I right now?"
            ev "Everything went black, and I think I passed out."
            hide eira
            show headmaster
            sk "You're bright, I'll give you that."
            sk "Your body is strong too, most would've died without protection."
            sk "Eidolon Academy is a presigious school for the best of the best."
            sk "You have been selected due to your academic performances as well as your potential as a holder."
            sk "At this current moment, you are in my office."

        "Who are you?":
            show eira
            ev "Who are you?"
            hide eira
            show headmaster
            sk "My name is Headmaster Sable Korrin. Most call me Headmaster or Mrs. Korrin."
            sk "You may call me either, or something else if you preferred."
            sk "I'm in charge of everything from schedules, disciplinary actions, to just ensuring all students are out of their dorms each morning."
            sk "If you need anything during your time at the academy, I'm always here to help you out"
        "What is a holder?":
            show eira
            ev "What is a holder?"
            hide eira
            "The headmaster smiles warmly."
            show headmaster
            sk "Holders are humans capable of more."
            hide headmaster
            show eira
            ev "More.. what?"
            hide eira 
            show headmaster
            sk "Energy. Dark magic, if you will."
            sk "You will be alongside five others around your age."
            sk "But I believe you, my dear, will be special."
    sk "Now, with that being said. It is time to get your registered."
    sk "We only allow five students per level typically, but when we reviewed your file.."
    sk "We decided it was only best to make an exception."
    sk "You however, are now the only student who has not selected a class yet."
    "The headmaster lays out multiple envelopes infront of you."
    sk "Please, select one of these."
    menu:
        "1.":
            sk "Beautiful choice Eira."
            $ group = 1
        "2.":
            sk "Beautiful choice Eira."
            $ group = 2
        "3.":
            sk "Beautiful choice Eira."
            $ group = 3
        "4.":
            sk "Beautiful choice Eira."
            $ group = 4
        "No.":
            "This is not optional."
            menu:
                "1":
                    sk "Good."
                    $ group = 1
                "2":
                    sk "Good."
                    $ group = 2
                "3":
                    sk "Good."
                    $ group = 3
                "4":
                    sk "Good."
                    $ group = 4
                "I'm not Picking.":
                    "The headmistress frowns at you."
                    sk "That's.. disappointing."
                    sk "Since you decided not to pick, the choice has been made for you."
                    sk "Good luck Eira."
                    "Classification.. Pending."
                    $ group = 5
    scene black
    "Everything goes black again."
    "Nothing hits you this time though.."
    "Things just go black."
    sk "Please don't be scared, You're just being registered."
    sk "Now, you may feel a little.. pinch."
    "You feel like something is slicing into your arm.."
    "But in seconds.. it's gone.."
    "You feel normal again."

    scene dorm-bed:(
        xysize(1920,1280)
    "When you awaken again, you're in a bed.."
    ev "This is.. weird.."
    "You say out loud to nobody in particular. "
    "The room is fairly large so you decide to get up to look around."
    
    scene bathroom:
        xysize(1920,1280)
    "Your bathroom is pretty big.."
    "It has all of the essentials, toothpaste, shampoo, conditioner, a new toothbrush..."
    "There's a closet full of wash cloths and towels"
    "The shower also has a bath tub.."
    "When you look under the sick, you see everything from a blow dryer, to pads, and there's a note.."
    "'If there's anything you want scent wise, please place an order in the kitchen! Once approved we will get it to you!'"
    "All of this.. for free?"
    "You then decide to walk into the final rooms."

    scene kitchen:
        xysize(1920, 1280)
    "Outside of your bedroom, you have a kitchen."
    "Not a massive one, of course.. but it has two rooms attached."
    "One's a small laundry room.."
    "The other just has little shelves.. like a pantry maybe.."
    "You go through the different cabinets.."
    "You find things varying from pots and pans.."
    "To cups and plates.."
    "There's a drawer full of knives, forks, spoons.. etc." 
    "And there's another with a larger spoon, spatulas, tongs.."
    "On the counter is one more note with your name on it."
    "'Welcome to your dorm! Your key is just your handprint, you put it on the sensor to enter.'"
    "'There's a screen on the refridgerator where you can place orders'"
    "'It will ask you for a key to confirm, just use your handprint.'"
    "'I hope you get settled in, and we will see you first thing tomorrow!'"

return
