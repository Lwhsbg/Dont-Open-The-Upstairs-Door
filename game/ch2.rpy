label footsteps:
    scene black
    with dissolve
    centered "{size=+8}CHAPTER 2{/size}\n{size=+3}THE FOOTSTEPS{/size}"
    pause 1.0
    scene living_room
    with fade
    with dissolve
    "You wake up some time after midnight."
    "You must have fallen asleep on the sofa."
    "The house is very quiet."
    "And then you hear it."
    "Footsteps."
    "Slow footsteps, that were crossing the ceiling above you."
    "One step."
    "Another, then another."
    "They stop directly over your head."
    "You then remember the first rule that was given."
    scene kitchen_dark at bg_fit
    with dissolve
    show ethan at right
    with dissolve
    e "Could not sleep?"
    p "I heard something upstairs."
    e "Did you?"
    p "Footsteps. Someone was walking around."
    e "Old houses settle."
    p "That sounded like someone was walking."
    e "Please do not start."
    menu:
        "What do you ask Ethan?"
        "Ask if somebody else lives here.":
            $ trust -= 1
            p "Is there somebody else staying here in this house?"
            e "no."
            p "Then who is that upstairs?"
            e "Nobody."
            p "You are not making this easy."
            e "I know."
            e "My sister used to live here."
            e "She died when we were just children."
            p "I am sorry. I did not know."
            e "Nobody talks about her anymore."
            e "That is how my parents wanted it to be like."
        "Tell him that you will ignore the noises.":
            $ trust += 1
            p "Fine, I will ignore it if you want that so bad."
            e "Good."
            "He looks relieved."
            e "That is all that you need to do."
            p "You are making it sound like it is a ritual."
            e "Maybe it is."
        "Ask him how his sister died.":
            $ trust -= 1
            p "You mentioned your sister. How did she die?"
            "Ethan goes completely still."
            e "She disappeared."
            p "You said that she died."
            e "We never found her."
            e "My parents stopped looking."
            p "How does someone even disappear inside a house?"
            e "I do not know, that is what I have been trying to understand."
    "Ethan leaves you alone."
    hide ethan
    with dissolve
    scene hallway_dark at bg_fit
    with dissolve
    with fade
    "As you walk past an old cabinet, you spot something that immediately catches your eye."
    "A photograph lies behind a pile of yellowed papers."
    menu:
        "Look at the photograph?"
        "Pick it up.":
            $ found_photo = True 
            $ clues += 1
            "The photograph shows three children standing outside the house." 
            "Ethan is one of them."
            "A little girl stands besides him."
            "The third child looks strangely familiar."
            "You turn the photograph over."
            "Someone has written a sentence on the back."
            "\"We buried the wrong one. \""
            "You read it twice."
            "You do not understand what it means at all."
        "Leave it where it is.":
            "You decide not to touch it."
            "Something about the photograph makes you uncomfortable."
    scene hallway_dark at bg_fit
    with dissolve
    with fade
    "A floorboard creaks above you."
    "Then a child's voice speaks to you from upstairs."
    l "Ethan?"
    l "Why did you leave me here?"
    show ethan at right 
    with hpunch
    with dissolve
    e "Go to your room."
    p "Ethan, who is that?"
    e "NOW."
    hide ethan
    with dissolve
    scene bedroom at bg_fit
    with dissolve
    with fade
    "You lock the bedroom door."
    "You sit at the edge of the bed until the house goes quiet."
    "At some point, you fall asleep again."
    jump ch3



