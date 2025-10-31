import turtle as trtl
import random as rand
#import leaderboard as lb

font_setup = ("Arial",40,"normal")
score = 0

wn = trtl.Screen()

#Start Screen

#Tell the user how to start
trtl.hideturtle()
trtl.teleport(-65,45)
trtl.write("Click the turtle to play!" , font=font_setup)

play_turtle = trtl.Turtle(shape="turtle")
play_turtle.color("VioletRed3")
play_turtle.turtlesize(4)


def start_click(x,y):
    trtl.clearscreen()
    global play
    #Ask user name
    player_name = trtl.textinput("Name", "Enter your name")
    

    while "," in player_name or len(player_name)==0:
        player_name = trtl.textinput("Name", "Please do not use a comma, Enter your name")
    start()
    #create score
    score_writer = trtl.Turtle()
    score_writer.hideturtle()
    score_writer.teleport(-18,165)
    score_writer.write(score, font=font_setup)

#create leaderboard
leaderboard_file_name = "125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []

#start game
play_turtle.onclick(start_click)


def start():
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
    mole_xpositions = [0, -210, 210, 0, -210, 210]
    mole_ypositions = [100, -60, -60, -240, 270, 270]
    #mole.teleport(0,100)
    #mole.teleport(-210,-60)
    #mole.teleport(210,-60)
    #mole.teleport(0,-240)
    #mole.teleport(-200, 270)
    #mole.teleport(210, 270)
    xcor = rand.choice(mole_xpositions)
    ycor = mole_ypositions(mole_xpositions[xcor])
    mole.teleport(xcor, ycor)


#Timer
    #Add timer for whole game

    #Add timer to individual turtles **Optional**

#Score

    #Add/Subtract
def change_score():
    score_writer.clear()
    global score
    score += 1
    score_writer.pendown()
    score_writer.write(score, font=font_setup)
'''
#Update leaderboard
    # get the names and scores from the leaderboard file
leader_names_list = lb.get_names(leaderboard_file_name)
leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)
'''
    #Placement

    #Create medals to be earned for high enough scores **Optional**

#Ending/Restart

    #Create ending screen with leaderboard and score

    #Ask user if they want to play again

    #Restart loop or say goodbye

wn.mainloop()
