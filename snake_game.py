"""

1. Create a window and set its properties
2. Create head of the snake and set its properties
3. Create food randomly and set its properties
4. Create a function to set direction values
5. Keyboard Bindings
6. Create a function move() for head movement
7. Check if snake head touches the food
    a. The food should appear at random positions
    b. Attach bodies to the head
    c. Update the score and the high score

Formula for calculating distance between two objects: D = sqrt[(x2 - x1) ^ 2 + (y2 - y1) ^ 2]


"""

import turtle, time, random

score = 0
high_score = 0

#Create a list to store bodies

body_list = []

#Create a window and set its properties

window = turtle.Screen()
window.title("Snake Game by Aadit")
window.bgcolor("#27cc53")
width = 600
height = 600
window.setup(width, height)
window.tracer(0)

#Creating head of snake and its properties

head = turtle.Turtle()

#Classic shapes

head.turtlesize(1.5)
head.shape("turtle")
head.penup()
head.color("blue")
direction = "stop"

#Creating food and set its properties

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-(width/2) + 20, (width/2) - 20)
y = random.randint(-(height/2) + 20, (height/2) - 20)
food.goto(x, y)

#Create a pen object to write score on window

pen = turtle.Turtle()
pen.shape("circle")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
text = f"Score: {score} \nHigh Score: {high_score}"
pen.write(text, align="center", font=("comic sans ms", 16,"bold"))

#Create a function to set direction values

def head_up():
    global direction
    if direction != "down":
        direction = "up"
        head.setheading(90)

def head_left():
    global direction
    if direction != "right":
        direction = "left"
        head.setheading(180)
   
def head_right():
    global direction
    if direction != "left":
        direction = "right"
        head.setheading(0)

def head_down():
    global direction
    if direction != "up":
        direction = "down"
        head.setheading(270)

def exit_game():
    global run  
    run = False

#Creating keyboard bindings

window.listen()

window.onkeypress(head_up, "W")
window.onkeypress(head_up, "w")
window.onkeypress(head_up, "Up")
window.onkeypress(head_down, "S")
window.onkeypress(head_down, "s")
window.onkeypress(head_down, "Down")
window.onkeypress(head_left, "A")
window.onkeypress(head_left, "a")
window.onkeypress(head_left, "Left")
window.onkeypress(head_right, "D")
window.onkeypress(head_right, "d")
window.onkeypress(head_right, "Right")
window.onkeypress(exit_game, "Escape")

def move(): 


    if direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    elif direction == "left":
        x = head.xcor()
        head.setx(x - 20)
           

run = True

while run:
    window.update()

    #Check if head touches the border

    if head.xcor() > width/2 - 10 or head.xcor() < -(width/2 + 10) or \
       head.ycor() > height/2 - 10 or head.ycor() < -(height/2 + 10):
        head.goto(0,0)
        direction = "stop"

        for body in body_list:
            body.goto(1000,1000)

        body_list.clear()

        #Reset the score
        
        score = 0
        pen.clear()
        text = f"Score: {score} \nHigh Score: {high_score}"
        pen.write(text, align="center", font=("comic sans ms", 16,"bold"))
        
    #Check if snake head touches the food

    if head.distance(food) < 20:
        x = random.randint(-(width/2) + 20, (width/2) - 20)
        y = random.randint(-(height/2) + 20, (height/2) - 20)
        food.goto(x, y)
                                                                                                
        #Increase the score and respective high score

        score += 10
        if score > high_score:
            high_score = score

        pen.clear()

        text = f"Score: {score} \nHigh Score: {high_score}"
        pen.write(text, align="center", font=("comic sans ms", 16,"bold"))

        #Create the body of the snake

        body = turtle.Turtle()
        body.turtlesize(1.25)
        body.color("blue")
        body.shape("circle")
        body.penup()
        body_list.append(body)

    #Adding remaining bodies

    for body in range(len(body_list) - 1, 0, -1):
        x = body_list[body - 1].xcor()
        y = body_list[body - 1].ycor()
        body_list[body].goto(x, y)
            
    
    #Adding first body
    
    if len(body_list) > 0:
        x = head.xcor()
        y = head.ycor()
        body_list[0].goto(x, y)
        
    #Create move function. VERY IMPORTANT

    move()

    #Check if snake touches itself

    for body in body_list:

        if body.distance(head) < 20:
            head.goto(0,0)
            direction = "stop"

            for body in body_list:
                body.goto(1000,1000)

            body_list.clear()

            #Reset the score
            
            score = 0
            pen.clear()
            text = f"Score: {score} \nHigh Score: {high_score}"
            pen.write(text, align="center", font=("comic sans ms", 16,"bold"))
            
    time.sleep(0.075)

window.bye()
