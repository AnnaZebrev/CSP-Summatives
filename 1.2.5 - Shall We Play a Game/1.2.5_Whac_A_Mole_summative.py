import turtle as trtl
import random as rand
import leaderboard as lb

font_setup = ("Arial",40,"normal")
score = 0
timer = 15
counter_interval = 1000
timer_up = False

wn = trtl.Screen()

#Start Screen

#Tell the user how to start
trtl.hideturtle()
trtl.teleport(-65,45)
trtl.write("Click the turtle to play!" , font=font_setup)

#initialize turtles
play_turtle = trtl.Turtle(shape="turtle")
play_turtle.color("VioletRed3")
play_turtle.turtlesize(4)

#create score
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.teleport(20,165)

#create counter
counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-230,165)


def start_click(x,y):
    trtl.clearscreen()
    global play
    global player_name
    #Ask user name
    player_name = trtl.textinput("Name", "Enter your name")

    while "," in player_name or len(player_name)==0:
        player_name = trtl.textinput("Name", "Please do not use a comma, Enter your name")
    start()
    score_writer.write("Score: " +str(score), font=font_setup)

#create leaderboard
leaderboard_file_name = "a125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []

#start game
play_turtle.onclick(start_click)

def start():
#Add background and turtle images

#screen setup
    wn.ontimer(countdown, counter_interval)
    global screen_width
    global screen_height
    global mole
    screen_width = 400 #set width of screen
    screen_height = 400 #set height of screen

    
    #Create turtle image instead of shape
    mole_image = "mole.gif"
    wn.addshape(mole_image)
    mole = trtl.Turtle(shape = mole_image)
    move_mole()
    mole.onclick(mole_clicked)

    #Main background
    wn.bgpic("mole_background.gif")

#Add randomization to turtle movement

#Make list of specific locations based on background and then pick a random location from the list
def move_mole():
    global mole
    mole_xpositions = [1, -211, 211, 0, -210, 210]
    mole_ypositions = [100, -60, -60, -240, 270, 270]
    xcor = rand.choice(mole_xpositions)
    ycor = mole_ypositions[mole_xpositions.index(xcor)]
    mole.hideturtle()
    mole.teleport(xcor, ycor)
    mole.showturtle()

#start countdown
def countdown():
  global counter
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up!", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

#chnage score and move mole when clicked
def mole_clicked(x,y):
    change_score()
    move_mole()

#Score
    #Add/Subtract
def change_score():
    global score_writer
    score_writer.clear()
    global score
    score += 1
    score_writer.pendown()
    score_writer.write("Score: " +str(score), font=font_setup)

#Update leaderboard
def manage_leaderboard():
    global score
    global mole
    global player_name
    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
    trtl.clearscreen()
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, mole, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, mole, score)


wn.mainloop()
