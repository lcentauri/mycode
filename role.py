#! /usr/bin/python3

user_name = input("Whats your name you dirty bum? \n>") 

print("you think your name is " + user_name + "? No its not its stupid, get up stupid")

print("Your in a sewer, you ask why you're in a sewer? Shut up you just are. You have two choices ahead of you, \n A. you can go right \n B. left \n C. OR SUPRISE 3rd option which would be just to lie down and die slowly.")

first_choice = input("What is your choice? \n>")

if first_choice.title().strip() == "A": 
    print("Of course you chose to go right you bafoon, anyways you continue on and see 3 tin cans. Now you have a proper choice. Which can of beans do you eat? \n A. The sparkley blue one? \n B. Its more of a tin than a can one? \n Or the one that obviously has a rat in it?")

if first_choice.title().strip() == "B":
    print("Good job!, super original. Im so proud, no no you cant turn back now. Only forward. Its fine I'm sure that was a ok choice.")

if first_choice.title().strip() == "C": 
    print("YOU WON! CONGRATS! Look at you, you upredictable rebel you... I was lying by the way, I know your smooth brain probably didt comprehend that. You absolutely lost...  Please spare us both and dont come back")
