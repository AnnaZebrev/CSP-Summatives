#import turtle module
import turtle as trtl

#import random module
import random

#create a heart shaped turtle
trtl.addshape("heart", ((0,5), (2,7), (3,8), (5,9), (6,9), (7,9), (8,8.5), (9,8), (10,6.5), (11,4), (10.5,2), (9.5,0), (0, -11), (-9.5,0), (-10.5,2), (-11,4), (-10,6.5), (-9,8), (-8,8.5), (-7,9), (-6,9), (-5,9), (-3,8), (-2,7)))

#welcome users and introduce them to the activity
trtl.hideturtle()
trtl.write("Welcome user! Let's draw a picture!", font=("Arial", 20, "normal"))

#create a list of colors for the background
colors = ["CornflowerBlue", "DarkSeaGreen2", "CadetBlue1", "Aquamarine", "DarkSeaGreen1", "CadetBlue2", "MediumAquamarine", "LightSteelBlue", "GreenYellow", "LightBlue", "LightBlue1", "LightCyan", "LightCyan3", "LightGreen", "Lavender", "LavenderBlush", "Thistle", "Plum"]

#create looping variable for main loop
draw = trtl.textinput("Begin?", "y/n?")
draw = draw.lower()
if draw == "y":
    answer = "y"
else:
    answer = "n"

#clear welcome screen and show turtle
trtl.clearscreen()
trtl.showturtle()

#create a drawing loop
while answer=="y":
    #create background
    trtl.teleport(-185,-10)

    for line in range(36):
        trtl.speed(15)
        trtl.color(random.choice(colors))
        trtl.forward(375)
        trtl.right(190)

    trtl.teleport(-248,-15)

    for line in range(36):
        trtl.color(random.choice(colors))
        trtl.forward(500)
        trtl.right(190)

    trtl.teleport(-397, -30)

    for line in range(36):
        trtl.color(random.choice(colors))
        trtl.forward(800)
        trtl.right(190)

   #pick a heart color
    is_error = False
    while not is_error:
        heart_color = trtl.textinput("Choose a color for a heart", "color:")
        try:
            trtl.color(heart_color)
            is_error = True
        except trtl.TurtleGraphicsError:
            is_error = False

    #create heart turtle
    heart = trtl.Turtle(shape="heart")

    #draw a heart in the center of the screen
    heart.color(heart_color)
    heart.setheading(90)
    heart.turtlesize(3)

    #pick a shape to go around the heart
    is_error = False
    while not is_error:
        new_shape = trtl.textinput("Pick a shape", "circle or turtle?")
        try:
            trtl.shape(new_shape)
            is_error = True
        except trtl.TurtleGraphicsError:
            is_error = False

    #pick color for first ring
    is_error = False
    while not is_error:
        color1 = trtl.textinput("Pick a color", "color 1:")
        try:
            trtl.color(color1)
            is_error = True
        except trtl.TurtleGraphicsError:
            is_error = False

    #pick color of second ring
    is_error = False
    while not is_error:
        color2 = trtl.textinput("Pick another color", "color 2:")
        try:
            trtl.color(color2)
            is_error = True
        except trtl.TurtleGraphicsError:
            is_error = False

    #pick color of third ring
    is_error = False
    while not is_error:
        color3 = trtl.textinput("Pick final color", "color 3:")
        try:
            trtl.color(color3)
            is_error = True
        except trtl.TurtleGraphicsError:
            is_error = False

    #draw ring 1 of the picked shape
    trtl.color(color1)
    trtl.penup()
    trtl.goto(15,60)
    trtl.shape(new_shape)
    trtl.pendown()
    for t in range(12):
        trtl.right(30)
        trtl.penup()
        trtl.forward(30)
        trtl.pendown()
        trtl.stamp()

    #draw ring 2 of picked shape
    trtl.color(color2)
    trtl.penup()
    trtl.goto(15,90)
    trtl.shape(new_shape)
    trtl.pendown()
    for t in range(18):
        trtl.right(20)
        trtl.penup()
        trtl.forward(30)
        trtl.pendown()
        trtl.stamp()

    #draw ring 3 of picked shape
    trtl.color(color3)
    trtl.penup()
    trtl.goto(20, 120)
    trtl.shape(new_shape)
    trtl.pendown()
    for t in range(18):
        trtl.right(20)
        trtl.penup()
        trtl.forward(40)
        trtl.pendown()
        trtl.stamp()

    #ask if the user wants to draw again
    answer = trtl.textinput("Would you like to draw again?", "y/n?")

    #clear drawing from screen
    trtl.clearscreen()

#hide turtle and leave a goodbye message
trtl.hideturtle()
trtl.write("Thanks for drawing!", font=("Arial", 24, "normal"))

#keep screen after program runs
wn = trtl.Screen()
wn.mainloop()
