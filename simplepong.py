import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @ TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600) # size of the window; (x - coordinate width; +- 400) (y - coordinate height; +- 300)
wn.tracer(0) # this stops the window from updating, this will speed the game up

# Score
score_a = 0
score_b = 0


# LESSON 2 ING THE PONG AND THE PADDLES:

# PADDLE A
# paddle_a is the name of the "paddle a" object
paddle_a = turtle.Turtle() # turtle is the module/object name; Turtle is the class name
paddle_a.speed(0) # sets the speed to the maximum possible speed
paddle_a.shape("square") # a built in function
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # the shapesize method stretches / adjusts the width and height  from its original  20ft wide by 20ft heigh to: 100Tall [20ft x 5] by 20Wide [20 x 1 the default]
paddle_a.penup()
paddle_a.goto(-350,0) # LEFT SIDE PADDLE [ -350,0]


# PADDLE B
paddle_b = turtle.Turtle() # turtle is the module/object name; Turtle is the class name
paddle_b.speed(0) # sets the speed to the maximum possible speed
paddle_b.shape("square") # a built in function
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # the shapesize method stretches / adjusts the width and height  from its original  20ft wide by 20ft heigh to: 100Tall [20ft x 5] by 20Wide [20 x 1 the default]
paddle_b.penup()
paddle_b.goto(350,0) # RIGHT SIDE PADDLE [ 350,0]


# BALL
ball1 = turtle.Turtle() # turtle is the module/object name; Turtle is the class name
ball1.speed(0) # sets the speed to the maximum possible speed
ball1.shape("square") # a built in function
ball1.color("green")
ball1.penup()
ball1.goto(0,0) 
ball1.dx = 0.19
ball1.dy = -0.19

# BALL
ball2 = turtle.Turtle() # turtle is the module/object name; Turtle is the class name
ball2.speed(0) # sets the speed to the maximum possible speed
ball2.shape("square") # a built in function
ball2.color("blue")
ball2.penup()
ball2.goto(0,0) 
ball2.dx = 0.19
ball2.dy = -0.19

ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("yellow")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = 0.19
ball3.dy = 0.19

# Ball
ball4 = turtle.Turtle()
ball4.speed(0)
ball4.shape("square")
ball4.color("red")
ball4.penup()
ball4.goto(0, 0)
ball4.dx = -0.19
ball4.dy = 0.19

balls = [ball1, ball2, ball3, ball4]



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(' Player A: 0 Player B: 0', align='center', font=(' Courier', 24, ' normal'))


# Function
def paddle_a_up(): # you define the function (ycor()) with [def]
    y = paddle_a.ycor() # paddle_a is the name of the object; the (.ycor()) method is from the turtle module. this method returns the (y) coordinate
    y += 20
    paddle_a.sety(y) # paddle_a set (y) to the new (y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
    # the function has been defined but isnt active until you calL it: wn.listen()

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")  
wn.onkeypress(paddle_a_down, "s")  
wn.onkeypress(paddle_b_up, "Up")  
wn.onkeypress(paddle_b_down, "Down") 
 
# Main game loop
while True: 
    wn.update() 

for ball in balls:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wa&")

    if ball.ycor() < 290:
        ball2.sety(290)
        ball2.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal")) 
       
        # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1
            os.system("afplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1
            os.system("afplay bounce.wav&")
        
    # AI Player
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball

    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
        paddle_b_up()

    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor()) > 10:
       paddle_b_down()
   