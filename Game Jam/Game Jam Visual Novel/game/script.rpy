define mc = Character('Main Character', color="#c8ffc8")
define sk = Character('Shopkeeper', color="#c8c8ff")


label start:
    mc "I'm really hungry... I'm going to go buy something from the Corner Store."

    "Should I get up to leave?"

menu:

    "Yes, I have to eat.":
        jump Elevators
    
    "No, I would rather starve to death so I can chud out today.":
        jump First_Bad_Ending_Path

label Elevators:

    "After some painful shuffling, I finally got out of bed, making my way to the hallway."

    mc "Man...I shouldn't have gotten out of bed. I already know the elevator will be packed this morning..."

    "I dragged my feet to the elevators, taking my sweet time so that I could adjust to the brightness in the hallway."

    # Something with images goes here under this.

    mc "Here I am once again at the elevators for the sixth floor. *Sigh*"

    "Do I really want to take the elevators right now?"

menu:
    "Yes, I need to stop being lazy.":
        jump Inside_Elevators
    
    "No, I want to explore first.":
        jump Hallway

label Inside_Elevators:
    mc "What am I thinking? I need to get this over with as fast as possible so I can get back to bed!"

    "I confidently pump my fist against my chest, in an attempt to summon the motivation to continue onwards to the tunnels."

label Hallway:
    mc "Mmm..."

    mc "I want to go explore the other hallway. Who knows, things might be different today."

# Ending Sequence 1
label First_Bad_Ending_Path:
    mc "Yeah... nah. I want to stay in bed a bit longer."

    "And stay in bed I did. Unfortunately, I found out the hard way to not ignore the body's craving for food."

    "--BAD ENDING--"

    return