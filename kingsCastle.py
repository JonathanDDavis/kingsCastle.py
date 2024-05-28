import time
import random
import sys

#def dlayPrint(x):
#    for i in x:
#            sys.stdout.write(i)
#            sys.stdout.flush
#            time.sleep(0.25)
#print("What is your name")
#name = input()
#print("It is nice to meet you " + name)

#ready = False
#while ready == False:
#	print("Are you ready to play?")
#	choice = input()
#	if choice.lower() == "yes":
#		print("Okay we will start")
#		ready = True
#	elif choice.lower() == "no":
#		print("Just tell me when you are ready")
#		ready == False
#	else:
#		print("That is not a vaild answer. Please type yes or no")
print("You have been summoning you to the castle. When you get to the castle the king tells you that you are goign to play a game of hide and see with him. Right after he tells you that you seek smoke go around him and he is gone. You notce there are 6 ways to go. You can go to the east, west, north, south, upstairs, and downstairs.")
directionText = ["You walk to the east and you see" , "You walk to the west and you see" , "You walk to the north and you see" , "You walk to the south and you see" , "You walk upstairs and you see" , "You walk downstairs and you see"]
areas = [" a kitchen filled with the kings personal chefs." , " " , " the kings thorne room. The only thing in the room is the throne and a large red carpet on the floor." , " the area where you came in at. It is a large garden with lawn hedges made into different animal and creatures." + " " + " "]


locations = ["north", "south", "east", "west", "upstairs", "downstairs"]

randomLocation = random.choice (locations)

kingsLocation = randomLocation.lower()

print(kingsLocation)

validInput = False
while validInput == False:
	choice = input("Please pick a location: east, west, north, south, upstairs, and downstairs ").lower()
	if choice == "north":
		print( directionText[2] + areas[2])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	elif choice == "south":
		print( directionText[3] + areas[3])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	elif choice == "east":
		print( directionText[0] + areas[0])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	elif choice == "west":
		print( directionText[1] + areas[1])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	elif choice == "upstairs":
		print( directionText[4] + areas[4])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	elif choice == "downstairs":
		print( directionText[5] + areas[5])
		if choice == kingsLocation:
			print("You found the King!")
		validInput = True
	else:
			print("Invalid Input. Please type north, south, east, west, upstairs, or downstairs")
print("The King gave you the castle because you found him.")
