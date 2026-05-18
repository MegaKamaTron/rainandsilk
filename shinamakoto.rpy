# =========================================================
# Chapter 3: The Road Knows Her Name
# Shina & Makoto — Pilgrimage Day
# =========================================================
#
# NOTE: Add the following to 02_characters.rpy before use:
#
# define sh = Character(
#     "Shina",
#     color="#B5562A",
#     who_color="#B5562A",
#     ctc="ctc_icon",
#     ctc_pause="ctc_icon",
#     ctc_timedpause="ctc_icon",
#     ctc_position="fixed",
# )
#
# define mk = Character(
#     "Makoto",
#     color="#8B6A9B",
#     who_color="#8B6A9B",
#     ctc="ctc_icon",
#     ctc_pause="ctc_icon",
#     ctc_timedpause="ctc_icon",
#     ctc_position="fixed",
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

    op "Four years on the same roads teaches you things no one thinks to mention."
    op "Which stone she steps around without looking. Which bell she waits for before she moves."
    op "The way she pauses at a threshold — not hesitation. Something closer to courtesy."

    $ duck(level=0.35, delay=0.4)
    op "Shina had not catalogued any of this deliberately."
    op "She had simply been paying attention."
    $ unduck(level=0.55, delay=1.5)

    op "The mountain road to the high shrine wound through cedar and stone the same way it always had."
    op "She had walked it four times now. Maybe five."
    op "Each time, the Priestess moved through it, it was as if she had forged the landscape itself."
    op "Each time, Shina walked two steps ahead."
    op "Not because she was told to--"
    op "--but simply because she chose to."

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

    n "Morning at the mountain shrine arrived in layers — birdsong before light, then the slow bleed of grey into amber through the paper screens."

    n "Makoto was already at her writing desk when Shina appeared in the doorframe."
    n "Despite both of her sandals being untied, she still thought it was a good idea to carry two cups, balanced in one hand. "

    show shina tea at st_right 
    with dissolve
    n "She had not knocked."
    n "She never knocked anymore."

    sh "Tea's going cold."
    show makoto neutral at st_left 
    with dissolve
    mk "Then you should have brought it sooner."
    sh "Yeah, yeah."

    n "She set one cup beside the desk without being asked, then dropped onto the low step at the room's edge — the one the junior attendants used — and stretched her legs out in front of her."

    show shina relaxed at st_right
    n "Three attendants had told her, at various points over four years, that the step was not for her."
    n "She remained unaware of this."

    show makoto mischevious at st_left
    mk "The step again."
    show shina shrug closed at st_right
    sh "It's a good step."
    mk "There are four designated positions for a Shadow during morning correspondence."
    show shina relaxed at st_right
    sh "Sure."
    show makoto neutral
    mk "That step is not one of them."
    show shina shrug closed at st_right
    sh "Shame."
    hide shina with dissolve
    hide makoto with dissolve
    n "The priestess hid another smile behind her ceramic cup and sipped her tea."

    pause 0.5
    n "The morning bell was not far off."
    n "One of them was going to have to say it."
    n "Between the two of them, it was usually Shina."

# #######################################
# MENU 1
# #######################################
    $ menu_owner = "shina"
    menu:
        "\"Oi. Sun's up. You coming or what?\"":
            show shina casual at st_right
            with dissolve
            sh "Oi. Sun's up. You coming or what?"
            n "She said it from the step rather than the door, which was not the correct protocol for a Shadow in a formal context."
            n "Makoto set her brush down."
            show makoto_amused
            mk "I have been ready since before you arrived."
            show shina_annoyed
            sh "Then why are we still sitting here."
            mk "I was waiting to see how long it would take you to ask."
            n "Shina looked at her."
            n "Makoto's expression gave nothing back."
            show shina_neutral
            sh "Evil Priestess."
            show makoto_laughing_restrained

        "She just stands. Already holding the travel pack.":
            $ shina_honest_points += 1
            show shina casual at st_right
            with dissolve
            n "She didn't say anything."
            n "Just unfolded herself from the step, finished the last of the tea, and appeared in the edge of Makoto's reading light with the travel pack already over one shoulder."
            n "Makoto read one more line of the letter."
            show makoto_amused
            mk "You could simply say when you're ready."
            show shina_smug
            sh "This is faster."
            mk "It is also vaguely threatening."
            sh "Bonus."
            show makoto_laughing_restrained

        "\"The road won't walk itself, evil Priestess.\"":
            show shina casual at st_right
            with dissolve
            $ shina_honest_points += 1
            sh "The road won't walk itself, evil Priestess."
            n "Makoto set her brush down with the deliberate care of someone deciding not to laugh."
            show makoto amused
            mk "That title."
            show shina smug
            sh "Fits."
            mk "It grows on me."
            sh "Don't get used to it."
            show makoto laughing restrained
            mk "Too late."
            show shina embarrassed

    $ menu_owner = None
# #######################################
# END MENU 1
# #######################################

    hide shina_neutral with dissolve
    hide makoto_neutral with dissolve
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

    n "The road climbed in long, unhurried switchbacks through cedar and pine."
    n "The air carried the cold of last night's rain and the mountain pressed close on the uphill side."

    show makoto_neutral at stage_right with dissolve
    show shina_weapon_ready at stage_left with dissolve

    n "Makoto moved through it at the pace of someone who had done this many times — composed, unhurried, her shrine robes pale against the green."

    $ duck(level=0.3, delay=0.3)
    n "Shina walked two steps ahead."
    n "Not three. Two."
    n "Close enough to hear a footstep change."
    $ unduck(level=0.3, delay=1.5)

    show shina_neutral
    sh "Fork up ahead. Left path is faster. Stones are bad since the rain."
    show makoto_neutral
    mk "And the right?"
    sh "Longer. Better footing."
    show makoto_amused
    mk "You checked this morning."
    show shina_neutral
    sh "I check every time."

    n "She said it without particular weight."
    n "As if it were simply the most practical thing in the world."

    mk "Right path, then."
    sh "Right path."

    n "They walked."
    n "A pilgrim group passed going the other direction, bowing low when they recognized Makoto's robes."
    n "Shina's eyes tracked them around the bend."

    show makoto_amused
    mk "They were pilgrims, Shina."
    show shina_neutral
    sh "Probably."
    mk "Certainly."
    sh "Sure."

    show makoto_playful_formal
    mk "You do this every time someone bows."
    sh "I do it every time someone comes close."

    n "A beat."

    show shina_scratch_head
    sh "That came out more serious than I meant it."
    show makoto_amused
    mk "Did it."
    show shina_annoyed
    sh "Don't."
    n "Makoto looked ahead at the road."
    n "Which was worse."

    $ duck(level=0.25, delay=0.4)
    n "The path curved around a shelf of old rock, the valley opening wide and low below them on the left."
    n "Shina shifted half a step toward the drop side."
    n "Not a decision. Just what her feet did."
    $ unduck(level=0.3, delay=1.5)

    show makoto_neutral
    mk "You know, the court appoints Shadows specifically so a Priestess doesn't have to worry about the road."
    show shina_smug
    sh "Mm."
    mk "Experienced ones. Formal records. Institutional backing."
    sh "Sounds thorough."
    show makoto_playful_formal
    mk "You might take the afternoon off sometime."
    show shina_neutral
    sh "I'm fine here."
    show makoto_amused
    mk "I know you are."
    mk "I'm suggesting you might also be fine somewhere else. Occasionally."
    show shina_scratch_head
    sh "Yeah, not really a somewhere-else person."

    n "She said it the way she said things she meant."
    n "Plain. No room around it."

    show shina_neutral
    sh "For what it's worth. You could've gotten someone court-appointed."
    sh "Official record, letters of endorsement, the whole thing."
    sh "Didn't end up that way."
    show makoto_neutral
    mk "No."
    mk "It didn't."
    show shina_neutral
    sh "Just saying."

    $ duck(level=0.2, delay=0.4)
    n "She was looking at the tree line when she said it."
    n "The way she looked at things she was pretending not to think about."
    $ unduck(level=0.3, delay=1.5)

    show makoto_amused
    mk "I am not aware of having complained."
    show shina_neutral
    sh "I know."
    sh "Still."

    n "She left it there."
    n "Makoto let it stand."

    pause 0.5

    show shina_neutral
    sh "Ronin thing, I think."
    sh "You move until you find the thing worth stopping for."
    sh "Then you stop."

    n "She said it like it was road-logic."
    n "Practical habit. The kind of sentence that closes before anyone can look at it too long."

# #######################################
# MENU 2
# #######################################
    $ menu_owner = "shina"
    menu:
        "Shina catches herself."

        "\"Don't read into that.\"":
            sh "Don't read into that."
            show makoto_amused
            mk "I wasn't."
            show shina_annoyed
            sh "Good."
            mk "Though now I am."
            show shina_embarrassed
            sh "Evil Priestess."
            show makoto_laughing_restrained

        "She keeps walking. Doesn't take it back.":
            $ shina_honest_points += 1
            n "She didn't walk it back."
            n "Just kept moving, grip settling lower on the naginata the way it did when she'd said something true and decided to leave it standing."
            show makoto_flustered_hidden
            n "Makoto looked at the road ahead."
            n "Whatever was in her face, she kept it there."

        "She pivots. \"Anyway. Right path's around this rock.\"":
            sh "Anyway. Right path's around this rock. Watch your step."
            show makoto_playful_formal
            mk "You mentioned that."
            sh "Mentioning it again."
            show makoto_amused
            mk "Shina."
            show shina_annoyed
            sh "What."
            mk "You are very easy to read."
            show shina_embarrassed
            sh "I'm a closed book."
            mk "You are a very open scroll."
            show shina_annoyed
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

    show shina_weapon_ready at stage_left
    show makoto_neutral at stage_right
    window show dissolve_2

    n "The road narrowed through a stand of old cedar, roots crossing the stones in ridges worn smooth by years of feet."
    n "The light dropped here. The forest pressed close."

    n "Shina stopped."
    n "No warning. No word."
    n "One hand up."

    mk "Shina."
    sh "Hold on."

    $ duck(level=0.2, delay=0.3)
    n "She stepped off the path into the brush."
    n "Makoto waited."
    n "She had learned to read the difference between Shina's stillness when there was nothing and Shina's stillness when there was something."
    n "This was something."
    $ unduck(level=0.3, delay=1.5)

    n "A sound in the cedar, low and dry."
    n "Then Shina's hand came out of the brush holding a snake — dark-banded, thick through the middle, occupied with a shrew that had chosen the wrong moment to be visible."

    show makoto_amused
    mk "..."
    show shina_smug
    sh "Yeah."

    n "She carried it, unhurried, further into the brush on the uphill side of the road."
    n "Set it down."
    n "Came back."
    n "Picked up the naginata she'd propped against the cedar."

    show shina_smug
    sh "Shrew gets to live another day."
    show makoto_neutral
    mk "You could have walked us past it."
    sh "Could've."
    mk "Or made noise. It would have moved."
    sh "Probably."
    show makoto_amused
    mk "So why—"
    show shina_neutral
    sh "I don't know."
    sh "It wasn't doing anything worth dying for."

    n "She settled the naginata back across her shoulders."

    $ duck(level=0.15, delay=0.5)
    n "Makoto watched her."
    n "The way she'd moved into the brush — no announcement, no deliberation, just picked the thing up and carried it somewhere the problem resolved itself."
    n "The shrew. The snake. Shina, apparently, had a position on who got to walk away from an afternoon."
    n "She had not thought about it before moving."
    n "That was the part."
    $ unduck(level=0.3, delay=2.0)

    $ shina_guard_points += 1

    show makoto_flustered_hidden
    n "She said nothing about it."
    n "Fell back into step."

    show shina_neutral
    sh "Right. Where were we."
    show makoto_amused
    mk "You were explaining your philosophy on road fauna."
    show shina_smug
    sh "I don't have a philosophy."

    $ duck(level=0.15, delay=0.3)
    mk "No."
    mk "You just have instincts."
    $ unduck(level=0.3, delay=1.5)

    show shina_neutral
    n "She said it the way she said things that were true and didn't need pressing."
    n "Shina didn't answer."
    n "The road leveled briefly, opening on a view of the ridge, bright with the last of the afternoon."
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
    scene bg temple_dusk with slow_dissolve
    play ambience forestamb fadein 1.5 volume 0.7
    play music temple_theme fadein 2.0 volume 0.3
    pause 2.0
    window show dissolve_2

    n "The upper shrine came into view as the light started going."
    n "Stone lanterns already lit along the approach. Cedar smoke and cold rock."
    n "The sound of a bell, deeper than the ones in the valley."

    show makoto_neutral at stage_right with dissolve
    show shina_neutral at stage_left with dissolve

    n "Makoto's attendants met them at the outer gate."
    n "Greetings. Brief, formal. Makoto handled them the way she handled all of it, which was with the ease of someone who had long since stopped noticing how naturally the weight of this settled on her."
    n "Shina stood to the side and said nothing."
    n "Which was as close to formal as she got."

    $ duck(level=0.2, delay=0.3)
    n "The attendants led Makoto through the preparation. Robes confirmed, offerings laid, ritual items arranged."
    n "Shina followed as far as the inner gate."
    n "Then stopped."
    n "This was where she always stopped."
    n "The rite was Makoto's, and that threshold was hers."
    $ unduck(level=0.3, delay=1.5)

    show makoto_neutral
    n "Makoto paused at the gate and turned back."

    show makoto_playful_formal
    mk "The shrine has a kitchen. A garden with a decent view of the valley from the east wall."
    show shina_neutral
    sh "I know."
    mk "The attendants can show you. There's no reason to stand out here all evening."
    sh "I'm fine."
    show makoto_neutral
    mk "You've been on the road since dawn."
    sh "So have you."
    mk "I'm about to sit down for two hours."
    sh "Then someone should be outside when you come back out."

    n "A pause."
    n "Makoto looked at her — the steady, unhurried look she used when she was deciding whether to push."

    show makoto_amused
    mk "Shina."
    mk "Go eat something. I'll be—"

    show shina_neutral
    n "Shina shifted her weight."
    n "The easy answer was right there."
    n "She let it pass."

    $ duck(level=0.1, delay=0.4)
    sh "Evil Priestess."
    pause 1.0
    sh "I'm staying."
    $ unduck(level=0.2, delay=2.0)

    n "She dropped onto the step beside the inner gate — the wrong step, the one no one had marked for any purpose — and set the naginata across her knees."

    $ duck(level=0.1, delay=0.3)
    n "She did not look up."
    n "If her ears were warm, the collar of her haori covered it."
    $ unduck(level=0.2, delay=2.0)

    $ shina_honest_points += 1

    show makoto_neutral
    pause 1.0

    n "Makoto stood at the gate."
    n "Then she turned toward the inner shrine."

    $ duck(level=0.1, delay=0.4)
    mk "I know."
    $ unduck(level=0.2, delay=2.5)

    n "Two words."
    n "Facing the doors when she said them."

    hide makoto_neutral with dissolve
    pause 1.5

    show shina_neutral at stage_left

    $ duck(level=0.1, delay=0.3)
    n "The gate closed."
    n "Shina pulled her collar up against the evening chill and watched the lanterns come alive along the approach, one by one."
    $ unduck(level=0.2, delay=3.0)

    window hide
    pause 1.0
    hide shina_neutral with dissolve
    scene bg black with slow_dissolve
    stop music fadeout 2.0
    stop ambience fadeout 2.5
    pause 2.0

    if shina_honest_points >= 2:
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

    n "The rite did not take long."
    n "It never did, once the preparations were finished. The actual moment of it — the prayer, the offering, the formal words spoken to the dark — was quieter than most people imagined."

    show makoto_neutral at stage_center with dissolve
    pause 1.0

    n "Makoto sat alone in the inner room after the attendants withdrew."
    n "The offering smoke still moved upward in a thin thread, and the room had settled into the particular stillness of a place that has held many things without repeating them."

    $ duck(level=0.12, delay=0.5)
    n "Her right hand moved to her left wrist."
    n "Below the sleeve."
    n "She pressed her thumb against the stone — smooth, river-worn, the weight of it always exactly the same."
    n "She did not look at it."
    n "She did not need to."
    $ unduck(level=0.2, delay=3.0)

    show makoto_flustered_hidden
    n "She was thinking about the step outside the gate."
    n "The wrong step. The one no one had marked for any purpose."
    n "Shina on it, collar up, watching the lanterns come on."

    $ duck(level=0.1, delay=0.4)
    n "Her thumb moved once across the stone."
    n "Then stilled."
    n "The incense finished its thread."
    $ unduck(level=0.2, delay=3.5)

    n "Outside, she knew, Shina was not going anywhere."
    n "She had said so."
    n "In the plainest sentence she had managed all day, she had simply said so."

    hide makoto_flustered_hidden with slow_dissolve
    window hide
    stop music fadeout 3.0
    stop ambience fadeout 3.0
    pause 3.0
    scene bg black with slow_dissolve
    pause 2.0

    jump credits
    return
