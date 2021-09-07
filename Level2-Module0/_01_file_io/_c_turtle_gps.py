"""
Read file of directions to guide the turtle out of the maze!
"""
import turtle
from tkinter import messagebox
from PIL import Image

# ================= Instructions at the bottom of this file ===================

def set_background(filename):
    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(filename)
    rootwindow = window.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')

def check_escape(my_turtle):
    print('x: ' + str(my_turtle.xcor()) + ', y: ' + str(my_turtle.ycor()))

    if int(my_turtle.xcor()) == 85 and int(my_turtle.ycor()) == 275:
        messagebox.showinfo('ESCAPED', 'Your turtle escaped the maze!')
    else:
        messagebox.showerror('TRAPPED', 'Your turtle is still trapped in the maze!')

def initialize_turtle(my_turtle=None):
    if my_turtle is None:
        my_turtle = turtle.Turtle()
    my_turtle.hideturtle()
    my_turtle.shape('turtle')
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-95, -265)
    my_turtle.setheading(90)
    my_turtle.speed(3)
    my_turtle.color('#1DA1F2')
    my_turtle.pen(pendown=True, pencolor='#1DA1F2', pensize=4, outline=0)
    my_turtle.showturtle()
    return my_turtle

if __name__ == '__main__':
    window = turtle.Screen()
    set_background('simplemaze.png')

    # ====================== DO NOT EDIT THE CODE ABOVE ===========================

    # TODO 1) Create a Turtle object and initialize it with initialize_turtle()
    t = initialize_turtle()

    # TODO 2) Open the 'turtle_gps.txt' for reading

    # TODO 3) Read each line and move your turtle according to the direction
    #  and distance specified. For example if a line contains:
    #  FORWARD 50
    #  Your turtle should move forward 50 pixels, my_turtle.forwards(50)
    #
    #  Examples of the other directions are:
    #  LEFT 90      # Turn your turtle left by 90 degrees
    #  RIGHT 45     # Turn your turtle right by 45 degrees

    # TODO 4) Call check_escape() to see if your turtle escaped the maze!!!

    # ===================== DO NOT EDIT THE CODE BELOW ============================

    turtle.done()
