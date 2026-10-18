label investigate_truth:
    scene living_room at bg_fit
    with dissolve
    "You return to the living room."
    p "I want you to tell me what actually had happened."
    e "I have tried to remember."
    p "Try again."
    e "We were children."
    e "You came here to play."
    e "Lily was upstairs."
    e "We heard her crying behind the door."
    p "And I opened it?"
    e "That is what I remember."
    p "What did I see?"
    e "I do not know."
    if found_photo and found_diary and found_note:
        $ knows_childhood = True
        e "Wait"
        e "I have remembered something else."
        e "You came cack downstairs."
        e "You were crying, but you would not tell why."
        e "My mother told us to forget the whole thing."
        e "The next morning, you did not remember Lily at all."
        p "And you never told me?"
        e "I thought that forgetting was the only way to keep you safe."
        p "Safe from what?"
        e "Whatever was in that room."
    else:
        e "That is all that I can remember."
        e "I wish that I knew more."
    hide ethan
    with dissolve
    menu:
        "What do you do?"
        "Leave the house with Ethan.":
            if knows_childhood:
                jump ending_memory
            else:
                jump ending_escape
        "Open the upstairs door.":
            $ opened_door = True
            jump door_decision
        "Ask ethan about your childhood visit.":
            jump childhood_memory