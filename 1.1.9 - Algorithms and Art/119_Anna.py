import turtle as trtl

#create a heart shaped turtle
trtl.addshape("heart", ((0,5), (2,7), (3,8), (5,9), (6,9), (7,9), (8,8.5), (9,8), (10,6.5), (11,4), (10.5,2), (9.5,0), (0, -11), (-9.5,0), (-10.5,2), (-11,4), (-10,6.5), (-9,8), (-8,8.5), (-7,9), (-6,9), (-5,9), (-3,8), (-2,7)))

#welcome users and introduce them to the activity
print("Welcome user! Let's draw a picture!")

answer = "y"

#create a drawing loop
while answer=="y":


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

    #draw a ring of the picked shape
    trtl.penup()
    trtl.goto(10,85)
    trtl.shape(new_shape)
    trtl.pendown()
    for t in range(18):
        trtl.right(20)
        trtl.forward(30)
        trtl.stamp()




    #ask if the user wants to draw again
    answer = trtl.textinput("Would you like to draw again?", "y/n?")

    #clear drawing from screen
    trtl.clearscreen()

#hide turtle and leave a goodbye message
trtl.hideturtle()
trtl.write("Thanks for drawing!")


#keep screen after program runs
wn = trtl.Screen()
wn.mainloop()
