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
