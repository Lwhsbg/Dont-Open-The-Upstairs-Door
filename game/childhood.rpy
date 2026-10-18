label childhood_memory:
    scene black
    with fade
    "You stare at the photograph again."
    "Three children stand in front of the house."
    "Ethan looks about ten years old, and you look a bit younger."
    "Between you two stands a girl that has a wide, innocent smile."
    p "Ethan, who is she?"
    show ethan at right
    with dissolve
    with fade
    e "You really, you really do not remember?"
    p "I have seen her before. I just know that I have and nothing else."
    p "I cannot remember where either."
    e "Her name is the Lily. She was my little sister."
    "You take a look at the photo again."
    "There is something wrong about her face."
    "Something has scratched it repeatedly, leaving deep marks across the paper."
    p "Why would someone do this to a photograph?"
    e "I did it."
    p "You?"
    e "I could not stand looking at her anymore."
    p "What happened to her?"
    "Ethan takes a long breath, but he does not answer immediately."
    e "We used to play together all the time."
    e "Lily used to follow us everywhere around. She always wanted to be included in everythimg."
    e "One evening, we decided to play hide and seek."
    p "I remember, I do remember playing that with you."
    e "Maybe because you were the one that had suggested it."
    p "Okay... And?"
    e "Lily went upstairs to hide."
    e "We heard her running around to hide."
    e "For just a bit."
    e "Then suddenly, everything just went quiet."
    "Ethan looks up towards the ceiling."
    e "We just thought that she had found a really good hiding place."
    "We then proceeded to search the entire house. Every room, every cupboard, and even down the basement."
    e "But at the end of the day, we could not find her."
    p "What about the upstairs room? Did we check that place?"
    "Ethan's expression changes upon hearing that."
    e "We did, that was the last place that we checked."
    p "Why?"
    e "Because the door was locked and there was no way that Lily could have gotten in there."
    p "Couldnt we just open it? Did we not have the key to it?"
    e "We tried."
    e "We called for her, but she would just not answer."
    e "Eventually after a while, our parents arrived and then forced the door open, as it was the last possible place for her to be in."
    p "And Lily was inside?"
    e "No."
    "The silence that followed after that statement felt unbearable."
    e "The room was absolutely empty."
    "And the window was locked from the inside."
    e "After that, there was no where that Lily could have gone."
    p "That is just... impossible."
    e "I know..."
    "You look down at the photograph."
    "And for a brief moment, you remember a little girl holding your hand."
    l "{i}Promise that you will not tell anyone.{/i}"
    "The memory disappears and just flies away before you can even understand it."
    p "I think I remembered something about the past, for a brief moment."
    e "What did you remember?"
    p "Someone crying. I think it was Lily."
    "Ethan suddenly steps closer to you."
    e "What else?"
    p "I do not know. It is all blurry." 
    e "Try harder."
    p "I am trying!!"
    "Your voice echoes throughout the room."
    "For a moment, neither of you move."
    e "I am sorry."
    "He looks exhausted."
    e "I have spent years trying to figure out what happened that night. And now that you are finally here, I thought, i thought that you would remember something."
    p "Why did you not tell me any of this before?"
    e "Because you forgot."
    p "Fotrgot?"
    e "Yeah, you forgot everything."
    scene foyer_dark at bg_fit
    with fade 
    with dissolve
    "Then from upstairs, suddenly, comes a knock. A sudden knock."
    pause 1.0
    scene black
    "Then another."
    scene foyer_dark at bg_fit
    with dissolve
    with fade
    pause 1.0
    scene black
    with fade
    l "Ethan?"
    scene foyer_dark at bg_fit
    with dissolve
    with fade
    "Ethan's face turns pale."
    l "Are you still there?"
    e "Do not answer her."
    p "But that is Lily."
    e "No, it is not."
    "You look down at the photograph one more time."
    "The scratched up face of that girl in that photo almost seems familiar now."
    menu:
        "Ask Ethan to explain everything.":
            jump memory_confession
        "Tell Ethan that you want to leave.":
            jump ending_memory:
        "Go upstairs and just open the door.":
            $ opened_door = True
            jump door_decision
            


    