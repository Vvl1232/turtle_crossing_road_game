from turtle import Turtle, Screen
import random

#=========================== Create turtle and screen objects===============================
t = Turtle()
s = Screen()
level_display = Turtle()  
s.setup(width=600, height=600)
s.bgcolor("black")
s.tracer(0)

#============================ Create the player's turtle======================================
level_display.clear() 
level_display.color("white")
level_display.penup()
level_display.goto(-280, 260)
level_display.hideturtle()
level_display.write(f"Level:1", align="left", font=("Courier", 16, "normal"))

def turtle_move():
    t.penup()
    t.shape("turtle")
    t.color("yellow")
    t.left(90)
    t.goto(x=0, y=-280)

    def move_forward():
        if t.ycor() < 300:
            t.forward(10)
            check_next_level()

    s.listen()
    s.onkey(fun=move_forward, key="w")

turtle_move()

#========================= Create moving obstacles ====================================
obstacles = []
colors = ["red", "blue", "pink", "green", "purple"]
for _ in range(15):
    obstacle = Turtle()
    obstacle.shape("square")
    obstacle.shapesize(stretch_wid=1, stretch_len=3)
    obstacle.color(random.choice(colors))
    obstacle.penup()
    obstacle.goto(random.randint(-280, 280), random.randint(0, 280))
    obstacles.append(obstacle)

#======================================== collisions ============================================
move_delay = 100

def move_obstacles():
    global move_delay
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() - 10)

        if obstacle.xcor() < -300:
            obstacle.goto(random.randint(280, 300), random.randint(-280, 280))
        
        if t.distance(obstacle) < 20:
            t.color("red")
            t.penup()
            t.hideturtle()
            t.goto(0, 0)
            t.write("Game Over", align="center", font=("Courier", 24, "normal"))
            return  
    s.update()
    s.ontimer(move_obstacles, move_delay)

move_obstacles()

#========================================= next levels =============================================
level = 1

def check_next_level():
    global level, move_delay
    if t.ycor() >= 290:
        level += 1 
        t.goto(0, -280)
        for obstacle in obstacles:
            obstacle.goto(random.randint(-280, 280), random.randint(0, 280))
        
        level_display.clear() 
        level_display.color("white")
        level_display.penup()
        level_display.goto(-280, 260)
        level_display.hideturtle()
        level_display.write(f"Level: {level}", align="left", font=("Courier", 16, "normal"))
        
        if move_delay > 20:
            move_delay -= 10
        
        s.update()

s.update()
s.exitonclick()
