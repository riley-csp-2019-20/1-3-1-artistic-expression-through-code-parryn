import turtle as trtl

#Frog
frog = trtl.Turtle()

#Car
car = trtl.Turtle()

#writer
says = trtl.Turtle()
says.penup()
says.goto(-300, 50)
says.ht()
font_setup= ("arial", 50, "bold")

#Drawer
drawer = trtl.Turtle()
drawer.turtlesize(1)
drawer.pensize(20)
drawer.pencolor("limegreen")
drawer.speed(15)

#Title Screen
wn = trtl.Screen()
wn.bgcolor("deepskyblue")

#F
drawer.penup()
drawer.goto(-400, 200)
drawer.pendown()
drawer.right(90)
drawer.forward(400)

drawer.penup()
drawer.goto(-400, 200)
drawer.pendown()
drawer.left(90)
drawer.forward(200)

drawer.penup()
drawer.goto(-400, 50)
drawer.pendown()
drawer.forward(175)

#R
drawer.penup()
drawer.goto(-250, -200)
drawer.pendown()
drawer.left(90)
drawer.forward(150)

drawer.right(90)
drawer.forward(100)

drawer.right(90)
drawer.forward(25)

#O
drawer.penup()
drawer.goto(-100, -50)
drawer.pendown()
drawer.left(90)
drawer.forward(100)

drawer.right(90)
drawer.forward(150)

drawer.right(90)
drawer.forward(100)

drawer.right(90)
drawer.forward(150)

#G
drawer.penup()
drawer.goto(150, -50)
drawer.pendown()
drawer.left(90)
drawer.forward(100)

drawer.left(90)
drawer.forward(150)

drawer.left(90)
drawer.forward(100)

drawer.left(90)
drawer.forward(150)

drawer.right(180)
drawer.forward(300)

drawer.right(90)
drawer.forward(100)

#O
drawer.penup()
drawer.goto(200, -50)
drawer.pendown()
drawer.left(90)
drawer.forward(150)

drawer.left(90)
drawer.forward(100)

drawer.left(90)
drawer.forward(150)

drawer.left(90)
drawer.forward(100)

#N
drawer.penup()
drawer.goto(350, -200)
drawer.pendown()
drawer.right(90)
drawer.forward(150)

drawer.right(90)
drawer.forward(50)

drawer.right(90)
drawer.forward(150)

drawer.left(90)
drawer.forward(50)

drawer.left(90)
drawer.forward(150)

#says.up()
#says.goto(0, 0)
#says.write("Press Space")

#Start Game
def space():
    drawer.clear()
    drawer.color("white")

    says.clear()

    frog.up()
    frog.color("green")
    frog.turtlesize(3)
    frog.goto(0,-350)
  
    car.up()
    car.color("blue")
    car.turtlesize(5)

    car.up()
    


    steps = 0
    while steps < 50: 

                car.color("blue")
                car.turtlesize(5)
                car.goto(-400, -150)
                car.forward(900)    

        

                #if abs(car.distance - frog.distance) < 5:
                        #car.fillcolor("gray")
                        #frog.fillcolor("grey")
                        #frog.reset
                  











#movement functions
def frogup():
    frog.setheading(90)
    frog.forward(10)
   

def frogdown():
    frog.setheading(270)
    frog.forward(10)
   

def frogleft():
    frog.setheading(180)
    frog.forward(10)
   

def frogright():
    frog.setheading(0)
    frog.forward(10)
   

#wn
wn = trtl.Screen()

wn.onkeypress(space, "space")
wn.onkeypress(frogup, "Up")
wn.onkeypress(frogdown, "Down")
wn.onkeypress(frogleft, "Left")
wn.onkeypress(frogright, "Right")


wn.listen()

wn.mainloop()

