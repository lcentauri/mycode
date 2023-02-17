#!/usr/bin/env python3

import os

horse= {
        1:{"q":"You're in a sewer, you ask why you're in a sewer? Shut up you just are. You have the choices ahead of you",
           "A. you can go right" or "a": 2,
           "B. you go left like a dumbass" or "b": 3,
           "C. OR SUPRISE 3rd option which would be just to lie down and die slowly." or "c": "last"},
        2:{"q":"How many legs do you walk on?",
           "two": "last",
           "four": 3},
        3:{"q":"Really?",
           "no": 4,
           "yes": 4},
        4:{"q":"Can you read and write?",
           "no": 5,
           "yes": "last"},
        5:{"q":"Liar, you're reading this.",
           "no": "last",
           "yes": "last"},
       }

os.system("clear")
question= 1

while question != "last":
    print(horse[question]["q"])
    for x in horse[question]:
        if x != "q":
           print(f" - {x}")
    answer= input("\n>").strip().lower()
    os.system("clear")
    if answer in horse[question]:
        question= horse[question][answer]
        if question == "last":
            print("YOU WON! CONGRATS! Look at you, you upredictable rebel you... I was lying by the way, I know your smooth brain probably didn't comprehend that. You absolutely lost...  Please spare us both and dont come back")
    else:
        print("That's not an acceptable answer.")
