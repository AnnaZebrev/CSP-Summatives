import turtle as trtl

#create a heart shaped turtle
trtl.addshape("heart", ((0,5), (2,7), (3,8), (5,9), (6,9), (7,9), (8,8.5), (9,8), (10,6.5), (11,4), (10.5,2), (9.5,0), (0, -11), (-9.5,0), (-10.5,2), (-11,4), (-10,6.5), (-9,8), (-8,8.5), (-7,9), (-6,9), (-5,9), (-3,8), (-2,7)))

#welcome users and introduce them to the activity
print("Welcome user! Let's draw a picture!")

answer = "y"

#create a drawing loop
while answer=="y":
     

    #create background
    trtl.teleport(-185,-10)

    for line in range(36):
        trtl.speed(15)
        trtl.color("CornflowerBlue")
        trtl.forward(375)
        trtl.right(190)

    trtl.teleport(-248,-15)

    for line in range(36):
        trtl.color("DarkSeaGreen2")
        trtl.forward(500)
        trtl.right(190)

    trtl.teleport(-397, -30)

    for line in range(36):
        trtl.color("CadetBlue1")
        trtl.forward(800)
        trtl.right(190)

        
    
   #pick a heart color
   
    heart_color = trtl.textinput("Choose a color for a heart", "color:")

    #create heart turtle
    heart = trtl.Turtle(shape="heart")

    #draw a heart in the center of the screen
    heart.color(heart_color)
    heart.setheading(90)
    heart.turtlesize(3)

    #pick a shape to go around the heart
    new_shape = trtl.textinput("Pick a shape", "circle or turtle?")

    #pick color for first ring
    color1 = trtl.textinput("Pick a color", "color:")

    #pick color of second ring
    color2 = trtl.textinput("Pick another color", "color:")

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
