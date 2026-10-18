label ch3:
    scene black
    with dissolve
    centered "{size=+8}CHAPTER 2{/size}\n{size=+3}THE FOOTSTEPS{/size}"
    pause 1.0
    "3:17 AM."
    "Your phone screen is the only light in the room."
    "Three knocks from somewhere upstairs."
    "Knock, knock, knock."
    "You pull the blanket away and sit up."
    "Then Ethan's voice comes from upstairs."
    e "Hey, open the door."
    e "It's okay."
    "Your phone vibrates."
    "A message from ethan appears on the screen."
    "It says, I am in my room, do not leave yours."
    "Another message follows."
    "It says, whatever you hear, it is not me."
    scene upstairs_door at bg fit 
    with dissolve
    with fade
    v "You promised me that you would come back."
    v "Why would you leave me here?"
    "You do not remember making any promise."
    menu:
        "What do you do?"
        "Stay in your bedroom:":
            $ trust += 1
            scene bedroom at bg_fit
            with dissolve
            with fade
            "You push yourself against the headboard."
            "You do not move."
            "You do not answer."
            "The knocking then continues for several minutes."
            "Eventually, the footsteps retreat."
            "You spend the rest of the night staring at the door."
        "Find Ethan":
            $ investigated = True
            scene hallway_dark
            with dissolve
            "You step into the hallway."
            "The house different in the darkness."
            "You then reach Ethan's bedroom."
            "The door is open."
            "The bed is untouched."
            "His phone lies on the floor."
            "It's screen displays the messages that you received."
            "But the last message has been changed now."
            "It said, you should not have come back."
            $ clues += 1
        "Walk towards the upstairs door":
            $ trust -= 1
            scene upstairs_door at bg_fit
            with dissolve
            with fade
            "You climb the stairs."
            "Each step that you seem to take sounds louder than the last."
            v "Finally."
            v "I have been waiting for you."
            "The voice sounds exactly like yours."
            "You step back."
            "You do not remember ever hearing your own voice sound like that."
    




