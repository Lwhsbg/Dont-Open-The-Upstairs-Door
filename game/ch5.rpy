label ch5:
    scene black 
    with fade
    centered "{size=+8}CHAPTER 4{/size}\n{size=+3}THE BASEMENT{/size}"
    pause 1.0 
    scene upstairs_door at bg_fit
    with dissolve
    with fade
    show ethan at right
    with dissolve
    with fade
    e "Listen to me."
    e "Whatever happens, just do not open the door."
    p "What if Lily is still inside?"
    e "Lily is gone."
    p "And how do you know?"
    e "Because..."
    "He suddenly stops."
    e "Because sometimes i hear her asking to let her out."
    e "And sometimes i hear her asking me to come in."
    p "And what is the difference?"
    e "When it is Lily, she calls me Ethan."
    e "When it is the thing..."
    e "It calls me by the name that my mother used to call me when I was little."
    "He then looks directly at you."
    e "And it knows your name too..."
    hide ethan
    with dissolve
    "You stand infront of the forbidden door."
    "For the first time, you notice the scratches in the on the woodem frame."
    "Three are old, but the fourth scratch looks fresh."
    menu:
        "What will you do?"
        "Trust Ethan and leave the house.":
            jump ending_escape
        "Open the upstairs door.":
            $ opened_door = True
            jump door_decision
        "Search the house for the original photograph.":
            jump investigate_truth
        "Ask ethan about what you did that night.":
            jump childhood_memory
            
