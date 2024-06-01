from turtle import Turtle, Screen
import colorgram
import time

screen = Screen()
screen.colormode(255)

t = Turtle()

t.pu()
goto_x = -400
goto_y = -400
t.goto(goto_x,goto_y)
t.pd()
colors = colorgram.extract("goku.jpg",10)
while goto_y < 0:
    for q in colors:
    
        current_color = q.rgb
        t.color(current_color.r,current_color.g,current_color.b,)
        t.fillcolor(current_color.r,current_color.g,current_color.b,)
        
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        time.sleep(1)
        if goto_x < 0:
            goto_x += 50
        else:
            goto_y +=50
            goto_x = -400
        t.pu()
        t.goto(goto_x,goto_y)
        t.pd()
    





screen.exitonclick()