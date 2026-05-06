# =========================================================
# Chapter 1 - The Stolen Offering Box
# =========================================================

image cloud_drifts:
    Tile("gui/cloud_shadows.png")
    xpos 0
    # This must be a 'block' to loop correctly
    block:
        linear 80.0 xpos -1920 
        xpos 0
        repeat

# -----------------------------------------------------------------------------
# Optional placeholder transforms
# Replace with project-specific positioning later.
# -----------------------------------------------------------------------------

transform left_bodyguard:
    xalign -0.02
    yalign 1.0

transform right_bodyguard:
    xalign 1.05
    yalign 0.1

transform center_priestess:
    xalign 0.5
    yalign 1.0

# ##########################
# GAME STARTS HERE #
# ##########################

# Priestesses & Shadows
# Chapter 1 - Draft 1
# Episode 01: The Missing Offering Box
# Working file suggestion:
# game/scripts/episode_01_offering_box.rpy
# 
# Character shorthand assumed:
# e = Emiko
# s = Shina
# m = Makoto
# a = Aya

# -----------------------------------------------------------------------------
# Episode 01 variables
# Move these defaults to game/scripts/variables.rpy later.
# -----------------------------------------------------------------------------

default ep01_started = False
default ep01_complete = False

default emiko_points = 0
default shina_points = 0
default bond_points = 0
default chaos_points = 0
default duty_points = 0
default evidence_points = 0
default dignity_points = 0

default ep01_formal_shopkeepers = False
default ep01_curse_rumor = False
default ep01_split_up = False
default ep01_box_protected = False
default ep01_fight_messy = False
default ep01_dice_cup_taken = False

default ep01_public_rumor = "none"
default ep01_final_result = "unknown"


# -----------------------------------------------------------------------------
# Episode start
# -----------------------------------------------------------------------------
label start:
label chapter_1_start:
    $ current_chapter = "ch1"
    $ save_name = _("Chapter I")
    show shrine_courtyard_morning with dissolve

    # play music "audio/music/shrine_morning.ogg" fadein 1.0
    # play sound "audio/sfx/kitten_meow.ogg"

    $ set_location("Temple Courtyard", "Late Morning")
    n "Black fur. Tiny paws. One bad decision too far from safety."

    show shina exhasperated at right_bodyguard
    show emiko neutral at left_bodyguard
    with dissolve

    s "Tch."
    e "No."
    s "I didn't even say anything."
    e "Your face said too much."

    play sound "audio/sfx/kitten_meow.ogg"

    s "It's gonna fall."
    e "Then we call an attendant."
    s "By the time an attendant gets here with a ladder, we will be picking cat off the courtyard."

    e "Do not say that."
    s "You want me to lie?"
    n "Shina set her naginata against the shed wall and rolled her sleeves higher."

    e "The tiles are wet."
    s "I've got eyes."
    e "You tend to use them selectively."

    s "And you use your mouth far too much."
    s "Stand there and judge quietly."
    e "...."
    e "That has never been my method."

    n "Shina caught the beam and pulled herself up."
    play sound "audio/sfx/wood_creak.ogg"

    s "Stupid cat. Stupid roof. Stupid shrine with stupid tall sheds."
    e "Left foot higher."
    s "I know where my foot is."

    e "Then explain why it is on moss."
    s "Explain why you are still talking."
    e "Because your survival rate improves when I do."

    s "I hate it when you say that."
    s "It's only been true once. Or Twice."
    n "Shina reached the kitten and scooped it against her chest."

    play sound "audio/sfx/kitten_meow_soft.ogg"

    s "Easy. I’ve got you. Do NOT scratch my face off."
    n "The kitten burrowed itself into the open fold of her shirt."

    e "It has good tactical instincts."
    s "Do not compliment the cat."
    e "I was criticizing you."

    show servant neutral at center_priestess
    with dissolve

    servant "Oh!"
    n "A passing servant stopped under the walkway, staring up."
    servant "Lady Shina, that is very impressive!"

    s "Do not."
    servant "What?"
    s "Speak as if I am nobility. Shina." 
    servant "But--"
    s "Just Shina."

    play sound "audio/sfx/single_clap.ogg"
    n "The servant clapped once."
    play sound "audio/sfx/cat_panic.ogg"
    n "The kitten panicked."
    s "H-hey! Calm down you little ass-- Gah--"
    play sound "audio/sfx/roof_slip.ogg"

    n "Four claws hit Shina’s collar. One paw slapped her cheek. Her foot slipped on the wet edge."
    n "She dropped from the wall, twisted halfway down, and hit the mud on her back with the kitten pinned safely against her chest."

    play sound "audio/sfx/mud_fall.ogg"
    show shina wet_embarrassed at left_bodyguard
    with dissolve

    play sound "audio/sfx/kitten_meow_soft.ogg"
    n "The kitten poked its head out from Shina’s collar and meowed."

    s "Alive."
    e "Unfortunately."

    e "I'm talking about the cat."
    s "I am talking about you."
    e "Of course you are."

    e "You climbed badly."
    s "And yet I still succeeded."
    e "You succeeded into the mud."
    s "Unimportant details."

    show makoto amused at center_priestess
    with dissolve

    m "Shina."

    s "No."

    m "I only said your name."

    s "You said it like you saw all of this."

    m "I did see all of this."

    s "Evil priestess..."

    m "The kitten seems to like you."

    s "It attacked me."

    e "That does not weaken her point."

    play sound "audio/sfx/advisor_scream.ogg"

    advisor_1 "AAAAAAAH!"

    stop music fadeout 0.5

    n "All four of them turned toward the main hall."

    s "If that is another cat, I am leaving."

    e "Move."

    hide servant
    hide makoto
    with dissolve

    scene bg shrine_courtyard_morning
    with dissolve

    play music "audio/music/shrine_morning.ogg" fadein 1.0

    n "At the foot of the main hall, a young attendant stood with both hands over his mouth."

    n "He did not move when the first advisor arrived. He did not move when the Priestess arrived."

    show aya concerned at center_priestess
    with dissolve

    n "In fact, it seemed he had forgotten all motor function entirely as his breathing turned thin and quick."

    attendant "Nononononononono--"

    a "Please breathe."

    n "The attendant tried. It came out thin."

    attendant "P-Priestess Aya. The box. It’s--"

    a "Which box?"

    attendant "The offering box."

    n "Aya followed his eyeline to the empty square in front of the hall."

    n "Four pale marks remained where the wood had stood for years. Dust had gathered around them, leaving a clean absence at the center."

    a "Ah."

    advisor_1 "Ah? That is the word?"

    advisor_2 "The grounds open soon."

    advisor_1 "The merchants will see."

    advisor_2 "And then the merchants will talk."

    show emiko stern at left_bodyguard
    show shina wet_embarrassed at right_bodyguard
    with dissolve

    n "Shina stopped beside Emiko, mud still drying on one sleeve. The kitten, now confiscated by a passing servant, gave one offended mewl from behind them."

    s "That is theft."

    e "That is a security failure."

    s "You make crime sound like paperwork."

    e "Most crime becomes paperwork."

    s "That is the worst thing you’ve said all morning."

    a "Emiko."

    n "Emiko’s gaze moved over the empty space, then to the rear approach, then to the side path."

    e "Rear access needs checking. The gate, the storehouse path, and any drag marks near the hall."

    s "So. Theft."

    e "Security failure."

    s "You are very committed to making theft boring."

    advisor_1 "Please recover it before noon."

    advisor_2 "Quietly."

    show makoto amused at center_priestess
    with dissolve

    m "Quiet retrieval and Shina in the same sentence. A brave choice."

    s "Evil priestess."


label episode_01_offering_box:

    $ ep01_started = True

    scene black
    with fade

    play music "audio/music/shrine_morning.ogg" fadein 1.5

    scene bg shrine_courtyard_morning
    with dissolve
    with dissolve
    n "At the foot of the main hall, a young attendant stood with both hands over his mouth."
    n "He did not move when the first advisor arrived. He didn't move when the Priestess arrived."
    narrator "There it was. Seven trying years all for nothing. Perhaps it wasn't too late to open up the clobbler stand his father had encouraged him to take on all those years ago."
    n "In fact, it seemed that he had forgotten all motor functions entirely as his breaths quickened."
    attendant "Nononononnononononono--"
    a "Please breathe."
    show aya concerned at center_priestess

    n "The attendant tried. It came out thin."

    attendant "P-Priestess Aya! The box! It's--"
    a "Which box?"
    attendant "The offering box."

    n "Aya followed his eyeline to the empty square in front of the hall."
    n "Four pale marks remained where the wood had stood for years. Dust had gathered around them, leaving a clean absence at the center."

    a "Ah."

    show aya concerned at center_priestess

    advisor_1 "Ah? That is the word?"

    advisor_2 "The morning visitors arrive in less than an hour."

    advisor_1 "No, before that, the merchants arrive. The merchants talk."

    advisor_2 "The merchants talk to the fishmonger. The fishmonger talks to everyone."

    advisor_1 "By noon, half the town will believe the gods rejected our money box."

    a "The gods do not reject boxes."

    advisor_1 "Respectfully, Priestess, that will not stop people from saying it."

    n "Aya lowered her gaze to the marks again. Her expression stayed calm. Her fingers tightened once inside her sleeves."

    a "Call Emiko."

    advisor_2 "She is already on the grounds."

    n "The advisor's voice dropped."

    advisor_2 "She saw the empty platform from the east path and began questioning the gate guard before anyone called her."

    a "Of course she did."

    hide aya
    with dissolve

    stop music fadeout 1.0
    play music "audio/music/episode_mission.ogg" fadein 1.0

    show emiko stern at left_bodyguard
    with dissolve

    e "The rear gate latch was lifted from inside. The ground near the storehouse has drag marks. Two people moved it, maybe three if one of them had no spine."

    advisor_1 "This is a disaster."

    e "This is a security failure."

    show shina neutral at right_bodyguard
    with dissolve

    s "It is theft."

    e "Yes. Theft caused by a security failure."

    s "You make crime sound like bad paperwork."

    e "Most crime leaves paperwork."

    s "You must be thrilling at festivals."

    e "I work during festivals."

    s "That explains several things."

    show aya concerned at center_priestess
    with dissolve

    a "The offering box must be returned quietly."

    s "Quietly."

    n "Shina looked at Emiko, then at the empty marks, then back at Aya."

    s "You called both of us."

    a "Yes."

    s "And you still want quiet."

    a "I want quiet attempted."

    show makoto amused at center_priestess
    with dissolve

    m "That is fair wording."

    s "Evil priestess..."

    m "I have said nothing cruel."

    s "You were about to."

    m "I was about to say that quiet retrieval and Shina in the same sentence is a brave administrative experiment."

    s "There it is."

    e "We should close the grounds."

    advisor_1 "Absolutely not. Closing the grounds confirms panic."

    advisor_2 "Leaving them open invites questions."

    e "Questions are better than uncontrolled access after a breach."

    a "Emiko."

    n "Emiko stopped."

    a "We need the box back before the town finishes inventing its own explanation."

    e "Then we retrieve it before noon."

    s "We?"

    e "You have town contacts."

    s "I have people who owe me small amounts of money and dislike me less than they dislike guards. That is not the same thing."

    e "It is useful enough."

    m "There. A compliment."

    s "That was not a compliment. That was a nail driven through a board."

    a "Go together. Find what can be found. Do not turn the town against the shrine."

    n "Aya looked at Shina for the last part."

    s "Why did that land on me?"

    e "Experience."

    s "I hope your box is at the bottom of a river."

    e "It is not a box. It is an offering box."

    s "The distinction is already making this day longer."

    hide aya
    hide makoto
    with dissolve

    n "Emiko turned toward the gate. Shina followed two steps behind, naginata balanced over her shoulder."

    e "Do not carry that like a walking stick."

    s "It is touching the ground zero times."

    e "It is announcing you from twenty paces away."

    s "Good. Then suspicious people can panic early and save us time."

    jump ep01_town_investigation

# -----------------------------------------------------------------------------
# Investigation hub
# -----------------------------------------------------------------------------

label ep01_town_investigation:

    scene bg town_street_morning
    with fade

    play music "audio/music/town_day.ogg" fadein 1.0

    show emiko neutral at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    n "The town had already started its morning trade."
    n "Fishmongers rinsed their tables. A rice seller argued with a customer over half a scoop. Two children chased each other between hanging cloth signs until a grandmother snapped her fan at them."
    n "At every corner, someone noticed Emiko."
    n "At every corner after that, someone noticed Shina and decided not to be the first person to ask why she had brought a naginata to buy radishes."

    s "You are making people nervous."

    e "You are carrying a polearm."

    s "I carry it well."

    e "That is not the issue."

    s "It is usually the issue."

    e "We need information."

    s "Then ask for it like a person."

    e "I ask clearly."

    s "You ask like the answer will be written into a confession ledger."

    e "That would be convenient."

    n "They stopped at the first market lane. From here, the road split three ways: toward the shopkeepers, toward the cheap food stalls, and toward the alley behind the pawn house."

    menu:
        "How should Emiko and Shina investigate?"

        "Question the shopkeepers formally.":
            $ ep01_formal_shopkeepers = True
            $ evidence_points += 1
            $ dignity_points += 1
            $ emiko_points += 1
            jump ep01_formal_questioning

        "Spread a rumor that the stolen box may be cursed.":
            $ ep01_curse_rumor = True
            $ evidence_points += 1
            $ chaos_points += 1
            $ shina_points += 1
            $ ep01_public_rumor = "cursed_box"
            jump ep01_curse_rumor_route

        "Split up and compare clues later.":
            $ ep01_split_up = True
            $ evidence_points += 2
            $ bond_points -= 1
            jump ep01_split_up_route

# -----------------------------------------------------------------------------
# Route 1: Formal questioning
# -----------------------------------------------------------------------------

label ep01_formal_questioning:

    scene bg town_shopfront
    with dissolve

    show emiko neutral at left_bodyguard
    show shina annoyed at right_bodyguard
    with dissolve

    n "Emiko chose the shopkeepers first."
    n "She began with the rice seller, who became honest the way people became honest when a blade remained sheathed by choice."

    e "Last night. After the second bell. Did you see a cart pass this lane?"

    rice_seller "Many carts pass this lane."

    e "One carrying a large wooden shrine box."

    rice_seller "That is more specific."

    e "Yes."

    rice_seller "Then no."

    s "He is lying."

    rice_seller "I am not lying."

    s "You answered too fast."

    rice_seller "You have a blade on a stick. I answer fast for women with blades on sticks."

    e "Shina."

    s "Fine. Ask him the second question."

    e "Did you hear wheels?"

    rice_seller "No wheels. Scraping. Like someone dragged furniture and did not care who heard."

    e "Direction?"

    rice_seller "South lane. Toward the bathhouse. Or the old gambling rooms."

    s "Old gambling rooms?"

    rice_seller "Old. Closed. Very illegal if reopened."

    s "That means reopened."

    e "Names."

    rice_seller "I did not see faces."

    e "You saw enough to avoid saying more."

    n "The rice seller's mouth tightened."

    rice_seller "There was a boy. Not a child. Not grown. He had a blue cord tied around his wrist. Ran ahead and told them when the lane was clear."

    s "Blue cord. Gambling lookout. South lane. See? People talk better when you frighten them politely."

    e "We have a direction."

    s "And a boy."

    e "And a room that should not be open."

    s "Most rooms worth entering should not be open."

    e "That explains several things."

    s "Do not use my own line against me."

    jump ep01_alley_clue

# -----------------------------------------------------------------------------
# Route 2: Curse rumor
# -----------------------------------------------------------------------------

label ep01_curse_rumor_route:

    scene bg town_food_stalls
    with dissolve

    show emiko stern at left_bodyguard
    show shina smug at right_bodyguard
    with dissolve

    n "Shina bought one skewer, took two bites, and leaned against the stall counter as if she had nowhere important to be."

    e "We are working."

    s "I am working."

    e "You are eating."

    s "People trust eating. People distrust questions."

    n "The stall owner leaned in despite himself."

    stall_owner "Questions about what?"

    s "Nothing serious. Shrine box went missing."

    stall_owner "The offering box?"

    s "Might be cursed now."

    e "It is not cursed."

    s "You do not know that."

    e "I know the ritual register."

    s "Do you know every god's opinion on thieves?"

    e "Shina."

    s "Exactly. Mystery."

    n "Two customers stopped pretending not to listen."

    customer_1 "Cursed how?"

    s "Hard to say. Bad luck. Bad stomach. Dice landing wrong. Hands going numb. Maybe hair loss."

    e "Hair loss."

    s "Men fear it."

    customer_2 "Dice?"

    n "Shina turned her head a fraction."

    s "Did I say dice?"

    customer_2 "You did."

    s "Interesting that you heard that part."

    customer_2 "I hear many things."

    e "Then hear this. If the offering box is in a gambling room, anyone touching it has committed theft against the shrine. Return it now and that fact stays small."

    stall_owner "South lane. Old gambling room behind the bathhouse."

    customer_1 "They brought in a big wooden thing last night. Used a cloth over it."

    customer_2 "Blue cord boy watches the alley. He runs errands for them."

    e "Names."

    customer_2 "I like my teeth."

    s "A wise position."

    e "You started a public curse rumor."

    s "A useful public curse rumor."

    e "Aya requested quiet."

    s "No. Aya requested quiet attempted."

    n "Emiko looked toward the south lane."

    e "If this reaches the shrine before we return, you answer to her."

    s "Aya or Makoto?"

    e "Yes."

    s "That is cruel."

    jump ep01_alley_clue

# -----------------------------------------------------------------------------
# Route 3: Split up
# -----------------------------------------------------------------------------

label ep01_split_up_route:

    scene bg town_crossroad
    with dissolve

    show emiko neutral at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    e "We cover more ground apart."

    s "We also create twice the number of people annoyed at us."

    e "Efficient."

    s "That was almost a joke."

    e "No."

    s "It had bones."

    e "Meet at the bathhouse lane in fifteen minutes."

    s "If you arrest someone by then, leave me a note."

    hide shina
    with dissolve

    n "Emiko took the shopfronts. She spoke to six people in the time it took one tea seller to decide whether fear of the shrine was stronger than fear of local gamblers."
    n "Fear of the shrine won by a narrow margin."

    tea_seller "South lane. Dragging sound after the second bell. A boy with a blue cord checked the corner first."

    e "Who employs him?"

    tea_seller "People who do not put their names on doors."

    e "Describe the door."

    tea_seller "Red paint. Peeling. Back of the old bathhouse."

    scene bg bathhouse_alley
    with dissolve

    show shina neutral at right_bodyguard
    with dissolve

    n "Shina reached the bathhouse lane from the food stalls."
    n "She did not ask about the offering box. She asked who had suddenly become lucky."

    gambler_woman "Lucky?"

    s "Someone always brags."

    gambler_woman "A room behind the bathhouse had a run last night. Dice kept falling sixes. Men started bowing to the table."

    s "The table."

    gambler_woman "Big thing. Covered in cloth. Bad taste."

    s "Shrine wood?"

    gambler_woman "I did not say that."

    s "You did not need to."

    scene bg bathhouse_alley
    with dissolve

    show emiko neutral at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    n "They met beside the bathhouse drain."

    e "Red door. Blue cord lookout. Drag marks."

    s "Gambling room. Lucky dice. They are using your offering box as a table."

    n "Emiko's face did not change."

    s "Oh, that one hurt."

    e "It offended me on three levels."

    s "Only three?"

    e "I am choosing restraint."

    s "Put that on your family crest."

    if ep01_split_up:
        n "They both looked down the alley at the same time, then noticed the other had done it. Neither commented."
        $ bond_points += 1

    jump ep01_alley_clue

# -----------------------------------------------------------------------------
# Shared clue: alley and lookout
# -----------------------------------------------------------------------------

label ep01_alley_clue:

    scene bg bathhouse_alley
    with fade

    show emiko alert at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    stop music fadeout 1.0
    play music "audio/music/investigation_low.ogg" fadein 1.0

    n "The alley behind the bathhouse smelled of wet ash, old soap, and fish oil."
    n "A red door sat at the end, paint cracked around the handle."
    n "On the ground, two shallow grooves marked the dirt where heavy wood had been dragged inside."

    s "Subtle."

    e "They did not expect a search before noon."

    s "Or they are stupid."

    e "Both are possible."

    n "A boy stepped out from behind a rain barrel. Blue cord circled his wrist."
    n "He saw Emiko."
    n "He saw Shina."
    n "He made the correct decision too late."

    play sound "audio/sfx/footstep_scramble.ogg"

    show shina smug at right_bodyguard

    s "I have him."

    n "Shina hooked the end of her naginata shaft across the alley at ankle height. The boy jumped it, proud for half a breath."
    n "Emiko caught his collar when he landed."

    show emiko stern at left_bodyguard

    e "Name."

    lookout "No."

    e "Good. You know which answers are dangerous."

    s "Try easier. Is the shrine box inside?"

    lookout "No."

    s "That was worse."

    e "How many?"

    lookout "I cannot count."

    s "You can run messages but not count men?"

    lookout "I run fast."

    e "Five?"

    n "His eyes moved."

    e "Six."

    s "And probably drunk."

    e "Stay here."

    lookout "Are you arresting me?"

    e "Not yet."

    lookout "That is not better."

    s "It is honest."

    n "Emiko set him beside the rain barrel with one look sharp enough to pin him there."

    s "You know, if we had asked around separately, I would have found this faster."

    if ep01_split_up:
        e "You did."
        s "Do not agree after I complain. It ruins the shape of it."
    else:
        e "You may file that opinion with the advisor who handles inefficient suggestions."
        s "There is an advisor for that?"
        e "There is an advisor for everything. That is why nothing moves quickly."

    n "A burst of laughter came from inside the red door. Dice rattled against wood."

    e "The box is inside."

    s "Now you sound certain."

    e "I know its sound."

    s "You know the sound of an offering box being used as a gambling table."

    e "I know the sound of cedar planks under impact."

    s "That is somehow worse."

    jump ep01_gambling_den_reveal

# -----------------------------------------------------------------------------
# Gambling den reveal
# -----------------------------------------------------------------------------

label ep01_gambling_den_reveal:

    scene bg gambling_den_exterior
    with dissolve

    show emiko alert at left_bodyguard
    show shina weapon_ready at right_bodyguard
    with dissolve

    play sound "audio/sfx/sliding_door_force.ogg"

    n "Emiko opened the red door without knocking."

    scene bg gambling_den_interior
    with dissolve

    play music "audio/music/comedy_tension.ogg" fadein 0.7

    n "The room went quiet in pieces."
    n "First the dice stopped. Then the cups. Then the whispering."
    n "At the center of the room sat the missing offering box, turned sideways and draped with a stained cloth. Coins, cups, dice, and half a bowl of pickled vegetables covered the top."

    show emiko stern at left_bodyguard
    show shina smug at right_bodyguard
    with dissolve

    gambler_boss "Private room."

    e "Shrine property."

    gambler_boss "You have proof?"

    n "Emiko looked at the crest carved into the side of the box."

    e "Yes."

    s "That crest being from the shrine was your first mistake."

    gambler_1 "We thought it was decorative."

    s "Your second mistake was saying that out loud."

    e "Remove everything from the top."

    gambler_boss "Now, listen. No one here stole anything. A man sold it to us."

    e "Name."

    gambler_boss "He did not give one."

    e "Convenient."

    gambler_boss "He said it brought luck."

    s "Did it?"

    gambler_2 "Fourteen straight wins."

    e "It accepts offerings. It does not bless dice."

    gambler_2 "Could be branching out."

    n "Shina made a short sound through her nose."

    e "Do not laugh."

    s "I did not."

    e "Your face moved."

    s "I have a face. It does that."

    gambler_boss "Take the box. We do not need trouble."

    n "He set one hand on the side of the offering box."
    n "Emiko's hand went to her katana."

    e "Move your hand."

    gambler_boss "Careful. The room is small."

    s "He is right."

    n "Shina shifted her grip on the naginata, judging the low ceiling, the gamblers pressed along the walls, the box in the middle, the oil lamp near the paper screen."

    s "Very small."

    e "Then everyone should sit down."

    gambler_boss "Or?"

    e "You will sit down badly."

    n "For a moment, no one moved."
    n "Then one gambler reached for the dice cup."

    stop music fadeout 0.5
    play music "audio/music/fight_cramped_room.ogg" fadein 0.5

    jump ep01_fight_choice_one

# -----------------------------------------------------------------------------
# Fight choice one
# -----------------------------------------------------------------------------

label ep01_fight_choice_one:

    menu:
        "The room erupts. What comes first?"

        "Protect the offering box before fighting.":
            $ ep01_box_protected = True
            $ duty_points += 1
            $ dignity_points += 2
            $ emiko_points += 1
            jump ep01_fight_protect_box

        "Use clean discipline and control the room.":
            $ duty_points += 1
            $ emiko_points += 2
            jump ep01_fight_clean_discipline

        "Let Shina break their rhythm with improvised chaos.":
            $ chaos_points += 2
            $ shina_points += 2
            $ ep01_fight_messy = True
            jump ep01_fight_improvised_chaos

label ep01_fight_protect_box:

    show emiko alert at left_bodyguard
    show shina weapon_ready at right_bodyguard

    n "Emiko moved to the offering box first."
    n "A stool came at her from the left. She kicked it down before it reached the carved side panel."

    play sound "audio/sfx/wood_crack.ogg"

    n "Shina stepped over the stool and drove the butt of her naginata into a man's stomach."

    s "You are protecting the furniture?"

    e "Shrine property."

    s "It has pickles on it."

    e "That is why I am angry."

    n "Two gamblers tried to lift the box between them. Emiko caught the nearest wrist and folded the man onto his knees."

    gambler_1 "Ow. Ow. That is my wrist."

    e "Yes."

    n "A dice cup rolled toward the door. Shina pinned it under one sandal."

    s "This important?"

    e "Evidence."

    s "Ugly evidence."

    $ ep01_dice_cup_taken = True

    jump ep01_fight_choice_two

label ep01_fight_clean_discipline:

    show emiko alert at left_bodyguard
    show shina annoyed at right_bodyguard

    n "Emiko did not draw her blade."
    n "The room was too tight, the box too close, the walls too crowded with foolish men who would move the wrong way when frightened."
    n "She used the scabbard instead."

    play sound "audio/sfx/scabbard_hit.ogg"

    n "One strike to a wrist. One to a knee. One hard shove that sent a gambler into the wall without cutting him open."

    s "Efficient. Boring, but efficient."

    e "Left side."

    s "I see him."

    n "Shina swept the naginata shaft low. The man with the knife lost his footing and landed beside the offering box with a cough."

    gambler_3 "Knife was for vegetables."

    s "Then you should have stayed near vegetables."

    n "The dice cup rolled under the box. Emiko saw it, but another gambler grabbed for the oil lamp."

    e "Lamp."

    s "On it."

    jump ep01_fight_choice_two

label ep01_fight_improvised_chaos:

    show emiko stern at left_bodyguard
    show shina weapon_ready at right_bodyguard

    n "Shina grinned without warmth."

    s "Small room. Bad decisions. My kind of math."

    e "Do not damage the box."

    s "Then move the box."

    n "She hooked her naginata shaft under the stained cloth and ripped it sideways. Cups, dice, coins, and pickled vegetables flew across the room."

    play sound "audio/sfx/table_scatter.ogg"

    gambler_2 "My winnings!"

    s "Your evidence."

    n "A gambler slipped on a pickle and took down the man behind him."

    e "Shina."

    s "That one was the pickle."

    e "You created the pickle."

    s "The cook created the pickle. I revealed its purpose."

    n "Emiko blocked a punch with her forearm and drove the attacker back into a stack of crates."

    play sound "audio/sfx/crate_hit.ogg"

    e "The room is becoming less intact."

    s "Then we are halfway done."

    jump ep01_fight_choice_two

# -----------------------------------------------------------------------------
# Fight choice two
# -----------------------------------------------------------------------------

label ep01_fight_choice_two:

    menu:
        "The gambling boss goes for the rear door. How do they stop him?"

        "Emiko blocks the exit while Shina covers the box.":
            $ bond_points += 1
            $ duty_points += 1
            jump ep01_fight_exit_block

        "Shina cuts him off through the room while Emiko holds the center.":
            $ bond_points += 1
            $ shina_points += 1
            jump ep01_fight_room_cutoff

        "Ignore him and secure the box first.":
            $ dignity_points += 1
            $ evidence_points -= 1
            jump ep01_fight_secure_first

label ep01_fight_exit_block:

    n "Emiko reached the rear door before the gambling boss did."
    n "She put one hand against the frame and one hand on her sword hilt."

    e "No."

    gambler_boss "Move."

    e "No."

    gambler_boss "That all you say?"

    e "When it is enough."

    n "He swung. She stepped inside the strike and struck him once in the ribs with the scabbard."

    play sound "audio/sfx/body_hit.ogg"

    n "Behind her, Shina planted one foot on the offering box and pushed a gambler away with the naginata shaft."

    s "I am guarding your sacred table."

    e "Do not call it that."

    s "I said sacred."

    e "The second word was the problem."

    jump ep01_fight_end

label ep01_fight_room_cutoff:

    n "Shina did not chase straight."
    n "She stepped onto a crate, caught a ceiling beam with one hand, and dropped down in front of the rear door."

    play sound "audio/sfx/wood_creak.ogg"

    s "Leaving before the game ends?"

    gambler_boss "Get out of my way."

    s "Polite. Still no."

    n "He reached for a hidden knife. Shina caught his sleeve with the naginata hook and yanked his arm wide."

    s "Emiko."

    n "Emiko crossed the room in three steps and struck the knife from his hand."

    play sound "audio/sfx/knife_drop.ogg"

    e "You saw the sleeve."

    s "You saw me see it."

    e "Acceptable."

    s "Careful. That was almost another compliment."

    jump ep01_fight_end

label ep01_fight_secure_first:

    n "Emiko chose the box."
    n "She pushed it back against the wall and planted herself in front of it while Shina knocked two gamblers away from the coins scattered near the floor."

    s "Boss is running."

    e "The box leaves safely."

    s "And he leaves loudly."

    n "The rear door slammed open. Footsteps hit the outside stair."

    play sound "audio/sfx/door_slam.ogg"

    e "Track him after."

    s "After I finish protecting wood from men who keep losing to furniture."

    n "One gambler lifted both hands."

    gambler_1 "I surrender to the furniture."

    e "The shrine."

    gambler_1 "I surrender to the shrine."

    jump ep01_fight_end

# -----------------------------------------------------------------------------
# Fight result
# -----------------------------------------------------------------------------

label ep01_fight_end:

    stop music fadeout 1.0
    play music "audio/music/aftermath_light.ogg" fadein 1.0

    scene bg gambling_den_interior_after
    with dissolve

    show emiko stern at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    n "When the room stopped moving, six gamblers sat on the floor with their hands visible."

    if ep01_fight_messy:
        n "A seventh man remained half under a shelf, blinking at a pickle stuck to his sleeve."
        s "That one surrendered to lunch."
        e "Do not record that."
    else:
        n "Only one shelf had broken. Emiko looked at it, judged the damage, and filed her displeasure away for later use."

    if ep01_box_protected:
        n "The offering box had a new scratch along the lower left side, but the crest remained clean."
        e "Minor damage."
        s "That is the happiest I have heard you sound."
        e "It is not happiness."
    else:
        n "The offering box had acquired scratches, stains, and one small dent where a dice bowl had struck the lid."
        e "I will need oil, cloth, and an apology from every person in this room."
        gambler_2 "To you?"
        e "To the box."
        s "Start kneeling. She is serious."

    n "Shina crouched beside the box and lifted the stained cloth with two fingers."

    s "Who sold it?"

    gambler_1 "A man with a traveling hat. Kept his face down."

    e "Voice?"

    gambler_1 "Soft. Polite. Not from this district."

    s "Hands?"

    gambler_1 "Clean. No work marks."

    e "A hired thief or a clerk."

    s "Or both. Clerks steal in neat ways."

    e "This was not neat."

    s "The thief was neat. The buyers were idiots."

    n "The lookout boy peered through the open door."

    lookout "Are they dead?"

    s "Only socially."

    e "You ran messages. You will come with us."

    lookout "I knew that was coming."

    s "Yet you looked through the door. Curious and doomed. Common pairing."

    if ep01_dice_cup_taken:
        n "Shina handed Emiko the dice cup she had pinned earlier."
        s "Ugly evidence."
        e "Useful evidence."
        n "Inside the cup, a folded scrap of paper clung beneath the false bottom."
        e "Hidden compartment."
        s "In a dice cup. These people have layers. Bad ones, but layers."
        $ evidence_points += 1
    else:
        n "Emiko found the dice cup beneath the box after the room was cleared."
        n "A false bottom shifted when she turned it over."
        e "Hidden compartment."
        s "Of course the cup has secrets. Everything here smells like secrets and old soup."
        $ ep01_dice_cup_taken = True

    n "The paper inside held no name. Only a small sketch of the shrine's eastern gate and three short marks beside it."

    s "Counting marks?"

    e "Response marks."

    s "You know that from three lines?"

    e "The eastern gate is where the thieves exited. Three marks for three people, or three checks."

    s "Or someone cannot draw bushes."

    e "Possible. Less useful."

    n "Emiko folded the paper and placed it inside her sleeve."

    e "We return."

    s "With the box, the boy, six gamblers, a secret cup, and an odor that will follow us for blocks."

    e "Yes."

    s "Quiet attempted."

    e "Quiet failed."

    s "Not fully. No one is screaming."

    n "From outside, someone screamed that the cursed shrine box had eaten a gambler's luck."

    if ep01_curse_rumor:
        e "Shina."
        s "That spread faster than expected."
    else:
        s "Do not look at me. I did not start that one."
        e "You were near enough to deserve suspicion."

    jump ep01_return_to_shrine

# -----------------------------------------------------------------------------
# Return and end card
# -----------------------------------------------------------------------------

label ep01_return_to_shrine:

    scene bg shrine_courtyard_afternoon
    with fade

    play music "audio/music/shrine_afternoon.ogg" fadein 1.0

    show aya concerned at center_priestess
    with dissolve

    n "By midafternoon, the offering box stood again before the main hall."
    n "It had been scrubbed twice."
    n "It still smelled faintly of smoke, old coins, and pickled vegetables."

    show emiko neutral at left_bodyguard
    show shina neutral at right_bodyguard
    with dissolve

    advisor_1 "People are asking why the offering box smells like a tavern floor."

    s "Tell them spiritual humility."

    advisor_1 "Absolutely not."

    e "Tell them nothing. The box was recovered. The thieves are being held. The shrine grounds remain open."

    advisor_2 "There are rumors it was cursed."

    if ep01_curse_rumor:
        n "Aya looked at Shina."
        a "A curse rumor."
        s "A controlled investigative rumor."
        m "It reached the fishmonger before you reached the shrine."
        s "Fast fishmonger."
        m "Very fast. Very loud."
        s "Evil priestess..."
    else:
        a "A curse rumor began without your help?"
        s "Thank you for saying that where Emiko can hear it."
        e "I remain unconvinced."

    n "Makoto stood near the restored box, one sleeve over her mouth."

    show makoto amused at center_priestess
    with dissolve

    m "It does smell unfortunate."

    e "It will fade."

    m "The smell or the rumor?"

    e "Both."

    s "One of those is optimistic."

    a "Was anyone seriously hurt?"

    e "No."

    s "A few gamblers learned about floorboards."

    e "No one was seriously hurt."

    a "Good."

    n "Aya moved closer to the offering box. She did not touch the scratched side. She looked at it, then at Emiko."

    a "Thank you."

    e "Priestess."

    n "The answer came at once. Formal. Correct."
    n "Aya's gaze stayed on her for one quiet second longer than needed. Emiko looked away first."

    s "So. We are pretending this was quiet?"

    advisor_1 "We are describing it as swift internal recovery."

    s "That is pretending with nicer sandals."

    m "I like that phrase."

    advisor_2 "Please do not."

    n "Emiko removed the folded paper from her sleeve and passed it to Aya."

    e "This was inside a false-bottom dice cup. The eastern gate is drawn here. These marks may indicate the number of people used in the theft. They may also indicate timing."

    a "So the theft was not only theft."

    e "No."

    s "Someone wanted to see how fast we moved."

    m "And how loudly."

    s "Again, why did that land on me?"

    e "Experience."

    n "Aya studied the paper. The wind lifted one corner and pressed it against her thumb."

    a "Then we should assume this was watched."

    e "I already do."

    s "That must save you time. Assuming the worst as a hobby."

    e "It is not a hobby."

    s "No, hobbies bring joy."

    m "Shina."

    s "What? That was restraint."

    n "Aya folded the paper again, careful along the crease."

    a "We will handle the public story. You both should rest."

    e "I will inspect the eastern gate first."

    s "I will eat first."

    e "You ate during the investigation."

    s "That was work food."

    e "There is no such category."

    s "There is when I am working."

    m "Bring her something, Shina."

    s "Emiko?"

    m "Yes."

    s "She eats rules and disappointment."

    a "She likes rice cakes with black sesame."

    n "Emiko's head turned slightly."

    e "Priestess."

    a "You forget I notice things."

    n "Shina looked between them and wisely chose to make it someone else's problem later."

    s "Fine. Rice cakes. If she refuses, I am eating hers."

    e "I did not ask for food."

    a "No."

    n "Aya's smile was small enough to deny in public."

    a "You usually do not."

    n "Emiko had no answer ready for that."

    m "Remarkable. The offering box returns and Emiko loses a duel in the same afternoon."

    e "I did not lose a duel."

    s "You did not answer. That counts."

    e "No."

    s "Very compelling defense."

    n "The advisor cleared his throat with the desperation of a man watching dignity walk toward the edge of a roof."

    advisor_1 "The official statement?"

    a "The offering box was recovered through prompt action by the shrine's Shadows. The matter is contained."

    m "And no gambling room is to use sacred property as furniture again."

    advisor_2 "We cannot put that in the statement."

    s "Cowardice."

    e "For once, I agree."

    n "Shina stared at her."

    s "Do not do that without warning."

    n "Aya looked down at the paper in her hand. The three marks beside the eastern gate remained visible through the fold."

    a "Contained, then. For now."

    if evidence_points >= 3:
        $ ep01_final_result = "strong_evidence"
        n "The dice cup, the lookout, and the eastern gate sketch gave them more than a recovered box."
        n "Someone had tested the shrine and left measuring lines behind."
    elif chaos_points >= 3:
        $ ep01_final_result = "messy_recovery"
        n "The box had returned. So had the rumors."
        n "By evening, three versions of the story would exist, and none of them would help the advisors sleep."
    else:
        $ ep01_final_result = "clean_recovery"
        n "The box had returned with limited damage and enough evidence to trouble the quiet parts of the shrine."

    $ ep01_complete = True

    scene black
    with fade

    centered "Chapter 1 Complete"

    centered "The Missing Offering Box"

    centered "Result: [ep01_final_result]"

    stop music fadeout 1.5

    return
