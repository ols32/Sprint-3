import turtle
import os

wn=turtle.Screen()
wn.bgcolor("red")
wn.title("Grísaleikur")

level = 1
totlevel = 4
#Búum til klasa fyrir leikmanninn, Class definition.

class Player(turtle.Turtle):
    #self is a keyword.
    def __init__(self): #Initialize player
        turtle.Turtle.__init__(self) #Initialize turtle
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed = 1
        self.level = 1
    #
    def move(self):
        self.forward(self.speed)

        #Svo hann fari ekki út fyrir borð
        if self.ycor() >230 or self.ycor() <-230:
            self.left(90)
        if self.xcor() < -230:
            self.left(90)
        if self.xcor() > 0230:
            self.level += 1
            return False



     #Snúum alltaf 45 gráður þegar ýtt er á vinstri
    def turnleft(self):
        self.left(45)
#Snúum alltaf 45 gráður þegar ýtt er á hægri
    def turnright(self):
        self.right(45)

    def increasespeed(self):
        while self.speed < 2:
            self.speed += 0.2

    def decreasespeed(self):
        while self.speed > 0.5:
            self.speed -= 0.5

player = Player()

turtle.listen()
turtle.onkey(player.turnleft,"Left")
turtle.onkey(player.turnright,"Right")
turtle.onkey(player.increasespeed, "Up")
turtle.onkey(player.decreasespeed, "Down")

while player.level < 4 or player.level == 4:
    if player.level == 1:
        wn=turtle.Screen()
        wn.bgcolor("yellow") #fyrir stráborð
        player.penup() #höfum pennan uppi svo við drögum ekki línu allt sem hann fer
        player.setposition(-230,0) #Byrjunarstaða
        while True:
            if player.move() == False:
                break

    elif player.level == 2:
        wn=turtle.Screen()
        wn.bgcolor("brown")#fyrir tréborð
        player.penup()
        player.setposition(-230,0)
        while True:
            if player.move() == False:
                break
    elif player.level == 3:
        wn=turtle.Screen()
        wn.bgcolor("grey")
        player.penup()
        player.setposition(-230,0)
        while True:
            if player.move() == False:
                break
    elif player.level == 4:
        wn=turtle.Screen()
        wn.bgcolor("red")
        player.penup()
        player.setposition(-230,0)
        while True:
            if player.move() == False:
                break

        #Úlfurinn

        #Setja úlfinn í class
    #ulfur=turtle.Turtle()
    #ulfur.color("black")
    #ulfur.shape("triangle")
    #ulfur.penup()
    #ulfur.speed(3)
    #ulfur.setposition(-0,0)
    #ulfur.setheading(90)
    #ulfurspeed = 2
    #if(-230 < ulfur.xcor() <230) and (-230 < ulfur.ycor() <230):
        #ulfur.right(random.randint(-30,30))
        #turtle.forward(ulfurspeed)
    #else:
        #ulfur.right(180)
        #ulfur.forward(ulfurspeed)

delay = input("Halló")
wn.mainloop()
