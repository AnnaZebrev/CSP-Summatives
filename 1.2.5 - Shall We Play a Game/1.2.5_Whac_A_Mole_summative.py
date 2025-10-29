import turtle as trtl
import random
#import leaderboard

play = False

#Start Screen

#Ask if user wants to play

yes_turtle = trtl.Turtle(shape="turtle")
yes_turtle.turtlesize(4)
yes_turtle.teleport(-60,0)

no_turtle = trtl.Turtle(shape="turtle")
no_turtle.turtlesize(4)
no_turtle.teleport(60,0)


'''
start = trtl.textinput("Would you like to play?", "y/n?")
start = start.lower()
while start != "y" and start != "n":
    start = trtl.textinput("Please type y or n", "y/n?")
if start == "y":
    play = True #while loop for game play
if start == "n":
    trtl.hideturtle()
    trtl.write("Goodbye!")
'''

while play == True:

    #Ask user name
    player_name = trtl.textinput("Name", "Enter your name")

    while "," in player_name or len(player_name)==0:
        player_name = trtl.textinput("Name", "Please do not use a comma, Enter your name")

#Add background and turtle images

    #Main background


    #Create turtle image instead of shape

#Add randomization to turtle movement

    #Make list of specific locations based on background and then pick a random location from the list

#Timer
    #Add timer for whole game

    #Add timer to individual turtles **Optional**

#Score

    #Add/Subtract

    #Create leaderboard

    #Placement

    #Create medals to be earned for high enough scores **Optional**

#Ending/Restart

    #Create ending screen with leaderboard and score

    #Ask user if they want to play again

    #Restart loop or say goodbye

wn = trtl.Screen()
wn.mainloop()
