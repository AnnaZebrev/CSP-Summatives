import turtle as trtl
import random
#import leaderboard

font_setup = ("Arial",26,"normal")
   

play = False
wn = trtl.Screen()

#Start Screen

#Tell the user how to start
trtl.hideturtle()
trtl.teleport(-45,45)
trtl.write("Click the turtle to play!" , font=font_setup)

play_turtle = trtl.Turtle(shape="turtle")
play_turtle.color("VioletRed3")
play_turtle.turtlesize(4)


def start_click(x,y):
    trtl.clearscreen()
    global play
    #Ask user name
    player_name = trtl.textinput("Name", "Enter your name")
    play = True

    while "," in player_name or len(player_name)==0:
        player_name = trtl.textinput("Name", "Please do not use a comma, Enter your name")

#create leaderboard
leaderboard_file_name = "125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []

#start game
play_turtle.onclick(start_click)

while play == True:
#Add background and turtle images

#screen setup
    screen_width = 400 #set width of screen
    screen_height = 400 #set height of screen

        #Create turtle image instead of shape
    mole_image = "mole.gif"
    wn.addshape(mole_image)
    mole = trtl.Turtle(shape = mole_image)

    #Main background
    wn.bgpic("mole_background.gif")

#Add randomization to turtle movement

    #Make list of specific locations based on background and then pick a random location from the list

#Timer
    #Add timer for whole game

    #Add timer to individual turtles **Optional**

#Score

    #Add/Subtract

    #Update leaderboard

    #Placement

    #Create medals to be earned for high enough scores **Optional**

#Ending/Restart

    #Create ending screen with leaderboard and score

    #Ask user if they want to play again

    #Restart loop or say goodbye

wn.mainloop()
