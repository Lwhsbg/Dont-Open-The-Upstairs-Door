label ch4:
    scene black 
    with fade
    centered "{size=+8}CHAPTER 4{/size}\n{size=+3}THE BASEMENT{/size}"
    pause 1.0 
    scene kitchen at bg_fit
    with dissolve
    with fade
    "Later that morning, Ethan disappears."
    "You search for him all over the living room and the hallway."
    "A narrow door beneath the stairs stand open, which you had never seen before."
    "You never had ever noticed it."
    "You then call out Ethan's name as that could be the only place that he could be at."
    p "Ethan?"
    "No answer."
    "You had no choice but to go inside the basement to find Ethan."
    scene basement at bg_fit
    with dissolve
    with fade
    "You descend into the basement."
    "Old boxes you cannot imagine the age of are stacked against the walls."
    "There are photographs, letters and children's drawings."
    "You begin to search through them to maybe find something interesting."
    if not found_photo:
        "You discover an old photo of Ethan and a little girl."
        $ found_photo = True
        $ clues += 1
    "Beneath the photographs, you find a piece of folded paper."
    menu:
        "Read the paper?"
        "Read it carefully.":
            $ found_note = True
            $ clues += 1
            "The handwriting in the note is old and uneven."
            "The note says:"
            "{i}If you hear footsteps, do not count them.{/i}"
            "{i}If you hear your name, do not answer.{/i}"
            "{i}If the door opens, do not look at the mirror.{/i}"
            "Beneath the three rules that the note gives you, there seems to be another sentence writtrn doen."
            "{i}If there is a fourth knock, then it remembers you.{/i}"
        "Put it back.":
            "You fold the paper and then put it back in the box without reading it."
            "You do not want to know what it says at all."
    "You then notice a diary lying beneath a loose floorboard."
    menu:
        "Read the diary?"
        "Read it":
            $ found_diary = True
            $ clues += 1
            "Looks like the diary belonged to Ethan's Mother."
            "The first readable entry was dated to years ago."
            "It said:"
            "{i}Lily has started talking to the upstairs room again.{/i}"
            "{i}She says that someone who is inside, knows her name.{/i}"
            "{i}Lately, Ethan keeps on saying that he has been able to hear it too.{/i}"
            "You turn the page."
            "{i}We have told the children never to open the door.{/i}"
            "Another entry has been written in a different hand."
            "{i}It does not want to leave the room.{/i}"
            "{i}It wants someone to take it's place.{/i}"
            "{i}The final entry is dated to only a few days ago.{/i}"
            "{i}Ethan has started talking to it again.{/i}"
            "{i}"
