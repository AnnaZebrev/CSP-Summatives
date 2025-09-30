import turtle as trtl

#create a heart shaped turtle
trtl.addshape("heart", ((0,5), (2,7), (3,8), (5,9), (6,9), (7,9), (8,8.5), (9,8), (10,6.5), (11,4), (10.5,2), (9.5,0), (0, -11), (-9.5,0), (-10.5,2), (-11,4), (-10,6.5), (-9,8), (-8,8.5), (-7,9), (-6,9), (-5,9), (-3,8), (-2,7)))

#welcome users and aintodouce them to the activity
print("Welcome user! Let's draw a picture!")

#pick a heart color
heart_color = input("What color would you like the heart to be?")

#create heart turtle
heart = trtl.Turtle(shape="heart")

#draw a heart in the center of the screen
heart.color(heart_color)
heart.setheading(90)
heart.turtlesize(3)

#keep screen after program runs
wn = trtl.Screen()
wn.mainloop()
