import pygame
from dialogue_box import create_dialogue_box
from popup import create_popup


def conversation(display, playerpos, area, text, by_letter, on=True, quick=False):
    if [playerpos["x"], playerpos["y"]] in area:
        if on:
            if not quick:
                by_letter = create_dialogue_box(display, text, by_letter)
            else:
                create_dialogue_box(display, text)
        else:
            create_popup(display, "Press R to speak")
    else:
        on = False
        quick = False
        by_letter = [0, 0]
    return on, quick, by_letter