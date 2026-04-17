#MCs
define ev = Character('Eira Vale', color="#3d813d")
define sk = Character('Headmistress Sable Korrin', color="#4046b7")
define lr = Character('Lucian Reed', color="#b73d3d")
define mv = Character('Mira Vexley', color="#ad3db7")
define nh = Character('Noah Halden', color ="#3db7b7")
define sl = Character('Seraphine Lorne', color ="#b7ad3d")
define us = Character('UNASSIGNED', color="#FFFFFF")

#Eira's family
define evm = Character('Mom', color="#3d813d")
define evd = Character('Dad', color="#3d813d")

#Stats
define hunger = 10
# if hunger drops below 5 you will become hungy, if it is at 1 or 2 during a check, you will be starving, if it is 0, you will die.
define group = 0
#Group 1 = TBD
define mood = 0
#0 = null, 1 = happy, 2 = annoyed, 3 = upset, 4 = tired, 5 = hungry, 6 = nervous, 7 = angry, 8 = scared
define tiredness = 0
#If tiredness drops below 5, you will become tired. If tiredness ever hits zero, you will be forced to rest.
define health = 100


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
return
