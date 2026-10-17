transform bg_fit:
    xysize(1920,1080)
label start:
    $ trust = 0
    $ clues = 0
    $ found_photo = False
    $ found_diary = False
    $ found_note = False
    $ knows_childhood = False
    $ opened_door = False
    $ investigated = False
    scene house_exterior at bg_fit
    with dissolve 
    with fade 
    "The rain has been falling for nearly two hours."
    "Your phone lights up as you approach the old house."
    "It was your old friend, ethan asking if you were there yet."
    "You told him you were nearly there, about to arrive."
    "You do not know why he was texting you so worriedly."
    "But something in his messages made it difficult to say no."
    scene foyer at bg_fit
    with dissolve
    with hpunch
    show ethan at right 
    with dissolve
    e "Wow, so you actually came."
    p "You sounded like you really needed someone."
    e "Yeah, I guess I did."
    "He smiles, but it does not reach his eyes."
    e "You look different."
    p "It has been 3 years."
    e "Has it really?"
    "For a moment, he looks geniunely confused"
    e "Come in, I will show you around."
    hide ethan 
    scene hallway at bg_fit
    with dissolve
    with fade
    "The house smells of dust and damp wood."
    "Every wall is covered in old photographs."
    "Most of the faces have faded beyond recognition."
    scene living_room at bg_fit
    with dissolve
    show ethan at truecenter
    with dissolve
    e "Before you settle in for a while, I need to tell you something."
    p "That sounds reassuring."
    e "I am serious."
    e "There are three rules in this house."
    e "First, if you hear footsteps upstairs, ignore them."
    e "Second, if someone calls your name from upstairs, dont answer."
    e "Third..."
    "Ethan looks at the ceiling."
    e "No matter what happens, do not open the upstairs door."
    menu:
        "How do you respond?"
        "Ask him what is upstairs.":
            $ trust -= 1
            p "What is upstairs?"
            e "A bedroom."
            p "Then why cannot I open it?"
            e "Because I asked you not to."
            p "That is not an answer."
            e "It is the only one that i have."
        "Laugh and tell him that he is being ridiculous.":
            $ trust += 1
            p "Are you trying to scare me?"
            e "I wish I were."
