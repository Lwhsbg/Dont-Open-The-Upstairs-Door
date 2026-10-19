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
label ending_escape:
    scene hallway_dark at bg_fit
    with dissolve
    with fade
    "You step away from the door."
    p "I am not opening it."
    l "You are leaving me again?"
    "The voice inside sounds smaller now."
    "Almost like the little girl in the photograph."
    p "I am sorry, Lily."
    l "You always say that."
    "You turn away and head down the stairs."
    "Ethan follows from closely behind."
    scene foyer_dark at bg_fit
    with dissolve
    with fade
    e "Do not stop walking."
    p "What happens if we do?"
    e "I do not know."
    e "And I do not want to find out."
    "You reach the front door and pull it open."
    "Cold night air rushes into the house."
    scene house_exterior at bg_fit
    with dissolve
    with fade
    "For the first time all night, you can breathe properly."
    p "We need to tell someone."
    e "Tell them what?"
    e "That a little girl that has been missing for years is talking through a locked door."
    p "We cannot pretend like nothing ever happened."
    e "I am not asking you to forget, I am asking you to survive."
    "You both walk down the path and do not look back until you see the road."
    p "Will you be okay?"
    e "I do not know."
    "He gives you a tired smile."
    e "But at least we are outside."
    scene black
    with fade
    "You leave the town before sunrise."
    "You never return to the house."
    "You then never speak about that night with anyone else."
    "Months pass."
    "Then years."
    "The memories begin to be less vivid."
    "The nightmares become less frequent."
    "Eventually, you convince that all of that was just a dream."
    "Until one rainy evening, a knock comes on your door, then another, then another."
    "When you go check your door, there was nobody."
    "Just a picture laying down, of Lisa.."
    "And then from inside, three knocks come up."
    centered "{size =+ 12}ENDING 1{/size}\n\nYOU FOLLOWED THE RULES"
    return
label ending_curiosity:
    scene upstairs_door at bg_fit
    with dissolve
    with fade
    "You turn the handle."
    "The door opens with a long creak."
    scene black
    with fade
    "You expect to find a bedroom inside."
    "Instead, you end up finding a hallway that stretches into endless darkness."
    p "What is this place?"
    "There is no answer."
    "You look back, the stair disappears."
    l "You came back."
    p "Lily, is that you?"
    l "You left me here."
    p "I was a child. I did not know what was happening."
    l "You heard me."
    p "I am sorry."
    l "You said that you would come back."
    "You tried to move towards her."
    "The hallway grows more and more with every step."
    p "Please, I just want to go home."
    l "Huh? This is your home."
    "While running, you see ethan."
    "You hear him."
    e "Do not stop running!"
    "He reaches for your hand."
    "His fingers are ice cold."
    e "You should not have opened it."
    "You look into his face."
    "His eyes are completely dark."
    p "You are not ethan."
    "His smile widens."
    e "Does it matter?"
    centered "{size =+ 12}ENDING 2{/size}\n\nCURIOSITY KILLED YOU"
    return
label ending_memory:
    scene hallway_dark at bg_fit
    with dissolve
    with fade
    "You step away from the upstairs door."
    p "We are leaving."
    e "But Lily..."
    p "We cannot save someone if we do not understand what we are dealing with."
    e "I have been trying to understand for years."
    p "Then maybe it is time for you to stop trying."
    "Ethan looks towards the door then a soft knock comes from behind it."
    e "I am sorry, Lily..."
    "For a moment, the house is completely silent."
    "Then the voice speaks again."
    l "You always say that."
    "Ethan opens his eyes."
    e "Come on."
    "You follow him downstairs."
    "Neither of you looks back."
    centered "{size =+ 12}ENDING 3{/size}\n\nTHE MEMORY WE LEFT BEHIND"
    return
label ending_secret    




    