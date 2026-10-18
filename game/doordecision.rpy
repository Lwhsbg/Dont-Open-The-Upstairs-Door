label door_decision:
    scene upstairs_door at bg_fit
    with dissolve
    with fade
    "You stand in front of the upstairs door."
    "The wood is old and covered in scratches."
    "Some of them look like marks that are made by fingernails."
    p "Lily?"
    l "I am here.."
    p "I am sorry."
    l "You have said that already."
    p "I was a child, and i did not understand what i was doing."
    l "I was a child, too."
    "You do not have an answer for that."
    l "I called for you."
    l "I cried until my throat hurt."
    l "I waited for you to come back."
    p "I know."
    l "No, you do not. You know nothing."
    "Something scratches through the other side of the door."
    l "Do you even know for how long I have been here?"
    p "No."
    l "Neither do I."
    "The hallway lights flicker."
    "For an instance, you see a small shadow beneath the door."
    l "Open it."
    "You reach towards the handle, and then stop."
    e "Wait."
    "Ethan stands several steps behind you."
    e "Before you do anything, you need to understand something."
    p "What now?"
    e "I found a diary in our basement."
    e "It belonged to our parents."
    e "There was something written in that diary about that room."
    p "What did it say?"
    e "That the door should never be opened after 3:17."
    "You glance at the clock that was hanging on the wall."
    "3:16 AM."
    e "We have one minute."
    "From behind the door comes a quiet laugh."
    l "He is lying."
    p "What?"
    l "Ethan does not want you to know about what happened."
    e "Do not listen to her!"
    l "Ask him why he came back here."
    p "Why did you come back, Ethan?"
    e "Because I wanted to find out what happened to my sister."
    l "Ask him what he found."
    "Ethan says nothing."
    p "What did you find?"
    e "I found the truth."
    p "And? What is it?"
    e "This house does not keep people inside."
    "He looks directly at you."
    e "It keeps their memories."
    "The clock changes to 3:17am."
    "The door then unlocks with a quiet click."
    if found_photo and found_diary and found_note and clues>= 3:
        "You remember the photograph, the diary and the note."
        "Each clue tells you a part of the story."
        "That Lily did not simply disappear."
        "That something happened in this house and the truth has been waiting for you."
        menu:
            "Open the door":
                jump ending_secret
            "Turn away and leave":
                jump ending_escape
    else:
        "You have no idea of what it is awaiting inside."
        "You only know that the door is unlocked."
        menu:
            "Open the door":
                jump ending_curiosity
            "Walk away":
                jump ending_escape

    