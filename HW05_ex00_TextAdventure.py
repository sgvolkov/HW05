#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
from sys import argv

# Body

def infinite_stairway_room(name, count=0):
    print name + " walks through the door to see a dimly lit hallway."
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    next = raw_input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print name + ' takes the stairs'
        if (count > 0):
            print "but " + name + " is not happy about it"
        infinite_stairway_room(name, count + 1)
    # option 2 == "don't take stairs"
    if next == "don't take the stairs":
        pass
    else:
        gold_room(name)


def gold_room(name):
    print "This room is full of gold.  How much does " + name +" take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, " + name + " isn't greedy, " + name + " wins!"
        exit(0)
    else:
        dead(name + ", greedy bastard!")


def bear_room(name):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is " + name + " going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at " + name + " then slaps " + name + "'s face off.")
        elif next == "taunt" and not bear_moved:
            print "The bear has moved from the door. " + name + " can go through it now."
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews " + name + "'s leg off.")
        elif next == "open" or "door" and bear_moved:
            back_room(name)
        else:
            print "I got no idea what that means."

def back_room(name):
    print name + " enters the BACK ROOM, filled with awkward programmers."
    print "This room is where programmers enter an infinite programming loop"
    print name + " states her name, but no one cares, their eyes transfixed."
    print name + ": submit to your programming prison!"
    exit()


def cthulhu_room(name):
    print "Here " + name + " sees the great evil Cthulhu."
    print "He, it, whatever stares at " + name + " and " + name + " goes insane."
    print "Does " + name + " flee for her life or eat her head?"

    next = raw_input("> ")

    if "flee" in next:
        infinite_stairway_room(name)
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(name)


def dead(why):
    print why, "Good job!"
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game
    name = argv[1]
    print name + " is in a dark room."
    print "There is a door to her right and left."
    print "Which one does " + name + " take?"

    next = raw_input("> ")

    if next == "left":
        bear_room(name)
    elif next == "right":
        cthulhu_room(name)
    else:
        dead(name + " stumbles around the room until " + name + " starves.")

if __name__ == '__main__':
    main()
