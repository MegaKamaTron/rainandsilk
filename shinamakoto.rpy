# =========================================================
# Chapter 3: The Road Knows Her Name
# Shina & Makoto — Pilgrimage Day
# =========================================================
# 
# NOTE: Add the following to 02_characters.rpy before use:
# 
# define sh = Character(
# "Shina",
# color="#B5562A",
# who_color="#B5562A",
# ctc="ctc_icon",
# ctc_pause="ctc_icon",
# ctc_timedpause="ctc_icon",
# ctc_position="fixed",
# )
# 
# define mk = Character(
# "Makoto",
# color="#8B6A9B",
# who_color="#8B6A9B",
# ctc="ctc_icon",
# ctc_pause="ctc_icon",
# ctc_timedpause="ctc_icon",
# ctc_position="fixed",
# )
# 
# =========================================================

label chapter_3_start:
    $ current_chapter = "ch3"
    $ save_name = _("Chapter III")
    $ shina_honest_points = 0
    $ shina_guard_points = 0
    $ menu_owner = None

# =========================================================
# PROLOGUE
# =========================================================

label ch3_prologue:
    scene bg black with slow_dissolve
    window hide

    play music temple_theme fadein 2.5 volume 0.55
    pause 0.8
    play ambience forestamb fadein 2.0 volume 0.45
    pause 1.0

    op "Four years on the same roads, and she'd picked up things no one ever thought to tell her."
    op "She just had to... pay attention."
    op "Which stone to step around without thinking. Which bell to wait for before moving."
    op "The way she paused at a doorway, holding her breath just a little — not nervous, exactly. More like good manners toward whatever was on the other side."

    $ duck(level=0.35, delay=0.4)
    op "Shina hadn't kept a list on purpose. At least, she'd never admit she had."
    op "She just paid attention."
    op "Like any good Shadow would for their Priestess."
    $ unduck(level=0.55, delay=1.5)

    op "The mountain road to the high shrine wound through cedar and stone switchbacks, the same as always."
    op "She'd walked it with the Priestess more times than she could count. Only once alone — the day she decided to stay."
    op "Every time Makoto walked this path, it was like she'd carved it herself. Easy. Effortless. Like breathing."
    op "And every time they walked together, Shina stayed two steps ahead."
    op "Not because anyone told her to."
    op "Just because she wanted to."
    window hide
    scene bg black with slow_dissolve
    stop music fadeout 3.0
    pause 0.8
    stop ambience fadeout 2.5
    pause 2.0
    jump ch3_s1_morning
# =========================================================
# SCENE 1 — MORNING
# =========================================================
label ch3_s1_morning:
    scene bg shrine_room_morning
    with dissolve
    # play ambience morning_birds fadein 2.0 volume 0.6
    play music temple_theme fadein 1.5 volume 0.25
    pause 1.5

    n "Morning at the mountain shrine came in layers — birds before light, then gray bleeding into amber through the paper screens."

    n "Makoto sat at her writing desk when Shina appeared in the doorway, her messy hair almost brushing the top of the frame."
    n "Both sandals untied, and she still thought carrying two cups in one hand was a good idea."

    show shina smile at st_right
    with dissolve
    n "She hadn't knocked. Or closed the door behind her."
    n "She never knocked anymore."

    sh "Tea's getting cold."
    show makoto neutral at st_left
    with dissolve
    mk "Then perhaps you should've brought it sooner."
    sh "Yeah, yeah."

    n "She set one cup next to the desk without being asked, then dropped onto the low step at the edge of the room and stretched her legs out."

    show shina relaxed at st_right
    n "Three attendants had told her, at different points over the last four years, that the step wasn't for her."
    n "She had no idea."

    show makoto knowing at st_left
    mk "The step again."
    show shina shrug at st_right
    sh "It's a good step."
    mk "There are four designated spots for a Shadow during morning correspondence."
    show shina relaxed at st_right
    sh "Sure."
    show makoto neutral at st_left
    mk "That step isn't one of them."
    show shina shrug at st_right
    sh "That's too bad. It's a really good step."
    hide shina with dissolve
    hide makoto with dissolve
    n "The priestess hid another smile behind her cup and took a sip."

    # play sound "morningbell.ogg"
    pause 0.5
# #######################################
# MENU 1
# #######################################
    $ menu_owner = "shina"
    menu:
        "\"Oi. Sun's up. You coming or what?\"":
            show shina smile at st_right
            with dissolve
            sh "The sun's up, you know. Coming or what?"
            n "She said it from the step instead of the door, which definitely wasn't proper Shadow protocol."
            n "Makoto put her brush down."
            show makoto soft laugh at st_left
            mk "I've been ready since before you got here."
            show shina embarrassed at st_right
            sh "Then why are we still sitting here?"
            mk "I was seeing how long it'd take you to ask."
            show shina embarrassed at st_right
            sh "Evil Priestess."
            show makoto laugh hide at st_left

        "Say nothing.":
            $ shina_honest_points += 1
            show shina relaxed at st_right
            with dissolve
            n "Shina didn't say anything. Just unfolded herself from the step, finished her tea, and appeared at the edge of Makoto's reading light with the travel pack already over one shoulder."
            sh "Any good?"
            n "Makoto read one more line."
            sh "...No."
            sh "Then why keep reading?"
            show makoto soft laugh at st_left
            mk "You could just say when you're ready."
            show shina nagata smug at st_right
            sh "This is faster. And more fun."
            mk "It's also kind of threatening."
            sh "I'd call it 'strongly encouraging.'"
            show makoto laugh hide at st_left

        "\"The road won't walk itself, evil Priestess.\"":
            show shina relaxed at st_right
            with dissolve
            $ shina_honest_points += 1
            sh "The road won't walk itself, you know. Evil Priestess."
            hide shina with dissolve
            n "Shina stood and stretched again before picking up her naginata that she had rested leaning against the wall."
            n "Makoto set her brush down carefully — the way someone does when they're trying not to laugh."
            show makoto soft laugh at st_left
            mk "That name—"
            show shina nagata smug at st_right
            sh "-Fits."
            mk "--is growing on me."
            n "Shina made a sound like a scoff, then started watching the shadow of the rain chain outside sway in the morning light."
            sh "Yeah, yeah. Don't get too used to it."
            show makoto laugh hide at st_left
            mk "Too late."
    $ menu_owner = None
# #######################################
# END MENU 1
# #######################################
    pause 1.0
    hide shina with dissolve
    hide makoto with dissolve
    pause 0.5
    window hide
    scene bg black with dissolve
    stop music fadeout 1.5
    stop ambience fadeout 2.0
    pause 1.5
    jump ch3_s2_road
# =========================================================
# SCENE 2 — THE ROAD
# =========================================================
label ch3_s2_road:
    scene bg road_cedar_day
    with dissolve
    play ambience forestamb fadein 2.0 volume 1.0
    play music bgm_pilgrimage_soft fadein 1.5 volume 0.3
    pause 2.0
    window show dissolve_2

    n "The road climbed in long, lazy switchbacks through cedar and pine."
    n "The air still held last night's cold rain, and the mountain pressed close on the uphill side."

    show makoto neutral at stage_right with dissolve
    show shina resting nagata bored at stage_left with dissolve

    n "Makoto moved at the pace of someone who'd done this a hundred times — calm, unhurried, her pale shrine robes bright against all the green."

    $ duck(level=0.3, delay=0.3)
    n "Shina walked two steps ahead."
    n "Not three. Two."
    n "Close enough to hear if a footstep changed."
    $ unduck(level=0.3, delay=1.5)

    show bg road_fork with dissolve
    show shina nagata neutral
    sh "Fork up ahead. Left path's faster, but the stones are bad after the rain."
    show makoto neutral
    mk "And the right?"
    sh "Longer. Better footing."
    show makoto soft laugh
    mk "You checked this morning."
    show shina nagata neutral
    sh "I check every time."

    n "She said it like it was nothing. Like it was just the practical thing to do."

    mk "Right path, then."
    sh "Right path."

    n "They walked."

    # ── INVENTORY TRIGGER A — ROAD NOTES ──────────────────
    n "A beat of quiet. Then Shina reached into her travel pack without looking."
    $ inventory_valid_item = "road_notes"
    $ item_used = renpy.call_screen("inventory_screen")
    $ inventory_valid_item = ""

    if item_used == "road_notes":
        show shina relaxed at stage_left with dissolve
        n "She pulled out a small folded piece of paper. Worn soft from being handled so much."
        sh "I keep notes. Stones, drainage, which stretches get bad after rain."
        show makoto soft laugh at stage_right with dissolve
        mk "How long have you been doing this?"
        sh "Since the second pilgrimage."
        mk "You never mentioned it."
        sh "You never asked."
        n "She tucked the notes back away."
        n "Makoto didn't say anything else about it."
        n "The truth had been seen. That was enough."
        $ shina_honest_points += 1
    # ── END TRIGGER A ─────────────────────────────────────

    n "A group of pilgrims passed going the other way, bowing low when they recognized Makoto's robes."
    n "Shina watched them until they disappeared around the bend."

    show makoto soft laugh
    mk "They were pilgrims, Shina."
    show shina nagata neutral
    sh "Probably."
    mk "Definitely."
    sh "Sure."

    show makoto knowing
    mk "You do this every time someone bows."
    sh "I do it every time someone gets close."

    n "A beat."

    show shina nagata confused
    sh "That sounded more serious than I meant."
    show makoto soft laugh
    mk "Did it?"
    show shina nagata mad
    sh "Don't."
    n "Makoto looked ahead at the road."
    n "Which was worse."

    show bg road with dissolve
    $ duck(level=0.25, delay=0.4)
    n "The path curved around an old rock shelf, the valley opening up wide and low below them on the left."
    n "Shina shifted half a step toward the drop side."
    n "Not a decision. Just what her feet did."
    $ unduck(level=0.3, delay=1.5)

    show makoto neutral
    mk "You know, the court assigns Shadows so a Priestess doesn't have to worry about the road."
    show shina nagata smug
    sh "Mm."
    mk "Experienced ones. Formal records. Institutional backing."
    sh "Sounds thorough."
    show makoto knowing
    mk "You could take an afternoon off sometime."
    show shina nagata neutral
    sh "I'm fine here."
    show makoto soft laugh
    mk "I know you are."
    mk "I'm just saying you might also be fine somewhere else. Once in a while."
    show shina nagata confused
    sh "Yeah... not really a somewhere-else person."

    n "She said it the way she said things she meant."
    n "Plain. No extra room around it."

    show shina nagata neutral
    sh "For what it's worth. You could've gotten a court-appointed Shadow."
    sh "Official record, letters of recommendation..."
    mk "I could have."
    sh "Didn't end up that way."
    show makoto neutral
    mk "No. It didn't."
    show shina nagata neutral
    sh "Just saying."

    $ duck(level=0.2, delay=0.4)
    n "She was looking at the trees when she said it."
    n "The way she looked at things she was trying not to think about."
    $ unduck(level=0.3, delay=1.5)

    show makoto soft laugh
    mk "I don't remember ever complaining."
    show shina nagata neutral
    sh "I know."
    sh "Still."

    pause 0.5
    show shina nagata neutral
    sh "Ronin thing, I think."
    sh "You wander until you find something worth stopping for. Then you stop."

    n "She said it like it was just road logic. Practical habit. The kind of sentence that shuts down before anyone can look too close."

    # ── INVENTORY TRIGGER B — SHARED ROAD MEMORY ──────────
    n "The road was quiet. Shina watched the tree line."
    $ inventory_valid_item = "memory"
    $ item_used = renpy.call_screen("inventory_screen")
    $ inventory_valid_item = ""

    if item_used == "memory":
        n "The first time she'd stayed after being formally dismissed, nobody said anything."
        n "The Priestess just walked back through the inner gate without a word."
        n "Shina figured that meant she was allowed."
        n "Four years later, she still hadn't confirmed it."
        n "She also hadn't ever left before being released."
        n "Those two facts had quietly arranged themselves into something she didn't have a name for."
        $ shina_honest_points += 1
    # ── END TRIGGER B ─────────────────────────────────────

# #######################################
# MENU 2
# #######################################
    $ menu_owner = "shina"
    menu:
        "Shina catches herself."

        "\"Don't read into that.\"":
            sh "Don't read into that."
            show makoto soft laugh
            mk "I wasn't."
            show shina nagata mad
            sh "Good."
            mk "Though now I am."
            show shina embarrassed
            sh "Evil Priestess."
            show makoto laugh hide

        "She keeps walking. Doesn't take it back.":
            $ shina_honest_points += 1
            n "She didn't take it back."
            n "Just kept walking, her grip settling lower on the naginata the way it did when she'd said something true and decided to leave it there."
            show makoto neutral sad
            n "Makoto looked at the road ahead."
            n "Whatever was on her face, she kept it there."

        "She pivots. \"Anyway. Right path's around this rock.\"":
            sh "Anyway. Right path's around this rock. Watch your step."
            show makoto knowing
            mk "You mentioned that."
            sh "Mentioning it again."
            show makoto soft laugh
            mk "Shina."
            show shina nagata mad
            sh "What."
            mk "You're very easy to read."
            show shina embarrassed
            sh "I'm a closed book."
            mk "You're a very open scroll."
            show shina nagata mad
            sh "I hate this road."

    $ menu_owner = None
# #######################################
# END MENU 2
# #######################################

    window hide
    pause 0.5

    jump ch3_s3_snake

# =========================================================
# SCENE 3 — THE SNAKE
# =========================================================
label ch3_s3_snake:
    show bg road_snake with dissolve
    show shina resting nagata bored at stage_left
    show makoto neutral at stage_right
    window show dissolve_2

    n "The road narrowed through a stand of old cedar, tree roots crossing the stones in ridges worn smooth by years of footsteps."
    n "The light dropped here. The forest pressed in close."

    n "Shina stopped."
    n "No warning. No word."
    n "One hand up."

    mk "Shina."
    sh "Hold on."

    $ duck(level=0.2, delay=0.3)
    n "She stepped off the path into the brush."
    n "Makoto waited."
    n "She'd learned to tell the difference between Shina's stillness when there was nothing and Shina's stillness when there was something."
    n "This was something."
    $ unduck(level=0.3, delay=1.5)

    n "A dry, low sound in the cedar."
    n "Then Shina's hand came out of the brush holding a snake — dark-banded, thick through the middle, and very focused on a shrew that had picked the wrong moment to be visible."

    show makoto soft laugh
    mk "..."
    show shina nagata smug
    sh "Yeah."

    n "She carried it, slow and easy, further into the brush on the uphill side of the road."
    n "Set it down."
    n "Came back."
    n "Picked up the naginata she'd left leaning against the cedar."

    show shina nagata smug
    sh "Shrew gets another day."
    show makoto neutral
    mk "You could've just walked us past it."
    sh "Could've."
    mk "Or made some noise. It would've moved."
    sh "Probably."
    show makoto soft laugh
    mk "So why—"
    show shina nagata neutral
    sh "I don't know."
    sh "It wasn't doing anything worth dying for."

    n "She settled the naginata back across her shoulders."

    $ duck(level=0.15, delay=0.5)
    n "Makoto watched her."
    n "The way she'd moved into the brush — no announcement, no thinking about it. Just picked the thing up and carried it somewhere the problem solved itself."
    n "The shrew. The snake. Shina, apparently, had an opinion on who got to walk away from an afternoon."
    n "She hadn't thought about it before moving."
    n "That was the thing."
    $ unduck(level=0.3, delay=2.0)

    $ shina_guard_points += 1

    show makoto neutral sad
    n "She didn't say anything about it."
    n "Just fell back into step."

    show shina nagata neutral
    sh "Right. Where were we."
    show makoto soft laugh
    mk "You were explaining your philosophy on roadside animals."
    show shina nagata smug
    sh "I don't have a philosophy."

    $ duck(level=0.15, delay=0.3)
    mk "No."
    mk "You just have instincts."
    $ unduck(level=0.3, delay=1.5)

    show shina nagata neutral
    n "She said it the way she said true things that didn't need pushing."
    n "Shina didn't answer."
    n "The road leveled out for a bit, opening up to a view of the ridge, bright with the last of the afternoon."
    n "They walked."

    window hide
    pause 1.0
    scene bg black with dissolve
    stop music fadeout 1.5
    stop ambience fadeout 2.0
    pause 1.5

    jump ch3_s4_arrival


# =========================================================
# SCENE 4 — ARRIVAL
# =========================================================

label ch3_s4_arrival:
    scene bg temple_dusk_02 with slow_dissolve
    play ambience forestamb fadein 1.5 volume 0.7
    play music temple_theme fadein 2.0 volume 0.3
    pause 2.0
    window show dissolve_2

    n "The upper shrine came into view as the light started to fade."
    n "Stone lanterns already lit along the path. Cedar smoke and cold rock."
    n "A bell rang, deeper than the ones in the valley."

    show makoto neutral at stage_right with dissolve
    show shina nagata neutral at stage_left with dissolve

    n "Makoto's attendants met them at the outer gate."
    n "Greetings. Brief, formal. Makoto handled it all with the ease of someone who'd long stopped noticing how naturally the weight of this sat on her."
    n "Shina stood to the side and said nothing."
    n "Which was as close to formal as she got."

    $ duck(level=0.2, delay=0.3)
    n "The attendants led Makoto through the preparations. Robes checked, offerings laid out, ritual items arranged."
    n "Shina followed as far as the inner gate."
    n "Then stopped."
    n "This was where she always stopped."
    n "The rite was Makoto's. That threshold was hers."
    $ unduck(level=0.3, delay=1.5)
    
    show bg temple_dusk_02_door with dissolve
    show makoto neutral
    n "Makoto paused at the gate and turned back."

    show makoto knowing
    mk "The shrine has a kitchen. A garden with a decent view of the valley from the east wall."
    show shina nagata neutral
    sh "I know."
    mk "The attendants can show you. There's no reason to stand out here all evening."

    # ── INVENTORY TRIGGER C — DRIED PERSIMMON ─────────────
    n "Shina looked at the gate."
    $ inventory_valid_item = "trail_ration"
    $ item_used = renpy.call_screen("inventory_screen")
    $ inventory_valid_item = ""

    if item_used == "trail_ration":
        show shina relaxed at stage_left with dissolve
        n "She reached into her travel pack. Pulled out a cloth-wrapped piece of dried persimmon."
        n "Held it out toward Makoto without quite looking at her."
        sh "Take this. You'll be in there two hours, and you didn't eat at the waystation."
        show makoto neutral sad at stage_right with dissolve
        n "Makoto looked at the offered food."
        n "Then at Shina, who was very carefully watching the cedar at the edge of the path."
        mk "..."
        n "She took it."
        n "Shina's hand went back to the naginata like nothing had happened."
        $ shina_honest_points += 1
        $ shina_guard_points += 1
    # ── END TRIGGER C ─────────────────────────────────────

    sh "I'm fine."
    show makoto neutral
    mk "You've been on the road since dawn."
    sh "So have you."
    mk "I'm about to sit down for two hours."
    sh "Then someone should be outside when you come back out."

    n "A pause."
    n "Makoto looked at her — that steady, unhurried look she used when she was deciding whether to push."

    show makoto soft laugh
    mk "Shina."
    mk "Go eat something. I'll be—"

    show shina nagata neutral
    n "Shina shifted her weight."
    n "The easy answer was right there."
    n "She let it pass."

    $ duck(level=0.1, delay=0.4)
    sh "Evil Priestess."
    pause 1.0
    sh "I'm staying."
    $ unduck(level=0.2, delay=2.0)

    n "She dropped onto the step beside the inner gate — the wrong step, the one nobody had marked for anything — and set the naginata across her knees."

    $ duck(level=0.1, delay=0.3)
    n "She didn't look up."
    n "If her ears were warm, her collar hid it."
    $ unduck(level=0.2, delay=2.0)

    $ shina_honest_points += 1

    show makoto neutral
    pause 1.0

    n "Makoto stood at the gate."
    n "Then she turned toward the inner shrine."

    $ duck(level=0.1, delay=0.4)
    mk "I know."
    $ unduck(level=0.2, delay=2.5)

    n "Two words."
    n "Said facing the doors."

    hide makoto with dissolve
    pause 1.5

    show shina nagata neutral at stage_left

    $ duck(level=0.1, delay=0.3)
    n "The gate closed."
    n "Shina pulled her collar up against the evening chill and watched the lanterns come alive along the path, one by one."
    $ unduck(level=0.2, delay=3.0)

    window hide
    pause 1.0
    hide shina with dissolve
    scene bg black with slow_dissolve
    stop music fadeout 2.0
    stop ambience fadeout 2.5
    pause 2.0

    if shina_honest_points >= 3:
        jump ch3_secret_coda
    else:
        jump credits


# =========================================================
# SECRET SCENE — THE BRACELET
# =========================================================

label ch3_secret_coda:
    scene bg temple_interior with slow_walk_zoom
    play music hazymoon fadein 2.5 volume 0.25
    play ambience "audio/temple_tone.mp3" fadein 3.0 volume 0.2
    window hide
    pause 2.0
    window show

    n "The rite didn't take long."
    n "It never did, once the preparations were done. The actual moment — the prayer, the offering, the formal words spoken into the dark — was quieter than most people thought."

    show makoto neutral at stage_center with dissolve
    pause 1.0

    n "Makoto sat alone in the inner room after the attendants left."
    n "The offering smoke still rose in a thin thread, and the room had settled into that particular stillness of a place that's held many things without ever repeating them."

    $ duck(level=0.12, delay=0.5)
    n "Her right hand moved to her left wrist."
    n "Under her sleeve."
    n "She pressed her thumb against the stone — smooth, river-worn, its weight always exactly the same."
    n "She didn't look at it."
    n "She didn't need to."
    $ unduck(level=0.2, delay=3.0)

    show makoto neutral sad
    n "She was thinking about the step outside the gate."
    n "The wrong step. The one nobody had marked for anything."
    n "Shina on it, collar up, watching the lanterns come on."

    $ duck(level=0.1, delay=0.4)
    n "Her thumb moved once across the stone."
    n "Then stopped."
    n "The incense finished its thread."
    $ unduck(level=0.2, delay=3.5)

    n "Outside, she knew, Shina wasn't going anywhere."
    n "She'd said so. And meant it."

    hide makoto with slow_dissolve
    window hide
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    pause 3.0
    scene bg black with slow_dissolve
    pause 2.0

    jump credits
    return








# # =========================================================
# # Chapter 3: The Road Knows Her Name
# # Shina & Makoto — Pilgrimage Day
# # =========================================================
# # 
# # NOTE: Add the following to 02_characters.rpy before use:
# # 
# # define sh = Character(
# # "Shina",
# # color="#B5562A",
# # who_color="#B5562A",
# # ctc="ctc_icon",
# # ctc_pause="ctc_icon",
# # ctc_timedpause="ctc_icon",
# # ctc_position="fixed",
# # )
# # 
# # define mk = Character(
# # "Makoto",
# # color="#8B6A9B",
# # who_color="#8B6A9B",
# # ctc="ctc_icon",
# # ctc_pause="ctc_icon",
# # ctc_timedpause="ctc_icon",
# # ctc_position="fixed",
# # )
# # 
# # =========================================================

# label chapter_3_start:
#     $ current_chapter = "ch3"
#     $ save_name = _("Chapter III")
#     $ shina_honest_points = 0
#     $ shina_guard_points = 0
#     $ menu_owner = None

# # =========================================================
# # PROLOGUE
# # =========================================================

# label ch3_prologue:
#     scene bg black with slow_dissolve
#     window hide

#     play music temple_theme fadein 2.5 volume 0.55
#     pause 0.8
#     play ambience forestamb fadein 2.0 volume 0.45
#     pause 1.0

#     op "Four years on the same roads taught her things no one ever thought to mention."
#     op "They simply required....awareness."
#     op "Which stone she stepped around without looking. Which bell she waited for before moving."
#     op "The way she paused at a threshold, with a soft held breath and a gentle reverence for whatever lied behind it. Never hesitation...something closer to courtesy."

#     $ duck(level=0.35, delay=0.4)
#     op "Shina had not catalogued any of this deliberately. At least, she'd never admit that that could be the case."
#     op "She had simply been paying attention."
#     op "Like any good Shadow would do for their Priestess."
#     $ unduck(level=0.55, delay=1.5)

#     op "The mountain road to the high shrine wound through cedar canopies and rugged stone switchbacks the same way it always had."
#     op "She had escorted the Priestess on this path with her countless times before. Only once alone, when she had made the choice to stay."
#     op "Each time, the Priestess moved through it, it was as if she had forged the landscape itself. Flawlessly, filled with a casual intention that made it seem as easy as breathing."
#     op "Each time they traveled together, Shina walked two steps ahead."
#     op "Not because she was told to--"
#     op "--but simply because she chose to."
#     window hide
#     scene bg black with slow_dissolve
#     stop music fadeout 3.0
#     pause 0.8
#     stop ambience fadeout 2.5
#     pause 2.0
#     jump ch3_s1_morning
# # =========================================================
# # SCENE 1 — MORNING
# # =========================================================
# label ch3_s1_morning:
#     scene bg shrine_room_morning
#     with dissolve
#     # play ambience morning_birds fadein 2.0 volume 0.6
#     play music temple_theme fadein 1.5 volume 0.25
#     pause 1.5

#     n "Morning at the mountain shrine arrived in layers; birdsong before light, then the slow bleed of grey into amber through the paper screens."

#     n "Makoto was at her writing desk when Shina appeared in the doorframe. The tips of her unruly hair just brushing the top of the door frame."
#     n "Despite both of her sandals being untied, she still thought it was a good idea to carry two cups, balanced in one hand. "

#     show shina smile at st_right
#     with dissolve
#     n "She had not knocked. Nor closed the door after her."
#     n "She never knocked anymore."

#     sh "Tea's going cold."
#     show makoto neutral at st_left
#     with dissolve
#     mk "Then you should have brought it sooner."
#     sh "Yeah, yeah."

#     n "She set one cup beside the desk without being asked, then dropped onto the low step at the room's edge, and stretched her legs out in front of her."

#     show shina relaxed at st_right
#     n "Three attendants had told her, at various points over the past four years, that the step was not for her."
#     n "She remained unaware of this."

#     show makoto knowing at st_left
#     mk "The step again."
#     show shina shrug at st_right
#     sh "It's a good step."
#     mk "There are four designated positions for a Shadow during morning correspondence."
#     show shina relaxed at st_right
#     sh "Sure."
#     show makoto neutral
#     mk "That step is not one of them."
#     show shina shrug at st_right
#     sh "Shame. It's a really good step."
#     hide shina with dissolve
#     hide makoto with dissolve
#     n "The priestess hid another smile behind her ceramic cup and sipped her tea."

#     # play sound "morningbell.ogg"
#     pause 0.5
# # #######################################
# # MENU 1
# # #######################################
#     $ menu_owner = "shina"
#     menu:
#         "\"Oi. Sun's up. You coming or what?\"":
#             show shina smile at st_right
#             with dissolve
#             sh "The sun's up, you know. You coming or what?"
#             n "She said it from the step rather than the door, which was not the correct protocol for a Shadow in a formal context."
#             n "Makoto set her brush down."
#             show makoto soft laugh
#             mk "I have been ready since before you arrived."
#             show shina embarrassed
#             sh "Then why are we still sitting here?"
#             mk "I was waiting to see how long it would take you to ask."
#             show shina embarrassed at st_right
#             sh "Evil Priestess."
#             show makoto laugh hide

#         "She just stands.":
#             $ shina_honest_points += 1
#             show shina relaxed at st_right
#             with dissolve
#             n "Shina didn't say anything. Simply just unfolded herself from the step, finished the last of the tea, and appeared in the edge of Makoto's reading light with the travel pack already over one shoulder."
#             sh "Any good?"
#             n "Makoto read one more line of the letter."
#             sh "...No."
#             sh "Then why keep reading?"
#             show makoto soft laugh
#             mk "You could simply say when you're ready."
#             show shina nagata smug
#             sh "This is faster. And more fun."
#             mk "It is also vaguely threatening."
#             sh "I would say it's more like, strongly encouraging."
#             show makoto laugh hide

#         "\"The road won't walk itself, evil Priestess.\"":
#             show shina relaxed at st_right
#             with dissolve
#             $ shina_honest_points += 1
#             sh "The road won't walk itself y'know, evil Priestess."
#             n "Makoto set her brush down with the deliberate care of someone deciding not to laugh."
#             show makoto soft laugh
#             mk "That title--"
#             show shina nagata smug
#             sh "-Fits."
#             mk "It's starting to grow on me."
#             n "Something akin to a scoff came from Shina's throat, as she suddenly starting watching the shadow of the rain chain outside the door grow and sway, glinting in the morning light."
#             sh "Yeah, yeah. Don't get used to it."
#             show makoto laugh hide
#             mk "Too late."
#             show shina embarrassed
#     $ menu_owner = None
# # #######################################
# # END MENU 1
# # #######################################
#     hide shina with dissolve
#     hide makoto with dissolve
#     pause 0.5
#     window hide
#     scene bg black with dissolve
#     stop music fadeout 1.5
#     stop ambience fadeout 2.0
#     pause 1.5
#     jump ch3_s2_road
# # =========================================================
# # SCENE 2 — THE ROAD
# # =========================================================
# label ch3_s2_road:
#     scene bg road_cedar_day
#     with dissolve
#     play ambience forestamb fadein 2.0 volume 1.0
#     play music bgm_pilgrimage_soft fadein 1.5 volume 0.3
#     pause 2.0
#     window show dissolve_2

#     n "The road climbed in long, unhurried switchbacks through cedar and pine."
#     n "The air carried the cold of last night's rain and the mountain pressed close on the uphill side."

#     show makoto neutral at stage_right with dissolve
#     show shina resting nagata bored at stage_left with dissolve

#     n "Makoto moved through it at the pace of someone who had done this many times — composed, unhurried, her shrine robes pale against the green."

#     $ duck(level=0.3, delay=0.3)
#     n "Shina walked two steps ahead."
#     n "Not three. Two."
#     n "Close enough to hear a footstep change."
#     $ unduck(level=0.3, delay=1.5)

#     show bg road_fork with dissolve
#     show shina nagata neutral
#     sh "Fork up ahead. Left path is faster. Stones are bad since the rain."
#     show makoto neutral
#     mk "And the right?"
#     sh "Longer. Better footing."
#     show makoto soft laugh
#     mk "You checked this morning."
#     show shina nagata neutral
#     sh "I check every time."

#     n "She said it without particular weight. As if it were simply the most practical thing in the world."

#     mk "Right path, then."
#     sh "Right path."

#     n "They walked."

#     # ── INVENTORY TRIGGER A — ROAD NOTES ──────────────────
#     n "A beat of quiet. Then Shina reached into her travel pack without looking."
#     $ inventory_valid_item = "road_notes"
#     $ item_used = renpy.call_screen("inventory_screen")
#     $ inventory_valid_item = ""

#     if item_used == "road_notes":
#         show shina relaxed at stage_left with dissolve
#         n "She held out a small square of folded paper. Well-handled. The fold lines were soft with use."
#         sh "Keep a running record. Stones, drainage, which stretches go bad after rain."
#         show makoto soft laugh at stage_right with dissolve
#         mk "How long have you been doing this?"
#         sh "Since the second pilgrimage."
#         mk "You never mentioned it."
#         sh "You never asked."
#         n "She took the notes back. Put them away."
#         n "Makoto said nothing else about it."
#         n "The thing that was true had been seen. That was enough."
#         $ shina_honest_points += 1
#     # ── END TRIGGER A ─────────────────────────────────────

#     n "A pilgrim group passed going the other direction, bowing low when they recognized Makoto's robes."
#     n "Shina's eyes tracked them around the bend."

#     show makoto soft laugh
#     mk "They were pilgrims, Shina."
#     show shina nagata neutral
#     sh "Probably."
#     mk "Certainly."
#     sh "Sure."

#     show makoto knowing
#     mk "You do this every time someone bows."
#     sh "I do it every time someone comes close."

#     n "A beat."

#     show shina nagata confused
#     sh "That came out more serious than I meant it."
#     show makoto soft laugh
#     mk "Did it?"
#     show shina nagata mad
#     sh "Don't."
#     n "Makoto looked ahead at the road."
#     n "Which was worse."

#     show bg road with dissolve
#     $ duck(level=0.25, delay=0.4)
#     n "The path curved around a shelf of old rock, the valley opening wide and low below them on the left."
#     n "Shina shifted half a step toward the drop side."
#     n "Not a decision. Just what her feet did."
#     $ unduck(level=0.3, delay=1.5)

#     show makoto neutral
#     mk "You know, the court appoints Shadows specifically so a Priestess doesn't have to worry about the road."
#     show shina nagata smug
#     sh "Mm."
#     mk "Experienced ones. Formal records. Institutional backing."
#     sh "Sounds thorough."
#     show makoto knowing
#     mk "You might take the afternoon off sometime."
#     show shina nagata neutral
#     sh "I'm fine here."
#     show makoto soft laugh
#     mk "I know you are."
#     mk "I'm suggesting you might also be fine somewhere else. Occasionally."
#     show shina nagata confused
#     sh "Yeah, not really a somewhere-else person."

#     n "She said it the way she said things she meant."
#     n "Plain. No room around it."

#     show shina nagata neutral
#     sh "For what it's worth. You could've gotten someone court-appointed."
#     sh "Official record, letters of endorsement..."
#     mk "I could have."
#     sh "Didn't end up that way."
#     show makoto neutral
#     mk "No. It didn't."
#     show shina nagata neutral
#     sh "Just saying."

#     $ duck(level=0.2, delay=0.4)
#     n "She was looking at the tree line when she said it."
#     n "The way she looked at things she was pretending not to think about."
#     $ unduck(level=0.3, delay=1.5)

#     show makoto soft laugh
#     mk "I am not aware of ever having complained."
#     show shina nagata neutral
#     sh "I know."
#     sh "Still."

#     pause 0.5
#     show shina nagata neutral
#     sh "Ronin thing, I think."
#     sh "You move until you find the thing worth stopping for. Then you stop."

#     n "She said it like it was road-logic. Practical habit. The kind of sentence that closes before anyone can look at it too long."

#     # ── INVENTORY TRIGGER B — SHARED ROAD MEMORY ──────────
#     n "The road was quiet. Shina watched the tree line."
#     $ inventory_valid_item = "memory"
#     $ item_used = renpy.call_screen("inventory_screen")
#     $ inventory_valid_item = ""

#     if item_used == "memory":
#         n "The first time she'd stayed past the formal dismissal, no one had said anything."
#         n "The Priestess had simply walked back through the inner gate without comment."
#         n "Shina had assumed that meant she was permitted."
#         n "Four years later she still had not confirmed this."
#         n "She had also never left before being released."
#         n "These two facts had quietly organized themselves into something she didn't have a word for."
#         $ shina_honest_points += 1
#     # ── END TRIGGER B ─────────────────────────────────────

# # #######################################
# # MENU 2
# # #######################################
#     $ menu_owner = "shina"
#     menu:
#         "Shina catches herself."

#         "\"Don't read into that.\"":
#             sh "Don't read into that."
#             show makoto soft laugh
#             mk "I wasn't."
#             show shina nagata mad
#             sh "Good."
#             mk "Though now I am."
#             show shina embarrassed
#             sh "Evil Priestess."
#             show makoto laugh hide

#         "She keeps walking. Doesn't take it back.":
#             $ shina_honest_points += 1
#             n "She didn't walk it back."
#             n "Just kept moving, grip settling lower on the naginata the way it did when she'd said something true and decided to leave it standing."
#             show makoto neutral sad
#             n "Makoto looked at the road ahead."
#             n "Whatever was in her face, she kept it there."

#         "She pivots. \"Anyway. Right path's around this rock.\"":
#             sh "Anyway. Right path's around this rock. Watch your step."
#             show makoto knowing
#             mk "You mentioned that."
#             sh "Mentioning it again."
#             show makoto soft laugh
#             mk "Shina."
#             show shina nagata mad
#             sh "What."
#             mk "You are very easy to read."
#             show shina embarrassed
#             sh "I'm a closed book."
#             mk "You are a very open scroll."
#             show shina nagata mad
#             sh "I hate this road."

#     $ menu_owner = None
# # #######################################
# # END MENU 2
# # #######################################

#     window hide
#     pause 0.5

#     jump ch3_s3_snake

# # =========================================================
# # SCENE 3 — THE SNAKE
# # =========================================================
# label ch3_s3_snake:
#     show bg road_snake with dissolve
#     show shina resting nagata bored at stage_left
#     show makoto neutral at stage_right
#     window show dissolve_2

#     n "The road narrowed through a stand of old cedar, roots crossing the stones in ridges worn smooth by years of feet."
#     n "The light dropped here. The forest pressed close."

#     n "Shina stopped."
#     n "No warning. No word."
#     n "One hand up."

#     mk "Shina."
#     sh "Hold on."

#     $ duck(level=0.2, delay=0.3)
#     n "She stepped off the path into the brush."
#     n "Makoto waited."
#     n "She had learned to read the difference between Shina's stillness when there was nothing and Shina's stillness when there was something."
#     n "This was something."
#     $ unduck(level=0.3, delay=1.5)

#     n "A sound in the cedar, low and dry."
#     n "Then Shina's hand came out of the brush holding a snake — dark-banded, thick through the middle, occupied with a shrew that had chosen the wrong moment to be visible."

#     show makoto soft laugh
#     mk "..."
#     show shina nagata smug
#     sh "Yeah."

#     n "She carried it, unhurried, further into the brush on the uphill side of the road."
#     n "Set it down."
#     n "Came back."
#     n "Picked up the naginata she'd propped against the cedar."

#     show shina nagata smug
#     sh "Shrew gets to live another day."
#     show makoto neutral
#     mk "You could have walked us past it."
#     sh "Could've."
#     mk "Or made noise. It would have moved."
#     sh "Probably."
#     show makoto soft laugh
#     mk "So why—"
#     show shina nagata neutral
#     sh "I don't know."
#     sh "It wasn't doing anything worth dying for."

#     n "She settled the naginata back across her shoulders."

#     $ duck(level=0.15, delay=0.5)
#     n "Makoto watched her."
#     n "The way she'd moved into the brush — no announcement, no deliberation, just picked the thing up and carried it somewhere the problem resolved itself."
#     n "The shrew. The snake. Shina, apparently, had a position on who got to walk away from an afternoon."
#     n "She had not thought about it before moving."
#     n "That was the part."
#     $ unduck(level=0.3, delay=2.0)

#     $ shina_guard_points += 1

#     show makoto neutral sad
#     n "She said nothing about it."
#     n "Fell back into step."

#     show shina nagata neutral
#     sh "Right. Where were we."
#     show makoto soft laugh
#     mk "You were explaining your philosophy on road fauna."
#     show shina nagata smug
#     sh "I don't have a philosophy."

#     $ duck(level=0.15, delay=0.3)
#     mk "No."
#     mk "You just have instincts."
#     $ unduck(level=0.3, delay=1.5)

#     show shina nagata neutral
#     n "She said it the way she said things that were true and didn't need pressing."
#     n "Shina didn't answer."
#     n "The road leveled briefly, opening on a view of the ridge, bright with the last of the afternoon."
#     n "They walked."

#     window hide
#     pause 1.0
#     scene bg black with dissolve
#     stop music fadeout 1.5
#     stop ambience fadeout 2.0
#     pause 1.5

#     jump ch3_s4_arrival


# # =========================================================
# # SCENE 4 — ARRIVAL
# # =========================================================

# label ch3_s4_arrival:
#     scene bg temple_dusk_02 with slow_dissolve
#     play ambience forestamb fadein 1.5 volume 0.7
#     play music temple_theme fadein 2.0 volume 0.3
#     pause 2.0
#     window show dissolve_2

#     n "The upper shrine came into view as the light started going."
#     n "Stone lanterns already lit along the approach. Cedar smoke and cold rock."
#     n "The sound of a bell, deeper than the ones in the valley."

#     show makoto neutral at stage_right with dissolve
#     show shina nagata neutral at stage_left with dissolve

#     n "Makoto's attendants met them at the outer gate."
#     n "Greetings. Brief, formal. Makoto handled them the way she handled all of it, which was with the ease of someone who had long since stopped noticing how naturally the weight of this settled on her."
#     n "Shina stood to the side and said nothing."
#     n "Which was as close to formal as she got."

#     $ duck(level=0.2, delay=0.3)
#     n "The attendants led Makoto through the preparation. Robes confirmed, offerings laid, ritual items arranged."
#     n "Shina followed as far as the inner gate."
#     n "Then stopped."
#     n "This was where she always stopped."
#     n "The rite was Makoto's, and that threshold was hers."
#     $ unduck(level=0.3, delay=1.5)
    
#     show bg temple_dusk_02_door with dissolve
#     show makoto neutral
#     n "Makoto paused at the gate and turned back."

#     show makoto knowing
#     mk "The shrine has a kitchen. A garden with a decent view of the valley from the east wall."
#     show shina nagata neutral
#     sh "I know."
#     mk "The attendants can show you. There's no reason to stand out here all evening."

#     # ── INVENTORY TRIGGER C — DRIED PERSIMMON ─────────────
#     n "Shina looked at the gate."
#     $ inventory_valid_item = "trail_ration"
#     $ item_used = renpy.call_screen("inventory_screen")
#     $ inventory_valid_item = ""

#     if item_used == "trail_ration":
#         show shina relaxed at stage_left with dissolve
#         n "She reached into the travel pack. Pulled out a cloth-wrapped piece of dried persimmon."
#         n "Held it out toward Makoto without quite looking at her."
#         sh "Take this. You'll be in there two hours and you didn't eat at the waystation."
#         show makoto neutral sad at stage_right with dissolve
#         n "Makoto looked at the offered food."
#         n "Then at Shina, who was very carefully watching the cedar at the edge of the approach."
#         mk "..."
#         n "She took it."
#         n "Shina's hand returned to the naginata like nothing had happened."
#         $ shina_honest_points += 1
#         $ shina_guard_points += 1
#     # ── END TRIGGER C ─────────────────────────────────────

#     sh "I'm fine."
#     show makoto neutral
#     mk "You've been on the road since dawn."
#     sh "So have you."
#     mk "I'm about to sit down for two hours."
#     sh "Then someone should be outside when you come back out."

#     n "A pause."
#     n "Makoto looked at her — the steady, unhurried look she used when she was deciding whether to push."

#     show makoto soft laugh
#     mk "Shina."
#     mk "Go eat something. I'll be—"

#     show shina nagata neutral
#     n "Shina shifted her weight."
#     n "The easy answer was right there."
#     n "She let it pass."

#     $ duck(level=0.1, delay=0.4)
#     sh "Evil Priestess."
#     pause 1.0
#     sh "I'm staying."
#     $ unduck(level=0.2, delay=2.0)

#     n "She dropped onto the step beside the inner gate — the wrong step, the one no one had marked for any purpose — and set the naginata across her knees."

#     $ duck(level=0.1, delay=0.3)
#     n "She did not look up."
#     n "If her ears were warm, the collar of her haori covered it."
#     $ unduck(level=0.2, delay=2.0)

#     $ shina_honest_points += 1

#     show makoto neutral
#     pause 1.0

#     n "Makoto stood at the gate."
#     n "Then she turned toward the inner shrine."

#     $ duck(level=0.1, delay=0.4)
#     mk "I know."
#     $ unduck(level=0.2, delay=2.5)

#     n "Two words."
#     n "Facing the doors when she said them."

#     hide makoto with dissolve
#     pause 1.5

#     show shina nagata neutral at stage_left

#     $ duck(level=0.1, delay=0.3)
#     n "The gate closed."
#     n "Shina pulled her collar up against the evening chill and watched the lanterns come alive along the approach, one by one."
#     $ unduck(level=0.2, delay=3.0)

#     window hide
#     pause 1.0
#     hide shina with dissolve
#     scene bg black with slow_dissolve
#     stop music fadeout 2.0
#     stop ambience fadeout 2.5
#     pause 2.0

#     if shina_honest_points >= 3:
#         jump ch3_secret_coda
#     else:
#         jump credits


# # =========================================================
# # SECRET SCENE — THE BRACELET
# # =========================================================

# label ch3_secret_coda:
#     scene bg temple_interior with slow_walk_zoom
#     play music hazymoon fadein 2.5 volume 0.25
#     play ambience "audio/temple_tone.mp3" fadein 3.0 volume 0.2
#     window hide
#     pause 2.0
#     window show

#     n "The rite did not take long."
#     n "It never did, once the preparations were finished. The actual moment of it — the prayer, the offering, the formal words spoken to the dark — was quieter than most people imagined."

#     show makoto neutral at stage_center with dissolve
#     pause 1.0

#     n "Makoto sat alone in the inner room after the attendants withdrew."
#     n "The offering smoke still moved upward in a thin thread, and the room had settled into the particular stillness of a place that has held many things without repeating them."

#     $ duck(level=0.12, delay=0.5)
#     n "Her right hand moved to her left wrist."
#     n "Below the sleeve."
#     n "She pressed her thumb against the stone — smooth, river-worn, the weight of it always exactly the same."
#     n "She did not look at it."
#     n "She did not need to."
#     $ unduck(level=0.2, delay=3.0)

#     show makoto neutral sad
#     n "She was thinking about the step outside the gate."
#     n "The wrong step. The one no one had marked for any purpose."
#     n "Shina on it, collar up, watching the lanterns come on."

#     $ duck(level=0.1, delay=0.4)
#     n "Her thumb moved once across the stone."
#     n "Then stilled."
#     n "The incense finished its thread."
#     $ unduck(level=0.2, delay=3.5)

#     n "Outside, she knew, Shina was not going anywhere."
#     n "She had said so. And meant it."

#     hide makoto with slow_dissolve
#     window hide
#     stop music fadeout 3.0
#     stop ambience fadeout 3.0
#     pause 3.0
#     scene bg black with slow_dissolve
#     pause 2.0

#     jump credits
#     return
