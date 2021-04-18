# 27/01/2021
import turtle
import time
import random
from prettytable import PrettyTable

A = input('Enter your name: ')
print('~~~~~~~~~~~~~~~~~~Controls~~~~~~~~~~~~~~~~~~')
o = PrettyTable()
o.field_names = ['controls']
o.add_row(['W to move UP'])
o.add_row(['S to move DOWN'])
o.add_row(['A to move LEFT'])
o.add_row(['D to move RIGHT'])
print(o)
print('~~~~~~~~~~~~~Supported Colors~~~~~~~~~~~~~')
x = PrettyTable()
x.field_names = ['simple colors' , 'OK colors' , 'OP colors']
x.add_row(['medium orchid','dark goldenrod','olive drab',])
x.add_row(['purple','white','lime',])
x.add_row(['green yellow' , 'hot pink','magenta',])
x.add_row(['dark green','orange red','yellow',])
x.add_row(['steel blue','tomato','deep sky blue',])
x.add_row(['spring green','hot pink','coral',])
x.add_row(['lawn green','violet','medium purple',])
x.add_row(['deep pink','salmon','cyan',])
print(x)
colors = ['medium purple','white','steel blue','green yellow','chartreuse','slate gray','dark cyan','bisque']

#print('The Following are the valid colors')
#print('cyan\nbrown\npurple\nwhite\nred\nblue\ngreen\nhot pink\nmagenta\nmedium turquoise\ngreen yellow')
B = input('Enter your snake''s HEAD COLOR: ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
C = input('Enter your desired FOOD COLOR: ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
D = input('Enter your snake''s TAIL COLOR: ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
var=input('Are u ready to play(Y/N): ')
if var=='N':
    exit()
else:
    delay = 0.1
dict={}
# Score
score = 0
high_score = 0

# Set up the screen
ss = turtle.Screen()
ss.title("Sanp ka khel")
ss.bgcolor(random.choice(colors))
#ss.bgcolor("medium purple")
ss.setup(width=600, height=600)
turtle.bgpic('giphy.gif')
ss.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color(B)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(C)
food.penup()
food.goto(0,100)

tail = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Bradley Hand ITC", 24, "bold"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard roles
ss.listen()
ss.onkeypress(go_up, 'w')
ss.onkeypress(go_down, "s")
ss.onkeypress(go_left, "a")
ss.onkeypress(go_right, "d")

# Main game loop
while True:
    ss.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        V=input('Do yo want to continue(Y/N): ')
        if V=='N':
            tt=input('Do u want to see the highscores(Y/N): ')
            if tt=='Y':
                dict[A] = high_score
                for key, value in dict.items():
                    print(key, ' : ', value)
                    print('Bye')
                exit()
            else:
                print('Bye')
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                exit()
        elif V=='Y':
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

        # Hide the tail
        for segment in tail:
            segment.goto(1000, 1000)
        
        # Clear the tail list
        tail.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Bradley Hand ITC", 24, "bold"))


    #collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(D)
        new_segment.penup()
        tail.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Bradley Hand ITC", 24, "bold"))

    # Move the end tail first in reverse order
    for index in range(len(tail)-1, 0, -1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x,y)

    move()    

    # Check for head collision with the body tail
    for segment in tail:
        if segment.distance(head) < 20:
            # asking the user for Continuation
            J = input('Do yo want to continue(Y/N): ')
            if J == 'N':
                tt=input('Do u want to see the highscores(Y/N): ')
                if tt == 'Y':
                    dict[A] = high_score
                    for key, value in dict.items():
                        print(key, ' : ', value)
                    #----if something goes wrong----
                    #jj =(dict.values())
                    #for var in jj:
                     #   print(var)
                    #keys = (dict.keys())
                    #for varr in keys:
                     #   print(varr)
                    #print(keys, end=''), print('=', end=''), print(jj)
                    print('Bye')
                    exit()
                else:
                    print('Bye')
                    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                    exit()
            elif J == 'Y':
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"
            
        
            # Hides the tail
            for segment in tail:
                segment.goto(1000, 1000)
        
            # Clears the tail list
            tail.clear()

            # Reset the score
            score = 0
            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Bradley Hand ITC", 24, "bold"))
            
        

    time.sleep(delay)

#ss.mainloop()
