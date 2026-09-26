define mc = Character('Main Character', color="#c8ffc8")
define sk = Character('Shopkeeper', color="#c8c8ff")

image 6_Hallway_Left = "6th Floor Left Hallway Forward.jpg"
image 6_Elevators = "6th floor Dorm Entrance.jpg"
image 6_Hallway_Right = "6th Floor Dorm Right Hallway.jpg"
image balloon = "6th Floor Left Hallway Balloon Zoom In.jpg"
image Elevator_Open = "Elevator Open.jpg"
image Elevator_Interior = "Elevator Interior.jpg"
image Tunnels_Start = "Tunnels Start (From Dorm Elevator).jpg"

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

    scene 6_Hallway_Left

    mc "Man...I shouldn't have gotten out of bed. I already know the elevator will be packed this morning..."

    "I dragged my feet to the elevators, taking my sweet time so that I could adjust to the brightness in the hallway."

    # Something with images goes here under this.
    scene 6_Elevators

    mc "Here I am once again at the elevators for the sixth floor. *Sigh*"

    "Do I really want to take the elevators right now?"

menu:
    "Yes, I need to stop being lazy.":
        jump Inside_Elevators
    
    "No, I want to explore first.":
        jump Hallway # Work on this after finishing the Main Story.

label Inside_Elevators:
    mc "What am I thinking? I need to get this over with as fast as possible so I can get back to bed!"

    "I confidently pump my fist against my chest, in an attempt to summon the motivation to continue onwards to the tunnels."

    mc "Oh, right. I need to press the button to go down. I'm so dumb..."

    "I walk up to the elevator's buttons."

    "*CLICK*"

    "After a bit of waiting, an elevator comes down, announcing its arrival with a small chime."

    scene Elevator_Open

    mc "Wow, I forget how fast these elevators come down on weekends. Then again, who's going to be using the elevators this early? Especially on a weekend."

    "I make my way into the elevator."

    scene Elevator_Interior

    "It was a pretty smooth ride down, didn't have much going on...since it's an elevator."

    "*DING*"

    "I arrived at the A level, where the tunnels are. I stepped off the elevator, taking in the scenery of the same 8 vending machines always seen on the Ellingson side of the tunnels."

    scene Tunnels_Start

    mc "Wow... no matter how many times I come down here, I'm still mesmerized by the vending machines down here."

    mc "Actually...I could just get some food from one of the vending machines down here!"

    "Do I get food from the vending machines?"

menu:
    "Yes! I don't need to walk to the corner store if I do!":
        jump Ending_Sequence # Come back to code this.
    
    "No, the food probably sucks anyways.":
        jump Tunnel_Hallways

label Tunnel_Hallways:
    mc "Yeah, no. What was I thinking? The vending machine food could be poisoned..."

    "I strode past the vending machines, my mind dead set on making it to the corner store...for now."

    "It was going to be quite the walk, due to me venturing to the corner store from the Ellingson side of the tunnels."

    # Scene for hallway

    "I came face to face with the doorway leading to the Gibson tunnels."

    "There, I saw..."

    "Nothing out of the ordinary. I continued onward."

    

label Hallway:
    mc "Mmm..."

    mc "I want to go explore the other hallway. Who knows, things might be different today."

    scene 6_Hallway_Right

# Ending Sequence 1
label First_Bad_Ending_Path:
    mc "Yeah... nah. I want to stay in bed a bit longer."

    "And stay in bed I did. Unfortunately, I found out the hard way to not ignore the body's craving for food."

    "--BAD ENDING--"

    return